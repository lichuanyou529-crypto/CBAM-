# -*- coding: utf-8 -*-
"""2026-11-09 当日补录：SGS Belgium N.V. 获比利时 BELAC 的 CBAM 核查机构认可。

背景：当日晨间核验（本期第 9 期）未检索到该官宣，初稿记「本周无新增机构，维持 7 家」；
下午复核发现 SGS 官网 2026-11-06 新闻《Strengthening European CBAM Verification Capabilities
with Belgian Accreditation》，据此补录，机构数由 7 家增至 8 家。
口径：官宣范围为行业口径（水泥／铝／化肥／钢铁／氢／电力），非 (EU) 2025/2551 附件 I 的
活动组口径；BELAC 官网新闻页与认可库暂无对应条目，故 NAB 公示项记 0.5，披露指数 27.5。
"""
import json, io, os

P = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data.json'))
d = json.load(io.open(P, encoding='utf-8'))

names = [v['nameEn'] for v in d['verifiers']]
assert 'SGS BELGIUM N.V.' not in names, 'SGS BELGIUM N.V. 已存在，勿重复录入'

# ── 1) 新增机构卡片 ──────────────────────────────────────────────
sgs_be = {
    "name": "SGS 比利时",
    "nameEn": "SGS BELGIUM N.V.",
    "group": "SGS 集团（瑞士）",
    "groupNote": "持证主体为集团比利时公司。SGS 集团至此在欧盟有两个 CBAM 持证法人（意大利 SGS ICS ITALIA S.R.L. 与本条），官宣称两者互补，合称可覆盖全部 CBAM 行业",
    "nab": "BELAC",
    "nabCn": "比利时",
    "announced": "2026-11-06",
    "nabDecided": None,
    "entity": "SGS BELGIUM N.V.（比利时）",
    "certNo": "未公开（官宣未载明认可证书编号）",
    "standard": "未公开（CBAM 认可统一依据 EN ISO/IEC 17029:2019；BELAC 名录条目待核验）",
    "validFrom": None,
    "validTo": None,
    "scopeGroups": [],
    "scopePending": [],
    "scopeText": "官宣载明覆盖<b>水泥、铝、化肥、钢铁、氢、电力</b>六大品类——这是<b>行业口径，不是 (EU) 2025/2551 附件 I 的活动组口径</b>。11 个活动组的逐组授权未载明，待 BELAC 认可附件核验。",
    "route": "由比利时 NAB BELAC 授予（机构官宣口径；BELAC 官网新闻页与认可库暂未见对应公示条目）",
    "registry": "未公开，须在取得认可后两个月内完成 CBAM 登记库注册",
    "officialListed": False,
    "china": {
        "v": 1,
        "t": "SGS 集团中国法人通标标准（SGS-CSTC）服务网络成熟，2026-11-05 以中文发布《聚焦CBAM｜碳价持续走高》企业问答并举办 CBAM 正式核查研讨会；持证主体为比利时法人，中国团队能否执行现场核查须向机构书面确认。"
    },
    "site": "https://www.sgs.com/",
    "srcs": [
        "SGS 官网新闻《Strengthening European CBAM Verification Capabilities with Belgian Accreditation》（2026-11-06，en-sg/en-tr 等多区域版本一致）",
        "SGS 通标中文稿《聚焦CBAM｜碳价持续走高！企业如何应对2027年CBAM核查》（2026-11-05，sgsonline.com.cn）",
        "BELAC 官网新闻页（2026-11-09 复核：无 SGS Belgium CBAM 条目；最新一条为 2026-10-30 招募 EU ETS／CBAM／EUMR 评审专家）"
    ],
    "note": "<b>待核验项：</b>①BELAC 认可库条目与<b>认可编号</b>——本榜 2026-11-09 复核，BELAC 官网新闻页无对应公告，认可库中是否有 CBAM 专项条目未查到；②<b>逐组活动组范围</b>——官宣只到「行业」一层（水泥／铝／化肥／钢铁／氢／电力），行业到活动组的拆分（如钢铁=V+VIII？化肥=III+IV？电力=LI？）只能以 BELAC 认可附件为准，签约前务必索取原件逐组核对；③有效期。三者缺任何一项都不能作为合同依据。<br><b>口径提示：</b>①这是比利时首例、全榜第 8 家持证机构；②与 SGS ICS ITALIA S.R.L.（意大利）是<b>两个独立持证法人，认可范围互不通用</b>——签合同时认准法人主体，不要拿意大利的范围当比利时的用；③「覆盖全部 CBAM 行业」是集团合并口径，不代表任一单法人可全范围核查。",
    "d": {"nab": 0.5, "entity": 1, "cert": 0, "scope": 0, "registry": 0, "china": 1},
    "biz": {
        "price": "未公开",
        "pricing": "未公开（签约前须向机构索取书面报价）",
        "area": "比利时法人持证；集团口径为 100 余国服务网络（含中国）",
        "langs": "英文 / 法文 / 荷兰文；集团中国团队提供中文服务",
        "ob": "未公开（可否做 OB 联合现场核查须向机构确认）"
    },
    "tags": {
        "sign": "有（机构官宣已获 BELAC 认可；认可编号与登记库注册状态未公开）",
        "remote": "未公开",
        "annual": "待向机构确认"
    },
    "history": [
        {
            "d": "2026-11-09",
            "t": "本榜首次收录（当日补录）。依据 SGS 官网 2026-11-06 官宣：SGS Belgium N.V. 获比利时 BELAC 的 EU CBAM 核查机构认可，范围载为水泥／铝／化肥／钢铁／氢／电力六大品类（行业口径）。认可编号、逐组附件与有效期均未公示，BELAC 官方渠道暂无对应条目，披露指数 27.5。"
        }
    ]
}
d['verifiers'].append(sgs_be)

