# -*- coding: utf-8 -*-
"""圖0 v2.0｜Ni 總圖：翻譯＋驗證（四站退到背景）"""
import os
from nisvg import SVG, INK, MUTED, RED, PANEL
from common import *

os.makedirs(OUT, exist_ok=True)
s = SVG(1900, "pa0", "藥物分析全科｜Ni 總圖：翻譯＋驗證",
        "藥物分析 17 章的 Ni：把分子之間的一個差異翻譯成座標上的距離（探針、把柄、座標三格，每章不同），"
        "再用兩條全科共用的式子驗證讀數（寬度、誰在騙讀數）。四站 M01–M04 以淡色泳道留在背景。"
        "深灰實線為資訊流程，紅虛線為驗證不過時分析者的回查。示意，不按比例。")

y = header(s, "PHARMACEUTICAL ANALYSIS / 全科 17 章 / Ni＝翻譯＋驗證 / v2.0",
           "藥物分析全科｜Ni 總圖：翻譯＋驗證",
           "**母句：把分子之間的一個差異，翻譯成一條座標上的距離，再證明這個數字沒有騙你。**"
           "前半「翻譯」把 17 章分開；後半「驗證」是全科共用的。")
X0, W = 50, 1800

# ---------- 0. three subjects ----------
y += 30
subj = [
    ("藥理／藥化", "W", ["Ni 在問：藥物進去後，**系統長什麼形狀**？", "{{#61717a|自然形式：系統原型（回饋、增益、開關）}}"]),
    ("生物藥劑", "W", ["Ni 在問：藥量**怎麼流動、怎麼守恆**？", "{{#61717a|自然形式：存量、流量、速率常數}}"]),
    ("藥物分析", "F", ["Ni 在問：看不見的分子，**怎麼變成可信的數字**？", "自然形式：**翻譯＋驗證**（本圖）"]),
]
sw = (W - 2 * 20) / 3
hs = [s.card_h(sw, t, b, tsize=25, bsize=22, pad=18, gap=6) for t, st, b in subj]
hm = max(hs)
for i, (t, st, b) in enumerate(subj):
    s.card(X0 + i * (sw + 20), y, sw, t, b, st, tsize=25, bsize=22, pad=18, gap=6, min_h=hm)
y += hm + 14
y = s.para(X0, y, W, "四站 M01–M04 是 17 章共用的工作流程，每章長得都一樣，當 Ni 會沒有資訊量，所以這版把它退到背景；"
           "真正把 17 章分開的，是翻譯的三格。", 22, MUTED, 1.45) + 30

# ---------- 1. main diagram on swimlanes ----------
BW = W / 4
bx = [X0 + i * BW for i in range(4)]
CW = BW - 40          # card width inside a lane
cx = [b + 20 for b in bx]

# brackets
by = y + 10
s.line(X0 + 8, by + 24, X0 + 3 * BW - 12, by + 24, INK, 3)
s.line(X0 + 8, by + 14, X0 + 8, by + 34, INK, 3)
s.line(X0 + 3 * BW - 12, by + 14, X0 + 3 * BW - 12, by + 34, INK, 3)
s.text(X0 + 1.5 * BW, by + 8, "翻譯：①②③ 每章不同", 27, INK, 700, "middle")
s.line(X0 + 3 * BW + 12, by + 24, X0 + W - 8, by + 24, RED, 3)
s.line(X0 + 3 * BW + 12, by + 14, X0 + 3 * BW + 12, by + 34, RED, 3)
s.line(X0 + W - 8, by + 14, X0 + W - 8, by + 34, RED, 3)
s.text(X0 + 3.5 * BW, by + 8, "驗證：④⑤ 全科共用", 27, RED, 700, "middle")
lane_top = by + 50
at_lanes = s.mark()
lane_ids = [s.new_id() for _ in range(4)]
lane_lab = ["背景 M01 先定問題", "背景 M02 準備與測量", "背景 M03 讀訊號", "背景 M04 核對結論"]
for i in range(4):
    s.text(bx[i] + BW / 2, lane_top + 36, lane_lab[i], 21, MUTED, 400, "middle", box=lane_ids[i])
y1 = lane_top + 62

# lane 1
q_b, _ = s.card(cx[0], y1, CW, "問題",
                ["要知道什麼？身分、含量、雜質、結構、晶型、元素？",
                 "**先決定要保留什麼**：溶解就失去晶型；GC 要能氣化；旋光要保留掌性。"],
                "W", tsize=25, bsize=21, pad=18, gap=6)
