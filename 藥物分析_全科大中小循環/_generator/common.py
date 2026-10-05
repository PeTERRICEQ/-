# -*- coding: utf-8 -*-
"""Single source for chapter spines used by all six figures."""
from nisvg import SVG, INK, MUTED, RED, PANEL

OUT = "/home/user/-/藥物分析_全科大中小循環"
VER = "v1_0"
FILES = {
    0: f"藥物分析_全科_圖0_大循環Ni總圖_{VER}.svg",
    1: f"藥物分析_全科_圖1_中循環I能量帳_光譜九章_{VER}.svg",
    2: f"藥物分析_全科_圖2_中循環II時間帳_分離七章_{VER}.svg",
    3: f"藥物分析_全科_圖3_中循環III質荷帳與偵測接點_{VER}.svg",
    4: f"藥物分析_全科_圖4_讀數校正與回查總表_{VER}.svg",
    5: f"藥物分析_全科_圖5_跨科類比_藥理型別與藥動同構_{VER}.svg",
}

FAM = {"I": "E", "II": "C", "III": "D", "BR": "B", "READ": "A", "QC": "F"}

# 中循環卡：每章一個。M01–M04 是該章套用全科四站後的樣子；
# loops 為該章講義的小循環存檔點與 L 編號（沿用原章 ID）。
SPEC = [
    dict(k="sp", name="光譜概論", arche="能量梯子", nL=12,
         line="波長越短，每顆光子能量越大，碰得到越深的能階；先認是哪一階，才知道儀器在量什麼。",
         M=["同一錠可問含量、身分、微量雜質或晶型；溶解後不再保留晶格（L12）",
            "E＝hν＝hc／λ；光子能量對上能階差才會作用（L1–L4）",
            "吸收、放射、散射、核訊號、離子、繞射，六種訊號各量不同的量（L5–L10）",
            "斜率是靈敏度；偵測極限還要看雜訊（L11）"],
         eq="ṽ（cm⁻¹）＝10⁷／λ（nm）；E ∝ 1／λ",
         loops="L1–3 量與單位｜L4 躍遷｜L5–10 各法訊號｜L11 偵測｜L12 晶型",
         trap="ppb 是比例、pg 是質量，不能只看指數互換；0.5 nm 屬 X 射線，用 XRD 比晶格。"),
    dict(k="uv", name="UV-Vis", arche="乘法變加法", nL=20,
         line="每層吸收使透光率相乘變小；取 −log 後變成可相加的 A，才會和濃度成正比。",
         M=["匹配空白、溶媒、pH 與稀釋先定好（L01、L11、L14）",
            "價電子躍遷 π→π*、n→π*；共軛縮小能隙（L05–L09）",
            "λmax 是位置，A 是大小；差異、微分光譜與 DAD 另讀（L15、L17、L18）",
            "Beer 定律只在有效條件下成立；雜散光與光變少的誤差方向相反（L03、L20）"],
         eq="A＝−log T＝εbc＝A(1%,1cm)·b·c",
         loops="A 光到得了 L13・14・16｜B 如何吸光 L05–07｜C 結構與 pH 改譜 L08–11｜D 讀數→濃度 L01–04｜E 選擇性與數學 L12・17・18｜F 資料與品質 L15・19・20",
         trap="T＝1% 時 A＝2；1−T 不一定全是藥物吸收，散射也會使光變少。"),
    dict(k="fl", name="螢光", arche="激發態水庫・多出口", nL=20,
         line="吸收的光先存成激發態，再從螢光、非輻射、系間跨越等出口離開；走螢光出口的比例就是 Φ。",
         M=["三條路：天然螢光 F、衍生化產物 F、選擇性熄滅差值 ΔF（L01–L03）",
            "Φ＝kf／Σk；剛性↑、溫度↓、去氧 → Φ↑；重原子、溶氧會淬熄（L04–L10）",
            "選 λex、收 λem（常 90° 側收）；扣散射與空白（L11–L14）",
            "低吸收時 F 才正比 c；高濃度內濾使 F 偏離甚至下降（L14、L20）"],
         eq="F≈2.303·K·I₀·Φ·ε·b·c（低吸收）",
         loops="A 檢品與路徑 L01–03｜B 能量與分流 L04–06｜C 結構與條件 L07–10｜D 光路與訊號 L11–14｜E 指定反應 L15–18｜F 結果與品質 L19–20",
         trap="λem 比 λex 長（Stokes）；檢品可比 UV 稀約 10–100 倍；螢光與磷光分流不同（L06）。"),
    dict(k="ir", name="IR", arche="彈簧琴", nL=14,
         line="化學鍵像彈簧：越硬（k↑）、越輕（μ↓）振動越快、波數越高；振動要改變偶極矩才會吸收。",
         M=["官能基、身分、晶形或含量？選製樣：KBr、糊漿、溶液、薄膜、氣槽、ATR、DRIFT（L08–L11）",
            "ṽ ∝ √(k／μ)；偶極矩改變才 IR 活性（L01–L04）",
            "峰位 cm⁻¹；%T 圖吸收向下（A 圖向上）；氫鍵 O–H 帶寬（L05–L07）",
            "含指紋區的完整比對；固態差異先查晶形與製樣（L08、L10、L14）"],
         eq="ṽ＝(1／2πc)·√(k／μ)",
         loops="吸收規則 L01–04｜讀譜 L05–08｜製樣與晶形 L09–11｜FT、NIR 與品質 L12–14",
         trap="C–D 比 C–H 低波數（μ↑）；共軛羰基低移、β-lactam 小環高移；NIR 弱約千倍，說的是強度不是頻率。"),
    dict(k="rm", name="Raman", arche="能量找零", nL=10,
         line="雷射光子撞到分子後，散射光子少了（Stokes）或多了（anti-Stokes）一份振動能量；量的是這個差額。",
         M=["固體、溶液、製劑甚至包裝內都可量；保留固態才能問晶型（L7、L8）",
            "振動要改變極化率，與 IR 互補；虛擬態不是螢光的真實激發態（L2、L3）",
            "位移＝ṽ雷射−ṽ散射；先濾掉 Rayleigh；色散式或 FT（L4、L5）",
            "指紋比對；定量要代表性取樣＋校正（L9）"],
         eq="Δṽ＝ṽ₀−ṽs；換雷射，位移不變、絕對波長改變",
         loops="能量交換 L1・2・10｜選擇律 L3｜讀數與背景 L4–6｜取樣與晶型 L7・8｜定量 L9",
         trap="長波雷射可降低螢光背景，但 Raman 訊號也變弱（L6）；anti-Stokes 弱，因為已在激發振動態的分子少（L10）。"),
    dict(k="nmr", name="NMR", arche="磁場陀螺合唱", nL=24,
         line="核在 B₀ 中分成自旋能階，RF 對上拉莫爾頻率才共振；四個讀數各回答一件事。",
         M=["選核種（I＝½：¹H、¹³C、¹⁹F、³¹P）、氘代溶媒、目的（L01、L02、L15）",
            "ν＝γB₀／2π；族群差小使靈敏度低；脈衝 → FID → FT（L03、L04、L14）",
            "δ 看環境、積分看 H 數、n＋1 裂分看鄰居、J（Hz）看連接（L05–L12）",
            "四讀數互相約束；qNMR 面積接回物質量；DOSY 依擴散（L21–L24）"],
         eq="δ＝(ν−ν_ref)／ν_ref×10⁶（ppm）",
         loops="A 核自旋 L01–04｜B 峰數與位置 L05–08｜C 裂分與積分 L09–12｜D 複雜譜與儀器 L13–16｜E 碳譜與相關 L17–20｜F 應用與品質 L21–24",
         trap="換高場時 δ 與 J 不變、Δν（Hz）變大，Δν／J 變大更接近一級譜（L13）；D₂O 使 OH、NH 峰消失（L15）。"),
    dict(k="at", name="原子光譜", arche="元素音叉", nL=16,
         line="自由原子沒有振動與轉動能階，只剩電子躍遷，所以譜線很窄；先原子化，再量被吸掉的燈光或原子自己放的光。",
         M=["元素、基質、空白與前處理（L08、L14）",
            "原子化；AAS 吸收中空陰極燈的特徵線；AES、ICP 量激發後的放光（L02–L05、L12）",
            "分光＋斬光扣背景，得淨讀數 A 或發射強度（L06、L11）",
            "校正曲線或標準添加；分清四種干擾再修正（L13、L16）"],
         eq="A＝log(I₀／I) ∝ c（校正範圍內）",
         loops="原子化與激發 L01–05・07｜四干擾：L08 物理・L09 化學・L10 離子化・L11 光譜｜校正與選法 L12–16",
         trap="磷酸根化學干擾加 LaCl₃ 釋放劑；Na D 線約 589 nm（3p→3s）；題本 Na／K 輸注液偏 AES，Pb、Ni、Zn、Ca／Mg 偏 AAS。"),
    dict(k="ri", name="折光", arche="光的減速帶", nL=9,
         line="光進入較密介質會變慢並偏折，n＝c／v；只讀到一個數，所以條件要固定。",
         M=["鑑別、純度或估濃度；液體薄膜要完全接觸（L6）",
            "Snell：n₁sinθ₁＝n₂sinθ₂；臨界角形成明暗邊界（L1–L3）",
            "Abbe 讀邊界得 n（20 °C、589 nm）；RI 偵測器讀流出液與移動相的差 Δn（L3、L9）",
            "固定 T 與 λ；用水值校正；單一 n 不能指認雜質（L4、L5、L7、L8）"],
         eq="n＝c／v；sinθc＝n₂／n₁",
         loops="光學 L1–3｜條件 L4–6｜校正與判讀 L7–8｜偵測器 L9",
         trap="溫度改變 n 可能被誤當成組成改變（L4）；RI 偵測器怕梯度沖提，基線會隨組成漂移（L9）。"),
    dict(k="or", name="旋光", arche="左右手速度差", nL=10,
         line="掌性分子對左、右圓偏光的折射率不同，平面偏極光因此被轉一個角度 a；除掉 l、c 才得到物質常數 [α]。",
         M=["分析物必須具掌性；避免外消旋與氣泡（L4）",
            "鈉 D 線 589 nm → 起偏鏡 → 半影稜鏡 → 樣品管 l → 檢偏鏡（L1–L3）",
            "讀 a（°）與方向（＋／−）；a ∝ l×c（L5）",
            "[α]＝100a／(l·c)；比對規格、求含量或鏡像比例（L6、L9）"],
         eq="[α]＝100a／(l·c)（l：dm；c：g／100 mL）",
         loops="讀角度 L1–2｜為什麼會轉 L3–4｜歸一化 L5–7｜判讀 L8–10",
         trap="(＋)／(−) 和 D／L、R／S 沒有必然對應（L8）；[α] 偏低可能是混入鏡像體或不旋光雜質，處置不同。"),
    # ---------------- 分離 ----------------
    dict(k="ex", name="萃取", arche="一次分配＋pH 開關", nL=27,
         line="兩相只交換到一次平衡就停；pH 決定藥是中性（進有機相）還是帶電（留在水相）。",
         M=["要取誰、排除誰：去油、去蛋白、濃縮或連續取樣（L01）",
            "D＝K×中性分率；鹽析與破乳；SPE 活化→上樣→洗滌→沖提；離子交換、親和、SPME、SFE、微透析（L02–L23）",
            "濃度比不等於量比，m＝c×V；回收與濃縮倍數分開算（L24、L25）",
            "內標補共同損失，但找不回已失去的藥；不合格先定位原因（L26、L27）"],
         eq="q＝Va／(Va＋D·Vo)；萃 n 次剩 qⁿ（少量多次較完全）",
         loops="A 認相與 pH L01–07｜B SPE 四步 L08–12｜C 電荷・結構・尺寸 L13–18｜D 特殊取樣 L19–23｜E 濃縮・回收・品質 L24–27",
         trap="收哪一層看藥在哪一相，不看哪一層在上（L05）；找失落的藥要查上樣、洗液、沖提三段（L10）。"),
    dict(k="chr", name="層析概論", arche="差速賽跑", nL=16,
         line="分子只有待在移動相時才前進；越常停在固定相，走得越慢，所以 tR＝t₀(1＋k′)。",
         M=["要分開哪兩個成分？比保留、分離、效率或含量（L01）",
            "K＝cS／cM；k′＝K·VS／VM；擴散與質傳使峰變寬（L05、L12–L14）",
            "位置 tR、面積、峰寬 W 與不對稱（L02、L15）",
            "α 比相對保留；Rs 判斷有沒有分開；N、H 比效率（L06–L11）"],
         eq="Rs≈(√N／4)·((α−1)／α)·(k′／(1＋k′))；H＝A＋B／u＋Cu",
         loops="A 讀懂一次分析 L01–03｜B 保留可比 L04–06｜C 解析度與效率 L07–09｜D 參數收益 L10–11｜E 展寬機制 L12–14｜F 峰形與證據 L15–16",
         trap="α＝1 時 N 再大也分不開；N 變 4 倍，Rs 才變 2 倍；拖尾因子大於 1。"),
    dict(k="tlc", name="TLC", arche="平面賽跑・前緣是尺", nL=18,
         line="溶劑靠毛細作用爬上薄板；斑點中心走的距離 ÷ 溶劑前緣走的距離＝Rf。",
         M=["點樣線要高於液面；限量試驗比的是點上去的質量（L01、L13）",
            "矽膠（正相）留住極性者；石蠟塗層（逆相）留住疏水者；調溶劑、加酸鹼（L04–L08）",
            "Rf 介於 0–1；254 nm 暗點、365 nm 螢光、呈色劑、碘蒸氣（L02、L10–L12）",
            "同 Rf 只能支持、不能證明同一物；定量要校正；HPTLC、二維展開（L03、L14、L17、L18）"],
         eq="Rf＝斑點中心距離／溶劑前緣距離",
         loops="A 走流程讀位置 L01–03｜B 固定相比保留 L04–06｜C 操作條件 L07–09｜D 看見斑點 L10–12｜E 位置、量與活性 L13–15｜F 用途與升級 L16–18",
         trap="斑點拖尾或前緣歪，回查點樣量、解離與槽況（L09）；碘蒸氣呈色可逆，適合要回收時用（L12）。"),
    dict(k="hplc", name="HPLC", arche="液相拔河・換尺分離", nL=24,
         line="分析物在固定相與移動相之間拔河；換掉比較的尺（極性、電荷、孔徑、掌性），就換掉分離依據。",
         M=["能溶於移動相、不必氣化的檢品（L01）",
            "逆相 C18 疏水者晚出；正相矽膠極性者晚出；pH 改解離；有機比例↑ → tR↓（L05–L12）",
            "tR、面積、峰寬；UV／DAD、螢光、電化學、RI、ELSD、CAD（L03、L19–L22）",
            "外標或內標回算濃度；小粒徑效率高但需高壓（L23、L24）"],
         eq="外標 c＝(S−b)／a；內標 R＝Ax／AIS",
         loops="A 儀器與讀數 L01–04｜B 保留與固定相 L05–08｜C 配方、酸鹼與時間 L09–12｜D 換分離依據 L13–16｜E 立體、反應與光學 L17–20｜F 偵測與定量 L21–24",
         trap="弱酸在 pH 降低時中性比例↑，逆相保留↑，弱鹼方向相反（L09）；分子篩大分子先出（L15）；鹼性藥在殘餘矽醇上拖尾（L08）。"),
    dict(k="gc", name="GC", arche="沸點樓梯＋溫度電梯", nL=27,
         line="先要能完整氣化；柱溫一升，成分都更願意待在氣相，保留變短；沸點跨度大時用程式升溫。",
         M=["可揮發又耐熱嗎？不行就頂空、SPME、鹼化萃取或衍生化（L01、L14–L18）",
            "固定相放大差異；中空柱、載氣與進樣（分流、PTV）決定峰寬（L04–L13）",
            "tR、保留指數 I、面積；FID、ECD、TCD、NPD、MS（L08、L19–L23）",
            "內標補共同變動；面積百分比需響應相近；精密度與 LOD（L24–L27）"],
         eq="內標 R＝Ax／AIS；I 以正烷烴為刻度（需同固定相與溫度模式）",
         loops="A 能不能測 L01–03｜B 保留→分離 L04–08｜C 帶窄可重現 L09–13｜D 送進 GC L14–18｜E 偵測器 L19–23｜F 可信結果 L24–27",
         trap="ECD 遇鹵素等電負性分子時電子電流變小（L20）；分流只送一小份進柱以防超載（L11）；升溫基線上升先查固定相流失（L06）。"),
    dict(k="sfc", name="SFC／SFE", arche="可調密度的溶劑", nL=20,
         line="CO₂ 超過臨界點（約 31.1 °C、73.8 bar）後，密度隨壓力可調；密度越高溶解力越強，保留越短。",
         M=["要萃取（SFE）還是分離測量（SFC）？要溶得進去，但不必氣化（L01、L02）",
            "壓力→密度→溶解力；低黏度、高擴散使分析快；改質劑調極性與表面作用（L03–L08）",
            "k、α、Rs；UV、MS（減壓後離子化）、FID（需相容介面）（L09、L10、L14–L16）",
            "校正、稀釋與回收分開算；漂移先列候選原因（L19、L20）"],
         eq="ΔP＝Pin−Pout；背壓（BPR）不是壓降",
         loops="A 任務與相態 L01–04｜B 流體改保留與峰寬 L05–07｜C 改質劑、選擇性與管柱 L08–11｜D 硬體 L12–16｜E 萃取、含量與品質 L17–20",
         trap="溫度同時改密度與揮發，方向不能硬背成單向（L07）；SFE 取出來不等於量出來（L17）。"),
    dict(k="ce", name="CE", arche="水流＋自走", nL=28,
         line="管壁帶負電，拖著整管水往陰極流（EOF）；每個離子再依自己的淌度順流或逆流，兩個速度相加決定到達順序。",
         M=["登記 pH、pKa／pI、電極位置與模式（L01、L08、L09）",
            "μEOF＝−εζ／η；v＝(μEOF＋μep)E；塗層、pH、離子強度改 EOF；焦耳熱與吸附使峰變寬（L02–L07、L10–L16）",
            "電泳圖：遷移時間、面積、峰寬；短光徑 UV、間接 UV 負峰（L23–L25）",
            "比對標準；依目的選 CZE、MEKC、CGE、CIEF、ITP、CEC（L17–L22、L27、L28）"],
         eq="E＝V／Ltot；tm＝Leff／(μapp·E)；μep＝q／(6πηr)",
         loops="1 電荷與方向 L01–03・06–09｜2 管壁改水流 L04・05・10–12｜3 效率被破壞 L13–16｜4 分離模式 L17–22｜5 峰→證據 L23–25｜6 儀器與結論 L26–28",
         trap="一般順序是陽離子→中性（隨 EOF）→陰離子（L06）；中性物要靠 MEKC 微胞才分得開（L17）；β-CD 製造立體選擇性（L18）。"),
    # ---------------- 質譜 ----------------
    dict(k="ms", name="MS", arche="先充電，再秤重", nL=33,
         line="中性分子無法被電場分選；先讓它帶電，再依 m／z 分開，最後扣回加上的電荷與加合物。",
         M=["小分子、蛋白質或元素？要分子量、結構或濃度（L33）",
            "離子源：EI、CI、ESI、APCI／APPI、MALDI；分析器：磁場、四極柱、離子阱、TOF、Orbitrap／FTICR（L08–L20）",
            "m／z、相對豐度、同位素峰距（約 1／z）、碎片峰差（L01–L07、L21–L26）",
            "回推中性 M；MS／MS 選母離子碰撞看子離子；內標定量；ICP-MS 測元素（L27–L33）"],
         eq="[M＋H]⁺：M＝m／z−1；[M＋zH]ᶻ⁺：M＝z·(m／z)−z（名目質量）",
         loops="A 看懂圖 L01–07｜B 變成離子 L08–13｜C 儀器每段 L14–20｜D 峰群與碎片 L21–26｜E MS／MS L27–29｜F 方法、定量與品質 L30–33",
         trap="一個 Cl 的 M：M＋2≈3：1，一個 Br≈1：1，S 使 M＋2 約 4.4%（L21）；中性名目質量為奇數 → 奇數個 N（L23）。"),
]
BY = {c["k"]: c for c in SPEC}
SPEC_I = ["sp", "uv", "fl", "ir", "rm", "nmr", "at", "ri", "or"]
SPEC_II = ["ex", "chr", "tlc", "hplc", "gc", "sfc", "ce"]
SPEC_III = ["ms"]
TOTAL_L = sum(c["nL"] for c in SPEC)


