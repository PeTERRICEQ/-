"""TLC 遮住測試（只看 p1 三個本體＋p2 零件卡綠底）。v0＝只看共用標準句（分配、把柄）。"""
import json, os
E1, E2, E3 = "E1", "E2", "E3"
M = {}
V0 = set()
def a(i, E, t, why, v0=False):
    M[i] = dict(E=E, t=t, why=why)
    if v0: V0.add(i)
# ── E1 Rf ──
a("100-1-40", E1, "Y", "酸性物 HA、A⁻ 兩型 Rf 不同 → 拖尾；加 acetic acid 壓成 HA 一型")
a("101-1-34", E1, "Y", "數氫鍵點：ibuprofen 只有 COOH → 最不像矽膠、Rf 最大；選項中只有 A 把 ibuprofen 放最後", True)
a("107-1-14", E1, "Y", "鹽最像矽膠（最極性）→ sodium phosphate Rf 最小", True)
a("108-1-29", E1, "Y", "石蠟是油的固定相：碳鏈最長、最飽和 → 最油 → 待最久 → stearic acid Rf 最小", True)
a("110-2-37", E1, "Y", "serine 側鏈 OH 最極性 → 最像矽膠 → Rf 最小", True)
a("112-1-29", E1, "Y", "越極性越像矽膠、走越短 → Rf X > Z > Y", True)
a("114-2-39", E1, "Y", "retinoic acid 有 COOH 最極性 → Rf 最小", True)
a("115-1-37", E1, "Y", "去掉酯多一個游離 OH → 更像矽膠 → Rf < 0.51；只多一個 OH、不是鹽 → 0.20 而非 0.05", True)
# ── E2 把柄 ──
a("101-1-32", E2, "Y", "F254 背景發螢光，吸 UV 的分析物遮光 → 所在處背景螢光消失")
a("102-1-33", E2, "Y", "皮質類固醇 α-ketol 側鏈可還原 → tetrazolium 被還原成藍色 formazan")
a("103-1-37", E2, "Y", "胺醣有游離 NH₂ → ninhydrin", True)
a("104-1-35", E2, "Y", "胜肽有游離 NH₂（N 端、lysine）→ ninhydrin", True)
a("105-2-31", E2, "Y", "反應型呈色劑把分子改掉；碘只溶進斑點、會昇華走 → 可逆、回收影響最小")
a("106-2-30", E2, "Y", "濃 H₂SO₄ 加熱讓固醇脫水成共軛 → 螢光")
a("109-2-37", E2, "Y", "胺基酸有 NH₂ → ninhydrin", True)
a("110-1-39", E2, "Y", "tetrazolium 還原產物是藍色 formazan → 紅色斑點錯；A、C、D 皆可由把柄推為真")
a("111-1-37", E2, "Y", "同 102-1-33：類固醇藍點 → alkaline tetrazolium blue")
a("113-1-39", E2, "Y", "10% HCl 沒有可反應成有色物的對象 → 沒有把柄", True)
a("114-1-32", E2, "Y", "ninhydrin 認 N–H、Dragendorff 認鹼性氮 → 併用篩含氮藥；三級胺沒有 N–H 不反應")
a("103-2-11", "孤點", "N", "BTB 是 pH 指示劑，用把柄推會選 amine；官方 lipid 是事實記憶")
a("100-2-33", "孤點", "N", "長波 UV 燈 365 nm（題本 360）是數字事實")
# ── E3 開放平板 ──
a("102-2-35", E3, "Y", "A：開放板揮發物跑掉（對）；B：薄層加厚 → 點得多 → 半製備（對）；C：毛細作用任何方向都爬（對）→ 剩 D；G＝石膏是孤點")
a("106-1-30", E3, "Y", "不純物要先分開、再和參考品同板並排比；滴定、重量、UV 分不開成分")
a("107-2-31", E3, "Y", "點的大小只反映點上去的 C×V：0.04／4＝1%")
a("108-2-31", E3, "Y", "點樣、乾燥、展開都在空氣中 → 揮發物跑掉 → TLC 不適合定量")
a("114-1-33", E3, "Y", "沒有幫浦，展開劑靠毛細作用在多孔薄層中爬")
a("115-1-36", E3, "Y", "TLC 固定相要是能鋪成多孔薄層的細粉；polysiloxane 是黏稠液體（GC 固定液）→ 不是")
a("115-2-37", E3, "Y", "同板比對只能半定量；賦形劑多又多半沒把柄 → 定量所有賦形劑不是應用")
a("103-1-32", "孤點", "N", "要知道 agarose 是電泳用凝膠、矽藻土 G 是 TLC 材料（材料名稱）；本體只推得出要多孔細粉")
a("113-2-36", "E3+E2", "2", "E3：開放板把各化學形式分開、全部留在板上；E2：把柄＝放射性，掃描各區活性 → TLC；AAS 只認元素、GC 要揮發")

d = json.load(open("/home/user/-/藥物分析_全景/_build/k16/藥分_100-115_1280題.json"))
ids = [x["id"] for x in d if x["ch"][0] == "tlc"]
assert set(ids) == set(M), (set(ids) - set(M), set(M) - set(ids))
json.dump({i: M[i] for i in sorted(M)}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tlc_mask.json"), "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(M), Counter(v["t"] for v in M.values()), Counter(v["E"] for v in M.values()))
ok = [i for i in M if M[i]["t"] in "Y2"]
print("Y+2", len(ok), round(100 * len(ok) / len(M), 1))
old = [i for i in M if int(i[:3]) <= 107]; new = [i for i in M if int(i[:3]) >= 108]
print("old", len(old), sum(M[i]["t"] in "Y2" for i in old), "new", len(new), sum(M[i]["t"] in "Y2" for i in new))
print("v0", len(V0))
