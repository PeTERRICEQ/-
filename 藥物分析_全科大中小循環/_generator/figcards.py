# -*- coding: utf-8 -*-
"""五格指紋卡：每章一張（翻譯 ①②③ ＋ 驗證 ④⑤）"""
import os
from nisvg import SVG, INK, MUTED, RED, PANEL
from common import *

D = os.path.join(OUT, CARD_DIR)
os.makedirs(D, exist_ok=True)
X0, W = 50, 1800


def cell(s, x, y, w, i, ans, st, formula=None, min_h=0, measure=False):
    num, name, q = FP_Q[i]
    body = []
    if formula:
        body.append(f"**{formula}**")
    body.append("{{#61717a|" + q + "}}")
    body.append(ans)
    if measure:
        return s.card_h(w, f"{num} {name}", body, tsize=27, bsize=23, pad=20, gap=8)
    yb, _ = s.card(x, y, w, f"{num} {name}", body, st, tsize=27, bsize=23, pad=20, gap=8, min_h=min_h)
    return yb


def make(k, idx):
    c = BY[k]
    fam = FAM_OF[k]
    fc = PANEL[fam][1]
    name = CHAP_FILE[k]
    s = SVG(1900, f"fp{idx:02d}", f"{c['name']}｜五格指紋卡",
            f"{c['name']}的五格指紋：翻譯三格（探針、把柄、座標）是本章和別章不同之處，"
            "驗證兩格（寬度、誰在騙讀數）對應全科共用的解析度式與讀數式。括號內為原章小循環 L 編號。示意。")
    y = header(s, f"PHARMACEUTICAL ANALYSIS / 五格指紋卡 / {name} / v1.0",
               f"{c['name']}｜{c['arche']}：五格指紋", c["line"])
    y += 18
    y = s.para(X0, y, W, f"**母式**　{c['eq']}　　{{{{{MUTED}|小循環 L×{c['nL']}}}}}", 23, INK, 1.45) + 30

    # ---- 翻譯 ----
    s.text(X0, y + 28, "翻譯　這一章和別章不同的地方", 27, fc, 700)
    y += 50
    gap = 56
    w3 = (W - 2 * gap) / 3
    hm = max(cell(s, 0, 0, w3, i, FP[k][i], fam, measure=True) for i in range(3))
    for i in range(3):
        x = X0 + i * (w3 + gap)
        cell(s, x, y, w3, i, FP[k][i], fam, min_h=hm)
        if i < 2:
            s.arrow([(x + w3 + 3, y + hm / 2), (x + w3 + gap - 4, y + hm / 2)])
    row1_b = y + hm
    s.text(X0 + w3 + 6, y + hm / 2 - 12, "去碰", 20, MUTED)
    s.text(X0 + 2 * w3 + gap + 2, y + hm / 2 - 12, "放大", 20, MUTED)

    # ---- 驗證 ----
    w2 = (W - 24) / 2
    c3x = X0 + 2 * (w3 + gap) + w3 / 2
    c4x = X0 + w2 / 2
    c5x = X0 + w2 + 24 + w2 / 2
    bus = row1_b + 34
    s.arrow([(c3x, row1_b + 2), (c3x, bus)], head=False)
    s.arrow([(c4x, bus), (c3x, bus)], head=False)
    y = bus + 70
    s.text(X0, bus + 50, "驗證　全科共用的兩條式子", 27, RED, 700)
    for cx in (c4x, c5x):
        s.arrow([(cx, bus), (cx, y - 3)])
    f4 = "解析度＝位置差 ÷ 寬度"
    f5 = "讀數＝斜率 × 量＋背景"
    hm = max(cell(s, 0, 0, w2, 3, FP[k][3], "A", f4, measure=True),
             cell(s, 0, 0, w2, 4, FP[k][4], "F", f5, measure=True))
    cell(s, X0, y, w2, 3, FP[k][3], "A", f4, min_h=hm)
    cell(s, X0 + w2 + 24, y, w2, 4, FP[k][4], "F", f5, min_h=hm)
    y += hm + 26

    y, _ = s.card(X0, y, W, None,
                  ["**答錯時先分流**：錯在翻譯（①–③：用錯探針、認錯把柄、讀錯座標或單位）→ 回該格括號裡的 L；"
                   "錯在驗證（④⑤：分不開、被假訊號騙）→ 也查圖4 的污染型與回查路由。",
                   "{{#61717a|小循環存檔點　" + c["loops"] + "}}"],
                  "W", bsize=22, pad=18, gap=8)
    y += 18
    y, _ = s.card(X0, y, W, None,
                  ["{{#61717a|背景流程（四站）：M01 先定問題，決定要保留什麼 → M02 放 ①② → M03 放 ③ → M04 放 ④⑤，符合才交出答案。}}"],
                  "W", bsize=20, pad=14, dash="8 6")
    y += 24
    y = footer(s, y, [f"來源：藥物分析_{name} 建構講義（括號內為原章 L 編號）。總覽與跨章比較見 圖0 與 圖6 五格指紋矩陣。示意。"])
    fn = f"藥物分析_{name}_五格指紋卡_v1_0.svg"
    s.save(os.path.join(D, fn), height=int(y + 26))
    return fn


ORDER = SPEC_I + SPEC_II + SPEC_III
for i, k in enumerate(ORDER, 1):
    print(make(k, i))
