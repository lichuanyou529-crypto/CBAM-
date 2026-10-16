#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把 data.json 的内容写回 index.html 的内置快照区（EMBEDDED_DATA）。
用途：直接双击打开 index.html（file:// 协议）时浏览器不允许 fetch 本地 json，
      页面会回退到内置快照。每次改完 data.json 后跑一次本脚本，快照就同步了。

用法： python tools/embed-snapshot.py
"""
import os, re, json, sys, datetime

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HTML = os.path.join(HERE, "index.html")
JSONF = os.path.join(HERE, "data.json")

if not os.path.exists(JSONF):
    sys.exit("找不到 data.json")

data = json.load(open(JSONF, encoding="utf-8"))
# 打上本地时间（北京时间）时间戳，供页面展示与版本比对
tz = datetime.timezone(datetime.timedelta(hours=8))
stamp = datetime.datetime.now(tz).replace(microsecond=0).isoformat()
data.setdefault("meta", {})["generatedAt"] = stamp
json.dump(data, open(JSONF, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

body = json.dumps(data, ensure_ascii=False, indent=2)
body = "\n".join("  " + ln if ln.strip() else ln for ln in body.split("\n"))

src = open(HTML, encoding="utf-8").read()
pat = re.compile(r"(var EMBEDDED_DATA\s*=\s*)(\{.*?\n[ \t]*\};)", re.S)
if not pat.search(src):
    sys.exit("index.html 中未找到 EMBEDDED_DATA 数据块")
new = pat.sub(lambda m: m.group(1) + body + ";", src, count=1)
open(HTML, "w", encoding="utf-8").write(new)

print("已把 data.json 写回 index.html 内置快照")
print("  基准日  :", data["meta"].get("dataAsOf"))
print("  时间戳  :", stamp)
print("  机构数  :", len(data.get("verifiers", [])))