d_top = q_b + 44
s.arrow([(cx[0] + CW / 2, q_b + 2), (cx[0] + CW / 2, d_top - 3)])
d_b, _ = s.card(cx[0], d_top, CW, "找一個差異",
                ["兩個分子之間，或分子與背景之間，**哪裡不一樣**？",
                 "能階、極化率、光速、分配、電荷、質量……這個差異就是接下來要放大的東西。"],
                "W", tsize=25, bsize=21, pad=18, gap=6)

# lane 2
p1_b, p1 = s.card(cx[1], y1, CW, "① 探針：用什麼碰？",
                  ["光子（含雷射、偏極光）", "第二相（液、固、氣、超臨界）", "電場", "先游離，再用電場、磁場或飛行時間分選"],
                  "W", tsize=25, bsize=21, pad=18, gap=4)
p2_top = p1_b + 44
s.arrow([(cx[1] + CW / 2, p1_b + 2), (cx[1] + CW / 2, p2_top - 3)])
s.text(cx[1] + CW / 2 + 12, p1_b + 30, "去碰", 20, MUTED)
p2_b, _ = s.card(cx[1], p2_top, CW, "② 把柄：碰到哪個差異？",
                 ["能階差｜極化率改變｜光速差（n、左右圓偏光）｜相間分配｜電荷與大小｜質量與電荷"],
                 "W", tsize=25, bsize=21, pad=18, gap=4)
# d -> p1
mid_d = (d_top + d_b) / 2
mid_p1 = (y1 + p1_b) / 2
chx = bx[1] + 2
s.arrow([(cx[0] + CW + 2, mid_d), (chx + 8, mid_d), (chx + 8, mid_p1), (cx[1] - 3, mid_p1)])

# lane 3
p3_b, _ = s.card(cx[2], y1, CW, "③ 座標：讀哪條軸？",
                 ["能量軸：λ、ṽ、δ", "時間或距離：tR、Rf、tm", "m／z", "單一數值：n、a",
                  "**位置** → 是誰（只支持，不證明）", "**大小** → 多少（校正後才是濃度）", "**形狀** → 環境或品質"],
                 "W", tsize=25, bsize=21, pad=18, gap=4)
mid_p2 = (p2_top + p2_b) / 2
mid_p3 = (y1 + p3_b) / 2
chx = bx[2] + 2
s.arrow([(cx[1] + CW + 2, mid_p2), (chx + 8, mid_p2), (chx + 8, mid_p3), (cx[2] - 3, mid_p3)])

# lane 4
v4_b, _ = s.card(cx[3], y1, CW, "④ 寬度：分得開嗎？",
                 ["**解析度＝位置差 ÷ 寬度**",
                  "拉大位置差：選擇性 α、換固定相或模式。縮小寬度：效率 N、控溫、減少展寬。"],
                 "A", tsize=25, bsize=21, pad=18, gap=6)
v5_top = v4_b + 40
s.arrow([(cx[3] + CW / 2, v4_b + 2), (cx[3] + CW / 2, v5_top - 3)])
v5_b, _ = s.card(cx[3], v5_top, CW, "⑤ 誰在騙讀數：量得準嗎？",
                 ["**讀數＝斜率 × 量＋背景**",
                  "扣背景（空白、斬光）；量斜率（外標、內標、標準添加）；找第二個獨立讀數（DAD、MS、二維）。"],
                 "F", tsize=25, bsize=21, pad=18, gap=6)
ok_top = v5_b + 40
s.arrow([(cx[3] + CW / 2, v5_b + 2), (cx[3] + CW / 2, ok_top - 3)])
ok_b, _ = s.card(cx[3], ok_top, CW, "符合 → 有條件的答案",
                 ["寫明方法、條件與範圍；身分只說證據支持到哪裡。"], "C", tsize=24, bsize=21, pad=16, gap=6)
mid_v4 = (y1 + v4_b) / 2
chx = bx[3] + 2
s.arrow([(cx[2] + CW + 2, mid_p3), (chx + 8, mid_p3), (chx + 8, mid_v4), (cx[3] - 3, mid_v4)])

content_b = max(d_b, p2_b, p3_b, ok_b)
# red return: from ⑤ left edge, down under lanes, back to ② bottom
ret_y = content_b + 40
v5_mid = (v5_top + v5_b) / 2
rx_ = bx[3] - 8
s.arrow([(cx[3] - 2, v5_mid + 30), (rx_, v5_mid + 30), (rx_, ret_y), (cx[1] + CW / 2, ret_y), (cx[1] + CW / 2, p2_b + 3)],
        RED, 3, dash="10 7")
