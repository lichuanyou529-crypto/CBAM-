# -*- coding: utf-8 -*-
"""生成公众号封面：把中文标题/数据压到模型出的底图上（模型不写中文，避免错字）。

输出（WeChat 首图比例 2.35:1）：
  cover/公众号封面_1080x460.png
  cover/公众号封面_900x383.png
"""
import os, glob
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
COVER_DIR = os.path.join(BASE, 'cover')
OUT_DIR = os.path.join(BASE, 'cover')

# 找底图（排除已合成的成品）
cands = [p for p in sorted(glob.glob(os.path.join(COVER_DIR, '*.png')), key=os.path.getmtime)
         if not os.path.basename(p).startswith('公众号封面')]
src = cands[-1]
print('底图:', os.path.basename(src))

FONT_DIR = r'C:\Windows\Fonts'
F_BOLD = os.path.join(FONT_DIR, 'msyhbd.ttc')
F_REG = os.path.join(FONT_DIR, 'msyh.ttc')

def font(path, size):
    return ImageFont.truetype(path, size)

# 1) 裁成 2.35:1
im = Image.open(src).convert('RGB')
W, H = im.size
target_ratio = 2.35
tw, th = W, int(round(W / target_ratio))
if th > H:
    th = H; tw = int(round(H * target_ratio))
left = (W - tw) // 2
top = (H - th) // 2
im = im.crop((left, top, left + tw, top + th))
print('裁剪后:', im.size)

# 2) 左侧压一层暗色渐变，保证文字可读
ov = Image.new('L', (tw, th), 0)
d = ImageDraw.Draw(ov)
for x in range(tw):
    # 左侧最暗 ~55%，到 62% 宽度处衰减为 0
    if x < tw * 0.62:
        a = int(150 * (1 - x / (tw * 0.62)) ** 1.4)
    else:
        a = 0
    d.line([(x, 0), (x, th)], fill=a)
dark = Image.new('RGB', (tw, th), (6, 40, 31))
im = Image.composite(Image.blend(im, dark, 0.0), im, ov.point(lambda v: 255 - v))
# 上面 composite 用法不稳，改用 alpha 叠加
dark_layer = Image.new('RGBA', (tw, th), (6, 40, 31, 255))
dark_layer.putalpha(ov)
im = im.convert('RGBA')
im = Image.alpha_composite(im, dark_layer).convert('RGB')

dr = ImageDraw.Draw(im)
S = tw / 1080.0   # 以 1080 宽为设计基准做缩放

def T(x, y, text, f, fill, anchor=None):
    dr.text((int(x * S), int(y * S)), text, font=f, fill=fill, anchor=anchor)

# 3) 文字
GREEN_LIGHT = (126, 222, 186)
WHITE = (255, 255, 255)
WHITE_80 = (235, 245, 241)

f_eyebrow = font(F_REG, int(23 * S))
f_t1 = font(F_BOLD, int(78 * S))
f_t2 = font(F_BOLD, int(78 * S))
f_sub = font(F_REG, int(29 * S))
f_meta = font(F_REG, int(23 * S))
f_pill = font(F_BOLD, int(22 * S))

X = 64
T(X, 78, 'Trade Free HOT · 你身边的合规专家', f_eyebrow, (168, 226, 205))

# 主标题两行
T(X, 132, 'CBAM 核查机构', f_t1, WHITE)
T(X, 214, '信息披露榜单', f_t2, WHITE)

# 分隔线
y_line = 316
dr.line([(int(X * S), int(y_line * S)), (int((X + 300) * S), int(y_line * S))], fill=(126, 222, 186), width=max(2, int(4 * S)))

T(X, 338, '5 家已公示机构 · 11 个活动组逐组比对', f_sub, WHITE_80)
T(X, 382, '数据基准日 2026-10-14 · 每周一更新', f_meta, (176, 208, 199))

# 右侧胶囊：欧委会名录仍为 0 的对比（宽度按文字实测自适应，防止出界）
pill_text = '欧委会名录 0 家 · NAB 已公示 5 家'
tw_text = dr.textlength(pill_text, font=f_pill)
pad_x = int(20 * S)
ph = int(52 * S)
pw = int(tw_text) + pad_x * 2
px, py = tw - int(64 * S) - pw, int(60 * S)
pill = Image.new('RGBA', (pw, ph), (255, 255, 255, 30))
im.paste(Image.alpha_composite(
    Image.new('RGBA', pill.size, (255, 255, 255, 0)), pill), (px, py), pill)
dr.text((px + pad_x, py + int(13 * S)), pill_text, font=f_pill, fill=(214, 240, 232))

# 4) 输出
out_big = im.resize((1080, int(round(1080 / 2.35))), Image.LANCZOS)
out_small = im.resize((900, 383), Image.LANCZOS)
p1 = os.path.join(OUT_DIR, '公众号封面_1080x460.png')
p2 = os.path.join(OUT_DIR, '公众号封面_900x383.png')
out_big.save(p1)
out_small.save(p2)
print('已输出:')
print(' ', p1, out_big.size)
print(' ', p2, out_small.size)
