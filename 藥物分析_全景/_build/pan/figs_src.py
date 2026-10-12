"""一次性：把上傳的章節 SVG 依「章 × 圖種」改名存進 repo（只修簡體字與尺寸，不改內容）。
來源檔名是上傳時的雜湊前綴；之後重建只讀 repo 裡的 藥物分析_全科大中小循環/各章圖組/。"""
import glob, os, re, sys

UP = sys.argv[1] if len(sys.argv) > 1 else "/root/.claude/uploads/27534a2c-1e30-5d14-9da3-4fcd4627ac86"
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
OUT = os.path.join(REPO, "藥物分析_全科大中小循環", "各章圖組")
KIND = {"macro": "圖1_大循環母圖", "micro": "圖2_小循環掛載點圖", "map": "圖3_方法分類與大小循環對照",
        "inst": "圖4_儀器與操作考點", "calc": "圖5_公式與誤差判讀"}
# 章名（與網頁章名相同）→ 五張圖的上傳前綴（macro, micro, map, inst, calc）
SRC = {
    "光譜概論": ("03162b0c", "219ec588", "79ed2d79", "4c972215", "52d06391"),
    "UV": ("aae3b8e4", "db8238b3", "57ec171c", "6603ec77", "52977e4c"),
    "螢光": ("a19a7811", "5e5a67d7", "313b5c0a", "77be24a5", "29a6dd75"),
    "IR": ("2d24b0d6", "d5b6fb02", "5862b9a3", "7833b328", "df88b2c1"),
    "Raman": ("8c991d49", "c8e17e5b", "9d86fed9", "d8f84817", "f19837f2"),
    "NMR": ("29c8ee0b", "02c88785", "496700ab", "f771529f", "a6b2aa96"),
    "原子光譜": ("be982eb5", "4e18b99c", "1ad6028f", "718e3e97", "29ecf7fd"),
    "折光": ("d3fb9844", "1e79d298", "171e7aa6", "55f88302", "18ff345a"),
    "旋光": ("d32129e8", "0bc9965f", "43a97139", "f02c25f8", "a0c58c54"),
    "萃取": ("adf13c3c", "9ea89d22", "c6447324", "352324b7", "073e85ac"),
    "層析概論": ("6c166934", "7a49bdde", "efb03c9c", "813b3641", "3eb3f9e4"),
    "TLC": ("d89dd45c", "e95b1801", "21572e09", "ae0a0122", "dd1d0941"),
    "HPLC": ("34fba12f", "d813d63a", "48d1e6d6", "0d67ba0d", "ca21b985"),
    "GC": ("64d66c36", "76a61944", "4be1dc9b", "fb6fade9", "d980addf"),
    "SFC": ("cb72156d", "f410e059", "f7df1b7c", "202400fe", "10e3301b"),
    "CE": ("45fa65b3", "ee30af11", "f58729e8", "11c30ef6", "b2bf507b"),
    "MS": ("56e4ef94", "18311f0c", "f53a2c02", "e2f74798", "48084399"),
}
# 圖上的簡體字（逐字核對過的 6 處）
FIX = [("補偿", "補償"), ("编造", "編造"), ("模块", "模組"), ("學习", "學習"), ("阅讀", "閱讀"),
       ("讀数", "讀數"), ("具体", "具體"), ("侧面", "側面")]


def fix_size(s):
    """只有 viewBox、width="100%" 的圖：補上像素寬高，縮放時不變形。"""
    head = re.search(r"<svg\b[^>]*>", s).group(0)
    vb = re.search(r'viewBox="\s*[\d.\-]+[\s,]+[\d.\-]+[\s,]+([\d.]+)[\s,]+([\d.]+)', head)
    if not vb:
        return s
    w, h = vb.group(1), vb.group(2)
    nh = re.sub(r'\swidth="[^"]*"', "", head)
    nh = re.sub(r'\sheight="[^"]*"', "", nh)
    nh = nh.replace("<svg", f'<svg width="{w}" height="{h}"', 1)
    return s.replace(head, nh, 1)


def main():
    n = 0
    for ch, pres in SRC.items():
        d = os.path.join(OUT, ch)
        os.makedirs(d, exist_ok=True)
        for kind, pre in zip(KIND, pres):
            src = glob.glob(os.path.join(UP, pre + "-*.svg"))
            assert len(src) == 1, (ch, kind, pre, src)
            s = open(src[0], encoding="utf-8").read()
            ver = re.search(r"_(v\d+_\d+)\.svg$", src[0]).group(1)
            for a, b in FIX:
                s = s.replace(a, b)
            s = fix_size(s)
            open(os.path.join(d, f"{ch}_{KIND[kind]}_{ver}.svg"), "w", encoding="utf-8").write(s)
            n += 1
    print("wrote", n, "->", OUT)


if __name__ == "__main__":
    main()
