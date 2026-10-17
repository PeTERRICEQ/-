"""彙整：各章 pick up spec 裡哪些引擎是共用本體的落地；各章遮住測試統計。輸出 shared_tally.json。"""
import importlib.util, glob, os, re, json, collections
HERE = os.path.dirname(os.path.abspath(__file__))
SPECS = os.path.join(HERE, "../../essence/specs")
SIG = [("把柄", ["探針只量一種物理量", "偵測器只量一種物理量"]), ("計量", ["讀數和量成正比", "偵測器讀數和量成正比"]),
       ("擴散", ["同一種分子走的路徑不同"]), ("能隙", ["光子能量 E＝hν 要剛好對上"]),
       ("解離", ["pH 對 pKa 決定", "質子只往比現在更想要它的地方走"]), ("分配", ["分子在兩相之間來回分配", "分子在固定相和流動相之間來回分配"]),
       ("光源", ["光源只放得出", "燈只放得出"])]
NAME = dict(spec="光譜概論", uv="UV", flu="螢光", irram="IR 與 Raman", nmr="NMR", aas="原子光譜", ripol="折光與旋光", ext="萃取",
            chr="層析概論", tlc="TLC", hplc="HPLC", gc="GC", sfc="SFC", ce="CE", ms="MS", naq="非水滴定", acid="水溶液酸鹼與中和",
            kfash="水分與灰分", valgen="確效與藥典通則", redox="氧化還原、電化學與錯合", pptid="沉澱、限量與鑑別", fatoil="油脂與揮發油")
def load(p):
    sp = importlib.util.spec_from_file_location("s_" + os.path.basename(p)[:-3], p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m.SPEC
def num(n):
    return sum(int(x) for x in re.findall(r"\d+", str(n))) if n is not None else 0
land = collections.defaultdict(list)
for p in sorted(glob.glob(os.path.join(SPECS, "*2.py"))):
    k = os.path.basename(p)[:-4]; S = load(p)
    for pk in ("p1", "p2", "p3", "p4"):
        for col in ("left", "right", "full", "bottom"):
            for b in (S.get(pk) or {}).get(col, []):
                if b.get("type") != "engine": continue
                v = b["vec"]
                for eng, sigs in SIG:
                    if any(v.startswith(s) or s in v[:80] for s in sigs):
                        land[eng].append(dict(ch=k, chn=NAME.get(k, k), L=b["L"], name=b["name"], n=num(b.get("n")))); break
mask = {}
for f in sorted(glob.glob(os.path.join(HERE, "*_mask.json"))):
    d = json.load(open(f)); c = collections.Counter(x.get("t") for x in d.values())
    old = [i for i in d if int(i[:3]) <= 107]; new = [i for i in d if int(i[:3]) >= 108]
    ok = lambda ids: sum(1 for i in ids if d[i].get("t") in ("Y", "2"))
    mask[os.path.basename(f)[:-10]] = dict(n=len(d), Y=c["Y"], two=c["2"], N=c["N"], old=[ok(old), len(old)], new=[ok(new), len(new)])
json.dump(dict(land=land, mask=mask), open(os.path.join(HERE, "shared_tally.json"), "w"), ensure_ascii=False, indent=1)
for e, L in land.items(): print(e, sum(x["n"] for x in L), [(x["chn"], x["L"], x["n"]) for x in L])
t = [sum(m[k] for m in mask.values()) for k in ("n", "Y", "two", "N")]
print("全書", t, f"{(t[1]+t[2])/t[0]:.1%}")
