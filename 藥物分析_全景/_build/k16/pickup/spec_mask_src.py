"""光譜概論 遮住測試（v2.0 本體）。產生 spec_mask.json，並印統計。
v0＝共用「能隙」標準句單獨使用；v1＝v1.1 一句 Ni（光子能量 E＝hc/λ 對上哪一階就量哪種事件；選能保留題目要的資訊的方法）
"""
import json, os
E1, E2, E3 = "E1", "E2", "E3"
M, V = {}, {}


def a(i, E, t, why, v0="N", v1="N"):
    M[i] = dict(E=E, t=t, why=why)
    V[i] = (v0, v1)


# ── E1 能隙 ──
a("100-2-18", E1, "Y", "IR 的光子只對得上振動能階，碰不到電子；UV、AAS、AES 都是電子躍遷", "Y", "Y")
a("100-2-21", E1, "Y", "E＝hν：無線電波頻率最低 → 能量最低（只對得上核自旋）", "Y", "Y")
a("103-2-27", E1, "Y", "UV 對上價電子（π、n）→ A、B 對；芳環 π→π* 強 → D 對 → 剩 C（10：1：0.1 是錯的比值）", "Y", "Y")
a("104-1-29", E1, "Y", "電子能階上疊振動、轉動 → UV 是寬帶；IR 每種鍵各一條振動 → 指紋 → 未知物定性 IR 勝，D 錯")
a("105-2-4", E1, "Y", "NMR 讀核自旋，能階差最小 → 用 RF，波長最長", "Y", "Y")
a("105-2-6", E1, "Y", "核自旋能階差極小 → 上下兩層人數幾乎一樣 → 淨吸收極弱 → 要最多檢品")
a("106-1-27", E1, "Y", "λ＝1／ṽ＝1／40000 cm⁻¹＝2.5×10⁻⁵ cm＝250 nm → 紫外光", "Y", "Y")
a("107-1-9", E1, "Y", "E＝hν；h 是常數（J·s、erg·s），不隨波長變；c＝νλ 不是 h", "Y", "Y")
a("108-1-28", E1, "Y", "能量 UV > 可見 > IR → 波長反過來：紅外 > 可見 > 紫外", "Y", "Y")
a("109-1-3", E1, "Y", "頻率用 Hz、波長用 nm、IR 用 cm⁻¹；E＝hcṽ → 波數越大能量越高 → A 錯", "Y", "Y")
a("113-1-21", E1, "Y", "每個分子都有振動能階 → 溶媒和樣品在 IR 到處都吸 → 光徑 1 cm 會全黑 → IR 槽要很薄，A 錯")
a("113-1-23", E1, "Y", "UV 在可見光（約 400–800 nm）之前、X-ray 之後 → 220 nm；0.5 nm＝X-ray、2200 nm＝NIR", "Y", "Y")

# ── E2 能量怎麼進、讀什麼 ──
a("101-2-13", E2, "Y", "吸收＝照進去讀少了多少 → IR；Raman 讀改方向的散射光、螢光讀放出的光、MS 數離子")
a("103-1-22", E2, "Y", "MS 在暗背景上一個一個數離子 → 偵測極限最低（pg 級）")
a("104-1-14", E2, "Y", "Raman 散射約百萬個光子才一個 → 訊號最弱又怕螢光背景 → 題本選最不適合定量（物理上仍可定量）")
a("105-1-28", E2, "Y", "MS 直接數離子、背景近零 → 偵測極限最低")
a("107-1-2", E2, "Y", "可見、紫外、紅外都是照進去讀少了多少（吸收）→ 只剩 Raman；官方把讀樣品送出來的散射光歸放射")
a("109-1-26", E2, "Y", "ppb 級要在暗背景上數訊號 → MS；UV、IR 要從亮光裡扣小差，NMR 更弱")
a("112-1-16", E2, "Y", "AES 由火焰或電漿把原子熱激發，讀它自己放的光 → 不需激發光源；IR、UV 要燈照，螢光要燈激發")
a("113-1-20", E2, "Y", "鈉燈是原子燈，只放 589 nm 一條線 → 不能當連續的 VIS 光源 → B 錯；D₂ 放電給 UV、氙燈夠強給螢光、加熱的 metal oxide 給 IR")
a("114-2-14", E2, "Y", "原子發射靠火焰、電漿供能，讀自己放的光 → 不須特定光源")
a("114-2-20", E2, "Y", "quartz halogen 是加熱的鎢絲 → VIS → A 對；UV 不用鎢、IR 不用鈉 D 線、螢光要強光源不用 D₂")