def header(svg, kicker, title, sub, y=0):
    svg.text(50, 62, kicker, 20, MUTED)
    svg.text(50, 120, title, 40, INK, 700)
    return svg.para(50, 142, 1800, sub, 25, INK, 1.45)


def footer(svg, y, lines):
    for i, s in enumerate(lines):
        y = svg.para(50, y, 1800, s, 20, MUTED, 1.4) + 4
    return y


def mini_station_strip(svg, x, y, w, labels=None, h=62):
    """Four small station chips with arrows; returns bottom y."""
    labels = labels or ["M01 先定問題", "M02 準備與測量", "M03 讀訊號", "M04 核對結論"]
    gap = 34
    cw = (w - 3 * gap) / 4
    for i, lab in enumerate(labels):
        cx = x + i * (cw + gap)
        rid = svg.rect(cx, y, cw, h, "W", rx=14)
        svg.text(cx + cw / 2, y + h / 2 + 9, lab, 23, INK, 700, "middle", box=rid)
        if i < 3:
            svg.arrow([(cx + cw + 3, y + h / 2), (cx + cw + gap - 3, y + h / 2)])
    return y + h


def chapter_body(c):
    """Paragraph list for one chapter medium-loop card."""
    st = ["M01", "M02", "M03", "M04"]
    body = [("line", c["line"])]
    for code, txt in zip(st, c["M"]):
        body.append(("m", f"**{code}**　{txt}"))
    body.append(("eq", f"**母式**　{c['eq']}"))
    body.append(("loops", f"**小循環存檔點**　{c['loops']}"))
    body.append(("trap", f"**陷阱**　{c['trap']}"))
    return body


