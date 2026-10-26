# -*- coding: utf-8 -*-
"""生成《CBAM 核查机构信息披露榜单》宣传海报。

设计原则：纯本地渲染（模型写中文必出错字，中文一律本地压字），
深绿品牌底色 + 细网格/圆环装饰 + 白色信息卡 + 站点二维码。
输出 1080×1440（3:4）。
"""
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1440
M = 88
HERE = os.path.dirname(os.path.abspath(__file__))
DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
URL = "https://lichuanyou529-crypto.github.io/CBAM-/"

FONT_DIR = r"C:\Windows\Fonts"


def F(bold, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, "msyhbd.ttc" if bold else "msyh.ttc"), size)


# ---------- 配色 ----------
BG_TOP = (6, 52, 42)
BG_BOT = (11, 92, 74)
GREEN_LIGHT = (126, 222, 186)
GREEN_DIM = (62, 132, 110)
WHITE = (255, 255, 255)
WHITE_80 = (223, 240, 234)
MUTED = (156, 200, 186)
CARD_TITLE = (11, 91, 71)
CARD_URL = (26, 122, 98)
CARD_HINT = (124, 154, 144)

# ---------- 1. 渐变底 ----------
base = Image.new("RGB", (W, H))
d = ImageDraw.Draw(base)
for y in range(H):
    t = y / (H - 1)
    d.line([(0, y), (W, y)],
           fill=tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3)))

# ---------- 2. 装饰层：细网格 + 圆环 ----------
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
for x in range(0, W, 60):
    od.line([(x, 0), (x, H)], fill=(255, 255, 255, 10))
for y in range(0, H, 60):
    od.line([(0, y), (W, y)], fill=(255, 255, 255, 10))
od.ellipse([W - 360, -200, W + 200, 360], outline=(126, 222, 186, 48), width=2)
od.ellipse([W - 280, -120, W + 120, 280], outline=(126, 222, 186, 30), width=2)
od.ellipse([-280, H - 440, 320, H + 160], outline=(126, 222, 186, 26), width=2)
base = Image.alpha_composite(base.convert("RGBA"), ov).convert("RGB")
dr = ImageDraw.Draw(base)


def T(x, y, s, f, fill, anchor=None):
    dr.text((x, y), s, font=f, fill=fill, anchor=anchor)


# ---------- 3. 头部文字 ----------
T(M, 106, "Trade Free HOT · 你身边的合规专家", F(False, 30), GREEN_LIGHT)
T(M, 172, "CBAM 核查机构", F(True, 92), WHITE)
T(M, 288, "信息披露榜单", F(True, 92), WHITE)
dr.rectangle([M, 444, M + 300, 450], fill=GREEN_LIGHT)
T(M, 492, "四个模块，串起 CBAM 从业者最关心的一条信息链", F(False, 33), WHITE_80)
T(M, 545, "机构库  →  规则  →  案例  →  实操经验", F(False, 33), GREEN_LIGHT)

# ---------- 4. 三个数据 ----------
stats = [
    ("5", "家", "NAB 已公示机构"),
    ("11", "组", "CBAM 活动组逐组比对"),
    ("0", "家", "欧委会官方名录"),
]
colw = (W - 2 * M) / 3
nf, uf, lf = F(True, 68), F(False, 30), F(False, 25)
for i, (num, unit, label) in enumerate(stats):
    cx = M + colw * i
    dr.rectangle([cx, 668, cx + 4, 776], fill=GREEN_DIM)
    T(cx + 26, 660, num, nf, WHITE)
    wnum = dr.textlength(num, font=nf)
    dr.text((cx + 26 + wnum + 8, 700), unit, font=uf, fill=GREEN_LIGHT)
    T(cx + 26, 762, label, lf, MUTED)

T(M, 862, "数据基准日 2026-10-14 · 每周一更新 · 每条信息均标注来源", F(False, 24), MUTED)

# ---------- 5. 白色二维码卡 ----------
CX, CY, CW, CH, CR = 64, 920, W - 128, 340, 28
dr.rounded_rectangle([CX, CY, CX + CW, CY + CH], radius=CR, fill=(255, 255, 255))

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=1, border=2)
qr.add_data(URL)
qr.make(fit=True)
qimg = qr.make_image(fill_color=(11, 91, 71), back_color=(255, 255, 255)).convert("RGB")
n = qimg.size[0]
scale = max(1, 210 // n)
qimg = qimg.resize((n * scale, n * scale), Image.NEAREST)
qw = qimg.size[0]
qx = CX + 46
qy = CY + (CH - qw) // 2
base.paste(qimg, (qx, qy))

tx = qx + qw + 48
T(tx, 1006, "扫码查看完整榜单", F(True, 40), CARD_TITLE)
T(tx, 1074, URL, F(False, 24), CARD_URL)
T(tx, 1122, "手机扫码，或直接在浏览器打开这个网址", F(False, 22), CARD_HINT)

# ---------- 6. 底部免责 ----------
T(W / 2, 1322, "本榜衡量的是信息披露程度，不是机构能力排名 · 非官方内容已显著标注",
  F(False, 22), (140, 186, 172), anchor="ma")

# ---------- 7. 输出 ----------
p1 = os.path.join(HERE, "CBAM信息披露榜单-海报.png")
base.save(p1, quality=95)
print("已输出:", p1, base.size)

if os.path.isdir(DESKTOP):
    p2 = os.path.join(DESKTOP, "CBAM信息披露榜单-海报.png")
    base.save(p2, quality=95)
    print("已输出:", p2)
