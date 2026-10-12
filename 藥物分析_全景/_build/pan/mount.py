"""從每章「圖2 小循環掛載點圖」讀出 L 掛在哪一個 M 站（依文件順序：L 標題之後第一個出現的 M 站；
框內沒寫就用最近的 M 標題）。NMR 的圖2 只分存檔點，改用講義母圖的站別（下方 OVERRIDE）。"""
import glob, html, os, re

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
FIGDIR = os.path.join(REPO, "藥物分析_全科大中小循環", "各章圖組")
# NMR：依圖1 母圖「第2站 L09→L12→L10→L11→L23；第3站 組數L02／位置L03／面積L04／分裂L05–L07；
# 第4站 L08、L17–L20、L21／L22、L24」與圖2「L13–L16 解較複雜的題（讀訊號）」
OVERRIDE = {"NMR": {1: 1, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 4, 9: 2, 10: 2, 11: 2, 12: 2, 13: 3, 14: 3,
                    15: 4, 16: 3, 17: 4, 18: 4, 19: 4, 20: 4, 21: 4, 22: 4, 23: 2, 24: 4}}
ST = {"第1站": 1, "第2站": 2, "第3站": 3, "第4站": 4}


def texts(svg):
    out = []
    for m in re.finditer(r"<text\b([^>]*)>(.*?)</text>", svg, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        fs = re.search(r'font-size="([\d.]+)"', m.group(1))
        if t:
            out.append((t, float(fs.group(1)) if fs else 0))
    return out


def mounts(ch):
    if ch in OVERRIDE:
        return dict(OVERRIDE[ch])
    f = glob.glob(os.path.join(FIGDIR, ch, "*圖2_*.svg"))[0]
    res, curL, lastM = {}, None, None
    for t, fs in texts(open(f, encoding="utf-8").read()):
        # 旋光：左欄是 M 站大標，之後的 L 框都歸它（先判斷，才不會被前一個 L 吃掉）
        if re.match(r"^M0\d\s", t) and fs >= 29:
            lastM, curL = int(t[2]), None
            continue
        if t.startswith("→"):
            continue
        mL = re.match(r"^L(\d{1,2})\s*｜", t)
        if mL:
            curL = int(mL.group(1))
            if curL not in res and lastM:
                res[curL] = ("hdr", lastM)
            continue
        ms = re.findall(r"M0(\d)", t)
        # 站名標題（框外、只有站名）：更新目前站
        if ms and not curL:
            lastM = int(ms[0])
        if ms and curL and (curL not in res or res[curL][0] == "hdr"):
            res[curL] = ("box", int(ms[0]))
    return {k: v[1] for k, v in res.items()}


if __name__ == "__main__":
    for d in sorted(os.listdir(FIGDIR)):
        m = mounts(d)
        print(f"{d:6}", len(m), " ".join(f"L{k}:M{v}" for k, v in sorted(m.items())))
