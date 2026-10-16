# -*- coding: utf-8 -*-
"""V3 收尾修补：
1) 删除 SGS 重复的两条 V3 更正历史（保留内容更完整的那条）
2) 为 EmiCert 补一条 V3 更正历史（note 已说明回调至 85，但 history 缺记录）
"""
import json, io, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data.json')
P = os.path.normpath(P)

d = json.load(io.open(P, encoding='utf-8'))

for v in d['verifiers']:
    name = v['name']

    # 1) SGS：去重 V3 条目
    if name.startswith('SGS'):
        hist = v.get('history', [])
        v3 = [h for h in hist if h.get('d') == '2026-10-14']
        if len(v3) > 1:
            # 保留最长的一条
            keep = max(v3, key=lambda h: len(h.get('t', '')))
            hist = [h for h in hist if h not in v3] + [keep]
            hist.sort(key=lambda h: h.get('d', ''), reverse=True)
            v['history'] = hist
            print('SGS: 合并 %d 条 V3 记录 -> 1 条' % len(v3))

    # 2) EmiCert：补 V3 记录
    if name.startswith('EmiCert'):
        hist = v.get('history', [])
        if not any(h.get('d') == '2026-10-14' for h in hist):
            hist.insert(0, {
                'd': '2026-10-14',
                't': 'V3 更正：已从 ESYD 官网直接下载认可证书附件（No.874-9，Annex V1/20）原样核对，确认为 11 组全覆盖；V2 标注的 LI／LII「待核验项」系误读附件中「对应 EU ETS 活动组」列的 n/a，予以撤回。披露指数由 65 回调至 85。'
            })
            v['history'] = hist
            print('EmiCert: 已补 V3 更正记录')
        # 同步修正 V2 条目里已失效的措辞
        for h in v['history']:
            if h.get('d') == '2026-10-13' and '仍列为待核验项' in h.get('t', ''):
                h['t'] = h['t'].replace('据此重算，披露指数由 85 调整至 65。LI／LII 仍列为待核验项。',
                                        '据此重算，披露指数由 85 调整至 65（该结论已于 V3 撤回）。')

json.dump(d, io.open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('\n已写回', P)

# 复核
d2 = json.load(io.open(P, encoding='utf-8'))
W = {'nab': 15, 'entity': 15, 'cert': 15, 'scope': 25, 'validity': 10, 'registry': 15, 'china': 5}
print('\n%-26s %-9s %-6s %-5s %s' % ('name', 'nab', 'index', '组数', 'history'))
for v in d2['verifiers']:
    idx = round(sum(v['d'].get(k, 0) * w for k, w in W.items()))
    print('%-26s %-9s %-6s %-5s %d 条' % (v['name'][:26], v['nab'], idx, len(v['scopeGroups']), len(v.get('history', []))))
