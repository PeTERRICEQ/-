"""TLC 題型練習（STJ 式）：5 個題型，每題型一張題目卡＋一張詳解卡。
題型清單與全部題號：_build/k16/pickup/tlc_types.json（題數、母題、變形都用 python 核對過）。本體名稱同 tlc2.py。"""

E1 = "E1 點走多遠"
E2 = "E2 看不看得到"
E3 = "E3 板子攤在空氣中"

T = [
    dict(no="TLC-01", name="呈色劑配把柄：這個藥用哪個呈色劑", E=E2, n=8, src="103-1-37",
         stem="胺醣類抗生素（aminoglycoside antibiotics）如 gentamycin 的薄層層析定性分析中，常使用下列何種呈色試劑來進行其鑑別？",
         opts={"A": "Iodine vapor", "B": "Ninhydrin solution", "C": "Alkaline tetrazolium blue", "D": "Ethanol／Sulphuric acid 20%"},
         ans="B",
         chain=["本體 E2：呈色劑只和分子身上某個基團反應成有色物，沒有那個基團就看不到",
                "→ 先找 gentamicin 的把柄：胺醣＝糖環上掛著好幾個游離 NH₂",
                "→ 認 N–H 的呈色劑是 ninhydrin，和 NH₂ 縮合成紫色",
                "→ **B**"],
         why_not=["A 錯：碘蒸氣靠溶進親脂斑點，胺醣極親水，而且碘不針對胺基",
                  "C 錯：tetrazolium 認可還原的 α-ketol，那是皮質類固醇的把柄",
                  "D 錯：H₂SO₄／EtOH 加熱讓固醇骨架脫水，針對固醇"],
         var=[("104-1-35", "換成胜肽 aprotinin → N 端與 lysine 有 NH₂ → 仍是 ninhydrin"),
              ("102-1-33", "換成皮質類固醇白底藍點 → α-ketol 還原四唑鹽 → tetrazolium"),
              ("106-2-30", "固醇噴灑加熱發螢光 → 脫水成共軛 → H₂SO₄／EtOH"),
              ("114-1-32", "ninhydrin 敘述題 → 三級胺沒有 N–H 不反應 → 併用 Dragendorff 篩含氮藥")],
         trap="看到「胺」就選 ninhydrin。三級胺 N 上沒有 H，要改 Dragendorff。"),

    dict(no="TLC-02", name="矽膠板 Rf 排序：誰最小", E=E1, n=7, src="114-2-39",
         stem="利用矽膠薄層層析法分析 retinol、vitamin A acetate、retinoic acid 及 vitamin A palmitate，以適當溶媒展開，下列何者之 Rf 值最小？",
         opts={"A": "retinol", "B": "vitamin A acetate", "C": "vitamin A palmitate", "D": "retinoic acid"},
         ans="D",
         chain=["本體 E1：越像板子待越久、走越短，Rf 越小",
                "→ 矽膠的 Si–OH 用氫鍵抓極性基 → 這裡的「像」＝極性與氫鍵點",
                "→ 四者同一骨架，只差尾端：COOH > 游離 OH > 短酯 > 長鏈酯",
                "→ retinoic acid 最像矽膠 → Rf 最小 → **D**"],
         why_not=["A 錯：retinol 只有一個 OH，氫鍵能力比 COOH 弱",
                  "B 錯：acetate 把 OH 酯化蓋掉 → 跑得更遠",
                  "C 錯：palmitate 是長鏈酯，最油 → 跑最遠，Rf 最大"],
         var=[("107-1-14", "換成 hydrocortisone 家族 → 鹽最極性 → sodium phosphate 最小"),
              ("115-1-37", "給 acetate 0.51 問 hydrocortisone → 多一個 OH → 變小，但不是鹽 → 0.20"),
              ("110-2-37", "換成胺基酸 → serine 側鏈 OH 最極性 → 最小"),
              ("108-1-29", "換成石蠟逆相板 → 方向相反：最長、最飽和的 stearic acid 最小")],
         trap="沒認板就排序。石蠟板上越油越慢，和矽膠相反。"),

    dict(no="TLC-03", name="TLC 適合做什麼、不適合做什麼", E=E3, n=4, src="108-2-31",
         stem="針對揮發性藥物（如麻醉劑）而言，下列何種層析法不適合做為其分析定量的方法？",
         opts={"A": "高效液相層析法", "B": "氣相層析法", "C": "薄層層析法", "D": "毛細管電泳法"},
         ans="C",
         chain=["本體 E3：TLC 板子攤在空氣中，點樣、乾燥、展開都開放",
                "→ 揮發性麻醉劑點上去、吹乾時就蒸發跑掉",
                "→ 板上剩下的量不等於點上去的量 → 不能定量",
                "→ HPLC、CE 在密閉管路裡，GC 本來就為揮發物設計 → **C**"],
         why_not=["A 錯：HPLC 樣品在密閉液流中，不會跑掉",
                  "B 錯：GC 要求樣品能氣化，揮發物最適合",
                  "D 錯：CE 在密閉毛細管中進行"],
         var=[("115-2-37", "問哪個不是應用 → 半定量、賦形劑多半沒把柄 → 定量所有賦形劑"),
              ("106-1-30", "PIC/S 原料藥不純物 → 要先分開再同板比參考品 → TLC"),
              ("113-2-36", "放射化學純度 → 各化學形式分開、全部留在板上讀活性 → TLC")],
         trap="以為層析法都能定量。TLC 開放、同板比，擅長鑑別與限量。"),

    dict(no="TLC-04", name="呈色劑反不反應：可逆與無對象", E=E2, n=2, src="105-2-31",
         stem="進行薄層層析分析時，下列何種標示劑（location reagent）的使用，對於檢品的回收影響程度最小？",
         opts={"A": "ninhydrin solution", "B": "alkaline tetrazolium blue", "C": "potassium permanganate", "D": "iodine vapour"},
         ans="D",
         chain=["本體 E2：呈色劑靠和分子的某個基團反應才顯色",
                "→ 反應成新鍵 → 分子被改掉 → 刮下來的已不是原物",
                "→ 碘蒸氣只溶進親脂斑點、不成新鍵 → 放著又昇華走",
                "→ 可逆 → 對回收影響最小 → **D**"],
         why_not=["A 錯：ninhydrin 和 NH₂ 縮合，胺基被改掉",
                  "B 錯：tetrazolium 被分子還原，分子同時被氧化",
                  "C 錯：KMnO₄ 把分析物氧化掉"],
         var=[("113-1-39", "問哪個不適用 → 10% HCl 沒有可反應成有色物的對象 → 不作顯色劑")],
         trap="以為呈色劑都只是染色。除了碘，其他都靠化學反應改掉分子。"),

    dict(no="TLC-05", name="板材：能鋪成多孔細粉的才是固定相", E=E3, n=2, src="115-1-36",
         stem="下列何者不是 TLC 常用之固定相？",
         opts={"A": "聚矽氧烷（polysiloxane）", "B": "矽膠 G（silica gel G）", "C": "纖維素（cellulose）", "D": "矽藻土 G（kieselguhr G）"},
         ans="A",
         chain=["本體 E3：TLC 的固定相是鋪在板上的多孔細粉薄層，展開劑靠毛細作用爬",
                "→ 能磨成細粉、鋪成多孔層的才行：矽膠、纖維素、矽藻土",
                "→ polysiloxane 是黏稠液體，塗在 GC 毛細管內壁當固定液",
                "→ 鋪不成多孔薄層 → **A**"],
         why_not=["B 錯：silica gel G 是最常用的板，G 是石膏黏合劑",
                  "C 錯：纖維素持水，當分配層析的支持物",
                  "D 錯：矽藻土 G 浸上液態石蠟就是逆相板"],
         var=[("102-2-35", "敘述題問錯誤 → G＝gypsum 石膏，寫 methylcellulose 錯（揮發物跑掉、加厚半製備、下降展開都對）")],
         trap="看到「矽」就以為是 TLC。polysiloxane 是 GC 固定液，agarose 是電泳凝膠。"),
]

