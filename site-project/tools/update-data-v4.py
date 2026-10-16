# -*- coding: utf-8 -*-
"""V4 数据调整：
1) 评分维度去掉「证书有效期」（CBAM 认可证书一年一审核，各机构有效期口径一致，不构成区分度）
   权重重排：scope 25->30，registry 15->20，其余不变，合计仍为 100
2) 各机构 d 对象删除 validity 键
3) 删除 bids / bidPortals（招标商机模块已下线）
4) meta.changelog 插入 V4 条目
"""
import json, io, os

P = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data.json'))
d = json.load(io.open(P, encoding='utf-8'))

# 1) dims
dims = d['dims']
dims = [x for x in dims if x['k'] != 'validity']
for x in dims:
    if x['k'] == 'scope':
        x['w'] = 30
    if x['k'] == 'registry':
        x['w'] = 20
d['dims'] = dims
total = sum(x['w'] for x in dims)
assert total == 100, '权重合计 %s != 100' % total

# 2) verifier d
for v in d['verifiers']:
    v.get('d', {}).pop('validity', None)

# 3) 移除招标商机数据
d.pop('bids', None)
d.pop('bidPortals', None)

# 4) changelog
d['meta']['changelog'].insert(0, {
    'd': '2026-10-14',
    't': '【V4 布局与口径调整】①站点布局改为左侧固定导航 + 单列信息流（信息流卡片带排名轨道），筛选栏改为胶囊控件；'
         '②「信息披露指数」评分维度由 7 项调整为 6 项：删除「证书有效期」维度——CBAM 认可证书均为一年一审核，'
         '各机构有效期口径一致，该维度不构成信息披露的区分度；权重重排为 nab15 / entity15 / cert15 / scope30 / registry20 / china5，'
         '合计仍为 100，各机构指数相应重算（证书有效期信息仍在卡片详情中展示，只是不再计分）；'
         '③应读者反馈，「⑤招标与商机信息」模块下线，页面聚焦机构库、法规、案例、实操经验四模块，'
         '案例模块新增「里程碑日历」视图（案例日期 + NAB 决议 / 官宣 / 认可生效与到期节点）。'
})

json.dump(d, io.open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('已写回', P)
print('dims:', [(x['k'], x['w']) for x in d['dims']], '合计', total)
W = {x['k']: x['w'] for x in dims}
for v in d['verifiers']:
    idx = round(sum(v['d'].get(k, 0) * w for k, w in W.items()))
    print('%-26s 新指数 %s' % (v['name'][:26], idx))
print('bids' in d, 'bidPortals' in d)
