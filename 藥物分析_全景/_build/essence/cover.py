"""覆蓋檢核：正解選項的關鍵詞有沒有出現在精華頁文字裡（字面比對，仿藥理藥化的做法）。
英文取 3 個字母以上的詞；沒有英文就取正解選項裡連續 3 個以上的中文字段。只有圖的題目列為「需看圖」。
用法：python3 essence/cover.py hplc"""
import json, os, re, sys


def load_spec(key):
    """用檔案路徑載入 specs/<key>.py（避免 gc 這類名字撞到內建模組）。"""
    import importlib.util
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "specs", f"{key}.py")
    sp = importlib.util.spec_from_file_location(f"yf_spec_{key}", path)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m.SPEC
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "../../.."))
Q = json.load(open(os.path.join(REPO, "藥物分析_全景/app/data/q.json"), encoding="utf-8"))
STOP = {"the", "and", "with", "for", "from", "are", "not", "has", "its", "this", "that", "which", "used", "was"}
def norm(s): return re.sub(r"[\s，、；：（）()＋+／/\-–—·・。,.:;]", "", s).lower()
ABBR = {"evaporative light scattering": "ELSD", "refractive index": "RI", "diode array": "DAD", "fluorescence detector": "螢光",
        "electron capture": "ECD", "electrochemical": "電化學", "octadecyl": "C18", "tetrahydrofuran": "THF", "acetonitrile": "ACN",
        "methanol": "MeOH", "flame ionization": "FID", "thermal conductivity": "TCD", "mass spectrometry": "MS"}
def check(key, chs=None):
    txt = open(os.path.join(HERE, "out", f"{key}.txt"), encoding="utf-8").read()
    for full, ab in ABBR.items():
        if ab.lower() in txt.lower(): txt += " " + full
    T, Tn = txt.lower(), norm(txt)
    chs = chs or [key]
    rows = []
    for q in Q:
        if not set(q["ch"]) & set(chs): continue
        ans = " ".join(q["o"].get(a, "") for a in q["a"]) or q["t"]
        en = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9\-]{2,}", ans) if w.lower() not in STOP]
        if en: hit = any(w.lower() in T for w in en); key_ = en
        else:
            zh = [x for x in re.findall(r"[一-鿿α-ωΑ-Ω0-9]{3,}", norm(ans))]
            grams = {z[i:i + 3] for z in zh for i in range(len(z) - 2)}
            hit = bool(grams) and sum(g in Tn for g in grams) >= max(1, len(grams) // 3); key_ = zh
        img = "［圖］" in q["s"] and not ans.strip()
        rows.append((q["id"], hit, img, key_[:4], q["s"][:60], ans[:60]))
    n = len(rows); h = sum(r[1] for r in rows)
    print(f"{key}：{h}/{n}（{h / n:.0%}）字面命中")
    for r in rows:
        if not r[1]: print("  ✗", r[0], "|", r[4], "=>", r[5], "| 詞", r[3])
    return rows
if __name__ == "__main__":
    import importlib
    sys.path.insert(0, os.path.join(HERE, "specs"))
    for k in sys.argv[1:]:
        S = load_spec(k)
        check(k, S.get("keys"))