LINES = 6


def drill(t):
    return dict(type="drill", no=t["no"], name=t["name"], E=t["E"], n=t["n"], src=t["src"],
                stem=t["stem"], opts=t["opts"], lines=LINES)


def sol(t):
    return dict(type="sol", no=t["no"], name=t["name"], ans=t["ans"], chain=t["chain"],
                why_not=t["why_not"], var=t["var"], trap=t.get("trap"))


VARS = {t["no"]: "、".join(v[0] for v in t["var"]) for t in T}
SUMMARY = dict(
    label="④ 題型總表", sub="5 個原始套路題型，一個題型＝一個本體的一種投影",
    read="16 年 30 題中，這 5 個題型涵蓋 23 題（77%）。只收出現 ≥ 2 次的同問法題，孤點題留在 p3。依題數排序，同題數時 108–115 年還在考的排前面。",
    cols=[0.66, 0.34],
    left=[dict(type="table", title="題型總表",
               cols=[("編號", 1.0), ("題型", 3.1), ("本體", 1.6), ("題數", 0.7), ("母題", 1.1), ("變形題號", 3.0)],
               rows=[[t["no"], t["name"], t["E"], str(t["n"]), t["src"], VARS[t["no"]]] for t in T])],
    right=[
        dict(type="box", tone="grn", title="怎麼練", list=True, lines=[
            "**遮住詳解頁**：練習頁和詳解頁一前一後，先把後一頁蓋住。",
            "**先寫本體**：在 ① 寫下這題考哪個本體（E1、E2、E3），一句話就好。",
            "**推一次**：在 ② 從本體一步一步推到選項，每步只用一個箭頭。",
            "**翻頁對照**：拿詳解的推導鏈逐步核對，找出第一個推錯的步驟。",
            "**推錯回 p1**：回 ① 本體推導版找那個本體，再看歷年變形，換一個問法再推一次。"]),
        dict(type="box", tone="blu", title="三個本體（同 p1）", list=True, lines=[
            "**E1 點走多遠**：越像板子待越久、走越短，Rf 越小。矽膠像極性，石蠟像油",
            "**E2 看不看得到**：呈色劑只認一個基團，沒有把柄就看不到。反應會改掉分子，碘可逆",
            "**E3 板子攤在空氣中**：同板並排比、只能半定量，揮發物會跑掉"]),
        dict(type="box", tone="yel", title="分布", list=True, lines=[
            "E1：1 型 7 題（TLC-02）",
            "E2：2 型 10 題（TLC-01、04）",
            "E3：2 型 6 題（TLC-03、05）",
            "未收：加醋酸減拖尾、F254 暗點、限量 C×V、毛細作用各 1 題，孤點 3 題（360 nm、BTB、agarose），回 p1、p3 看"]),
    ],
)


def pages():
    out = [SUMMARY]
    for g in range(0, len(T), 4):
        grp = T[g:g + 4]
        rng = f'{grp[0]["no"]}–{grp[-1]["no"]}' if len(grp) > 1 else grp[0]["no"]
        if len(grp) == 4:
            L, R = grp[:2], grp[2:]
        else:  # 不足 4 個：左右各放，詳解頁同位置
            h = (len(grp) + 1) // 2
            L, R = grp[:h], grp[h:]
        out.append(dict(label="④ 題型練習", sub=f"{rng}：先寫本體，再推一次",
                        read="遮住下一頁。① 寫這題考哪個本體，② 從本體一步一步推到答案，再翻頁對照。",
                        cols=[0.5, 0.5], left=[drill(t) for t in L], right=[drill(t) for t in R]))
        out.append(dict(label="④ 題型詳解", sub=f"{rng}：推導鏈從本體出發",
                        read="逐步核對推導鏈，找出第一個推錯的步驟，再回 p1 找本體。歷年變形題號都是同一題型的真題。",
                        cols=[0.5, 0.5], left=[sol(t) for t in L], right=[sol(t) for t in R]))
    return out


SPEC = dict(PAGES=pages())