def chapter_card(s, x, y, w, c, st="E", min_h=0, measure=False, bsize=21, pad=20):
    fill, stroke = PANEL[st]
    title = f"{c['name']}｜{c['arche']}　{{{{{MUTED}|L×{c['nL']}}}}}"
    inner = w - 2 * pad
    body = chapter_body(c)
    sizes = {"line": bsize, "m": bsize, "eq": bsize, "loops": bsize - 1, "trap": bsize - 1}
    colors = {"line": INK, "m": INK, "eq": INK, "loops": MUTED, "trap": RED}
    h = pad + s.para_h(inner, title, 26, 1.3) + 10
    for i, (kind, p) in enumerate(body):
        h += s.para_h(inner, p, sizes[kind], 1.42) + (10 if kind in ("line", "eq", "loops") or (kind == "m" and p.startswith("**M04")) else 4)
    h += pad - 4
    if measure:
        return h
    h = max(h, min_h)
    rid = s.rect(x, y, w, h, "W", stroke=stroke, sw=2.5)
    # colored title band
    tb = s.para_h(inner, title, 26, 1.3) + pad + 4
    s.raw(f'<path d="M{x+1.2:.1f},{y+tb:.1f} L{x+1.2:.1f},{y+18:.1f} Q{x+1.2:.1f},{y+1.2:.1f} {x+18:.1f},{y+1.2:.1f} '
          f'L{x+w-18:.1f},{y+1.2:.1f} Q{x+w-1.2:.1f},{y+1.2:.1f} {x+w-1.2:.1f},{y+18:.1f} L{x+w-1.2:.1f},{y+tb:.1f} Z" fill="{fill}"/>')
    cy = s.para(x + pad, y + pad, inner, title, 26, stroke, 1.3, 700, box=rid) + 10
    for kind, p in body:
        cy = s.para(x + pad, cy, inner, p, sizes[kind], colors[kind], 1.42, box=rid)
        cy += 10 if kind in ("line", "eq", "loops") or (kind == "m" and p.startswith("**M04")) else 4
    return y + h


