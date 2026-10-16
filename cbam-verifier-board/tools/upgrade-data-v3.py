#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""一次性脚本：给 data.json 补上《Trade Free HOT》五模块所需的数据结构。
已经跑过就不会重复插入（按键存在与否判断）。
"""
import json, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(HERE, "data.json")
d = json.load(open(P, encoding="utf-8"))

d["meta"]["dataAsOf"] = "2026-10-14"
d["meta"]["changelog"].insert(0, {
    "d": "2026-10-14",
    "t": "站点升级为《Trade Free HOT》五模块：①核查机构榜（新增商务信息、附加标签、每家机构的历史回溯）②核查法规与认证规则指南 ③核查案例集锦 ④实操经验与风险避坑 ⑤招标与商机信息。页头统一为 Trade Free HOT「你身边的合规专家」；页脚按规范展示壹碳数科服务范围、企业微信二维码位、公众号「听碳的声音」与免责声明。所有非官方内容已做显著标注。"
})

# ---------- ② 法规与指南 ----------
regs = [
    {"no": "(EU) 2023/956", "cn": "CBAM 基本条例（碳边境调节机制）", "kind": "基础法", "when": "2023 年公布生效",
     "what": "确立整套机制：受管控的进口商品范围、授权 CBAM 申报人制度、CBAM 证书的购买与清缴、主管机关职责与罚则。管的是「要不要做、谁负责」。",
     "url": "https://eur-lex.europa.eu/eli/reg/2023/956/oj", "urlLabel": "EUR-Lex 原文 ↗"},
    {"no": "(EU) 2023/1773", "cn": "CBAM 过渡期实施细则", "kind": "实施细则", "when": "2023 年起适用",
     "what": "过渡期报告义务：隐含排放怎么算、哪些参数必须用实际值、哪些可以用默认值、前驱物料如何折算、CBAM 报告的字段与提交方式。管的是「怎么算」。",
     "url": "https://eur-lex.europa.eu/eli/reg_impl/2023/1773/oj", "urlLabel": "EUR-Lex 原文 ↗"},
    {"no": "(EU) 2025/2551", "cn": "CBAM 核查机构认可条件（委托条例）", "kind": "认可规则", "when": "本案核实依据",
     "what": "规定核查机构如何获得认可。本榜反复引用的条款都在这一部：附件 I 把 CBAM 切成 11 个活动组逐组批准；第 4 条给出「由 EU ETS 认可范围扩展」的路径；第 5 条要求现场评估；第 6(2) 条规定证书必须载明的六项要素；第 6(3) 条为有效期；第 14 条年度监督；第 15 条年度安排；附件 II 1.7.2／1.7.3 为公正性与利益冲突规则。管的是「谁来查、怎么批」。",
     "url": "https://eur-lex.europa.eu/eli/reg_del/2025/2551/oj", "urlLabel": "EUR-Lex 原文 ↗"},
    {"no": "(EU) 2018/2067", "cn": "EU ETS 核查与核查机构认可条例（AVR）", "kind": "延伸适用",
     "what": "EU ETS 的温室气体核查与核查机构认可规则。目前所有已公示的 CBAM 认可机构走的都是「由 ETS 核查认可范围扩展而来」这条路径，看不懂它，就看不懂 CBAM 认可的范围边界。",
     "url": "https://eur-lex.europa.eu/eli/reg/2018/2067/oj", "urlLabel": "EUR-Lex 原文 ↗"},
    {"no": "欧盟 CBAM 门户", "cn": "欧盟委员会 CBAM 专页", "kind": "官方入口", "when": "持续更新",
     "what": "政策口径、申报安排、State-of-play 认可进展 PDF 都挂在这里，是所有一手信息的总入口。",
     "url": "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en", "urlLabel": "打开 ↗"},
    {"no": "CBAM 核查专页", "cn": "《Verification of CBAM emissions》", "kind": "官方名录", "when": "名录尚未上线",
     "what": "欧委会承诺在此刊登已认可的 CBAM 核查机构名录。截至本榜基准日页面仍为「The list of accredited CBAM verifiers will be published on this page」，收录 0 家——这正是本榜主张改查各 NAB 官方公示的原因。",
     "url": "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-verification_en", "urlLabel": "打开 ↗"},
    {"no": "核查与认可指南", "cn": "《CBAM 核查及核查机构认可指南》", "kind": "官方指南", "when": "2026-08-24",
     "what": "欧委会面向核查与认可环节的指南文件，涵盖核查程序、认可要求与现场访问。",
     "url": "", "pending": True}
]

cases = [
    {"d": "2026-09-14", "type": "认可里程碑",
     "t": "ESYD 签发 No. 874-9——第一份可对外的 CBAM 核查认可证书",
     "s": "希腊认可机构 ESYD 向 EMICERT CERTIFICATION SERVICES S.A. 签发认可证书 No. 874-9 及附件 Annex V1/20，依据 ELOT EN ISO/IEC 17029:2019，有效期 2026-09-14 至 2030-06-09，附件逐组列载第 I–VIII 组及 L 组；LI（进口电力）与 LII（间接排放）的逐组证据仍需向机构索取附件原件确认。",
     "takeaway": "这张证书第一次给出「CBAM 认可长什么样」的实物样本：发证机构、机构名称与唯一编号、认可范围与活动组、设立国、生效与到期日、依据文件——照这六项去核对其他机构，就能分清真认可和宣传稿。",
     "tags": ["希腊 ESYD", "EmiCert", "ISO/IEC 17029", "附件逐组列载"],
     "src": "ESYD 认可证书 No. 874-9 及附件 Annex V1/20（2026-09-14）"},
    {"d": "2026-09-28", "type": "NAB 集中批复",
     "t": "ACCREDIA 一次性批复三家，范围却各不相同",
     "s": "意大利 ACCREDIA 在同一次 CSA CI 决议中批复 BUREAU VERITAS ITALIA S.P.A.、SGS ICS ITALIA S.R.L.、RINA SERVICES S.A. 三家，路径全部为「由 EU ETS（(EU) 2018/2067）认可范围扩展」。范围并非一致：RINA SERVICES S.A. 未包含第 VIII 组（钢铁制品与铝制品）；必维意大利与 SGS ICS 意大利未包含 LI 组（进口到欧盟关境的电力）。",
     "takeaway": "同一天、同一个 NAB 批出来的三家，认可范围都不一样。签约前必须逐组比对，看到「某集团已获 CBAM 认可」就下单是最常见的踩坑方式。",
     "tags": ["意大利 ACCREDIA", "ETS 范围扩展", "活动组差异", "第 VIII 组"]},
    {"d": "2026-10-07", "type": "格局数据",
     "t": "欧委会 State-of-play：24 家 NAB 同意提供认可，7 国开放第三国通道",
     "s": "受理认可申请的 NAB 达 18 家；法国 COFRAC、希腊 ESYD、意大利 ACCREDIA、荷兰 RvA、波兰 PCA、斯洛伐克 SNAS、瑞典 Swedac 共 7 家的 NAB 受理第三国核查机构的申请。目前已走出去的是希腊与意大利两条线。",
     "takeaway": "中国机构要做 CBAM 核查，入口在这 7 国 NAB；对中国出口企业来说，这决定了未来可选机构的国别分布与现场核查成本。",
     "tags": ["第三国通道", "7 国 NAB", "State-of-play"]}
]

tips = [
    {"stage": "签约前", "t": "先定产品落在第几组，再看报价",
     "risk": "CBAM 认可按活动组逐组授予。报价再便宜，缺你那产品所在的组就等于白做——例如钢铁制紧固件、钢丝与线材制品、五金件、铝型材都落在第 VIII 组，而当前有一家已公示机构恰恰没有 VIII 组。",
     "do": "先确定 CN 编码 → 回到本榜「11 组活动组覆盖对照」确认组别 → 拿组别去筛机构，最后才谈价格。",
     "ref": "(EU) 2025/2551 附件 I"},
    {"stage": "签约前", "t": "核对的是「签发报告的那个法人」，不是集团品牌",
     "risk": "集团宣传口径与证书上的持证主体不一致是常态。报告由不具资格的关联公司签发，申报环节照样会被退回。",
     "do": "索要认可证书，核对机构全称、唯一认可标识、生效与到期日三项是否与合同签署主体一致。",
     "ref": "(EU) 2025/2551 第 6(2) 条"},
    {"stage": "签约前", "t": "确认报告签发日落在认可有效期内",
     "risk": "认可有五年有效期上限，但目前多数已公示机构的起止日期并未随公告公开，无法从外部判断。",
     "do": "把有效期写进合同：报告签发日必须落在认可有效期内，并要求机构提供证书证明。",
     "ref": "(EU) 2025/2551 第 6(3) 条"},
    {"stage": "数据准备", "t": "数据拿不到，就只能回退默认值——成本通常高于自己测",
     "risk": "关键工序缺实测数据时只能使用默认值，默认值往往偏保守，直接抬高证书清缴成本。",
     "do": "提前把这些工序拆开：能实测的先布计量，测不到的提前与进口商确定数据口径和替代方案。"},
    {"stage": "数据准备", "t": "多现场、租赁产线、外协工序的定性要提前写死",
     "risk": "同一条产线，写成自有设施与写成外包工序，在 CBAM 下是两条完全不同的数据路径，后期改口径几乎等于重做。",
     "do": "生产主体、人员归属、设备权属、物料物权、质量责任五项开工前书面定清，后续所有材料统一口径。"},
    {"stage": "现场核查", "t": "远程审核与 OB 联合现场核查能力要提前问",
     "risk": "多数机构尚未公开这两项能力，等到排才发现不支持，差的就不是差旅费而是排期。",
     "do": "询价阶段就问清：是否支持远程审核、在中国是否有现场团队、能否与已合作的核查伙伴做 OB 联合现场审核。"},
    {"stage": "报告签发", "t": "确认机构已完成 CBAM 登记库注册",
     "risk": "拿到认可不等于能在登记库出具可被申报引用的正式报告；两件事之间存在时间差。",
     "do": "要求机构书面确认登记库注册状态与预计可签发日期，并写进合同交付节点。"},
    {"stage": "全程", "t": "盯 NAB 公示，不要只盯机构官宣",
     "risk": "机构官宣是二手信息，且可能早于或晚于 NAB 公示；两者出现偏差时以 NAB 为准。",
     "do": "每周一对一次 ACCREDIA 决议、ESYD 证书等 NAB 官方渠道，本榜①模块即为该动作的替代品。"}
]

bid_portals = [
    {"n": "TED · 欧盟官方招标公告", "url": "https://ted.europa.eu"},
    {"n": "中国政府采购网", "url": "http://www.ccgp.gov.cn"},
    {"n": "全国公共资源交易平台", "url": "https://www.ggzy.gov.cn"},
    {"n": "欧盟委员会 CBAM 门户", "url": "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en"}
]

if "regs" not in d:
    d["regs"] = regs
if "cases" not in d:
    d["cases"] = cases
if "tips" not in d:
    d["tips"] = tips
if "bids" not in d:
    d["bids"] = []
if "bidPortals" not in d:
    d["bidPortals"] = bid_portals

# ---------- ① 机构卡的商务信息 / 附加标签 / 历史回溯 ----------
def key(v):
    return v["nameEn"].strip().upper()

BIZ = {
    "BUREAU VERITAS ITALIA S.P.A.": dict(
        price="未公开", pricing="未公开（签约前须向机构索取书面报价）",
        area="集团口径为全球服务网络（公开宣介，具体国别能力须确认）",
        langs="中文 / 英文（2026-10-08 已发布中文稿件）",
        ob="未公开（可否与中国本地机构做 OB 联合现场核查，须向机构确认）",
        sign="有（已获 ACCREDIA 认可，具备签发资格；CBAM 登记库注册状态未公开）",
        remote="未公开", annual="待向机构确认",
        hist=[("2026-10-13", "本榜 V2 更正：活动组范围已在 ACCREDIA 2026-09-28 决议中逐组列明，此前标注「未公开」有误，披露指数由 28 上调至 75。"),
              ("2026-10-12", "本榜首次收录。")]),
    "SGS ICS ITALIA S.R.L.": dict(
        price="未公开", pricing="未公开（签约前须向机构索取书面报价）",
        area="集团口径为多国服务网络（公开宣介，具体国别能力须确认）",
        langs="中文 / 英文（通标已发布中文公告）",
        ob="未公开（可否做 OB 联合现场核查，须向机构确认）",
        sign="有（已获 ACCREDIA 认可，具备签发资格；CBAM 登记库注册状态未公开）",
        remote="未公开", annual="待向机构确认",
        hist=[("2026-10-13", "本榜 V2 更正：活动组范围已在 ACCREDIA 决议中逐组列明；同时更正持证法人为 SGS ICS ITALIA S.R.L.，披露指数由 28 上调至 75。"),
              ("2026-10-12", "本榜首次收录。")]),
    "EMICERT CERTIFICATION SERVICES S.A.": dict(
        price="未公开", pricing="未公开（签约前须向机构索取书面报价）",
        area="希腊法人签发，中国现场由 CTI 华测团队执行（「中国现场核查 + 欧盟签发」模式）",
        langs="中文 / 英文 / 希腊文（设有中文服务页）",
        ob="可与 CTI 华测中国碳团队配合执行本地现场核查",
        sign="有（已获 ESYD 认可，具备签发资格；CBAM 登记库注册状态未公开）",
        remote="未公开", annual="待向机构确认",
        hist=[("2026-10-13", "本榜 V2 更正：附件中的「n/a」实为「对应 EU ETS 活动组」列，并非未获授权；据此重算，披露指数由 85 调整至 65。LI／LII 仍列为待核验项。"),
              ("2026-10-12", "本榜首次收录。")]),
    "RINA SERVICES S.A.": dict(
        price="未公开", pricing="未公开（签约前须向机构索取书面报价）",
        area="集团口径覆盖多国（公开宣介，具体国别能力须确认）",
        langs="英文为主；截至本期未检索到面向中国客户的中文 CBAM 服务宣介",
        ob="未公开（可否做 OB 联合现场核查，须向机构确认）",
        sign="有（已获 ACCREDIA 认可，具备签发资格；CBAM 登记库注册状态未公开）",
        remote="未公开", annual="待向机构确认",
        hist=[("2026-10-13", "本榜 V2 更正：持证法人更正为 RINA SERVICES S.A.（非 RINA S.p.A.）；活动组范围已在 ACCREDIA 决议中逐组列明，披露指数由 33 上调至 65。同时首次披露其未获第 VIII 组授权。"),
              ("2026-10-12", "本榜首次收录。")]),
}

for v in d["verifiers"]:
    cfg = BIZ.get(key(v))
    if not cfg:
        continue
    v["biz"] = {"price": cfg["price"], "pricing": cfg["pricing"], "area": cfg["area"],
                "langs": cfg["langs"], "ob": cfg["ob"]}
    v["tags"] = {"sign": cfg["sign"], "remote": cfg["remote"], "annual": cfg["annual"]}
    v["history"] = [{"d": a, "t": b} for a, b in cfg["hist"]]

json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("data.json 已升级")
print("  法规条目 :", len(d["regs"]))
print("  案例条目 :", len(d["cases"]))
print("  经验条目 :", len(d["tips"]))
print("  商机条目 :", len(d["bids"]), "（官方采集源", len(d["bidPortals"]), "个）")
for v in d["verifiers"]:
    print("  机构  :", v["nameEn"], "| biz:", bool(v.get("biz")), "| tags:", bool(v.get("tags")), "| history:", len(v.get("history", [])))