# ── E3 要什麼資訊選保留它的方法 ──
a("102-1-14", E3, "Y", "晶型在固態排列裡；IR 可直接量固體，振動受晶格鄰居影響 → IR；UV 要溶解、MS 要游離、AAS 要原子化，晶格都沒了", "N", "Y")
a("102-2-13", E3, "Y", "雜質要先和主成分分開才認得出身分 → LC 分離＋MS 給 m/z → LC-MS；RI、NMR、IR 混在一起讀", "N", "Y")
a("103-2-14", E3, "Y", "裸錠＝不能溶解 → 要直接讀固體的 NIR 反射；NMR、MS、UV 都要先處理成溶液或離子", "N", "Y")
a("103-2-21", E3, "Y", "異構物差在每個核的鄰居 → NMR 逐核讀環境（化學位移、耦合）", "N", "Y")
a("104-1-13", E3, "Y", "晶型要保留固態 → 四選一只有 IR 能直接讀固體", "N", "Y")
a("104-1-26", E3, "Y", "立體結構在每個核的鄰居與空間關係 → NMR 給最多", "N", "Y")
a("107-1-26", E3, "Y", "LC-MS-MS 要溶解再游離 → 晶格沒了；Raman、XRD、固態 NMR 都直接讀固體", "N", "Y")
a("113-1-11", E3, "Y", "diffusion NMR（DOSY）量溶液中的擴散 → 晶格已溶掉；ssNMR、ATR、漫反射都直接量固體", "N", "Y")

# ── 孤點 ──
a("101-2-16", "孤點", "N", "官方選 D（AAS 與透光率無關）。E2 推得 AAS 也是讀燈光少了多少，和官方相反")
a("104-1-21", "孤點", "N", "E2 排除加熱燈絲（W、石英鹵素 → VIS），但 D₂ 和 Xe 都是放電燈；D₂ 專放 UV 連續光要記")
a("110-1-22", "孤點", "N", "方向（電子 > 振動 > 轉動）推得出，排除 1：10：100；10：1：0.1 和 100：1：0.01 的倍數要記")

HERE = os.path.dirname(os.path.abspath(__file__))
if __name__ == "__main__":
    d = json.load(open(os.path.join(HERE, "../藥分_100-115_1280題.json"), encoding="utf-8"))
    ids = [q["id"] for q in d if q["ch"] and q["ch"][0] == "spec"]
    miss = set(ids) - set(M); extra = set(M) - set(ids)
    assert not miss and not extra, (miss, extra)
    out = {i: M[i] for i in ids}
    json.dump(out, open(os.path.join(HERE, "spec_mask.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    n = len(ids)
    c = Counter(m["t"] for m in out.values())
    print("題數", n, dict(c), "Y+2=%d (%.1f%%)" % (c["Y"] + c["2"], 100 * (c["Y"] + c["2"]) / n))
    print(Counter((m["E"], m["t"]) for m in out.values()))
    for half, rng in [("100-107", range(100, 108)), ("108-115", range(108, 116))]:
        hs = [i for i in ids if int(i.split("-")[0]) in rng]
        ok = sum(out[i]["t"] in "Y2" for i in hs)
        print(half, len(hs), ok, "%.1f%%" % (100 * ok / len(hs)))
    for k, nm in [(0, "v0"), (1, "v1")]:
        print(nm, sum(V[i][k] == "Y" for i in ids))
    print("N:", [i for i in ids if out[i]["t"] == "N"])
