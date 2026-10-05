# -*- coding: utf-8 -*-
"""圖2｜中循環Ⅱ 時間帳：分離七章"""
import os
from nisvg import SVG, INK, MUTED, RED, PANEL
from common import *

s = SVG(1900, "pa2", "藥物分析全科｜中循環Ⅱ 時間帳：分離七章",
        "分離 7 章的中循環：上方是共同的差速引擎（K→k′→α→N→Rs）與展寬模型，中段是一次分配到多次分配、再換移動相或驅動力的分支，"
        "下方 7 張卡把全科四站換成各章內容，並列出小循環存檔點與高頻陷阱。深灰實線為資訊流程或因果，示意，不按比例。")

y = header(s, "PHARMACEUTICAL ANALYSIS / 全科 / 中循環Ⅱ 時間帳 / v1.0",
           "中循環Ⅱ｜時間帳：第二相 × 分配（分離 7 章）",
           "**一句主幹：每個分子只有待在移動相時才會前進；越常被固定相留住，走得越慢。差速＝分離，時間（或距離）就是座標。**"
           "萃取只做一次分配；層析把分配重複幾千次；CE 換成電場推動。")
X0, W = 50, 1800
y += 26
y = mini_station_strip(s, X0, y, W, ["M01 先定問題", "M02 分配與遷移", "M03 讀時間座標", "M04 解析度與校正"]) + 34

# ---------- engine ----------
s.text(X0, y + 28, "共同引擎：從「偏愛哪一相」一路推到「分開了沒」", 27, INK, 700)
y += 50
eng = [
    ("K", "分配常數", "K＝cS／cM", "分析物本身偏愛哪一相；只看分子與兩相，不含體積。"),
    ("k′", "保留因子", "k′＝K·VS／VM＝(tR−t₀)／t₀", "在這支柱上被多延遲幾倍；tR＝t₀(1＋k′)。"),
    ("α", "選擇性", "α＝k′₂／k′₁", "兩峰中心拉開多少；後出 ÷ 先出，要扣掉 t₀。"),
    ("N", "效率", "N＝16(tR／W)²；H＝L／N", "峰有多窄；H 小、N 大較好。"),
    ("Rs", "解析度", "Rs＝2ΔtR／(W₁＋W₂)", "距離 ÷ 寬度；夠大才算分開。"),
]
n = len(eng)
gap = 40
ew = (W - (n - 1) * gap) / n
hs = [s.card_h(ew, f"{a}｜{b}", [c, d], tsize=25, bsize=21, pad=16, gap=6) for a, b, c, d in eng]
hm = max(hs)
for i, (a, b, c, d) in enumerate(eng):
    x = X0 + i * (ew + gap)
    s.card(x, y, ew, f"{a}｜{b}", [f"**{c}**", d], "C", tsize=25, bsize=21, pad=16, gap=6, min_h=hm)
    if i < n - 1:
        s.arrow([(x + ew + 3, y + hm / 2), (x + ew + gap - 4, y + hm / 2)])
y += hm + 20

kw = (W - 24) / 2
k1, _ = s.card(X0, y, kw, "三個旋鈕：Rs≈(√N／4)·((α−1)／α)·(k′／(1＋k′))",
               ["**N**：柱長、粒徑、流速、溫度　**α**：換固定相、移動相組成、pH、溫度　**k′**：溶劑強度、溫度。",
                "α＝1 時 N 再大也分不開；N 變 4 倍，Rs 才變 2 倍；k′ 太小幾乎不分離，太大只是拖時間。（層析 L10–L11）"],
               "W", tsize=24, bsize=21, pad=18)
k2, _ = s.card(X0 + kw + 24, y, kw, "為什麼峰會變寬：H＝A＋B／u＋Cu",
               ["**A** 多路徑（填充不均）　**B／u** 縱向擴散（流速慢時主導）　**Cu** 質傳跟不上（流速快時主導）。",
                "所以流速有最佳點，不是越快越好；薄膜、低黏度主要在壓 C 項，小粒徑同時壓 A 與 C。（層析 L12–L14、HPLC L24、SFC L05）"],
               "W", tsize=24, bsize=21, pad=18)
y = max(k1, k2) + 34

# ---------- branch tree ----------
s.text(X0, y + 28, "同一個引擎，換移動相或驅動力", 27, INK, 700)
y += 50
tw2 = 560
t1, ex_id = s.card(X0, y, tw2, "一次分配｜萃取",
                   ["兩相平衡一次就停；讀**哪一相、多少量**（D、q、回收）。", "pH 開關決定藥在哪一相。"],
                   "C", tsize=25, bsize=21, pad=18)
t2, chr_id = s.card(X0 + tw2 + 70, y, tw2, "多次分配｜層析概論",
                    ["沿著管柱重複分配幾千次 → 小差異累積成時間差；讀 **tR、面積、W**。"],
                    "C", tsize=25, bsize=21, pad=18)
