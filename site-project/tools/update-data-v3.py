#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
V3 数据更新：补录瑞典 Swedac 认可的 Intertek Certification AB，
并按 ACCREDIA 决议 Rev.01（2026-10-09 签署）与 ESYD 证书附件（No.874-9）
更正 RINA / SGS / EmiCert 的活动组范围。
用法： python tools/update-data-v3.py
"""
import json, os

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(HERE, "data.json")
d = json.load(open(P, encoding="utf-8"))

G = {v["nameEn"]: v for v in d["verifiers"]}

# ---------------- Intertek（新增） ----------------
intertek = {
    "name": "Intertek 天祥（瑞典）",
    "nameEn": "INTERTEK CERTIFICATION AB",
    "group": "Intertek 集团（英国）",
    "groupNote": "瑞典实体位于斯德哥尔摩 Kista",
    "nab": "Swedac",
    "nabCn": "瑞典",
    "announced": "2026-10-13",
    "nabDecided": "2026-10-13",
    "entity": "INTERTEK CERTIFICATION AB（瑞典 Kista）",
    "certNo": "Swedac 认可号 1639",
    "standard": "认可库条目按 (EU) 2025/2551 附件 I 逐组列示；具体依据标准以认可证书原件为准",
    "validFrom": "2026-10-13",
    "validTo": "2031-10-13",
    "scopeGroups": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "LI", "LII"],
    "scopePending": [],
    "scopeText": "瑞典 Swedac 认可库条目（No. 1639）按 (EU) 2025/2551 附件 I 逐组列示：I 煅烧粘土／水泥熟料／水泥／高铝水泥、II 氢／氨、III 硝酸、IV 尿素／混合肥料、V 烧结矿／生铁／DRI／粗钢、VI 铁合金、VII 未锻轧铝、VIII 钢铁及铝制品、LI 进口到欧盟关境的电力、LII 间接排放。",
    "route": "由 Swedac 按 ISO/IEC 17029 受理并授予（瑞方当前优先处理瑞典、乌克兰、英国的申请）",
    "registry": "未公开，须在取得认可后两个月内完成 CBAM 登记库注册",
    "officialListed": False,
    "china": {
        "v": 1,
        "t": "Intertek 集团在中国设有广泛的分支与实验室网络（集团公开宣介口径）。但本次获认可的持证主体为瑞典法人，能否由中国团队执行现场核查，须向机构书面确认。"
    },
    "site": "https://www.intertek.com/",
    "srcs": [
        "Swedac 认可库条目 No. 1639（认可日 2026-10-13，有效期至 2031-10-13）",
        "Swedac 官网新闻《Första svenska organet ackrediterat för CBAM-verifiering》（2026-10-13）"
    ],
    "note": "<b>范围缺口提示：</b>所列条目<b>不含 L 组（CCUS）</b>。若你的申报涉及碳捕集、利用与封存相关的排放扣减，需在签约前书面确认。",
    "d": {"nab": 1, "entity": 1, "cert": 1, "scope": 1, "validity": 1, "registry": 0, "china": 1},
    "biz": {
        "price": "未公开",
        "pricing": "未公开（签约前须向机构索取书面报价）",
        "area": "瑞典法人持证；集团口径为全球服务网络（具体国别服务能力须确认）",
        "langs": "英文 / 瑞典文；中文服务能力须向机构确认",
        "ob": "未公开（可否做 OB 联合现场核查须向机构确认）"
    },
    "tags": {
        "sign": "有（已获 Swedac 认可，具签发资格；CBAM 登记库注册状态未公开）",
        "remote": "未公开",
        "annual": "待向机构确认"
    },
    "history": [
        {"d": "2026-10-14", "t": "本榜首次收录（V3）。依据 Swedac 认可库条目 No.1639：认可日 2026-10-13，有效期至 2031-10-13，活动组 I–VIII、LI、LII。"}
    ]
}

# ---------------- 更正 ----------------
bv = G["BUREAU VERITAS ITALIA S.P.A."]
bv["certNo"] = "ACCREDIA 决议正文未载明认可证书编号（名录中另见注册号，以认可证书原件为准）"
bv["note"] = "<b>范围缺口提示：</b>未获 <b>LI 组（进口到欧盟关境的电力）</b>授权。必维意大利的范围在三份 ACCREDIA 文本（新闻稿 10-06、决议 Rev.00、决议 Rev.01）中表述一致，可放心按此比对。"
bv["d"] = {"nab": 1, "entity": 1, "cert": 0.5, "scope": 1, "validity": 0, "registry": 0, "china": 1}

sgs = G["SGS ICS ITALIA S.R.L."]
sgs["certNo"] = "ACCREDIA 决议正文未载明认可证书编号（以认可证书原件为准）"
sgs["scopeGroups"] = ["I", "II", "IV", "VI", "VIII", "L", "LI", "LII"]
sgs["scopePending"] = []
sgs["scopeText"] = "ACCREDIA 决议 Rev.01（2026-10-09 签署）列明：CBAM，适用于活动组 I、II、IV、VI、VIII、L、LI、LII。新闻稿（10-06）口径为 I–VIII、L、LII。两份文本不一致，以认可证书附件为准。"
sgs["note"] = "<b>⚠ 范围缺口提示（本次更正）：</b>按 ACCREDIA 决议 Rev.01，SGS ICS 意大利<b>未获 III 组（硝酸）、V 组（烧结矿／生铁／DRI／粗钢）、VII 组（未锻轧铝）</b>授权；但<b>含 LI 组（进口电力）</b>——与新闻稿口径相反。<b>硝酸、粗钢及上游铁水、未锻轧铝这类货物，签约前必须索取认可附件原件逐组核对。</b>"
sgs["d"] = {"nab": 1, "entity": 1, "cert": 0.5, "scope": 1, "validity": 0, "registry": 0, "china": 1}
sgs.setdefault("history", []).insert(0, {"d": "2026-10-14", "t": "V3 更正：以 ACCREDIA 决议 Rev.01 为准，范围由「I–VIII、L、LII」更正为「I、II、IV、VI、VIII、L、LI、LII」（缺 III／V／VII，含 LI）。ACCREDIA 新闻稿与决议两版口径不一致，本榜已并列记录。"})

rina = G["RINA SERVICES S.A."]
rina["scopeGroups"] = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "L", "LI", "LII"]
rina["scopePending"] = []
rina["scopeText"] = "ACCREDIA 决议 Rev.01（2026-10-09 签署）列明：CBAM，适用于活动组 I、II、III、IV、V、VI、VII、VIII、L、LI、LII（11 组全覆盖）。新闻稿（10-06）口径为 I–VII、L、LI、LII，不含 VIII。"
rina["note"] = "<b>⚠ 更正说明：</b>V2 版依据 ACCREDIA 新闻稿判断「RINA 未获第 VIII 组授权」——<b>该结论已撤回</b>。ACCREDIA 决议 Rev.01 明确含第 VIII 组（钢铁制品与铝制品），本榜以决议为准记录为 11 组全覆盖；新闻稿口径仍缺 VIII，两份文本不一致的原因 ACCREDIA 未作说明。<b>涉及钢铁／铝下游制品的，仍建议签约前索取认可附件原件确认。</b>"
rina["d"] = {"nab": 1, "entity": 1, "cert": 0.5, "scope": 1, "validity": 0, "registry": 0, "china": 0.5}
rina.setdefault("history", []).insert(0, {"d": "2026-10-14", "t": "V3 更正：撤回「未获第 VIII 组」结论，按 ACCREDIA 决议 Rev.01 更正为 11 组全覆盖（新闻稿口径仍缺 VIII，本榜并列记录）。披露指数由 65 调整为 68。"})

emi = G["EMICERT CERTIFICATION SERVICES S.A."]
emi["standard"] = "ELOT EN ISO 14065:2022 + ELOT EN ISO 14064-3:2019（认可证书 No.874-9 依 ELOT EN ISO/IEC 17029:2019 签发）"
emi["scopeGroups"] = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "L", "LI", "LII"]
emi["scopePending"] = []
emi["scopeText"] = "ESYD 证书 No.874-9 附件 V1/20（2026-09-14）逐组列示 CBAM 全部 11 个活动组：I–VIII 及 L、LI、LII。附件中 LI／LII 行的「n/a」仅出现在「对应 (EU) 2018/2067 活动组」列，表示 EU ETS 中无对应组，不代表未获授权。该范围附件取代 2026-03-23 的旧版。"
emi["note"] = "<b>更正说明：</b>V2 版把 LI／LII 列为「待核验项」，系误读附件中「对应 EU ETS 活动组」列的 n/a。现已从 ESYD 官网直接下载附件核对，确认为 <b>11 组全覆盖</b>，披露指数回调至 85。<br><b>提示：</b>ESYD 在线认可名录的可访问性曾出现波动，建议以证书附件原件为最终依据。"
emi["d"] = {"nab": 1, "entity": 1, "cert": 1, "scope": 1, "validity": 1, "registry": 0, "china": 1}

# 统一补齐 biz / tags / history 缺省值
BIZ_DEF = {
    "BUREAU VERITAS ITALIA S.P.A.": dict(
        area="集团口径为全球服务网络（公开宣介，具体国别服务能力须确认）",
        langs="中文 / 英文（2026-10-08 已发布中文稿件）",
        ob="未公开（可否与中国本地机构做 OB 联合现场核查须向机构确认）"),
    "SGS ICS ITALIA S.R.L.": dict(
        area="集团口径覆盖 100 多个国家和地区（公开宣介，具体国别服务能力须确认）",
        langs="中文 / 英文（通标已发布中文公告）",
        ob="未公开（可否做 OB 联合现场核查须向机构确认）"),
    "RINA SERVICES S.A.": dict(
        area="集团口径覆盖 70 余国（公开宣介，具体国别服务能力须确认）",
        langs="英文为主；截至本期未检索到面向中国客户的中文 CBAM 服务宣介",
        ob="未公开（可否做 OB 联合现场核查须向机构确认）"),
    "EMICERT CERTIFICATION SERVICES S.A.": dict(
            langs="中文 / 英文 / 希腊文（设有中文服务页）",
            ob="可由 CTI 华测中国碳团队配合执行本地现场核查"),
    "INTERTEK CERTIFICATION AB": dict(
            langs="英文 / 瑞典文；中文服务能力须向机构确认",
            ob="未公开（可否做 OB 联合现场核查须向机构确认）"),
}

for v in d["verifiers"] + [intertek]:
    key = v["nameEn"]
    cfg = BIZ_DEF.get(key, {})
    v.setdefault("biz", {
        "price": "未公开",
        "pricing": "未公开（签约前须向机构索取书面报价）",
        "area": cfg.get("area", "未公开，须向机构确认"),
        "langs": cfg.get("langs", "未公开，须向机构确认"),
        "ob": cfg.get("ob", "未公开，须向机构确认"),
    })
    v.setdefault("tags", {
        "sign": "有（已获 NAB 认可，具签发资格；CBAM 登记库注册状态未公开）",
        "remote": "未公开，须向机构确认",
        "annual": "待向机构确认",
    })
    v.setdefault("history", [])

# 已存在的四家，补一条 V3 记录（Intertek 已有）
for v in d["verifiers"]:
    if v["nameEn"] == "BUREAU VERITAS ITALIA S.P.A.":
        v["history"].insert(0, {"d": "2026-10-14", "t": "V3：三份 ACCREDIA 文本范围表述一致（I–VIII、L、LII；缺 LI）。因 ACCREDIA 未在决议正文列明认可证书编号，「认可编号」一项由满分下调为半分，披露指数由 75 调整为 68。"})
    if v["nameEn"] == "SGS ICS ITALIA S.R.L.":
        v["history"].insert(0, {"d": "2026-10-14", "t": "V3 更正（见 note）：按决议 Rev.01 更正活动组范围，披露指数由 75 调整为 68。"})
    if v["nameEn"] == "RINA SERVICES S.A.":
        pass  # 已在上面插入

# 插到最前（Intertek 认可日最新）
d["verifiers"].insert(0, intertek)

# meta
d["meta"]["dataAsOf"] = "2026-10-14"
d["meta"]["changelog"].insert(0, {
    "d": "2026-10-14",
    "errata": True,
    "t": "【V3 重要更正】①新增第 5 家：INTERTEK CERTIFICATION AB（瑞典 Swedac，认可号 1639，2026-10-13 授予，有效期至 2031-10-13，活动组 I–VIII、LI、LII，不含 L/CCUS）——数据源为 Swedac 官方认可库条目与官网新闻。②撤回 V2「RINA 未获第 VIII 组」的结论：ACCREDIA 决议 Rev.01（2026-10-09 签署）明确含第 VIII 组，本榜以决议为准，并将新闻稿口径并列记录。③更正 SGS ICS 意大利范围：按决议 Rev.01 为 I、II、IV、VI、VIII、L、LI、LII（缺 III／V／VII，含 LI），与新闻稿口径不一致。④更正 EmiCert：已从 ESYD 官网直接下载证书附件（No.874-9，附件 V1/20）核对，确认为 11 组全覆盖，此前标注的 LI／LII「待核验项」系误读附件中「对应 EU ETS 活动组」列的 n/a，予以更正。⑤机构卡新增「商务信息」「附加标签」「历史回溯」三块，全部缺口与未知项一律显式标注，不做估算。",
})

json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# 校验输出
W = sum(x["w"] for x in d["dims"])
print("权重合计:", W)
print("机构数:", len(d["verifiers"]))
for v in d["verifiers"]:
    s = sum(x["w"] * (v["d"][x["k"]] or 0) for x in d["dims"])
    print("  %3d  %-42s | VIII:%s | 认可日 %s" % (
        round(s), v["nameEn"],
        "有" if "VIII" in v["scopeGroups"] else "无",
        v.get("nabDecided") or "-"))
print("regs/cases/tips/bids/portals:", len(d["regs"]), len(d["cases"]), len(d["tips"]), len(d["bids"]), len(d["bidPortals"]))
