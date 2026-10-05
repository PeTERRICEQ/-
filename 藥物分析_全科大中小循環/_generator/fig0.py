# -*- coding: utf-8 -*-
"""圖0｜全科大循環 Ni 總圖"""
import os
from nisvg import SVG, INK, MUTED, RED, PANEL
from common import *

os.makedirs(OUT, exist_ok=True)
s = SVG(1900, "pa0", "藥物分析全科｜大循環 Ni 總圖",
        "藥物分析 17 章壓成一張圖：全科共用四站大循環 M01→M04；M02 分成三個中循環（能量帳、時間帳、質荷帳），"
        "匯流到 M03 的三個讀數（位置、大小、形狀），再到 M04 的兩條萬用式與回查。深灰實線為分析資訊流程，紅虛線為條件不符時分析者的回查。示意，不按比例。")

y = header(s, "PHARMACEUTICAL ANALYSIS / 全科 17 章 / 大・中・小循環 / v1.0",
           "藥物分析全科｜大循環 Ni 總圖",
           "**母句：分析＝把分子之間的一種差異，放大成一條座標上的距離；再用標準把讀數換回答案。**"
           "17 章只是換了「探針」與「座標」：光子讀能量、第二相讀時間、電荷讀質荷比。")

X0, X1 = 140, 1850
W = X1 - X0
CX = X0 + W / 2

# ---------- M01 ----------
y += 34
m01_top = y
y, m01 = s.card(X0, y, W, "M01｜先定問題：要回答什麼？要保留什麼？",
                ["身分、含量、雜質、結構、晶型，還是元素？**目的決定要保留的東西**："
                 "溶解後就問不到晶型（光譜概論 L12）；GC 要能完整氣化（GC L01）；旋光要保留掌性（旋光 L4）；"
                 "MS 先決定是分子還是元素（MS L33）。"], "W", bsize=23)
m01_mid = (m01_top + y) / 2

# ---------- branch to three medium loops ----------
gap = 30
cw = (W - 2 * gap) / 3
cols = [X0 + i * (cw + gap) for i in range(3)]
split_y = y + 44
s.arrow([(CX, y + 2), (CX, split_y)], head=False)
s.text(CX + 14, y + 34, "M02｜選一種探針去碰分子的把柄", 23, INK, 700)
s.arrow([(cols[0] + cw / 2, split_y), (cols[2] + cw / 2, split_y)], head=False)
fam_top = split_y + 40
for cx in cols:
    s.arrow([(cx + cw / 2, split_y), (cx + cw / 2, fam_top - 2)])

fam = [
    ("中循環Ⅰ｜能量帳：光子 × 能階（9 章）", "E",
     ["**探針**：光子（NMR 另加強磁場）。**把柄**：能階差、極化率、掌性、光速。",
      "**座標**：λ（nm）、ṽ（cm⁻¹）、δ（ppm）；折光、旋光只剩一個數（n、a）。",
      "**能量梯子（低→高）**：射頻＋B₀→核自旋（NMR）｜中紅外→振動（IR）｜近紅外→倍頻（NIR）｜"
      "紫外–可見→價電子（UV，再到螢光）｜原子窄線（AAS、AES）｜X 射線→晶格（XRD）。",
      "**側枝**：散射找零（Raman）；不換能量、只改光速（折光、旋光）。"],
     SPEC_I),
    ("中循環Ⅱ｜時間帳：第二相 × 分配（7 章）", "C",
     ["**探針**：第二相（固定相或另一液相）；CE 改用電場。**把柄**：極性、疏水、電荷、大小、揮發性、掌性。",
      "**座標**：時間 tR、tm（min）；距離比 Rf；萃取讀兩相量比。",
      "**核心**：分子只有在移動相時才前進 → tR＝t₀(1＋k′)。兩峰分開靠 α，峰窄靠 N。",
      "**路徑**：一次分配（萃取）→ 多次分配（層析）→ 換移動相：TLC、HPLC、GC、SFC → 換驅動力：CE。"],
     SPEC_II),
    ("中循環Ⅲ｜質荷帳：電荷 × 質量（1 章＋接點）", "D",
     ["**探針**：電場、磁場、飛行時間。**把柄**：質量與電荷。",
      "**座標**：m／z，不是分子量；要扣回電荷與加合物才得到中性 M。",
      "**核心**：先充電（離子源）→ 分選（分析器）→ 計數（偵測器）。",
      "**接點**：分離之後接偵測器，三個中循環在這裡縫合：UV／DAD、螢光、RI、MS、FID、ECD……（見圖3）"],
     SPEC_III),
]