s.arrow([(X0 + tw2 + 3, y + 50), (X0 + tw2 + 66, y + 50)])
s.text(X0 + tw2 + 2, y + 40, "重複", 20, MUTED)
note_x = X0 + 2 * (tw2 + 70)
t3, _ = s.card(note_x, y, W - (note_x - X0), "換驅動力｜CE",
               ["不靠分配，靠電荷與大小（淌度）；但讀數 tm、N、Rs 沿用層析的語言。MEKC、CEC 又把分配加回來。"],
               "W", tsize=25, bsize=21, pad=18, dash="8 6")
s.arrow([(X0 + 2 * tw2 + 73, y + 50), (note_x - 4, y + 50)], MUTED, 3, dash="8 6")
top_row_b = max(t1, t2, t3)
bus_y = top_row_b + 34
cx_chr = X0 + tw2 + 70 + tw2 / 2
s.arrow([(cx_chr, t2 + 2), (cx_chr, bus_y)], head=False)
br = [
    ("TLC", "毛細作用推溶劑上板", "可點樣；常溫", "Rf（距離比）"),
    ("HPLC", "幫浦推液體移動相", "溶得進移動相，不必氣化", "tR、面積"),
    ("GC", "載氣推氣態分子", "能完整氣化且耐熱", "tR、保留指數 I"),
    ("SFC", "超臨界 CO₂＋改質劑", "溶得進流體，不必氣化", "tR、k、α"),
]
bw = (W - 3 * 24) / 4
s.arrow([(X0 + bw / 2, bus_y), (X0 + 3 * (bw + 24) + bw / 2, bus_y)], head=False)
row_y = bus_y + 36
hs = [s.card_h(bw, a, [f"移動相：{b}", f"檢品：{c}", f"座標：{d}"], tsize=25, bsize=21, pad=16, gap=4) for a, b, c, d in br]
hm = max(hs)
for i, (a, b, c, d) in enumerate(br):
    x = X0 + i * (bw + 24)
    s.arrow([(x + bw / 2, bus_y), (x + bw / 2, row_y - 3)])
    s.card(x, row_y, bw, a, [f"移動相：{b}", f"檢品：{c}", f"座標：{d}"], "W", tsize=25, bsize=21, pad=16, gap=4, min_h=hm)
y = row_y + hm + 34

y = s.para(X0, y, W, "**怎麼讀下面每張卡：**卡片＝該章的中循環；M01–M04 是全科四站在這一章的樣子；括號裡是原章 L 編號；"
           "「小循環存檔點」照抄各章分組。", 22, INK, 1.45) + 22

# ---------- chapter cards ----------
cw = (W - 2 * 24) / 3
y = card_grid(s, X0, y, W, ["ex", "chr", "tlc", "hplc", "gc", "sfc"], 3, "C")
# last row: CE + comparison double-wide
hce = chapter_card(s, 0, 0, cw, BY["ce"], "C", measure=True)
cmp_body = [
    "**誰先出來**　正相（矽膠、TLC）：極性小者先走、Rf 大｜逆相 C18：極性大者先出｜分子篩：大分子先出（HPLC L15）｜"
    "GC 低極性柱：同系列沸點低者先出｜CE：陽離子 → 中性 → 陰離子（CE L06）。",
    "**pH 方向**　弱酸 pH↓ → 中性比例↑ → 逆相保留↑、萃入有機相↑；弱鹼反過來，pH↑ 才中性（萃取 L04、HPLC L09）。"
    "越過 pKa 約 2 單位後幾乎全翻，再加酸鹼沒有更好，還可能傷矽膠或藥（萃取 L12）。",
    "**一個旋鈕管全部成分**　柱溫（GC）與溶劑強度（HPLC）同時作用所有成分；早峰要弱、晚峰要強 → 程式升溫（GC L05）、梯度沖提（HPLC L11–L12）。",
    "**峰形回查**　拖尾 → 先查二級作用（殘餘矽醇，HPLC L08）、點樣與槽況（TLC L09）；CE 拖尾或前伸 → 導電不匹配與管壁吸附（CE L16）。",
    "**位置不是含量**　tR、Rf、tm 只回答誰；含量要面積＋校正；CE 遷移時間不同時面積要再除以 tm（CE L25）。",
]
hcmp = s.card_h(2 * cw + 24, "家族內對照：同一個時間帳，問法換了", cmp_body, tsize=26, bsize=21, pad=20, gap=8)
hm = max(hce, hcmp)
chapter_card(s, X0, y, cw, BY["ce"], "C", min_h=hm)
s.card(X0 + cw + 24, y, 2 * cw + 24, "家族內對照：同一個時間帳，問法換了", cmp_body, "W", tsize=26, bsize=21,
       pad=20, gap=8, min_h=hm)
y += hm + 30

y = footer(s, y, [
    "回查：讀不通先回卡上的「小循環存檔點」，再回原章 L。偵測器（UV、螢光、RI、FID、ECD、MS……）怎樣接在分離之後，見圖3；定量與回查路由見圖4。",
    "公式身分照各章公式護照：Rs 三因子式是等度、近高斯的近似；van Deemter 為簡化模型。來源：層析概論、TLC、HPLC、GC、SFC／SFE、萃取、CE 建構講義 v3.0。示意，不按比例。",
])
h = s.save(os.path.join(OUT, FILES[2]), height=int(y + 30))
print("saved", FILES[2], h)
