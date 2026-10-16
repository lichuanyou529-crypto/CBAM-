#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""V3 补录：案例模块新增 Intertek/Swedac 里程碑，法规模块补两个核验入口。"""
import json, os

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(HERE, "data.json")
d = json.load(open(P, encoding="utf-8"))

cases = [
    {"d": "2026-10-13", "type": "认可里程碑",
     "t": "Swedac 认可 Intertek Certification AB——北欧首例，全球第 4 例",
     "s": "瑞典国家认可机构 Swedac 于 2026-10-13 授予 Intertek Certification AB（斯德哥尔摩 Kista）CBAM 核查认可，认可号 1639，有效期 2026-10-13 至 2031-10-13。认可库条目按 (EU) 2025/2551 附件 I 逐组列示：I–VIII、LI、LII，不含 L（CCUS）。",
     "takeaway": "这是本榜首次收录北欧通道的机构。对出口企业有两个实际价值：Intertek 集团在中国有广泛的本地团队，现场核查的沟通与差旅成本更可控；同时它握有 LI（进口电力）与 LII（间接排放），水泥、化肥这类要报间接排放的货物少一层缺口。但 Swedac 当前优先处理瑞典、乌克兰、英国的申请，中国机构若想走这条线需先确认排队情况。",
     "tags": ["瑞典 Swedac", "Intertek", "认可号 1639", "北欧通道"],
     "src": "Swedac 认可库条目 No.1639（https://ackrediteringar.swedac.se/en/1639）；Swedac 官网新闻《Första svenska organet ackrediterat för CBAM-verifiering》（2026-10-13）"},
    {"d": "2026-09-28", "type": "NAB 集中批复",
     "t": "ACCREDIA 一次批复三家，但新闻稿与决议口径不一致",
     "s": "意大利 ACCREDIA 在同一次 CSA CI 决议中批复 BUREAU VERITAS ITALIA S.P.A.、SGS ICS ITALIA S.R.L.、RINA SERVICES S.P.A. 三家，路径均为「由 EU ETS（(EU) 2018/2067）认可范围扩展」。两份文本的范围并不一致：决议 Rev.01（2026-10-09 签署）中 RINA 含第 VIII 组、SGS 为 I／II／IV／VI／VIII／L／LI／LII；新闻稿（10-06）中 RINA 不含 VIII、SGS 为 I–VIII／L／LII。必维意大利在三份文本中均为 I–VIII、L、LII。ACCREDIA 未说明差异原因，且两份文本均未载明认可证书编号。",
     "takeaway": "同一家 NAB、同一天批出来的三家，范围都不一样，而且连 NAB 自己对外发布的两份文件都对不上。签约前要做的就一件事：向机构索取认可附件原件，逐组核对自己货物所在的活动组。"},
    {"d": "2026-09-14", "type": "认可里程碑",
     "t": "ESYD 签发 No.874-9——第一份可对外的 CBAM 核查认可证书",
     "s": "希腊认可机构 ESYD 向 EMICERT CERTIFICATION SERVICES S.A. 签发认可证书 No.874-9 及附件 V1/20（2026-09-14）。附件逐组列示全部 11 个 CBAM 活动组，依据 ELOT EN ISO 14065:2022 与 ELOT EN ISO 14064-3:2019；证书有效期至 2030-06-09，该范围附件取代 2026-03-23 的旧版。",
     "takeaway": "这张证书第一次给出「CBAM 认可长什么样」的实物样本：发证机构、机构名称与唯一编号、认可范围与活动组、设立国、生效与到期日、依据文件——照这六项去核对其他机构，就能分清真认可和宣传稿。"},
    {"d": "2026-10-07", "type": "格局数据",
     "t": "欧委会 State-of-play：24 家 NAB 同意提供认可，7 国开放第三国通道",
     "s": "受理认可申请的 NAB 达 18 家；法国 COFRAC、希腊 ESYD、意大利 ACCREDIA、荷兰 RvA、波兰 PCA、斯洛伐克 SNAS、瑞典 Swedac 共 7 国的 NAB 受理第三国核查机构的申请，其中 5 国已实际开放受理。目前已走出成果的是希腊、意大利、瑞典三条线。",
     "takeaway": "中国机构要做 CBAM 核查，入口在这 7 国 NAB；对中国出口企业来说，这决定了未来可选机构的国别分布与现场核查成本。"}
]

d["cases"] = cases
d["regs"].append({"no": "ACCREDIA 决议 Rev.01", "cn": "意大利认可机构 CSA CI 2026-09-28 决议（修订版）",
                 "kind": "核验入口", "when": "2026-10-09 签署",
                 "what": "本期三家意大利机构的持证法人与活动组范围均取自此文件。注意：与其 10-06 新闻稿相比，RINA 增加了第 VIII 组，SGS 的范围也有改动，两份文本口径不一致，ACCREDIA 未作说明。",
                 "url": "https://www.accredia.it/wp-content/uploads/2026/10/Delibera_CSA_CI_2026-09-28-signed_REV01.pdf",
                 "urlLabel": "决议原件 ↗"})
d["regs"].append({"no": "ESYD 证书附件", "cn": "希腊认可机构证书 No.874-9 附件 V1/20",
                 "kind": "核验入口", "when": "2026-09-14",
                 "what": "EmiCert 的认可范围原文，逐组列示全部 11 个 CBAM 活动组，并载明依据 ELOT EN ISO 14065:2022 与 ELOT EN ISO 14064-3:2019。该附件取代 2026-03-23 的旧版。",
                 "url": "https://esyd.gr/wp-content/uploads/2026/09/EMICERT_874_8-_V1_20_17029_eng.docx",
                 "urlLabel": "附件原文 ↗"})

json.dump(d, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("cases:", len(d["cases"]), "| regs:", len(d["regs"]))