col_bottoms = []
for i, (title, st, body, keys) in enumerate(fam):
    x = cols[i]
    at = s.mark()
    rid = s.new_id()
    pad = 22
    cy = fam_top + pad
    cy = s.para(x + pad, cy, cw - 2 * pad, title, 27, PANEL[st][1], 1.3, 700, box=rid) + 10
    for p in body:
        cy = s.para(x + pad, cy, cw - 2 * pad, p, 22, INK, 1.45, box=rid) + 8
    cy += 6
    for k in keys:
        c = BY[k]
        y2, _ = s.card(x + pad, cy, cw - 2 * pad, None,
                       [f"**{c['name']}**｜{c['arche']}　{{{{{MUTED}|L×{c['nL']}}}}}"], "W",
                       bsize=22, pad=12, rx=12)
        cy = y2 + 10
    if keys == SPEC_III:
        for t in ["偵測器｜把「到了」翻成訊號", "聯用｜GC-MS、LC-MS、SFC-MS、CE-MS"]:
            y2, _ = s.card(x + pad, cy, cw - 2 * pad, None, [f"**{t.split('｜')[0]}**｜{t.split('｜')[1]}"],
                           "W", bsize=22, pad=12, rx=12)
            cy = y2 + 10
    col_bottoms.append((x, cy, rid, st, at))

fam_bottom = max(b[1] for b in col_bottoms) + 12
for x, cy, rid, st, at in col_bottoms:
    s.rect(x, fam_top, cw, fam_bottom - fam_top, st, rid=rid, at=at)

# ---------- merge to M03 ----------
merge_y = fam_bottom + 44
for x, *_ in col_bottoms:
    s.arrow([(x + cw / 2, fam_bottom + 2), (x + cw / 2, merge_y)], head=False)
s.arrow([(cols[0] + cw / 2, merge_y), (cols[2] + cw / 2, merge_y)], head=False)
m03_top = merge_y + 40
s.arrow([(CX, merge_y), (CX, m03_top - 2)])

at = s.mark()
m03 = s.new_id()
pad = 22
cy = m03_top + pad
cy = s.para(X0 + pad, cy, W - 2 * pad, "M03｜讀座標：每一張圖都只有三種讀數", 27, PANEL["B"][1], 1.3, 700, box=m03) + 12
three = [
    ("位置 → 身分線索",
     ["光譜：λmax、ṽ、δ、元素特徵線", "分離：tR、Rf、tm、保留指數 I", "質譜：m／z",
      "**只能支持身分，不能單獨證明唯一身分。**"]),
    ("大小 → 含量",
     ["A、F、NMR 積分、峰面積、離子豐度", "Raman、發射強度、斑點深淺",
      "**經過校正才是濃度；不同化合物不能直接比面積。**"]),
    ("形狀 → 環境或品質",
     ["帶寬（氫鍵）、裂分 n＋1 與 J（鄰居）", "峰寬 N、拖尾、前伸、同位素峰群、電荷態間距",
      "**形狀先列候選原因，再用另一個讀數區分。**"]),
]
tw3 = (W - 2 * pad - 2 * 24) / 3
tops = cy
bots = []
for i, (t, b) in enumerate(three):
    bx = X0 + pad + i * (tw3 + 24)
    yb, _ = s.card(bx, tops, tw3, t, b, "W", tsize=25, bsize=22, pad=18)
    bots.append(yb)
