# -*- coding: utf-8 -*-
"""V5：法规模块按欧委会官网三大板块重构（立法和指南 / 注册 / 排放的验证）。
条目与链接来自 https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en
（2026-10-14 抓取核对）。"""
import json, io, os

P = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data.json'))
d = json.load(io.open(P, encoding='utf-8'))

SRC = 'https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en'

d['regsGroups'] = [
    {
        'id': 'leg', 'k': 'law',
        't': 'CBAM 立法和指南', 'en': 'CBAM legislation and guidance',
        'url': SRC,
        'desc': '碳边境调节机制的全部法律文本：基础条例（管"要不要做"）、实施细则（管"怎么算、怎么报"）、授权条例（管"谁来查"），以及欧委会发布的官方指南。'
    },
    {
        'id': 'reg', 'k': 'impl',
        't': 'CBAM 注册', 'en': 'CBAM registry',
        'url': SRC,
        'desc': 'CBAM 登记库（Registry）的设立与运行规则：授权申报人、进口商、海关与核查相关数据在登记库中的登记、查询与管理。'
    },
    {
        'id': 'ver', 'k': 'del',
        't': 'CBAM 排放的验证', 'en': 'Verification of CBAM emissions',
        'url': 'https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-verification_en',
        'desc': '排放核查的规则与参与方：核查原则、内嵌排放量计算方法、核查机构认可与核查行为规范，以及欧委会核查指南原文。'
    },
]

g1 = [
    ('Regulation (EU) 2023/956', 'CBAM 基本条例：创立碳边境调节机制，2023-05-17 生效', 'law', 'http://data.europa.eu/eli/reg/2023/956/oj'),
    ('Regulation (EU) 2025/2083', '简化与强化 CBAM 的修订条例（正式期制度调整）', 'law', 'http://data.europa.eu/eli/reg/2025/2083/oj'),
    ('Regulation (EU) 2023/956 并合版（2025-10-20）', '并入 2025/2083 修订后的基本条例现行有效文本', 'law', 'http://data.europa.eu/eli/reg/2023/956/2025-10-20'),
    ('Implementing Regulation (EU) 2023/1773', '过渡期实施细则：申报方法、排放核算与数据要求', 'impl', 'http://data.europa.eu/eli/reg_impl/2023/1773/oj'),
    ('Implementing Regulation (EU) 2025/2210', '运抵成员国大陆架 / 专属经济区的货物及加工产品的申报', 'impl', 'http://data.europa.eu/eli/reg_impl/2025/2210/oj'),
    ('Implementing Regulation (EU) 2025/486', '授权 CBAM 申报人（Authorised CBAM Declarant）资格规则', 'impl', 'http://data.europa.eu/eli/reg_impl/2025/486/oj'),
    ('Implementing Regulation (EU) 2025/2549', '授权申报人资格规则的更正案', 'impl', 'http://data.europa.eu/eli/reg_impl/2025/2549/oj'),
    ('Implementing Regulation (EU) 2025/2548', 'CBAM 证书价格的计算与公布方法', 'impl', 'http://data.europa.eu/eli/reg_impl/2025/2548/oj'),
    ('Implementing Regulation (EU) 2025/2619', '海关部门向 CBAM 主管机关传递信息的数据集', 'impl', 'http://data.europa.eu/eli/reg_impl/2025/2619/oj'),
    ('Implementing Regulation (EU) 2025/2620', '免费配额调整量（应清缴证书数量的计算）', 'impl', 'http://data.europa.eu/eli/reg_impl/2025/2620/oj'),
    ('Implementing Regulation (EU) 2025/2621', '默认值（default values）的确立', 'impl', 'http://data.europa.eu/eli/reg_impl/2025/2621/oj'),
    ('Implementing Regulation (EU) 2026/1740', '默认值确立的更正案（2026 年 7 月更新）', 'impl', 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202601740'),
]
g3_impl = [
    ('Implementing Regulation (EU) 2025/2546', '核查原则的适用：核查机构执行核查的方法与行为规范', 'impl', 'http://data.europa.eu/eli/reg_impl/2025/2546/oj'),
    ('Implementing Regulation (EU) 2025/2547', '货物内嵌排放量的计算方法（核查取数的依据）', 'impl', 'http://data.europa.eu/eli/reg_impl/2025/2547/oj'),
]
g3_del = [
    ('Delegated Regulation (EU) 2025/2551', '认可与核查授权条例：核查机构认可、11 个活动组范围与核查要求', 'del', 'http://data.europa.eu/eli/reg_del/2025/2551/oj'),
]
g3_gd = [
    ('Guidance on CBAM verification and accreditation', '欧委会官方指南：核查机构与国家认可机构如何执行 CBAM 核查与认可（2026-08-24 发布，PDF）', 'gd', 'https://taxation-customs.ec.europa.eu/document/download/030fe146-38e5-46b8-82b5-5f72da089a7b_en?filename=GUIDANCE%20ON%20CBAM%20VERIFICATION%20AND%20ACCREDITATION%20FOR%20VERIFIERS%20AND%20NATIONAL%20ACCREDITATION%20BODIES.pdf'),
]

d['regsGroups'][0]['items'] = [{'t': t, 'zh': zh, 'k': k, 'url': u} for t, zh, k, u in g1]
d['regsGroups'][1]['items'] = [
    {'t': 'Implementing Regulation (EU) 2024/3210（并合版）', 'zh': 'CBAM 登记库实施细则：登记库的结构、账户与数据管理（2026-01-01 并合版）', 'k': 'impl', 'url': 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02024R3210-20260101'},
    {'t': 'Implementing Regulation (EU) 2025/2550', 'zh': 'CBAM 登记库实施细则的修订 / 更正案', 'k': 'impl', 'url': 'http://data.europa.eu/eli/reg_impl/2025/2550/oj'},
]
d['regsGroups'][2]['items'] = [{'t': t, 'zh': zh, 'k': k, 'url': u} for t, zh, k, u in (g3_impl + g3_del + g3_gd)]

d.pop('regs', None)

d['meta']['changelog'].insert(0, {
    'd': '2026-10-14',
    't': '【V5 法规模块重构】按欧委会 CBAM 官网三大板块重新组织：①CBAM 立法和指南（12 条法律文本）②CBAM 注册（2 条登记库实施细则）'
         '③CBAM 排放的验证（核查原则、计算方法、2025/2551 授权条例与官方核查指南）。全部条目抓取并核对自欧委会官网'
         ' cbam-legislation-and-guidance 页面，链接直达 EUR-Lex 原文；原 regs 卡片列表下线。'
         '同时②③④三个模块的列表改为热榜式行设计（排名序号 + 细分割线 + 悬停高亮）。'
})

json.dump(d, io.open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('regsGroups:')
for g in d['regsGroups']:
    print(' -', g['t'], len(g['items']), '条')
print('regs 残留:', 'regs' in d)