lab_y = ret_y + 10
s.text(cx[1] + CW / 2 + 16, lab_y + 24, "驗證不過 → 改條件、換探針或換把柄（紅虛線＝分析者回查，不是分子繞圈）", 21, RED)
lane_bottom = lab_y + 50
for i in range(4):
    fill = "#efede3" if i % 2 == 0 else "#f3f1e8"
    s.rect(bx[i], lane_top, BW, lane_bottom - lane_top, "W", rx=0, sw=0, fill=fill, stroke=fill,
           rid=lane_ids[i], at=at_lanes)
y = lane_bottom + 40

# ---------- 2. translation table ----------
s.text(X0, y + 28, "翻譯表：17 章＝六組「探針 × 把柄 → 座標」", 27, INK, 700)
y += 48
widths = [230, 330, 450, 330, 460]
hdr = ["中循環", "① 探針", "② 把柄（被利用的差異）", "③ 座標", "章"]
rows = [
    ["Ⅰ 能量帳", "光子", "能階差：核自旋、振動、價電子、原子外層電子、晶格", "能量軸：δ（ppm）、ṽ（cm⁻¹）、λ（nm）",
     "光譜概論、NMR、IR、UV-Vis、螢光、原子光譜"],
    ["Ⅰ 能量帳（散射）", "雷射光子", "振動時極化率改變", "Raman 位移（cm⁻¹）", "Raman"],
    ["Ⅰ 能量帳（光速）", "不被吸收的光", "光速差：n；左右圓偏光速度差", "單一數值：n、a", "折光、旋光"],
    ["Ⅱ 時間帳", "第二相", "相間分配：極性、疏水、電荷、大小、揮發、掌性", "時間 tR、距離比 Rf、相量比 D",
     "萃取、層析概論、TLC、HPLC、GC、SFC／SFE"],
    ["Ⅱ 時間帳（電場）", "電場", "電荷與大小（淌度）", "遷移時間 tm", "CE"],
    ["Ⅲ 質荷帳", "先游離，再用電場或磁場", "質量與電荷", "m／z", "MS"],
]
y = table(s, X0, y, widths, hdr, rows, hsize=22, bsize=21, pad=12,
          head_styles=["G", "G", "G", "G", "G"]) + 40

# ---------- 3. how to use: Ni → 中層 → Ti → 小循環 ----------
s.text(X0, y + 28, "你的 Ni → Ti → 小循環，在藥分改成這樣走", 27, INK, 700)
y += 50
use = [
    ("1｜Ni：整科一張", "F", ["就是本圖的母句：翻譯＋驗證。", "不再每章各畫一個四站當 Ni。"]),
    ("2｜中層：五格指紋", "E", ["每章一張卡：①②③ 翻譯、④⑤ 驗證。", "17 張在「五格指紋卡」資料夾；並排比較看圖6。"]),
    ("3｜Ti：橫向接線", "A", ["不沿四站接，改沿共用變數接：下排六條線。", "圖6 直讀一欄，就是一條 Ti 線。"]),
    ("4｜小循環：標格號", "C", ["每條 L 標它在回答五格的哪一格。", "答錯先問：錯在翻譯，還是錯在驗證？"]),
]
uw = (W - 3 * 18) / 4
hs = [s.card_h(uw, t, b, tsize=24, bsize=21, pad=16, gap=6) for t, st, b in use]
hm = max(hs)
for i, (t, st, b) in enumerate(use):
    x = X0 + i * (uw + 18)
    s.card(x, y, uw, t, b, st, tsize=24, bsize=21, pad=16, gap=6, min_h=hm)
y += hm + 26

threads = [
    ("pH 開關", "pKa 兩側物種不同 → 吸收、螢光、保留、萃取、遷移方向與離子化一起改。",
     "UV L11–12｜螢光 L10｜TLC L08｜HPLC L09–10｜萃取 L03–04｜CE L08–09｜MS [M＋H]⁺"),
    ("溫度", "同時動到平衡、擴散與黏度；只讀一個數的方法最怕溫度。",
     "折光 L4｜旋光 L7｜螢光 L7｜GC L04–06｜SFC L07｜CE L14｜層析 L14"),
    ("背景與空白", "讀數＝目標訊號＋別人的訊號；先量別人，再扣掉。",
     "UV L01｜原子 L06｜Raman L5–6｜螢光 L12｜GC L06｜CE L24｜SFC L20"),
    ("歸一化", "把儀器條件除掉，剩下的才是物質指紋。",
     "NMR δ（L07）｜Raman 位移（L4）｜旋光 [α]（L6）｜層析 k′（L04）｜TLC Rf（L02）"),
    ("校正與內標", "斜率要用標準量出來；內標用比值抵消共同變動。",
     "UV L03｜螢光 L20｜原子 L13｜HPLC L23｜GC L24–25｜萃取 L26｜MS L30｜NMR L21"),
    ("晶型保留", "要問固態就不能先溶解；選能直接看固體的方法。",
     "光譜概論 L12｜IR L10｜Raman L8｜UV18｜XRD"),
]
tw_ = (W - 5 * 16) / 6
hs = [s.card_h(tw_, t, [a, b], tsize=23, bsize=19, pad=14, gap=6) for t, a, b in threads]
hm = max(hs)
for i, (t, a, b) in enumerate(threads):
    s.card(X0 + i * (tw_ + 16), y, tw_, "Ti 線｜" + t, [a, "{{#61717a|" + b + "}}"], "A", tsize=23, bsize=19,
           pad=14, gap=6, min_h=hm)