cy = max(bots) + 14
cy = s.para(X0 + pad, cy, W - 2 * pad,
            "**沒有座標軸的方法**（折光 n、旋光 a）只剩一個數，裡面沒有別的峰可以互相核對 → 最依賴固定溫度、波長、溶劑與標準。",
            22, INK, 1.45, box=m03) + pad
m03_bottom = cy
s.rect(X0, m03_top, W, m03_bottom - m03_top, "B", rid=m03, at=at)

# ---------- M04 ----------
m04_top = m03_bottom + 50
s.arrow([(CX, m03_bottom + 2), (CX, m04_top - 2)])
at = s.mark()
m04 = s.new_id()
cy = m04_top + pad
cy = s.para(X0 + pad, cy, W - 2 * pad, "M04｜核對結論：兩條萬用式＋回查", 27, RED, 1.3, 700, box=m04) + 12
fw = (W - 2 * pad - 24) / 2
f1_b, _ = s.card(X0 + pad, cy, fw, "① 解析度＝位置差 ÷ 寬度",
                 ["層析：Rs＝2ΔtR／(W₁＋W₂)；MS：m／Δm；NMR：一級譜要 Δν／J 夠大；原子光譜：相近譜線可能重疊。",
                  "**想分開**：拉大位置差（選擇性 α、換固定相或模式），或縮小寬度（效率 N、控溫、減少展寬）。"],
                 "W", tsize=25, bsize=22, pad=18)
f2_b, _ = s.card(X0 + pad + fw + 24, cy, fw, "② 讀數＝斜率 × 量＋背景",
                 ["A＝(εb)·c；F≈(2.303KI₀Φεb)·c；峰面積＝響應因子×量；qNMR 面積正比核數。",
                  "**求斜率與扣背景**：空白、外標、內標（比值抵消共同變動）、標準添加（在基質裡量斜率）。"],
                 "W", tsize=25, bsize=22, pad=18)
cy = max(f1_b, f2_b) + 14
ok_top = cy
ok_b, okid = s.card(X0 + pad, cy, fw, "符合 → 交出有條件的答案",
                    ["寫明方法、條件與範圍；身分只說證據支持到哪裡。"], "C", tsize=24, bsize=22, pad=16)
bk_b, _ = s.card(X0 + pad + fw + 24, cy, fw, "不符 → 紅虛線回到真正出錯的站",
                 ["回 M01：方法或檢品選錯｜回 M02：pH、溫度、流速、電壓等條件｜回 M03：單位或座標讀錯（%T 與 A、Hz 與 ppm、m／z 與 M）"],
                 "F", tsize=24, bsize=22, pad=16)
cy = max(ok_b, bk_b) + pad
m04_bottom = cy
s.rect(X0, m04_top, W, m04_bottom - m04_top, "F", rid=m04, at=at)

# red return lines on the left channel
ret_from = [m04_bottom - 40, m04_bottom - 70, m04_bottom - 100]
targets = [(m01_mid, 64), (fam_top + 60, 86), (m03_top + 60, 108)]
for (ty, chx), fy in zip(targets, ret_from):
    s.arrow([(X0, fy), (chx, fy), (chx, ty), (X0 - 3, ty)], RED, 3, dash="10 7")
s.text(52, m04_bottom + 34, "紅虛線：分析者回查（不是分子自己繞圈）", 20, RED)