def card_grid(s, x, y, w, keys, ncol, st, gap=24, rgap=26):
    cw = (w - (ncol - 1) * gap) / ncol
    rows = [keys[i:i + ncol] for i in range(0, len(keys), ncol)]
    for r in rows:
        hs = [chapter_card(s, 0, 0, cw, BY[k], st, measure=True) for k in r]
        hm = max(hs)
        for i, k in enumerate(r):
            chapter_card(s, x + i * (cw + gap), y, cw, BY[k], st, min_h=hm)
        y += hm + rgap
    return y


def table(s, x, y, widths, header, rows, hsize=22, bsize=20, pad=12, head_style="G",
          zebra=("#ffffff", "#fbfaf5"), stroke="#61717a", first_bold=True):
    """Simple wrapped table; each cell gets its own rect so the checker can verify containment."""
    def row_h(cells, size):
        return max(s.para_h(w - 2 * pad, c, size, 1.4) for w, c in zip(widths, cells)) + 2 * pad
    hh = row_h(header, hsize)
    cx = x
    for w, c in zip(widths, header):
        rid = s.rect(cx, y, w, hh, head_style, rx=0, sw=1.2)
        s.para(cx + pad, y + pad, w - 2 * pad, c, hsize, INK, 1.4, 700, box=rid)
        cx += w
    y += hh
    for i, r in enumerate(rows):
        r = [f"**{c}**" if (j == 0 and first_bold and "**" not in c) else c for j, c in enumerate(r)]
        rh = row_h(r, bsize)
        cx = x
        for j, (w, c) in enumerate(zip(widths, r)):
            rid = s.rect(cx, y, w, rh, "W", rx=0, sw=1.2, fill=zebra[i % 2], stroke=stroke)
            s.para(cx + pad, y + pad, w - 2 * pad, c, bsize, INK, 1.4, box=rid)
            cx += w
        y += rh
    return y
