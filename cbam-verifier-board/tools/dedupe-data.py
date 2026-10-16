#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""去重 data.json 里的 regs / cases / tips / verifiers，并补一条 Swedac 认可库入口。"""
import json, os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(HERE, "data.json")
d = json.load(open(P, encoding="utf-8"))

def dedupe(arr, keyfn):
    seen, out = set(), []
    for x in arr:
        k = keyfn(x)
        if k in seen:
            continue
        seen.add(k)
        out.append(x)
    return out

d["regs"]  = dedupe(d["regs"],  lambda r: (r.get("no", ""), r.get("cn", "")))
d["cases"] = dedupe(d["cases"], lambda c: (c.get("d", ""), c.get("t", "")))
d["tips"]  = dedupe(d["tips"],  lambda t: (t.get("t", "")))
d["verifiers"] = dedupe(d["verifiers"], lambda v: v.get("nameEn", ""))

if not any("ackrediteringar.swedac.se" in (r.get("url") or "") for r in d["regs"]):
    d["regs"].append({"no": "Swedac 认可库", "cn": "瑞典国家认可机构 · 认可查询库",
                     "kind": "核验入口", "when": "持续更新",
                     "what": "按认证、检验、验证与核查分类查询，可逐组查看认可范围与有效期。本期 Intertek 条目（No.1639）即取自此库。",
                     "url": "https://ackrediteringar.swedac.se/en/1639", "urlLabel": "打开条目 ↗"})

json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("regs:", len(d["regs"]))
for r in d["regs"]:
    print("   ", r["no"], "|", r["cn"][:34])
print("cases:", len(d["cases"]), "tips:", len(d["tips"]), "verifiers:", len(d["verifiers"]))