# ── 2) SGS 意大利卡片补一条历史 ─────────────────────────────────
for v in d['verifiers']:
    if v['nameEn'] == 'SGS ICS ITALIA S.R.L.':
        v['history'].insert(0, {
            "d": "2026-11-09",
            "t": "集团第二家持证法人落地：SGS Belgium N.V. 于 2026-11-06 官宣获比利时 BELAC 认可（本榜第 8 家）。两家为独立法人，认可范围互不通用。"
        })

# ── 3) NAB 行：比利时 BELAC 备注 ───────────────────────────────
for n in d['nabs']:
    if n['a'] == 'BELAC':
        n['rm'] = ('已出 SGS Belgium N.V.（2026-11-06 机构官宣；范围载为水泥／铝／化肥／钢铁／氢／电力六大品类，'
                   '认可编号与逐组附件未公示，本渠道官网新闻与认可库暂无对应条目；另于 2026-10-30 发布招募 '
                   'EU ETS／CBAM／EUMR 评审专家的公告）')

# ── 4) 修订当日 changelog：撤回「无新增」结论 ───────────────────
old_head = '【本周核验：口径差异消失，机构数维持 7 家】'
new_head = '【本周核验：SGS 比利时补录，机构数 7→8 家】'
old_5 = '⑤ 本周<b>无新增机构</b>，逐项复核：Swedac 认可库'
new_5 = ('⑤ <b>新增机构 1 家（当日补录）</b>：SGS 官网 2026-11-06 官宣 <b>SGS Belgium N.V. 获比利时 BELAC 的 '
         'CBAM 核查机构认可</b>——比利时首例、全榜第 8 家、SGS 集团第 2 个持证法人。范围载为<b>水泥、铝、化肥、'
         '钢铁、氢、电力</b>六大品类（<b>行业口径，非活动组口径</b>），认可编号、逐组附件与有效期均未载明；'
         'BELAC 官网新闻页（最新一条为 2026-10-30 招募 EU ETS／CBAM／EUMR 评审专家）与认可库暂无对应条目，'
         '故 NAB 公示项记 0.5，披露指数 27.5。<b>当日晨间核验未检索到该官宣，初稿曾记「本周无新增机构」，'
         '下午复核时补录并同步修订本条。</b>其余逐项复核：Swedac 认可库')
