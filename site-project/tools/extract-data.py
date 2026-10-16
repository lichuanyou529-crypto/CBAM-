#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
把 index.html 里内嵌的 EMBEDDED_DATA 对象导出为同目录的 data.json。
只在第一次建立 data.json 时需要；之后 data.json 就是唯一数据源。
用法： python tools/extract-data.py
"""
import os, re, subprocess, sys, json, datetime

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODE = r"C:\Users\lichuanyou\.workbuddy\binaries\node\versions\22.22.2-3\node.exe"
HTML = os.path.join(HERE, "index.html")
OUT = os.path.join(HERE, "data.json")
TMP = os.path.join(HERE, "_tmp_extract.js")

src = open(HTML, encoding="utf-8").read()
m = re.search(r"var EMBEDDED_DATA\s*=\s*(\{.*?\n\};)\s*\n", src, re.S)
if not m:
    m = re.search(r"var DATA\s*=\s*(\{.*?\n\};)\s*\n", src, re.S)
if not m:
    sys.exit("未在 index.html 中找到 EMBEDDED_DATA / DATA 数据块")

block = m.group(1).rstrip().rstrip(";")
js = (
    "var DATA = " + block + ";\n"
    "DATA.meta = DATA.meta || {};\n"
    "DATA.meta.generatedAt = new Date().toISOString();\n"
    "require('fs').writeFileSync(process.argv[2], JSON.stringify(DATA, null, 2), 'utf8');\n"
)
open(TMP, "w", encoding="utf-8").write(js)
subprocess.run([NODE, TMP, OUT], check=True)
os.remove(TMP)

d = json.load(open(OUT, encoding="utf-8"))
print("已生成", OUT)
print("  基准日      :", d["meta"]["dataAsOf"])
print("  生成时间    :", d["meta"]["generatedAt"])
print("  核查机构    :", len(d["verifiers"]), "家")
print("  活动组      :", len(d["groups"]), "组")
print("  NAB         :", len(d["nabs"]), "家")
