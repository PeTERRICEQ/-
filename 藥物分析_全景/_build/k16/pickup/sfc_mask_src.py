"""SFC 遮住測試（只看 specs/sfc2.py p1 的 E1 超臨界態、E2 CO₂ 這瓶流體、共用分配）。執行後寫出 sfc_mask.json。"""
import json, os
M = {}
def a(i, E, t, why): M[i] = dict(E=E, t=t, why=why)
a("103-1-34", "E2", "Y", "要臨界點低、便宜、不燃、無毒 → CO₂；N₂O 助燃會爆、NH₃ 有毒腐蝕、n-butane 易燃")
a("107-2-14", "E2", "Y", "同上 → CO₂；甲醇臨界溫度 240 °C 太高、液態氮沒有溶解力、甲酸腐蝕")
a("108-1-34", "E2", "Y", "臨界點低又安全便宜的流體很少，實用的幾乎只有 CO₂ → 種類多不是優點；A、C 由 E1（擴散快、壓力調密度）、B 由 E2（31 °C）推為真")
a("109-2-34", "共用", "Y", "α 是兩分子 k 的比，要各分子變得不一樣才會動 → 換流動相的化學性質（加 MeOH 改質劑）；壓力只讓密度齊升齊降，偵測器不碰分離")
a("110-1-35", "E2", "Y", "O=C=O 兩個鍵偶極抵消 → 非極性 → 高極性不是優點，極性物反而要加改質劑")
if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    d = json.load(open(os.path.join(here, "..", "藥分_100-115_1280題.json"), encoding="utf-8"))
    ids = [q["id"] for q in d if q["ch"] and q["ch"][0] == "sfc"]
    assert sorted(ids) == sorted(M), (ids, list(M))
    json.dump({i: M[i] for i in ids}, open(os.path.join(here, "sfc_mask.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(ids), Counter(M[i]["t"] for i in ids), Counter(M[i]["E"] for i in ids))