# ---------- threads ----------
y = m04_bottom + 70
s.text(X0, y + 30, "橫向主題線：同一個原理在不同章重複出現（考題最愛跨章換句話說）", 27, INK, 700)
y += 52
threads = [
    ("pH 開關", "pKa 兩側物種不同 → 吸收、螢光、保留、萃取、遷移方向與離子化一起改。",
     "UV L11–12｜螢光 L10｜TLC L08｜HPLC L09–10｜萃取 L03–04｜CE L08–09｜MS 的 [M＋H]⁺"),
    ("溫度", "溫度同時動到平衡、擴散與黏度；單一數值法最怕溫度。",
     "折光 L4｜旋光 L7｜螢光 L7｜GC L04–06｜SFC L07｜CE L14 焦耳熱｜層析 L14"),
    ("背景與空白", "讀數＝目標訊號＋別人的訊號；先量別人，再扣掉。",
     "UV L01｜原子 L06｜Raman L5–6｜螢光 L12｜GC L06｜CE L24｜SFC L20"),
    ("晶型保留", "要問固態，就不能先溶解；選能直接看固體的方法。",
     "光譜概論 L12｜IR L10｜Raman L8｜UV18｜XRD"),
    ("校正與內標", "斜率要用標準量出來；內標用比值抵消共同變動。",
     "UV L03｜螢光 L20｜原子 L13｜HPLC L23｜GC L24–25｜萃取 L26｜MS L30｜NMR L21"),
]
gw = (W - 4 * 18) / 5
hs = [s.card_h(gw, t, [a, b], tsize=24, bsize=20, pad=16) for t, a, b in threads]
hmax = max(hs)
for i, (t, a, b) in enumerate(threads):
    s.card(X0 + i * (gw + 18), y, gw, t, [a, "{{#61717a|" + b + "}}"], "A", tsize=24, bsize=20, pad=16, min_h=hmax)
y += hmax + 40

# ---------- figure map ----------
s.text(X0, y + 30, "圖組地圖：大 → 中 → 小", 27, INK, 700)
y += 52
maps = [
    ("圖0 本圖", "大循環：四站＋三個中循環＋三讀數＋兩條萬用式。"),
    ("圖1 能量帳", "光譜 9 章的中循環卡；每張卡掛該章小循環存檔點。"),
    ("圖2 時間帳", "分離 7 章：共同引擎 k′→α→N→Rs，再換移動相與驅動力。"),
    ("圖3 質荷帳＋接點", "MS 中循環；偵測器把光譜章接到分離章。"),
    ("圖4 讀數與回查", "三讀數總表、定量母式、讀數污染型、回查路由。"),
    ("圖5 跨科類比", "藥理型別庫 ⑪–⑯ 與藥動數學同構，各附類比界線。"),
]
mw = (W - 5 * 16) / 6
hs = [s.card_h(mw, t, [b], tsize=23, bsize=20, pad=14) for t, b in maps]
hmax = max(hs)
for i, (t, b) in enumerate(maps):
    s.card(X0 + i * (mw + 16), y, mw, t, [b], "W", tsize=23, bsize=20, pad=14, min_h=hmax)
y += hmax + 26

counts = "｜".join(f"{BY[k]['name']} {BY[k]['nL']}" for k in SPEC_I) + "　‖　" + \
         "｜".join(f"{BY[k]['name']} {BY[k]['nL']}" for k in SPEC_II) + "　‖　MS 33"
y = s.para(X0, y, W, f"**小循環共 {TOTAL_L} 條**（沿用各章 L 編號）：{counts}", 21, INK, 1.45) + 16
y = footer(s, y, [
    "讀法：大循環＝17 章共用的四站；中循環＝每章把四站換成自己的探針、把柄與讀數；小循環＝各章 L 卡，掛在某一站，取用上一站的資訊、交回下一站。",
    "旋光章原用 M01–M07 七格，本組併入四站：目的→（檢品＋光的準備＋作用）→讀數→歸一與判讀。",
    "來源：本次上傳之 17 章建構講義（光譜 9 章 v2.0、分離與 MS 8 章 v3.0）與大小循環編譯器 v3.0；藥理型別名稱取自你的「大循環對撞台」頁面。示意，不按比例。",
])
h = s.save(os.path.join(OUT, FILES[0]), height=int(y + 30))
print("saved", FILES[0], h)