hit = 0
for c in d['meta']['changelog']:
    if c['d'] == '2026-11-09' and old_head in c['t'] and old_5 in c['t']:
        hit += 1
        c['t'] = c['t'].replace(old_head, new_head).replace(old_5, new_5)
        # 在 ⑥ 之前追加 TÜV SÜD 待核验一句
        c['t'] = c['t'].replace('⑥ 下一节点', '另：第三方目录（cruxi.ai）称「TÜV SÜD 经 DAkkS 获 CBAM 认可」，DAkkS 官网无对应公示，与「DNV SE」一并挂待核验项，未收录。⑥ 下一节点')
assert hit == 1, f'期望恰好命中 1 条主 changelog，实际 {hit} 条'

# ── 5) 时间轴：插入 2026-11-06 ─────────────────────────────────
tl_dates = [t['d'] for t in d['timeline']]
assert '2026-11-06' not in tl_dates
i15 = tl_dates.index('2026-11-15')
d['timeline'].insert(i15, {
    "d": "2026-11-06",
    "t": "SGS 官宣：SGS Belgium N.V. 获 BELAC 认可",
    "s": "比利时首例、全榜第 8 家。官宣范围为水泥／铝／化肥／钢铁／氢／电力六大品类（行业口径），认可编号与逐组附件未公示。",
    "done": 1
})

# ── 6) 案例榜：插入认可里程碑 ──────────────────────────────────
d['cases'].insert(0, {
    "d": "2026-11-06",
    "type": "认可里程碑",
    "t": "BELAC 发出比利时首张 CBAM 核查认可——SGS Belgium N.V.（全榜第 8 家）",
    "s": "SGS 官网（2026-11-06）官宣 SGS Belgium N.V. 获比利时国家认可机构 BELAC 的 EU CBAM 核查机构认可，范围载为水泥、铝、化肥、钢铁、氢、电力六大品类，并称与意大利 SGS ICS ITALIA S.R.L. 已持有的 CBAM 认可形成互补。这是第 5 个出现持证机构的国家（希腊、意大利、瑞典、荷兰之后），也是 SGS 集团第 2 个持证法人。BELAC 官网新闻页与认可库暂无对应公示条目；同页最新新闻为 2026-10-30 BELAC 招募 EU ETS／CBAM／EUMR 评审专家。",
    "takeaway": "两点值得注意：①<b>发证国家首次 +1</b>——此前 4 家全部出自希腊／意大利／瑞典／荷兰四条线，比利时入列意味着产能线在增加（BELAC 还在扩招评审专家）；②SGS 成为<b>第一家「双法人持证」集团</b>，但两个法人的认可范围互不通用——合同认准法人主体，意大利的范围不能当比利利用。范围口径仍是行业（六大品类）而非活动组，签约前须索取 BELAC 附件原件逐组核对。",
    "tags": ["认可里程碑", "BELAC", "比利时", "SGS", "第 8 家"],
    "src": "SGS 官网新闻《Strengthening European CBAM Verification Capabilities with Belgian Accreditation》（2026-11-06）；BELAC 官网新闻页（2026-11-09 复核）"
})

json.dump(d, io.open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('补录完成：SGS Belgium N.V.（BELAC）')
print('  机构数 :', len(d['verifiers']))
print('  时间轴 :', len(d['timeline']), '条（含 2026-11-06）')
print('  案例   :', len(d['cases']), '条（最新', d['cases'][0]['d'], '）')
print('  基准日 :', d['meta']['dataAsOf'])