y += hm + 40

# ---------- 4. Ni test ----------
s.text(X0, y + 28, "怎麼確認這個 Ni 是真的：填一個講義沒教的方法", 27, INK, 700)
y += 50
tw2 = (W - 2 * 20) / 3
tests = [
    ("圓二色光譜 CD（講義外）", ["① 左、右圓偏光　② 掌性分子對兩者吸收不同　③ λ 軸上的吸收差 ΔA",
                            "推得出：要有掌性，也要有發色基；它是 UV 和旋光的交集。"]),
    ("離子遷移譜 IMS（講義外）", ["① 電場＋氣體　② 大小與電荷　③ 漂移時間",
                             "推得出：它就是在氣體裡跑的 CE；④ 寬度來自擴散，⑤ 要防共存離子。"]),
    ("最後一步：外部檢查", ["Ni 和 Ti 都在腦內，容易自己繞圈。",
                       "填完五格後，一定拿沒做過的國考題測：答得出、也說得出限制，才算抓到生成規則。"]),
]
hs = [s.card_h(tw2, t, b, tsize=24, bsize=21, pad=16, gap=6) for t, b in tests]
hm = max(hs)
for i, (t, b) in enumerate(tests):
    s.card(X0 + i * (tw2 + 20), y, tw2, t, b, "W", tsize=24, bsize=21, pad=16, gap=6, min_h=hm)
y += hm + 40

# ---------- 5. figure map ----------
s.text(X0, y + 28, "圖組地圖：Ni → 中層 → 小循環", 27, INK, 700)
y += 50
maps = [
    ("圖0 本圖 v2.0", "Ni：翻譯＋驗證；四站在背景。"),
    ("五格指紋卡 ×17", "每章一張：①②③ 翻譯、④⑤ 驗證。"),
    ("圖6 五格指紋矩陣", "17 章 × 5 格；直讀一欄＝Ti 線。"),
    ("圖1 能量帳", "光譜 9 章的中循環卡與能量梯子。"),
    ("圖2 時間帳", "分離 7 章與共同引擎 k′→α→N→Rs。"),
    ("圖3 質荷帳＋接點", "MS 與偵測器接點表。"),
    ("圖4 讀數與回查", "三讀數、定量六法、污染型、錯題路由。"),
    ("圖5 跨科類比", "藥理型別 ⑪–⑯ 與藥動同構。"),
]
mw = (W - 3 * 16) / 4
for r in range(2):
    row = maps[r * 4:(r + 1) * 4]
    hs = [s.card_h(mw, t, [b], tsize=23, bsize=20, pad=14) for t, b in row]
    hm = max(hs)
    for i, (t, b) in enumerate(row):
        s.card(X0 + i * (mw + 16), y, mw, t, [b], "W", tsize=23, bsize=20, pad=14, min_h=hm)
    y += hm + 16
y += 10
counts = "｜".join(f"{BY[k]['name']} {BY[k]['nL']}" for k in SPEC_I) + "　‖　" + \
         "｜".join(f"{BY[k]['name']} {BY[k]['nL']}" for k in SPEC_II) + "　‖　MS 33"
y = s.para(X0, y, W, f"**小循環共 {TOTAL_L} 條**（沿用各章 L 編號）：{counts}", 21, INK, 1.45) + 16
y = footer(s, y, [
    "v2.0 改動：主幹由四站大循環改為「翻譯＋驗證」，四站退為背景泳道；新增五格指紋卡 17 張與圖6。圖1–5 內容不變。",
    "旋光章原用 M01–M07，本組併入四站。CD、IMS 兩例在講義範圍外，只用來測試 Ni 能否生成新方法。",
    "來源：17 章建構講義（光譜 9 章 v2.0、分離與 MS 8 章 v3.0）與大小循環編譯器 v3.0；藥理型別名取自你的「大循環對撞台」頁面。示意，不按比例。",
])
h = s.save(os.path.join(OUT, FILES[0]), height=int(y + 30))
print("saved", FILES[0], h)
