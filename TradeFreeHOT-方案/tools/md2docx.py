#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把一个 Markdown 文件转成 Word 文档（保持用户定稿措辞，不经 AI 重写）。

用法（托管 Python）：
  python tools/md2docx.py <markdown绝对路径> <输出docx绝对路径>
"""
import json, os, re, subprocess, sys

E = r"D:\Program Files\WorkBuddy\resources\app.asar.unpacked\resources\plugins\workbuddy-builtin\skills\tencent-local-office-edit\edsdk.py"
P = r"C:\Users\lichuanyou\.workbuddy\binaries\python\envs\default\Scripts\python.exe"


def call(tool, kvs=None, js=None):
    cmd = [P, E, "call", tool]
    if kvs:
        cmd += kvs
    if js:
        cmd += ["--json", json.dumps(js, ensure_ascii=False)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout or "").strip()
    if not out:
        return {"_raw": "", "stderr": r.stderr}
    try:
        return json.loads(out)
    except Exception:
        pass
    # 有些工具返回纯文本（如 create_doc），从中尽力解析字段
    kv = dict(re.findall(r"(\w+)=([^\s,]+)", out))
    kv["_raw"] = out
    return kv


def main():
    md = os.path.abspath(sys.argv[1])
    dst = os.path.abspath(sys.argv[2])
    if not os.path.exists(md):
        sys.exit("找不到 md：" + md)
    os.makedirs(os.path.dirname(dst), exist_ok=True)

    # 1. 新建文档
    res = call("create_doc")
    fid = res.get("file_id") or res.get("new_doc_id")
    if not fid:
        sys.exit("create_doc 失败：" + json.dumps(res, ensure_ascii=False)[:400])

    # 2. 插入 markdown（用 file:// 避免转义与丢字）
    res = call("doc_insert_markdown", ["file_id=" + fid, "idx=0",
                                       "markdown=file://" + md.replace("\\", "/")])
    if res.get("_raw") is not None and not res.get("ok", True):
        print("插入返回：", json.dumps(res, ensure_ascii=False)[:300])

    # 3. 读结构，给标题段落补真正的 Word 标题样式
    #    注意：markdown 导入的标题只有字号加粗、没有 pStyle，导航窗格／自动目录会失效，
    #    所以这里按 resolve 出来的 Heading 节点，用 ranges 批量套命名样式。
    struct = call("doc_resolve_document_structure", ["file_id=" + fid, "mode=compact", "limit=0",
                                                     "text_preview_length=160"])
    nodes = struct.get("nodes", [])
    LEVEL2STYLE = {1: "TITLE", 2: "HEADING_1", 3: "HEADING_2", 4: "HEADING_3",
                   5: "HEADING_4", 6: "HEADING_4"}

    by_style = {}
    for n in nodes:
        if n.get("type") != "Heading":
            continue
        st = LEVEL2STYLE.get(n.get("heading_level") or 2)
        if not st:
            continue
        by_style.setdefault(st, []).append({"begin": n.get("start_index"), "end": n.get("end_index")})

    applied = 0
    for style, ranges in by_style.items():
        ranges = [r for r in ranges if r["begin"] is not None and r["end"] is not None]
        if not ranges:
            continue
        r = call("doc_apply_named_style", js={"file_id": fid, "ranges": ranges,
                                              "named_style_type": style})
        bad = ("错误" in r.get("_raw", "")) or r.get("ok") is False or r.get("error")
        applied += len(ranges)
        print("  ", style, len(ranges), "段", "失败：" + json.dumps(r, ensure_ascii=False)[:200] if bad else "OK")

    # 4. 保存
    r = call("save_file", ["file_id=" + fid, "file_path=" + dst.replace("\\", "/")])
    print("已生成：", dst)
    print("save:", json.dumps(r, ensure_ascii=False)[:200] if not r.get("ok", True) else "OK")


if __name__ == "__main__":
    main()
