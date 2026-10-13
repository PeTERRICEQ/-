---
title: 藥物分析｜高效能液相層析法 HPLC｜建構講義 v3.0
version: '3.0'
document_role: 建構講義
chapter_abbr: HPLC
computation: paper-and-pencil only
pairs_with: 藥物分析_高效能液相層析法HPLC_複習導航_v3_0
updated: '2026-10-02'
source_question_count: 102
understanding_loop_count: 24
svg_files:
- 藥物分析_高效能液相層析法HPLC_分析全流程母圖_v3_0.svg
- 藥物分析_高效能液相層析法HPLC_小循環掛載點圖_v3_0.svg
- 藥物分析_高效能液相層析法HPLC_全章方法分類與大小循環對照圖_v3_0.svg
- 藥物分析_高效能液相層析法HPLC_儀器與操作考點圖_v3_0.svg
- 藥物分析_高效能液相層析法HPLC_公式與誤差判讀總表_v3_0.svg
answer_provenance: 所附CH20題本；未提供官方答案表
external_dictionary: 未提供；不宣稱舊文提到的外部筆記已核對
---

# High-Performance Liquid Chromatography｜高效能液相層析法

HPLC先把混合物分開，再以相容的偵測器看見流出成分；保留時間、面積與峰寬回答不同問題。本章從一次完整分析開始，學會選模式、調相與pH、選偵測器，再把校正及品質接回結論。

複習入口：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0]]。第一輪讀四站與EX01，再走A→B→C；遇到離子、尺寸、親水或鏡像題，再接D→E→F。

## 四站主幹：把一次分析走完

| 站 | 先做什麼 | 交出的資訊 |
|---|---|---|
|M01 先定問題|分離哪些成分？要辨識、測含量，還是查不純物？|檢品特性、目的、對照標準與方法路徑|
|M02 準備與測量|製樣、配液、控制兩相、進樣分離與偵測。|相組成、pH、流量、溫度、柱規格及校正紀錄|
|M03 讀訊號|橫軸讀時間；峰面積讀響應；峰寬讀展寬。|t₀、tR、W：min；F：mL/min；面積：儀器積分單位|
|M04 核對結論|用參考與校正回答問題，再核對分離與品質。|有條件的辨識、含量或不純物結果；不符才回查|

### 圖1｜分析全流程母圖

<details>
<summary>展開向量圖</summary>

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="2670" viewBox="0 0 1900 2670" role="img" aria-labelledby="hplc3_g1_title hplc3_g1_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="hplc3_g1_title">HPLC｜一次分析的全流程母圖</title><desc id="hplc3_g1_desc">高效能液相層析教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊；藍線表示圖4液體流路，灰線表示訊號／分析資訊。座標曲線依各子圖標示。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="2670" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH20 / HPLC / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">HPLC｜一次分析的全流程母圖</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">先定問題，再製樣分離、讀訊號與校正；品質不符才沿紅虛線回查。</text>
<rect x="50" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="71" y="246" font-size="27" font-weight="600" fill="#24343f">M01｜先定問題</text>
<text x="71" y="288" font-size="23" font-weight="400" fill="#24343f">目的與檢品</text>
<polyline points="470,262 506,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="506.0,262.0 494.6,268.2 494.6,255.8" fill="#61717a"/>
<rect x="510" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="531" y="246" font-size="27" font-weight="600" fill="#24343f">M02｜準備與測量</text>
<text x="531" y="288" font-size="23" font-weight="400" fill="#24343f">製樣、作用與條件</text>
<polyline points="930,262 966,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="966.0,262.0 954.6,268.2 954.6,255.8" fill="#61717a"/>
<rect x="970" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="991" y="246" font-size="27" font-weight="600" fill="#24343f">M03｜讀訊號</text>
<text x="991" y="288" font-size="23" font-weight="400" fill="#24343f">量、單位與處理</text>
<polyline points="1390,262 1426,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1426.0,262.0 1414.6,268.2 1414.6,255.8" fill="#61717a"/>
<rect x="1430" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1451" y="246" font-size="27" font-weight="600" fill="#24343f">M04｜核對結論</text>
<text x="1451" y="288" font-size="23" font-weight="400" fill="#24343f">判讀、限制與品質</text>
<rect x="50" y="365" width="450" height="710" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="406" font-size="27" font-weight="600" fill="#9e771c">先放在左側的條件</text>
<text x="72" y="454.34" font-size="24" font-weight="400" fill="#24343f">檢品／基質與代表性</text>
<text x="72" y="488.42" font-size="24" font-weight="400" fill="#24343f">分析物溶解性、穩定性</text>
<text x="72" y="522.5" font-size="24" font-weight="400" fill="#24343f">可用的表面／電荷／尺寸差異</text>
<text x="72" y="556.58" font-size="24" font-weight="400" fill="#24343f">固定相與孔徑、粒徑</text>
<text x="72" y="590.66" font-size="24" font-weight="400" fill="#24343f">移動相組成、pH與鹽</text>
<text x="72" y="624.74" font-size="24" font-weight="400" fill="#24343f">流量F、溫度、進樣量</text>
<text x="72" y="658.82" font-size="24" font-weight="400" fill="#24343f">偵測特徵與校正範圍</text>
<text x="72" y="692.9" font-size="24" font-weight="400" fill="#24343f">同條件標準、空白與適用性</text>
<text x="72" y="726.98" font-size="24" font-weight="400" fill="#24343f"></text>
<text x="72" y="761.06" font-size="24" font-weight="400" fill="#24343f">不由一個tR證明唯一身分。</text>
<text x="72" y="795.14" font-size="24" font-weight="400" fill="#24343f">L01–04先建立條件與讀法。</text>
<rect x="560" y="365" width="1290" height="165" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="582" y="406" font-size="27" font-weight="600" fill="#61717a">M01｜先問要交出什麼</text>
<text x="582" y="454.34" font-size="24" font-weight="400" fill="#24343f">檢品適合LC嗎？要分開誰、量什麼？先選與目的相容的模式。L01 → L05–18</text>
<rect x="560" y="620" width="410" height="230" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="582" y="661" font-size="27" font-weight="600" fill="#326991">辨識／比對</text>
<text x="582" y="709.34" font-size="24" font-weight="400" fill="#24343f">同條件標準＋專一性證據；tR／光</text>
<text x="582" y="743.42" font-size="24" font-weight="400" fill="#24343f">譜只給有限線索。</text>
<polyline points="765,530 765,620" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="765.0,620.0 758.8,608.6 771.2,608.6" fill="#61717a"/>
<polyline points="765,850 765,915" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="1000" y="620" width="410" height="230" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="1022" y="661" font-size="27" font-weight="600" fill="#326991">含量測定</text>
<text x="1022" y="709.34" font-size="24" font-weight="400" fill="#24343f">有效外標或內標；回收與稀釋倍數</text>
<text x="1022" y="743.42" font-size="24" font-weight="400" fill="#24343f">有紀錄。</text>
<polyline points="1205,530 1205,620" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1205.0,620.0 1198.8,608.6 1211.2,608.6" fill="#61717a"/>
<polyline points="1205,850 1205,915" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="1440" y="620" width="410" height="230" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="1462" y="661" font-size="27" font-weight="600" fill="#326991">不純物／分離品質</text>
<text x="1462" y="709.34" font-size="24" font-weight="400" fill="#24343f">近鄰峰、低量檢出能力與Rs；不可</text>
<text x="1462" y="743.42" font-size="24" font-weight="400" fill="#24343f">只追求快。</text>
<polyline points="1645,530 1645,620" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1645.0,620.0 1638.8,608.6 1651.2,608.6" fill="#61717a"/>
<polyline points="1645,850 1645,915" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="765,915 1645,915" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="1205,915 1205,970" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1205.0,970.0 1198.8,958.6 1211.2,958.6" fill="#61717a"/>
<rect x="610" y="970" width="1200" height="340" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="632" y="1011" font-size="27" font-weight="600" fill="#286c68">M02｜準備與測量：共同匯入實際流路</text>
<text x="632" y="1059.34" font-size="24" font-weight="400" fill="#24343f">製樣／萃取與定容 → 配液、去氣泡 → 定量進樣 → 分離 → 所選偵測器</text>
<text x="632" y="1093.42" font-size="24" font-weight="400" fill="#24343f">NP／RP／IEC／離子對／SEC／HILIC／對掌性各用自己的保留依據。</text>
<text x="632" y="1127.5" font-size="24" font-weight="400" fill="#24343f">控制配方、pH、流量、溫度、柱規格與負載。</text>
<text x="632" y="1161.58" font-size="24" font-weight="400" fill="#24343f">若無需定量，不硬加檢量線；若需定量，同步量標準與空白。</text>
<polyline points="1205,1310 1205,1390" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1205.0,1390.0 1198.8,1378.6 1211.2,1378.6" fill="#61717a"/>
<rect x="610" y="1390" width="1200" height="305" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="632" y="1431" font-size="27" font-weight="600" fill="#326991">M03｜讀訊號：量、單位與處理</text>
<text x="632" y="1479.34" font-size="24" font-weight="400" fill="#24343f">t₀、tR、峰寬W：min；F：mL/min；VR：mL；k′、Rs、N：無單位。</text>
<text x="632" y="1513.42" font-size="24" font-weight="400" fill="#24343f">峰面積：所選偵測器訊號積分；不能把較晚／較高直接當較多。</text>
<text x="632" y="1547.5" font-size="24" font-weight="400" fill="#24343f">定量：先用校正，必要時面積比；再回算稀釋及原樣含量。</text>
<text x="632" y="1581.58" font-size="24" font-weight="400" fill="#24343f">L03、L19–23；紙筆C01–12。</text>
<polyline points="1205,1695 1205,1790" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1205.0,1790.0 1198.8,1778.6 1211.2,1778.6" fill="#61717a"/>
<rect x="610" y="1790" width="1200" height="350" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="632" y="1831" font-size="27" font-weight="600" fill="#356844">M04｜核對結論：只說資料支持的話</text>
<text x="632" y="1879.34" font-size="24" font-weight="400" fill="#24343f">辨識：比對條件、專一性與互補證據足夠嗎？</text>
<text x="632" y="1913.42" font-size="24" font-weight="400" fill="#24343f">含量：校正、單位、稀釋、回收與範圍可信嗎？</text>
<text x="632" y="1947.5" font-size="24" font-weight="400" fill="#24343f">不純物：峰可分、低量可測、基線與積分有效嗎？</text>
<text x="632" y="1981.58" font-size="24" font-weight="400" fill="#24343f">效率：N、H、Rs各回答不同問題；短柱與細粒須一起核對。</text>
<text x="632" y="2015.66" font-size="24" font-weight="400" fill="#24343f">通過方法要求 → 交出有條件結果。L23–24</text>
<polyline points="1205,2140 1205,2230" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1205.0,2230.0 1198.8,2218.6 1211.2,2218.6" fill="#61717a"/>
<rect x="610" y="2230" width="1200" height="195" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="632" y="2271" font-size="27" font-weight="600" fill="#356844">正常出口｜結果＋必要條件＋品質紀錄</text>
<text x="632" y="2319.34" font-size="24" font-weight="400" fill="#24343f">例如：EX01測定溶液X=10 µg/mL；兩峰教學Rs=1.5。</text>
<text x="632" y="2353.42" font-size="24" font-weight="400" fill="#24343f">仍依已驗證方法、標準與系統適用性要求判定。</text>
<rect x="50" y="1765" width="450" height="390" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="72" y="1806" font-size="27" font-weight="600" fill="#b72d4a">何種不符，回哪裡？</text>
<text x="72" y="1854.34" font-size="24" font-weight="400" fill="#24343f">方法不合 → 重查M01</text>
<text x="72" y="1888.42" font-size="24" font-weight="400" fill="#24343f">重疊／拖尾／漂移 → 修正M02</text>
<text x="72" y="1922.5" font-size="24" font-weight="400" fill="#24343f">讀錯軸／積分／單位 → 修正M03</text>
<text x="72" y="1956.58" font-size="24" font-weight="400" fill="#24343f">證據不夠 → 限定M04，再補證據</text>
<text x="72" y="1990.66" font-size="24" font-weight="400" fill="#24343f"></text>
<text x="72" y="2024.74" font-size="24" font-weight="400" fill="#24343f">紅線是分析者回查，不是分子回饋。</text>
<polyline points="610,1950 535,1950 535,1160 610,1160" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="610.0,1160.0 598.6,1166.2 598.6,1153.8" fill="#b72d4a"/>
<polyline points="610,2050 518,2050 518,448 560,448" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="560.0,448.0 548.6,454.2 548.6,441.8" fill="#b72d4a"/>
<polyline points="1810,1980 1878,1980 1878,1520 1810,1520" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1810.0,1520.0 1821.4,1513.8 1821.4,1526.2" fill="#b72d4a"/>
<text x="50" y="2602" font-size="20" font-weight="400" fill="#61717a">灰箭頭：分析資訊；藍色站：讀數；紅虛線：有條件回查。方法分支匯流，不是所有偵測器串成一列。</text>
<text x="50" y="2638" font-size="20" font-weight="400" fill="#61717a">原題：CH20 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

</details>

獨立圖檔：[[藥物分析_高效能液相層析法HPLC_分析全流程母圖_v3_0.svg]]


### M01｜先定問題

^hplc-c-m01

分離哪些成分？要辨識、測含量，還是查不純物？交出：檢品特性、目的、對照標準與方法路徑。

### M02｜準備與測量

^hplc-c-m02

製樣、配液、控制兩相、進樣分離與偵測。交出：相組成、pH、流量、溫度、柱規格及校正紀錄。

### M03｜讀訊號

^hplc-c-m03

橫軸讀時間；峰面積讀響應；峰寬讀展寬。交出：t₀、tR、W：min；F：mL/min；面積：儀器積分單位。

### M04｜核對結論

^hplc-c-m04

用參考與校正回答問題，再核對分離與品質。交出：有條件的辨識、含量或不純物結果；不符才回查。

**正常出口：**M01→M02→M03→M04→交出有條件結果。回線是分析者檢查與修正，並非藥物分子自動回饋；品質不符才回查。

| 不符的證據 | 具體动作與回站 |
|---|---|
|檢品／方法不回答原問題|重查代表性、可測特徵與方法，必要時重取樣；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m01\|M01]]|
|峰重疊、拖尾、時間漂移、壓力異常|查相組成、pH、流量、溫度、製樣與負載；修正再測；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02\|M02]]|
|讀錯軸、面積、峰寬／稀釋倍數|重新讀訊號、積分或換算，回代校正核對；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m03\|M03]]|
|只憑tR或高R²就下過強結論|核對專一性／驗證判準，補需要的參考或上游量測；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04\|M04]]|

## EX01｜先完成一次 C18 分離與定量

^hplc-c-ex01

**自編例，非來源考題。**要量錠劑中的X並檢查與Y分開。選已驗證的C18等度方法，製樣定容，固定F=1mL/min、溫度與進樣量；先以標準／空白確認方法和峰的對照。

| 檢查點 | 真正取得的資料 | 怎麼用 |
|---|---|---|
|M01|含量X，且須與Y分開|不先從峰高猜含量|
|M02|C18、固定配方／pH／F／溫度與校正|讀數才可比|
|M03|t₀=2min；X=4.0、Y=4.6min；各Wb=0.4min；X面積24|位置、寬度、面積分開記|
|M04|校正S=2c+4，c為µg/mL|c=(24−4)/2=10µg/mL；Rs=2×0.6/0.8=1.5|

成功交出：測定溶液X=10µg/mL；兩峰的教學Rs=1.5，仍按本方法的適用性要求判定。X的同條件標準對照與專一性是判峰的依據；未知物不能只靠一個tR唯一確認。計算細節见[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c06|C06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]；原樣含量再查稀釋與定容。

## 最小工具：不要先背整頁名詞

| 看到的詞 | 現在只需知道 | 容易混成什麼 |
|---|---|---|
|mobile／stationary phase|移動相帶流動；固定相提供保留或尺寸路徑|兩者不是都隨液體流走|
|tR／t₀|總流出時間／未保留通過時間，min|較晚不是較多|
|k′／capacity factor|扣通過時間後與基準相比，無單位|不是平衡分配常數K|
|峰面積／峰高|面積是積分訊號，用校正定量|峰高不是面積；不同分析物不可直接比濃度|
|Rs／N／H|兩峰分離／單峰相對展寬／單位長度板高|Rs高不等於只看一峰N；H與L同單位|
|F／u／dp／dc|體積流量／線性速度／填充粒徑／柱內徑|流量和速度、粒徑和內徑不能互換|
|sensitivity／selectivity／robustness|低量辨識／避開干擾／小幅條件變動下穩定|三張排序表问的是不同問題|

### 四步判讀器｜每道題先說這四句

^hplc-c-decide

1. **認方法／模式：**silica、C18、交換基團、孔隙、HILIC或手性環境？
2. **找可用差異：**是表面作用、疏水性、解離電荷、尺寸、立體作用還是偵測特徵？
3. **接到讀數：**較留／較快影響tR；偵測響應接面積；分離還需峰寬。
4. **回答問句：**圈正確、錯誤、最長、最短、無法，再核對條件及答案身分。

## 六個存檔點：把概念接回主幹

^hplc-c-groups

| 組 | 一句主幹 | 第一次閱讀 |
|---|---|---|
|A 先走儀器、讀訊號|目的、流路與讀數先分清，才知道該比較哪個量。|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01\|L01]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02\|L02]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03\|L03]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04\|L04]]|
|B 分清保留與固定相|先認固定相與作用，再比較分析物的可用差異。|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05\|L05]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06\|L06]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07\|L07]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]|
|C 控制配方、酸鹼與時間|解離、溶劑強度與流量改的是不同環節。|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10\|L10]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12\|L12]]|
|D 換一種分離依據|電荷、離子對、孔隙與親水層，各有自己的尺。|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13\|L13]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15\|L15]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16\|L16]]|
|E 加上立體、反應與光學線索|先給出可分離或可偵測的差異，再讀光學訊號。|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17\|L17]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18\|L18]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l19\|L19]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20\|L20]]|
|F 補讀數與定量品質|偵測機制與校正條件決定含量及效率結論。|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21\|L21]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23\|L23]]→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24\|L24]]|

每條L取用入口資訊、經短鏈、交出可用結果。圖2可一次查看全部24條。

### 圖2｜小循環掛載點圖

<details>
<summary>展開向量圖</summary>

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="4810" viewBox="0 0 1900 4810" role="img" aria-labelledby="hplc3_g2_title hplc3_g2_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="hplc3_g2_title">HPLC｜24 個小循環的掛載點</title><desc id="hplc3_g2_desc">高效能液相層析教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊；藍線表示圖4液體流路，灰線表示訊號／分析資訊。座標曲線依各子圖標示。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="4810" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH20 / HPLC / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">HPLC｜24 個小循環的掛載點</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">每個面板是一個存檔點；入口提供什麼、短鏈做什麼、出口如何用，都接回四站。</text>
<rect x="50" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="71" y="246" font-size="27" font-weight="600" fill="#24343f">M01｜先定問題</text>
<text x="71" y="288" font-size="23" font-weight="400" fill="#24343f">目的與檢品</text>
<polyline points="470,262 506,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="506.0,262.0 494.6,268.2 494.6,255.8" fill="#61717a"/>
<rect x="510" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="531" y="246" font-size="27" font-weight="600" fill="#24343f">M02｜準備與測量</text>
<text x="531" y="288" font-size="23" font-weight="400" fill="#24343f">製樣、作用與條件</text>
<polyline points="930,262 966,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="966.0,262.0 954.6,268.2 954.6,255.8" fill="#61717a"/>
<rect x="970" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="991" y="246" font-size="27" font-weight="600" fill="#24343f">M03｜讀訊號</text>
<text x="991" y="288" font-size="23" font-weight="400" fill="#24343f">量、單位與處理</text>
<polyline points="1390,262 1426,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1426.0,262.0 1414.6,268.2 1414.6,255.8" fill="#61717a"/>
<rect x="1430" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1451" y="246" font-size="27" font-weight="600" fill="#24343f">M04｜核對結論</text>
<text x="1451" y="288" font-size="23" font-weight="400" fill="#24343f">判讀、限制與品質</text>
<rect x="50" y="365" width="580" height="1890" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="70" y="408" font-size="28" font-weight="600" fill="#9e771c">A｜先走儀器、讀訊號</text>
<text x="70" y="460" font-size="23" font-weight="400" fill="#24343f">目的、流路與讀數先分清，才知道該比較哪個量。</text>
<rect x="65" y="540" width="550" height="395" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="87" y="581" font-size="27" font-weight="600" fill="#9e771c">L01｜什麼檢品適合走液相分析？</text>
<text x="87" y="629.34" font-size="23" font-weight="400" fill="#24343f">入 M01：檢品的溶解性、穩定性及分析目的</text>
<text x="87" y="662" font-size="23" font-weight="400" fill="#24343f">鏈：可溶且方法條件相容 → 選液相分離與偵測 →</text>
<text x="87" y="694.66" font-size="23" font-weight="400" fill="#24343f">留下可測的檢品</text>
<text x="87" y="727.32" font-size="23" font-weight="400" fill="#24343f">出 M02：方法適用性與檢品處理需求</text>
<rect x="65" y="960" width="550" height="395" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="87" y="1001" font-size="27" font-weight="600" fill="#9e771c">L02｜幫浦、進樣器與管柱各改變什麼？</text>
<text x="87" y="1049.34" font-size="23" font-weight="400" fill="#24343f">入 M02：流路、流量及固定的進樣量</text>
<text x="87" y="1082" font-size="23" font-weight="400" fill="#24343f">鏈：穩定送液／定量進樣 → 柱內不同保留 → 偵</text>
<text x="87" y="1114.66" font-size="23" font-weight="400" fill="#24343f">測器隨時間記錄</text>
<text x="87" y="1147.32" font-size="23" font-weight="400" fill="#24343f">出 M03：具有時間基準的層析圖</text>
<rect x="65" y="1380" width="550" height="395" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="87" y="1421" font-size="27" font-weight="600" fill="#9e771c">L03｜峰的位置、面積與寬度各回答什麼？</text>
<text x="87" y="1469.34" font-size="23" font-weight="400" fill="#24343f">入 M03：時間軸、峰訊號與相應參考</text>
<text x="87" y="1502" font-size="23" font-weight="400" fill="#24343f">鏈：時間／面積／寬度分開讀 → 配對保留／量／</text>
<text x="87" y="1534.66" font-size="23" font-weight="400" fill="#24343f">效率 → 得到有證據的結論</text>
<text x="87" y="1567.32" font-size="23" font-weight="400" fill="#24343f">出 M04：所求量與可支持的判讀</text>
<rect x="65" y="1800" width="550" height="395" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="87" y="1841" font-size="27" font-weight="600" fill="#9e771c">L04｜溶劑能混合，和能拿來萃取，有何差</text>
<text x="87" y="1879.34" font-size="27" font-weight="600" fill="#9e771c">別？</text>
<text x="87" y="1927.68" font-size="23" font-weight="400" fill="#24343f">入 M02：樣品基質、互溶性、目的與溶解度</text>
<text x="87" y="1960.34" font-size="23" font-weight="400" fill="#24343f">鏈：均相作移動相／兩相作萃取 → 控制分配與回</text>
<text x="87" y="1993" font-size="23" font-weight="400" fill="#24343f">收 → 取得可進樣溶液</text>
<text x="87" y="2025.66" font-size="23" font-weight="400" fill="#24343f">出 M02：適合分離且回收可核對的製樣</text>
<text x="70" y="2232" font-size="22" font-weight="400" fill="#9e771c">依序讀本組L；卡住回同號R／建構。</text>
<rect x="660" y="365" width="580" height="1890" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="680" y="408" font-size="28" font-weight="600" fill="#286c68">B｜分清保留與固定相</text>
<text x="680" y="460" font-size="23" font-weight="400" fill="#24343f">先認固定相與作用，再比較分析物的可用差異。</text>
<rect x="675" y="540" width="550" height="395" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="697" y="581" font-size="27" font-weight="600" fill="#286c68">L05｜在裸矽膠上，誰會比較晚流出？</text>
<text x="697" y="629.34" font-size="23" font-weight="400" fill="#24343f">入 M02：極性固定相、適當低極性移動相及分析</text>
<text x="697" y="662" font-size="23" font-weight="400" fill="#24343f">物</text>
<text x="697" y="694.66" font-size="23" font-weight="400" fill="#24343f">鏈：矽膠作用較強 → 在表面停留較久 → tR 較長</text>
<text x="697" y="727.32" font-size="23" font-weight="400" fill="#24343f">出 M04：正相的流出次序</text>
<rect x="675" y="960" width="550" height="395" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="697" y="1001" font-size="27" font-weight="600" fill="#286c68">L06｜在 C18 上，誰會比較晚流出？</text>
<text x="697" y="1049.34" font-size="23" font-weight="400" fill="#24343f">入 M02：疏水固定相、移動相與分析物在該 pH</text>
<text x="697" y="1082" font-size="23" font-weight="400" fill="#24343f">的性質</text>
<text x="697" y="1114.66" font-size="23" font-weight="400" fill="#24343f">鏈：較強疏水保留 → 平均遷移較慢 → tR 較長</text>
<text x="697" y="1147.32" font-size="23" font-weight="400" fill="#24343f">出 M04：逆相的相對流出次序</text>
<rect x="675" y="1380" width="550" height="395" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="697" y="1421" font-size="27" font-weight="600" fill="#286c68">L07｜比較官能基時，要先固定哪些條件？</text>
<text x="697" y="1469.34" font-size="23" font-weight="400" fill="#24343f">入 M02：完整結構、骨架、解離與選定模式</text>
<text x="697" y="1502" font-size="23" font-weight="400" fill="#24343f">鏈：先比可用結構差異 → 判與兩相作用 → 指定</text>
<text x="697" y="1534.66" font-size="23" font-weight="400" fill="#24343f">條件下排序</text>
<text x="697" y="1567.32" font-size="23" font-weight="400" fill="#24343f">出 M04：有理由且有限定的結構排序</text>
<rect x="675" y="1800" width="550" height="395" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="697" y="1841" font-size="27" font-weight="600" fill="#286c68">L08｜矽膠接上 C18 後，為何仍可能拖</text>
<text x="697" y="1879.34" font-size="27" font-weight="600" fill="#286c68">尾？</text>
<text x="697" y="1927.68" font-size="23" font-weight="400" fill="#24343f">入 M02：鍵結基團、殘餘矽醇基、pH 與峰形</text>
<text x="697" y="1960.34" font-size="23" font-weight="400" fill="#24343f">鏈：殘餘表面與帶電分析物作用 → 保留不均／拖</text>
<text x="697" y="1993" font-size="23" font-weight="400" fill="#24343f">尾 → 封端或調整條件</text>
<text x="697" y="2025.66" font-size="23" font-weight="400" fill="#24343f">出 M04：固定相選擇與拖尾候選原因</text>
<text x="680" y="2232" font-size="22" font-weight="400" fill="#286c68">依序讀本組L；卡住回同號R／建構。</text>
<rect x="1270" y="365" width="580" height="1890" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="1290" y="408" font-size="28" font-weight="600" fill="#356844">C｜控制配方、酸鹼與時間</text>
<text x="1290" y="460" font-size="23" font-weight="400" fill="#24343f">解離、溶劑強度與流量改的是不同環節。</text>
<rect x="1285" y="540" width="550" height="395" rx="18" fill="#fff" stroke="#356844" stroke-width="2"/>
<text x="1307" y="581" font-size="27" font-weight="600" fill="#356844">L09｜酸與鹼改 pH，保留為何常往相反方</text>
<text x="1307" y="619.34" font-size="27" font-weight="600" fill="#356844">向？</text>
<text x="1307" y="667.68" font-size="23" font-weight="400" fill="#24343f">入 M02：分析物為酸或鹼、pKa、移動相 pH 與</text>
<text x="1307" y="700.34" font-size="23" font-weight="400" fill="#24343f">RP 模式</text>
<text x="1307" y="733" font-size="23" font-weight="400" fill="#24343f">鏈：pH 改解離比例 → 疏水保留改變 → tR 方向改</text>
<text x="1307" y="765.66" font-size="23" font-weight="400" fill="#24343f">變</text>
<text x="1307" y="798.32" font-size="23" font-weight="400" fill="#24343f">出 M04：酸鹼題的保留方向</text>
<rect x="1285" y="960" width="550" height="395" rx="18" fill="#fff" stroke="#356844" stroke-width="2"/>
<text x="1307" y="1001" font-size="27" font-weight="600" fill="#356844">L10｜pKa 附近的 pH 改變，為何特別值得</text>
<text x="1307" y="1039.34" font-size="27" font-weight="600" fill="#356844">注意？</text>
<text x="1307" y="1087.68" font-size="23" font-weight="400" fill="#24343f">入 M02：pH 區間、pKa 及中性／離子態保留假設</text>
<text x="1307" y="1120.34" font-size="23" font-weight="400" fill="#24343f">鏈：比較區間與 pKa → 解離比例變化 → 判題定</text>
<text x="1307" y="1153" font-size="23" font-weight="400" fill="#24343f">保留變化</text>
<text x="1307" y="1185.66" font-size="23" font-weight="400" fill="#24343f">出 M04：變動大小的近似判斷</text>
<rect x="1285" y="1380" width="550" height="395" rx="18" fill="#fff" stroke="#356844" stroke-width="2"/>
<text x="1307" y="1421" font-size="27" font-weight="600" fill="#356844">L11｜移動相比例，怎樣轉成沖提強度？</text>
<text x="1307" y="1469.34" font-size="23" font-weight="400" fill="#24343f">入 M02：模式、溶劑種類及明確的比例順序</text>
<text x="1307" y="1502" font-size="23" font-weight="400" fill="#24343f">鏈：先認強溶劑 → 換成分率 → 比保留方向</text>
<text x="1307" y="1534.66" font-size="23" font-weight="400" fill="#24343f">出 M04：較強／較弱沖提與 tR 順序</text>
<rect x="1285" y="1800" width="550" height="395" rx="18" fill="#fff" stroke="#356844" stroke-width="2"/>
<text x="1307" y="1841" font-size="27" font-weight="600" fill="#356844">L12｜縮短分析時間，和改善分離，是同一</text>
<text x="1307" y="1879.34" font-size="27" font-weight="600" fill="#356844">件事嗎？</text>
<text x="1307" y="1927.68" font-size="23" font-weight="400" fill="#24343f">入 M02：等度／梯度、流量、柱長、溫度與 Rs</text>
<text x="1307" y="1960.34" font-size="23" font-weight="400" fill="#24343f">鏈：改變通過時間或保留 → 讀 tR／峰寬／峰距 →</text>
<text x="1307" y="1993" font-size="23" font-weight="400" fill="#24343f">比時間與分離品質</text>
<text x="1307" y="2025.66" font-size="23" font-weight="400" fill="#24343f">出 M04：有品質條件的操作調整</text>
<text x="1290" y="2232" font-size="22" font-weight="400" fill="#356844">依序讀本組L；卡住回同號R／建構。</text>
<rect x="50" y="2315" width="580" height="1890" rx="18" fill="#e8e1f2" stroke="#685185" stroke-width="2"/>
<text x="70" y="2358" font-size="28" font-weight="600" fill="#685185">D｜換一種分離依據</text>
<text x="70" y="2410" font-size="23" font-weight="400" fill="#24343f">電荷、離子對、孔隙與親水層，各有自己的尺。</text>
<rect x="65" y="2490" width="550" height="395" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="87" y="2531" font-size="27" font-weight="600" fill="#685185">L13｜陽離子交換樹脂為何帶負電？</text>
<text x="87" y="2579.34" font-size="23" font-weight="400" fill="#24343f">入 M02：固定基團電荷、分析物電荷、pH 與競爭</text>
<text x="87" y="2612" font-size="23" font-weight="400" fill="#24343f">離子</text>
<text x="87" y="2644.66" font-size="23" font-weight="400" fill="#24343f">鏈：相反電荷吸引 → pH／競爭鹽改作用 → 不同</text>
<text x="87" y="2677.32" font-size="23" font-weight="400" fill="#24343f">tR</text>
<text x="87" y="2709.98" font-size="23" font-weight="400" fill="#24343f">出 M04：IEC 的保留與沖提方向</text>
<rect x="65" y="2910" width="550" height="395" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="87" y="2951" font-size="27" font-weight="600" fill="#685185">L14｜離子對試劑要與誰帶相反電荷？</text>
<text x="87" y="2999.34" font-size="23" font-weight="400" fill="#24343f">入 M02：分析物在 pH 下的電荷及試劑疏水端</text>
<text x="87" y="3032" font-size="23" font-weight="400" fill="#24343f">鏈：反號作用／表面吸附 → 增加有效疏水保留 →</text>
<text x="87" y="3064.66" font-size="23" font-weight="400" fill="#24343f">RP 更能留住離子</text>
<text x="87" y="3097.32" font-size="23" font-weight="400" fill="#24343f">出 M04：離子對試劑選擇與相對 tR</text>
<rect x="65" y="3330" width="550" height="395" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="87" y="3371" font-size="27" font-weight="600" fill="#685185">L15｜分子篩的大分子，為何反而先出？</text>
<text x="87" y="3419.34" font-size="23" font-weight="400" fill="#24343f">入 M02：水動力尺寸、孔隙大小及有效分離範圍</text>
<text x="87" y="3452" font-size="23" font-weight="400" fill="#24343f">鏈：大者少進孔 → 可走體積較小 → 較早流出</text>
<text x="87" y="3484.66" font-size="23" font-weight="400" fill="#24343f">出 M04：SEC 的尺寸排序</text>
<rect x="65" y="3750" width="550" height="395" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="87" y="3791" font-size="27" font-weight="600" fill="#685185">L16｜HILIC 為何用高有機相，卻留住親水</text>
<text x="87" y="3829.34" font-size="27" font-weight="600" fill="#685185">物？</text>
<text x="87" y="3877.68" font-size="23" font-weight="400" fill="#24343f">入 M02：親水表面、高有機／少量水相及電荷條</text>
<text x="87" y="3910.34" font-size="23" font-weight="400" fill="#24343f">件</text>
<text x="87" y="3943" font-size="23" font-weight="400" fill="#24343f">鏈：親水層／表面作用 → 親水物較易保留 → 加</text>
<text x="87" y="3975.66" font-size="23" font-weight="400" fill="#24343f">水常較快沖出</text>
<text x="87" y="4008.32" font-size="23" font-weight="400" fill="#24343f">出 M04：HILIC 的模式與題圖次序</text>
<text x="70" y="4182" font-size="22" font-weight="400" fill="#685185">依序讀本組L；卡住回同號R／建構。</text>
<rect x="660" y="2315" width="580" height="1890" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="680" y="2358" font-size="28" font-weight="600" fill="#326991">E｜加上立體、反應與光學線索</text>
<text x="680" y="2410" font-size="23" font-weight="400" fill="#24343f">先給出可分離或可偵測的差異，再讀光學訊號。</text>
<rect x="675" y="2490" width="550" height="395" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="697" y="2531" font-size="27" font-weight="600" fill="#326991">L17｜鏡像異構物，靠什麼產生保留差異？</text>
<text x="697" y="2579.34" font-size="23" font-weight="400" fill="#24343f">入 M02：對映異構物與可作用的對掌環境</text>
<text x="697" y="2612" font-size="23" font-weight="400" fill="#24343f">鏈：與手性環境作用不同 → 自由能／保留不同 →</text>
<text x="697" y="2644.66" font-size="23" font-weight="400" fill="#24343f">對映峰分開</text>
<text x="697" y="2677.32" font-size="23" font-weight="400" fill="#24343f">出 M04：對掌性方法的可用性</text>
<rect x="675" y="2910" width="550" height="395" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="697" y="2951" font-size="27" font-weight="600" fill="#326991">L18｜衍生化，是把分析物的哪個弱點補起</text>
<text x="697" y="2989.34" font-size="27" font-weight="600" fill="#326991">來？</text>
<text x="697" y="3037.68" font-size="23" font-weight="400" fill="#24343f">入 M02：原分析物的偵測／分離弱點及反應產率</text>
<text x="697" y="3070.34" font-size="23" font-weight="400" fill="#24343f">鏈：接上合適基團 → 改偵測或保留 → 可辨識的</text>
<text x="697" y="3103" font-size="23" font-weight="400" fill="#24343f">產物訊號</text>
<text x="697" y="3135.66" font-size="23" font-weight="400" fill="#24343f">出 M03：衍生物的分離與偵測</text>
<rect x="675" y="3330" width="550" height="395" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="697" y="3371" font-size="27" font-weight="600" fill="#326991">L19｜UV 和 DAD 怎樣把流出物變成訊號？</text>
<text x="697" y="3419.34" font-size="23" font-weight="400" fill="#24343f">入 M03：分析物吸收、選定波長及校正</text>
<text x="697" y="3452" font-size="23" font-weight="400" fill="#24343f">鏈：光吸收隨流出改變 → 吸光度峰／光譜 → 定</text>
<text x="697" y="3484.66" font-size="23" font-weight="400" fill="#24343f">量或支持比對</text>
<text x="697" y="3517.32" font-size="23" font-weight="400" fill="#24343f">出 M04：吸光度訊號及有限的光譜證據</text>
<rect x="675" y="3750" width="550" height="395" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="697" y="3791" font-size="27" font-weight="600" fill="#326991">L20｜螢光選擇性，為何常比單純 UV 高？</text>
<text x="697" y="3839.34" font-size="23" font-weight="400" fill="#24343f">入 M03：激發波長、發射波長及分析物螢光特性</text>
<text x="697" y="3872" font-size="23" font-weight="400" fill="#24343f">鏈：能被激發且放出螢光 → 選發射光 → 較少背</text>
<text x="697" y="3904.66" font-size="23" font-weight="400" fill="#24343f">景干擾</text>
<text x="697" y="3937.32" font-size="23" font-weight="400" fill="#24343f">出 M04：螢光訊號與適用分析物</text>
<text x="680" y="4182" font-size="22" font-weight="400" fill="#326991">依序讀本組L；卡住回同號R／建構。</text>
<rect x="1270" y="2315" width="580" height="1890" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="1290" y="2358" font-size="28" font-weight="600" fill="#b72d4a">F｜補讀數與定量品質</text>
<text x="1290" y="2410" font-size="23" font-weight="400" fill="#24343f">偵測機制與校正條件決定含量及效率結論。</text>
<rect x="1285" y="2490" width="550" height="395" rx="18" fill="#fff" stroke="#b72d4a" stroke-width="2"/>
<text x="1307" y="2531" font-size="27" font-weight="600" fill="#b72d4a">L21｜電化學、PAD 與電導，讀的是同一種</text>
<text x="1307" y="2569.34" font-size="27" font-weight="600" fill="#b72d4a">量嗎？</text>
<text x="1307" y="2617.68" font-size="23" font-weight="400" fill="#24343f">入 M03：可氧化還原基團、電位控制或離子導電</text>
<text x="1307" y="2650.34" font-size="23" font-weight="400" fill="#24343f">鏈：選電位測電流／量離子導電 → 分清機制與訊</text>
<text x="1307" y="2683" font-size="23" font-weight="400" fill="#24343f">號 → 選適用偵測</text>
<text x="1307" y="2715.66" font-size="23" font-weight="400" fill="#24343f">出 M04：電流或電導訊號與方法配對</text>
<rect x="1285" y="2910" width="550" height="395" rx="18" fill="#fff" stroke="#b72d4a" stroke-width="2"/>
<text x="1307" y="2951" font-size="27" font-weight="600" fill="#b72d4a">L22｜沒發色基，怎麼選 RI、ELSD 或</text>
<text x="1307" y="2989.34" font-size="27" font-weight="600" fill="#b72d4a">CAD？</text>
<text x="1307" y="3037.68" font-size="23" font-weight="400" fill="#24343f">入 M03：分析物揮發性、移動相與是否梯度</text>
<text x="1307" y="3070.34" font-size="23" font-weight="400" fill="#24343f">鏈：折射差／殘留微粒／粒子電荷 → 訊號 → 適</text>
<text x="1307" y="3103" font-size="23" font-weight="400" fill="#24343f">用範圍與校正</text>
<text x="1307" y="3135.66" font-size="23" font-weight="400" fill="#24343f">出 M04：不靠發色基的讀數選擇</text>
<rect x="1285" y="3330" width="550" height="395" rx="18" fill="#fff" stroke="#b72d4a" stroke-width="2"/>
<text x="1307" y="3371" font-size="27" font-weight="600" fill="#b72d4a">L23｜峰面積，怎麼變成可信的濃度？</text>
<text x="1307" y="3419.34" font-size="23" font-weight="400" fill="#24343f">入 M03：校正、稀釋、樣品面積與內標加入時點</text>
<text x="1307" y="3452" font-size="23" font-weight="400" fill="#24343f">鏈：用標準建關係 → 外標面積／內標比值 → 回</text>
<text x="1307" y="3484.66" font-size="23" font-weight="400" fill="#24343f">算濃度及品質</text>
<text x="1307" y="3517.32" font-size="23" font-weight="400" fill="#24343f">出 M04：濃度、單位與可補償的誤差</text>
<rect x="1285" y="3750" width="550" height="395" rx="18" fill="#fff" stroke="#b72d4a" stroke-width="2"/>
<text x="1307" y="3791" font-size="27" font-weight="600" fill="#b72d4a">L24｜小粒徑提高效率，為何同時要更高</text>
<text x="1307" y="3829.34" font-size="27" font-weight="600" fill="#b72d4a">壓？</text>
<text x="1307" y="3877.68" font-size="23" font-weight="400" fill="#24343f">入 M02：粒徑、柱長、內徑、F／u與板高</text>
<text x="1307" y="3910.34" font-size="23" font-weight="400" fill="#24343f">鏈：細粒減少路徑／質傳展寬 → H下降 → 同L時N</text>
<text x="1307" y="3943" font-size="23" font-weight="400" fill="#24343f">增，但阻力增</text>
<text x="1307" y="3975.66" font-size="23" font-weight="400" fill="#24343f">出 M04：效率與壓力的有條件比較</text>
<text x="1290" y="4182" font-size="22" font-weight="400" fill="#b72d4a">依序讀本組L；卡住回同號R／建構。</text>
<rect x="50" y="4380" width="1800" height="270" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="4421" font-size="27" font-weight="600" fill="#9e771c">完整路線示範｜弱酸 aspirin 在 C18 升 pH</text>
<text x="72" y="4469.34" font-size="24" font-weight="400" fill="#24343f">M01 問tR變化 → M02 L06認RP、L09–10讀酸與pKa3.5 → pH3到5使A⁻增加</text>
<text x="72" y="4503.42" font-size="24" font-weight="400" fill="#24343f">M03 預期tR縮短 → M04 Q024選C，核對普通RP與樣品／柱穩定條件。</text>
<text x="72" y="4537.5" font-size="24" font-weight="400" fill="#24343f">這條短鏈交出方向；未提供各態保留，就不編造新tR。</text>
<text x="50" y="4742" font-size="20" font-weight="400" fill="#61717a">全部24條L均有入口、短鏈與用途；不同L是可重用工具，不把並列概念硬接成必然因果。</text>
<text x="50" y="4778" font-size="20" font-weight="400" fill="#61717a">原題：CH20 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

</details>

獨立圖檔：[[藥物分析_高效能液相層析法HPLC_小循環掛載點圖_v3_0.svg]]


## L01｜什麼檢品適合走液相分析？

^hplc-c-l01

**先問：**什麼檢品適合走液相分析？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m01|M01]]取用「檢品的溶解性、穩定性及分析目的」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]使用「方法適用性與檢品處理需求」。

**短鏈：**可溶且方法條件相容 → 選液相分離與偵測 → 留下可測的檢品。

HPLC 是 high-performance liquid chromatography（高效能液相層析法）。移動相是液體，檢品不必先氣化，常用於不易揮發、受熱可能分解或較大型的成分。仍要能溶解、穩定，並與管柱、偵測器和基質相容。

**立即用一次：**PEG 不易直接作常規 GC 分析，又缺乏強 UV 吸收；題目選 HPLC-ELSD。不是先看到「有機物」就選 UV。

**條件：**不同藥物、聚合物與生物製劑都有相應 LC 方法；不能單憑類別一概排除。

**易錯：**「只要溶於移動相就一定適用」漏掉穩定性、回收與偵測。

**閉卷自問：**肝素不是小分子，可以直接判它不能用 HPLC 嗎？

<details>
<summary>收起答案與最短理由</summary>

不能。LC 有不同模式與偵測法；Q048 題本一律給分，不能拿它證明所有肝素都不能分析。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q048|Q048｜109-1 #10]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l01|同題複習卡]]；來源與用途站见本節掛載。

## L02｜幫浦、進樣器與管柱各改變什麼？

^hplc-c-l02

**先問：**幫浦、進樣器與管柱各改變什麼？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「流路、流量及固定的進樣量」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m03|M03]]使用「具有時間基準的層析圖」。

**短鏈：**穩定送液／定量進樣 → 柱內不同保留 → 偵測器隨時間記錄。

流路是儲液瓶 → 去氣泡 → 幫浦 → 進樣器 → 保護柱 → 分析柱 → 所選偵測器 → 廢液；電腦另外收訊號。幫浦常設定體積流量 F，壓力由流路阻力形成。進樣器控制注入量，柱溫箱控制溫度，偵測器設定波長。

**立即用一次：**F 從 1 改成 2 mL/min，在保留體積相同的近似下，8 min 的峰變成 4 min；波長不由幫浦調整。

**條件：**定流量、等度沖提的簡化例子；梯度、黏度與選擇性變化要另核對。保護柱的粒徑依產品，不必一定較大。

**易錯：**設定流量不等於同時把壓力獨立鎖成常數。

**閉卷自問：**題目問泵的功能，四個選項為波長、滯留時間、溫度、進樣量，選哪個？

<details>
<summary>收起答案與最短理由</summary>

滯留時間；送液速度影響通過與流出時間。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q058|Q058｜108-2 #38]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f01|F01]]。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c02|C02]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c12|C12]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l02|同題複習卡]]；來源與用途站见本節掛載。

## L03｜峰的位置、面積與寬度各回答什麼？

^hplc-c-l03

**先問：**峰的位置、面積與寬度各回答什麼？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m03|M03]]取用「時間軸、峰訊號與相應參考」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「所求量與可支持的判讀」。

**短鏈：**時間／面積／寬度分開讀 → 配對保留／量／效率 → 得到有證據的結論。

chromatogram（層析圖）橫軸通常是時間，縱軸依偵測器是吸光度、電流或其他訊號。tR 是流出峰的位置；積分峰面積用於校正定量；寬度用於展寬與解析度。t₀ 是未保留標記通過所需時間。

**立即用一次：**A 在 4 min，B 在 8 min：只說 B 較晚流出。若兩者響應不同，即使面積相等也不能直接說濃度相等。

**條件：**辨識須同條件對照標準，必要時加光譜或其他方法；定量須有各自校正。

**易錯：**較晚、較高、較寬的峰都不直接等於含量較高。

**閉卷自問：**未知物與標準品 tR 相同，能獨自證明身分嗎？

<details>
<summary>收起答案與最短理由</summary>

不能。共流出可能存在；同 tR 是比對線索，需要方法的專一性證據。

</details>

先用EX01與[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c02|C02]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c06|C06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]练讀數；無另造來源Q。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c02|C02]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c06|C06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l03|同題複習卡]]；來源與用途站见本節掛載。

## L04｜溶劑能混合，和能拿來萃取，有何差別？

^hplc-c-l04

**先問：**溶劑能混合，和能拿來萃取，有何差別？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「樣品基質、互溶性、目的與溶解度」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]使用「適合分離且回收可核對的製樣」。

**短鏈：**均相作移動相／兩相作萃取 → 控制分配與回收 → 取得可進樣溶液。

移動相混合後應保持方法要求的均一組成，緩衝鹽也不能析出。液液萃取則常故意用兩個不互溶的液相，把藥物與油性基質分開。它們不是同一任務。THF、乙腈、甲醇能與水混溶；THF 的氧可接受水的氫鍵。

**立即用一次：**hydrocortisone 軟膏題選 MeOH／hexane：甲醇帶出藥物，己烷容納油性基質；仍要做回收試驗，不把藥物損失當成除基質成功。

**條件：**互溶依溫度、比例及鹽含量；CH20 是室溫常用組合題。正逆相切換先查互溶性與管柱建議。

**易錯：**DMF 是醯胺，不是醛；乙腈可以接受氫鍵，不是「完全不能氫鍵」。

**閉卷自問：**水／THF 與甲醇／正己烷，哪組一般形成兩相？

<details>
<summary>收起答案與最短理由</summary>

甲醇／正己烷；水／THF 一般可混溶。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q026|Q026｜111-1 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q040|Q040｜109-2 #27]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q047|Q047｜109-1 #8]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q059|Q059｜108-1 #11]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q069|Q069｜107-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q070|Q070｜106-2 #2]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q094|Q094｜103-1 #8]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f02|F02]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04|同題複習卡]]；來源與用途站见本節掛載。

## L05｜在裸矽膠上，誰會比較晚流出？

^hplc-c-l05

**先問：**在裸矽膠上，誰會比較晚流出？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「極性固定相、適當低極性移動相及分析物」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「正相的流出次序」。

**短鏈：**矽膠作用較強 → 在表面停留較久 → tR 較長。

normal-phase chromatography（正相）用較極性的固定相、相對低極性的移動相。裸矽膠表面有 silanol（矽醇基 Si–OH），可與分析物形成氫鍵等作用。類似骨架且不發生額外解離時，較能與矽膠作用者常留較久。

**立即用一次：**同碳數的丁烷、丁醛、丁酸在題定矽膠條件下：丁酸 > 丁醛 > 丁烷的 tR，對應 Q056 的 c>b>a。

**條件：**這是指定條件的相互作用比較；水分、酸鹼、溶劑與表面狀態可改變次序。

**易錯：**不能把「正相極性大較晚」搬到 C18 或 SEC。

**閉卷自問：**n-hexanol、benzene、n-hexane 在 Q087 的矽膠題如何排序？

<details>
<summary>收起答案與最短理由</summary>

tR：hexanol > benzene > hexane。醇可與表面強作用；苯的吸附不能只用永久偶極解釋。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q037|Q037｜110-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q050|Q050｜109-1 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q054|Q054｜108-2 #11]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q056|Q056｜108-2 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q071|Q071｜106-2 #31]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q087|Q087｜104-2 #32]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f03|F03]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f06|F06]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05|同題複習卡]]；來源與用途站见本節掛載。

## L06｜在 C18 上，誰會比較晚流出？

^hplc-c-l06

**先問：**在 C18 上，誰會比較晚流出？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「疏水固定相、移動相與分析物在該 pH 的性質」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「逆相的相對流出次序」。

**短鏈：**較強疏水保留 → 平均遷移較慢 → tR 較長。

reversed-phase chromatography（逆相）通常用疏水的鍵結固定相及水／有機溶劑。C18 又叫 ODS；octadecyl 是十八碳烷基。固定其他條件，疏水性較大的分析物常保留較久；離子化、表面殘餘基團及特定選擇性會補上其他作用。

**立即用一次：**toluene、propylbenzene、amylbenzene 為同族中性物；題定 C18 下，amylbenzene 最晚，toluene 最早。

**條件：**比較同類結構及相同條件；不能只數碳數就包辦所有藥物。C8／C18 保留要看實際相性質。

**易錯：**水比例提高常延長 RP 保留；別把正相的溶劑方向背過來。

**閉卷自問：**題目已給四蛋白親脂性 I>II>III>IV 且 C18 梯度分離良好，誰最後？

<details>
<summary>收起答案與最短理由</summary>

I；題目已指定可用的疏水性差異與合適方法。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q010|Q010｜112-2 #27]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q032|Q032｜110-2 #31]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q065|Q065｜107-1 #10]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q077|Q077｜106-1 #37′]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q081|Q081｜105-2 #32]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f05|F05]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06|同題複習卡]]；來源與用途站见本節掛載。

## L07｜比較官能基時，要先固定哪些條件？

^hplc-c-l07

**先問：**比較官能基時，要先固定哪些條件？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「完整結構、骨架、解離與選定模式」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「有理由且有限定的結構排序」。

**短鏈：**先比可用結構差異 → 判與兩相作用 → 指定條件下排序。

先看是否帶電，再看可形成氫鍵等作用的基團，並同時看疏水骨架。COOH、OH、胺、羰基、醚等可提供不同相互作用；一張官能基表只是近似提示，不是每個完整分子的唯一保留常數。位置異構物還涉及可接近性及氫鍵位置。

**立即用一次：**Q096：3-O-benzylmorphine 增加 O–CH₂–phenyl（苄基），題定 C18 最晚；normorphine 去掉 N-methyl，Q061 最早。不是把 benzyl 誤畫成 tolyl。

<details>
<summary>原圖輔助：比較結構／反應</summary>

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA/YAAAEOCAIAAACsJBteAAAACXBIWXMAAA7EAAAOxAGVKw4bAACxIElEQVR4nOydB1gUV9v312iMJlGjielfHlOMJdXYYkOk96qAqNhBRMSGYiMK6KPYsaCI2LDEEnvBDoqIvSOKGhSxIPhiAzG63z97XucdZ2aXXbbArvfv8vJaZs6cOTNzzn3+95n7nJHJXzFixIj//ve/coIgCIIgCIIgDMj/+3//73/+5390mKGM+0USnyAIgiAIgiAMD0l8giAIgiAIgjApSOITBEEQBEEQhElBEp8gCIIgCIIgTAqS+ARBEARBEARhUpDEJwiCIAiCIAiTgiQ+QRAEQRAEQZgUJPEJgiAIgiAIwqQgiU8QBEEQBEEQJgVJfIIgCIIgCIIwKUjiEwRBEARBEIRJQRKfIAiCIAiCIEwKkvgEQRAEQRAEYVKQxCcIgiAIgiAIk4IkPkEQBEEQBEGYFCTxCYIgCIIgCMKkIIlPEARBEARBECaFMUl8BweHS5cu4cfz588vqceNGzfE+ezdu9fCwkLZWYqKihwdHU+fPl2GEhYXFzdo0GDHjh1lOFZAYGDgkiVLNDqkRYsWksUOCwtLSEhgv728vLZv365pYa5cuYID7969q+mBBEEQBEEQhOGpQBL/9u3bWVlZKhJ8+OGHx48fx4/s7Ox3XqdKlSoymaxq1aqC7XZ2duJ81q1bh6wEG2/evPn48WP8wP/Ias+ePeqXnCM/Px/H7ty5swzHCmjZsuW4ceM0OqRy5cqHDh0Sb3d1deWy+vbbbzX1HOSKe/LZZ5/5+flpeiBBEARBEARheCqQxPf19a1Vq5aKBJzEFxMaGtq6dWs1TyQp8Z2dnfv06SPXTuLDT8CxaWlpZThWQHlJ/Pnz54+Wok2bNpUqVRo2bJjkXk2LShAEQRAEQeiPCiTxg4ODv/nmGxUJlEl8COtq1aodOHBAzRNJSvy6desuWLBArp3EP3v2LI7NzMwsw7ECtJH4JSUlp3mYm5vzJX5ERAS369q1a+LzIo2jhri5uWl/yQRBEARBEIROKH+Jv3bt2ry8PPyADG3WrBl+PHv2bP369VyxuHFl6PiePXviB/Zyh7948cLS0hLb1S+iWOKfOHEC0vzy5cty7SR+UlISjn348GEZjhWgvsSPi4ubqqBSpUr9+/fHjwsXLshehy/x+duhzsXnxR3WvvwEQRAEQRBEeVHOEj87OxtCs0qVKi4uLl5eXj/++CNEap06dbCRiyeB4vT29vb09MRGa2tr/I6NjeVygMDF9sDAQJwuIyOj5evk5ubyTzdz5swDBw5A4kMNL1y4kNs+atSoypUr+/n5de/e3dfXl52oO4/Vq1erc/Eo87vvvqtOSgG4qMjISP4WgcTPycn5/vvvod3Fx6LYtgpQ7BYtWuDHnTt3/uHh7OzMl/iLFi3idsFBEuTGSXxkslMNDh8+XIbrJQiCIAiCIPRHOUt8SEzo8mXLlgUHB1erVg0i1c3Nbfbs2UeOHCkuLuanTEtLw95jx44JcoBe91YA1Z6cnPzrr79CK0NqT5kyBekF1/bZZ5/NmzcPh8CpeOedd2bMmIGNULq4C5C2XRTA08CBFhYWXXisXLmSyyQkJERWViwtLcU34eXLlx9++GF8fDx/o0DiIw3Ueb9+/VTcTJ3E4nMSf8uWLZ+opG7duriipk2bCnLAPT979qyKUxAEQRAEQRB6pfwDdRiLFi2qXr06BLq7u7tkgvDwcAhKe3v7kpISyQQ4/ODBg56eni4uLvgTToJgQL2wsBA57Nu3jwXq7Ny5Eyp/9erV69evhzjOyclhyUoN1Ll27dohJTRp0gQnRUlSUlIkE5w7d06c4fHjx3FGQVi8OFAHTgsyx1UoK5huJb5qbt68aW5ujtuYmprK3w5/6ZtvvsHlzJ8/v9RMCIIgCIIgCH1QIST+yZMnobajoqJOnTr11ltvTZ06VZzm559/hnCsVauWj4+PXLHWOzecDMmOLe+//z7ke25uLn5s3rw5MTERh/BzgPxFDvn5+Vws/oYNG7Kzs5s1a8byZJQ5Fv/ly5coHq5a8m2DCiIiIr7//nvBRrHEv3//ftWqVdmcYEk4if/06dN1PHCBfInfv39/btetW7fE5+VL/CdPntjY2ERGRnIhTxDx8Mdq165taWkpPryoqAgeDu7AyJEj1b8DBEEQBEEQhA4pf4kPUfj1119DerLInMDAQEjV9PR0fpqMjIx3Faxdu7Zu3brTp08PCgpycnLauXPnd999BzWPNDVr1kxKSpIrRruRW69evXr37s3PhFPS/Om2+P32229fuXKFS1ZmiX/06FEcePbs2QYNGoSHh6t/4C+//DJ06FDBRsnptl26dGnevLmyfJjEx+PMzMzkR9TAMeBLfNwobpf4K11iiR8bG/vTTz/hLnXv3n3JkiWNGjX64osvli9frqwYaWlpMTExOFCdaycIgiAIgiB0TvlLfLBp0yZOUhcUFERFRT1//pyfYNiwYX5+fmzRzC1btjg4OAQpwK6mTZsyiV+jRg0m8Z89ewafoVKlSvwAemBmZsZi2fkS//Tp03FxcfxkZZb4I0eOrF+/vlwRUwQlreZRFy9exOkELo1cicRnLyJwiGRWkPheXl61atXivmXLsLGx0T5QJyUlBTcQZ4eLdfXqVdUXRRAEQRAEQZQjFULiq+bJkycffPDBgQMHuHXxnz59Kpb477333q5du9ghc+bMgRhla3FyZGVlXb9+XS5aNBO5/Q+PnJwcHLtx40b+xlILCZ/k008/jYiIkCuC9ZGDmuv0DxkyRBylI1e+aGa9evXGjBkj2Hj48OGePXvipI0bN161apVgnZxWrVpxD0Idid+1a9cDUuzfvx/PtHr16i1atBDsItFPEARBEARRcTACiR8dHd2oUSO27Az36SuxxK9Wrdq+ffvYXjs7O+hdwRo1HAKJHxAQoHoZnMqVK5dayNjYWPgY9+/fZ386Ozvb29uXetTjx49r1aolOfdAmcQfOnSo4BWBo6NjpUqVLC0tUVTJ6bY//vjjrFmz2O9SJX6TJk1wve9I8fbbb+MUVatWFWzHRnGgEUEQBEEQBFFeVHSJD2X/ySef/Pnnn/LXv24rlvgQpmx1l+3bt0OGhoWF1a9fX7zuu1wk8e/cuXOJB/sMVkJCAn+j6kLm5OTUrl2bP8H02LFjyKTUNeMnTpxYs2ZNyQegTOIfOXIEOZ88eZK/hU17FayoU1JSsnbtWgsLC6Rfs2YN21iqxEeCOXPmSO46ffo0svr777/5G3HPcd6DBw+qyJMgCIIgCIIwJBVd4gMu8kQg8Rs3bhwQEPDRRx9B4iMBE775+fn16tULDw8vKirCLsh9cYbir9vy0TQWH05Ihw4dvv76a8EE027duv3www/Pnj1TduDt27dr1KgRFRUluVeZxMfpvvjiC3GsjvyVxEcCCO7AwMCPFHTv3h2XA7+FpYGCt7W1HfoK8bo3derUgWMgWSSxxMe9+u677/AUlF0jQRAEQRAEYXiMQOJz8CX+pk2bRrzi1KlTuAaoz8zMTGtr66ZNm7LFeQYPHuzt7S3OR7cSPyQkBNo6JSVFsD0vL+/jjz8ODg5WdqCjo2P9+vXhikjuVSbxwcCBA+E8iLdzK+p89tlnnTt3/uuvv+BgrF69unr16tz0ZUj8Nm3acF/t9ff35+dw9+5dXPvRo0clzyuQ+LjJVlZWDRo0ULFUP0EQBEEQBGF4jFXiCzh37hzU54ULFxo3bsx9xOrEiROtW7cWJ9ahxI+IiEBiZZEtycnJkN1cHLyAjRs38uNtBKiQ+LhYeDji7VygzsuXL7mN8Hn4fo7qQJ2kpKQqVaoIvivMIZD406dP/+STT9gMZoIgCIIgCKLiYPQSPzo62tbWtm7dur///rtc8WEm/t6nT5+K89GJxIeMDgsLQ0rVS+AvXry4UqVKM2fOVJ2bGBUSXxnir9umpKQIRuVVS/yBAwfivMr2igN1xJ++kis+ZBYXF6fs7QRBEARBEAShb4xe4qempk6ePHnVqlXqf2tJe4kPz8HHxwfJIiMjSz0d9O5bb701YMAAwWL/qtFe4hcUFHz11Ve9evXip1Eh8V+8ePHZZ59Nnz5dWf6S020FFBcXv//++0g2duxYjQpPEARBEARB6AqjlPhJSUlT1WPGjBnifPgSf/bs2UGv07dvXyhUFxcX/sbBgwdzh0PpNmzYsFq1amydH3XYunUrhG+LFi2UfbWKwWYVv3z58u7du19++eWECRPUzF+uEPTs27rsz8LCwlatWv3www8PHz7kJ1Mh8bH97bffFg/M31eQn5+/du1anOLOnTsqigE3BiVHMtxY9QtPEARBEARB6BCjlPjx8fFd1KNHjx7ifPgSf/z48Z5qgKy4w21tbZs2bZqRkaFR4TMzM5s1a9a4cWPJdTwZo0eP5hbjr127dqmLdTKSk5PhP7zzzjs//fQT96Jgzpw5//nPf7KzswWJVUh8MzMzuDfi7X369OFKhTSllgf+gLIJuwRBEARBEIQBMCaJD1WtkwjvwsJCTQU6n4KCAo1Cbjhw1M2bN1UkePDgwZ49e5KSkg4dOqTRMjXp6ekHDx4UTDyQzGHfvn3KyvDkyZN79+6Jt9+5cydVwZkzZ1T4JwRBEARBEEQFwZgkPkEQBEEQBEEQpUISnyAIgiAIgiBMCpL4BEEQBEEQBGFSkMQnCIIgCIIgCJOCJD5BEARBEARBmBQk8QmCIAiCIAjCpCCJTxAEQRAEQRAmBUl8giAIgiAIgjApSOITBEEQBEEQhElBEp8gCIIgCIIgTAqS+ARBEARBEARhUpDEJwiCIAiCIAiTgiQ+QRAEQRAEQZgUJPEJgiAIgiAIwqQgiU8QBEEQBEEQJgVJfIIgCIIgCIIwKUjiEwRBEARBEIRJQRKfIAiCIAiCIEwKkvhGTElJyfnz569cuVLeBdGKy5cvN2jQ4NatW2qmT0tL26M5OIuyDKdOnbp48WIVZxwyZMi2bds0uiiibOTk5KBKFxYWlndBCI1h5igrK6u8C6IzZs2a5ezsrFFtvHTpUhmsU3p6urIM79y507Rp02PHjml5LTt37oQdU5EANnDy5MlanoV4QzAlQ52ZmYlr+eeff8q7IHqhQkj87OxsdAz4X0WaR48eIQ3snbYFNCH+/vtvmUz2ww8/qJN44sSJ9erVM6RUvXv3Lh4ZOn7VydC6cBW4FjWzxfXKNGfo0KHKMvT29laxF6CLnTNnjmAjmg2u7uHDh2oW25CwBnXz5k0102cpKCgo0Gup1KF79+54WOvWrSs1JfqYX375xcnJ6fnz5wYomFFTXFycnJycmJg4d+7cFStW7Nq168GDBzo/CzNHeChlOBZFgnUaP368zkulDNXW6cWLF+Hh4bicCRMmaJRtUFBQGawTLIyyDH19fT/44IPU1NTj6gEfQzKf+fPnqzgLgA309PQUbHz27BnuEu6VRjehHIE1OHz4cEJCwuzZs1evXq3+yJEKUElSUlJY81m5ciXcrZcvX5YtKyZj+BjRveWjvqGu+PznP//Btdy/f7/UlMbY6VQIid+gQQPc4kqVKqkYzEBzRRqoMR2U0VTQSOKzm9ytWzd9l4qBxlC7du327dtLWsMNGzZA2bPfAomfkZEBe6oiZ1xvZGRksQgYX+Tz+PFj8S4rKyuBiEfPXfkVrJetrBxWObk/9+7dixxyc3Pr1KnTunXrCuj9s2ddvXr1/Pz8UhMfOHCA3YFx48YZoGyqUb/nYAYBXLt2zQAFM1Lg7OGWvvvuuwJN+dZbbw0cOFC359JG4gcEBOBY9Ea6LZIyVFunGzduYBfKU61atZbKkWxckPiwNmIThDMiw+3bt4t3wZopE9+rVq3S1Fto06YNd/ihQ4c4qwULVqqV4ycYO3asXOHqIEPcK51oZX2zePHiDz/8UFDP+/TpU1RUVLYM79y5ExgY+P777wtu8qeffjpt2jT4P5pmyFktPh9//HFoaCjUf9kKWS68mRLfGDudCiTxwU8//aTMPSKJL0Yjib9z586ePXsaJqoHHaelpWXNmjUl38zA4KLPiIqKYn8KJD6qzQcffKAirgbXO2nSJPF2mBvkIym4bW1tBRIfAp0b97K2tu7SpYuKgbGGDRsOGzaM+5MbuWdn5C6k4sA1qIkTJ5aa2MHBgSU2Lon/9OnTkJCQGTNmGKBURsqff/75zjvv4H7WrVsXbR+iZOHChVOnTvXz84OqcHR01O3ptJH4WVlZKOGOHTt0WyRJVFinwsLCMWPGwCNCk4+Ojp4qxfDhw6tUqQJRDnUuzhwSH9ZGvB0CAjdnz5494l2wZpIS/8KFCzVq1IDlKdNV/gtUI2e1wsLCcFEqrBxsYIcOHbg/OU1//fp1aFzcsTIPXRsMyIPGjRvjGSUlJW3evDkiIgIdDW67+O2EOhw8eBA9EQ7H5Xfu3BnZxsXFTZgwwc7OjnlErVq1UmcMhQ+TMZ9//rmjAnNz83r16jHz+9tvv8GmlaGc5cKbKfGNsdOpQBIfBgj/KzuEJL4YjSS+IVm0aBEKFhsbK7l36dKlb7/9NveCUiDxX7x4AdFZv359ZXF+OpH4fMoWqMPw8PCAuVfhkJQLrEFBxn366aeqh5ogI1iXY3QSn1DNsmXL2Cgm3DyxGH3+/DlknG7PqI3ENySS1unmzZujR4/+8MMP0RbQKUJvSQ5PoL18/fXXP/30kzJtpyuJn5OT8+WXX0JNwh7u27dvjnqgeMquumyBOozZs2ej8KonLFUE0tPTcbv4WzIyMqpWrYrCnzp1SqOsTp48ydxjLy+vvLw8wV5kixqCvS1atCg1EpUPkzHwpvgbd+3axd6zwYvQqJDliCkZavUlvjFSgST+ihUrKlWqhHYlOdJMEl9MxZT4L1++/P777z/55BPJUS7sRQfp6+vLbRHH4j98+BASX1l/ow+JX+orbGUSHzoJe/39/ZVlXi6wBgX3A/9D6qlI2aNHD6Tx8fEhiW9KoE1Vq1YN5nTDhg0GO6lRSHxJ67R37140c2yH+odLXFBQ4OTkVKdOHRaSx7Fly5aaNWva2NiomGWoE4kPfwMGEHeS9c0xMTGO6pGUlKSsYJD4pVo5ZSa3qKiobt26sCoVfyBfDB4HLg1PVv1DUAdw/5kWV3bJqANsUDI8PFz9nCUlvlwhlrAdtU79rMoXUzLUJPE1ouwS/9KlS8HBwfjRoUMHcZpSJf7t27ePHj0KPz43N7fUM6LdZmdnK4svhI+BfATjNDgE2w8fPnzjxg3VmUOhnjp1KjU1Vc2omMePH2dmZkrGCz59+vTs2bNHjhwRDyTIRRIfnda5c+fS0tIkE5fKgwcPjh07Bs0qKc05UM7Tp0/jLLjhkgk2bdqk4m3MypUr0Z3w54RJTrc9c+YMNIqksMb1WltbR4lgSn38+PHiXd99951qiQ+le0k5jRs3VibxgYWFBfxS8aypefPmGVJg8WENCooE///888/KkqGlvP3220g8ZcoU1RL/6tWrqPknT55UZwkF1Y0L8gWV58KFC4LxNoag50AmSIwaIpm41GJcvnwZzVD1PH6Alg7TwQ/BKkeSk5Ojo6PLEObLB2oPt7FsMR7qP2t0irhvsHVPnjyRlybxS7UbqoFRYpZQdWgEHnpGRoYK2ytpnXAUxDG/jmHL6NGj0TrWrl2LP69du+bm5sYi1FXPvYHEh7URm6CwsDCcF9VbvAvWTCDxYVKaNWum2+nvkPiwYyqsHGygioCWyMhIlH/z5s2lnkgnFViH9O7dGyVnz1FNFi9eLFPMDFEdH3/w4EEkg9envt1QJvHZGd3d3SWP0qjtqNmPa0mpEh+dC1qrWCwxk37x4kXV7mJJSQn6CDRkSBp13pMgDZq85CoCaNfQV7Bp169flzyWL/G5XkNZYtWoaabkigk/KBIS63vmbsWS+BC77HYvWbJEkEaFxE9MTPzxxx9lPNDNwJQLkvn7+7/33ntQXeiWvv/+e5aS2WtuFxotc83ZgAfsNXsA27Ztg+Hm8m/btq2k0MejtbKy4qYugc8++wz2TtArQHPgdDDiqHwhISFvvfUWUqJHYdeCXYMHD4aJDA0N5Sb6VKpUyd7eXlDtOImPejl58mQWd8iAsRb00Nw18u8bOxdS+vn5ValShR2LjZJvDJEMPhj28u8D6qggGZPakgoPpuqbb74RjHkrW1EHErl69eriGBhc7+eff95UxNdffy1TRDSKd9WoUUNPgTpyRdwRzrtgwQLBdggsbG/fvj3UkorM9QFrUHfu3GnTpg1+7Nu3TzLZ8OHDsZcFmEpKfHiYcJk+/fRT7omjbqMewuwKUqpoXI0aNcIuGFC0DtxJLquPP/4Yj1iQD9dz4LmzKY8MlOGvv/7ip+QaEX8jdy5oEdQ07vBWrVpJTpBCr+Dk5MQaIICk69q1q6bxtboFpgYlQWUu8wgZDClrxRppRPWfNcBGGDo2g5Oda9SoUVlZWTIpia+O3eBsEbeFe74wbhMnTmRR0TJF6BGMlThqGclmz54Ne8udBRVAUGfkKq2TGMhi3AQfHx/48C1atFAntAldBqyN2ATB08Z569evL97FrBk/E9xJ3DTIPle1KbWr1SZQR654HDLF675S74D2FVi3oLKhPBrFUrZu3RqHTJ8+vdSUv/76q0wRgKBmzsokPvMAxcs3adR2Su3Hf/rpp/eUAGsMfwZOIH5LvmuCVcEubsBILPG5YuTk5NjY2HAFhqFgCyHC2PJNer169fbv3y8+0c2bN3v27Mm/ZPwOCAgQj7Jz1h5ykdkHNtec3zWgEX355ZdcVhCK4pNyEl8g85o0aSKIfBN3OpqaKbB7924YSe4stWrVgv9chjEsNalYEh+/k5KS8Btq9d69e/w0yiR+nz59ZIqlD3BD0Sahp11cXNi9mzJlCj8lq5RQFR9++CGLA4FYZCqE7UKBoSnxe8aMGZAsLBQPEnzLli14YB06dED+kN1ffPEF68kETwX1jIl7W1vbSZMmzZw5s3fv3qymokj8xJw0Hzt2bNWqVdGPOjo6spmRyAS7AgMDsbFmzZr4MWvWLKh/pl/RGfA7Jy4fFBKJYQtiYmLwPwvsc3Z2Fl8+v02yc+EGooJ+++234eHhKHPHjh3Z3YuPj+cfDrnA6iWsALQg7i2bponzwiPnp/zkk0/wQCUf9JAhQ+rUqSMYilAm8dFmLCws0GgF7r4+AnVgFpXZPgApo0LiwyRJdn7wV/F8UaNweI8ePdR5uaQrOIm/ceNG/JCcWPnw4UM8u48++gh+V1RUlEwk8R88eICKIVPI60GDBqFqQQKyLahgBw4c4CdW0biYAV2/fj0ENKQ2ujG0Ly8vLyYQBesksnzQimEr0ZlFK/j999+Z0eSvDi4ZpcbOxZRZ586dUZ/xCGDjsBG2W/Ci7MSJE8wiW1tb4ywRERGshqMjLMd5b6jty5YtY0amXbt2ZYiYx1Xj2E6dOql/iEbPOjU1lZk1PCBYLTxNDw8PPE13d3eZSOKraTeYLYI+5rZwzxcGDb0gTBxKNWDAADQoSZHEag7qM0QGDDVsLzPgy5cv5ydTYZ34wFzjqrt164ZKizKwMWD0TbDGqjtjHU63heBAlwS5g05nxOtA8QwbNoz7s2XLllD5qq8IjQLPSIWVgw1UPS0VLhOqh+qzyHVRgXUIfDyZIp5e/UPQ9vHQcVSpr+vlr8Zx1A/UlJT46AFRw2E5BYMLGrUddfpx1GfL10EPy0QLS4ZWj9/orcQlZ04I1/MqkxNdu3aFVmFiCTeHzfKCIwQpzLoGWAy+bRG8Yj116lTdunVlipfPMN1o8siEM+AC5cCsPW4pKjZ6FtgfXLWcZzpQWvQa2Dht2jT8Zp4b6jlEtjifuLg43AqIAdZrfPXVV0xx8V/RiDsdTc3UokWLUFpUMKZX0bRhkdjjE99znVDhJD7AxeNPfri2XInEh/CSKdxBwfdWYElh33Erjx49ym1klRKeH+yjwEyzXUi/atUqbuOhQ4ewERIcda5///7cdvgebKyIX1FOnjyJx4aTChaeRw1mo4moZNxGVi1gBFG3BINkrJ2grqCcfDUPdQJvWGCtWD4oIZ4iXyKnp6ezgUl+PIyyNonD4XPzX+rhqckUwzD8gkExsAbM19Aspbm5ObclIyODuShyEcnJybjD4hemKtbFv3btGoonGCPRh8SHRtmpHBgXFRIfIIGyzi8nJ4fdeXSicNYNox05iY96zoYlxKtlo0Jysl5S4qO/x0Y7Ozv4KvztbMgf18t/i62icTEDiioN08nfjhsLk4qKyi2fyuWDdsTW7GNANDC/ne9HqZD477///q5du7iNeXl5THAsXbqU24iLYmtZwLJzG1F5WCdqyAXaJUE9QW1hShr2UKMlC9nMCo2WfVD/WeMHGxUTjHFu376dDR8KJL6adkOZxEfzR1/L1wFwMJhzyH+lCd9Sphii4w/1sZT8OAoV1kmuqGZoJigJbjhchWrVquG2cG/AoO9RLUutGDqU+HJFCBmqLuQ73z7jbqBRw4fhtqCrVUfi4ygVVg42ULXEZ6NpytbdF6BNBdYGVJu0tLT9+/fjOULboQKgx9TI6p45c0amWIRKncRsUjs6UDUzZzIGvjF6K3SFc+fOhQuHhgNbdPr0aUFijdqOmv24gAULFiANU8ZyRfQI7liNGjUEoyEw6Wj1KCf3YSJlcgKH8x0eiCWm8iFRIOtZRJ9cMd3f3t4e20eNGsUl5oI44KXwx/VQGCcnJ5lorgJLDP9HoBCY6UAvgE7n4MGD/F2jR4/GLlwLP/iH6zX4U1ngXzGVz38/r0ziq2mm8IihEtEo+C/2cYtY9wSBJNcDFVHiw659/PHH2MJfQ00s8Z89e8aSHTlyRJwn9Irs9aEsVinr1KkjbvBsF5w8wXa4udgO71MQbDdkyBCBJHJzc+P7uHzYuuPoJrmGyqqFTDFaKUjMtRO+7mHASqJ+QBVx7ze4fMQhkiwYlz/HSFmbRE8miCOHmWABQpzsPnv2LHOluCbKQDthHjZXj1ESmdTk1KtXr6LXlHRVxRIfNbJdu3asGQxXwE9foVbUYTg7O+PUKgI3cS0wysy4JCYm6nvWGifx8Ts2Nha/obz5CWBhURJIFlaXxBIfxkimiKWRDMhm18IPs1HRuJgBlRxUhueMXfwF2lk+v/32m+AWsWnNKDO3RYXEF3/Fc+LEiTJFJDS3JSYmRrJULMoF+YhLa3hu376NJgMv6N1338XTEbQ+ZVhYWMgUg1tqnkWjZ80WV5GcF8imDPIlvvp2Q5nElymmlAhOZG1tLeMFc6Ij+OSTT2AzxTFFLCyHS6nMOoWGhrZo0QLKRqYIrezSpQtEA78540A0FnQQu3fvFnyYlj+KJNe1xJcrKiREDL/7hz2Ex8t3xtSU+NoE6gA4dZKPQwVlq8DaEBISInsFuksoSE2nNMA9YMJRncRsvpMgXFAFkuviQ4lCKQle82radtTpxwVcvHixevXqyI0fws5mJ69fv56fEvVW9vpsbGVyAmcUvItgnQuA68Xfzm5d+/btuS2zZs2SKYIgxEVFCdkbV37kDLP2cBUEiTnTIQ4Eha/Cgrr5EcssH36UIGPq1KkyhYslyFks8dUxU4C95xSXik2F53dPOqQiSny5YkVn1tFy9Vss8Zl0bt68uWSeLHwCjYfTCqxSDhgwQJyY7RIvIs7shfhzUWzZNU42oS2hA4D4VjZB7dtvv5Xx1u3iqoU4vIy1E/7nS/gwl4MT9Jy3Kta17I0bf8l2ZW3SwcFBfCL2SgueKPuTfegxLCxMnJIt27JmzRr2Z0JCAv7E4xMks7OzQ1OUnFkilvjoJiHmWBcrPkR7iQ8Z+gOPmjVrQpv+oBw8XHho3J/i1769evVSYUk58OBYnDr0xOHDh1Un1ga+xMfFwkdFB8CvbMuXL0eCvn37sj/FEp95yJA+kvmzw6EzuC0qGhczoJLihr0oa9KkiSAfseuLx8rW/eC2qJD4/HgeBpSZTBEVym0xMzPDFskVSFAZsEsQKFiOoLNnvcUXX3yxbNmyUv1DFtck6KRVoNGzZiZI8iPZELuy1yW++nZDmcSHcRMHxkC3yXiBy0yT4arFZ2EOCTdsr8w6wZ7DPqxcuTIzM1OwC1bI399fpnizJAZ+RcuWLfnpdSXx4Zn3fgXMS2/lHDx4UJnEh6XirBZcFxRYhZVDtYeTw98icNdZTRBPkysVTSuwNuzbtw/KDF15cHAwzKxMEQ0iFlX/iOCqGbMVGkl8GBP2Jy5NnDP/epmMwb0drQDemp+fH4vCRTn5Ewg1bTvq9ON8IFp+/vlneF+CcW7WjeIU/I2QudjIfzWqTE7gQQtOxIJFxV+1u3r1Krbzo+ZYpP727dvFpZW/6mT5Lye5EFBBSmY64OBJupSss+MLepaPwFeXK+IOsB0WT5CzWOKrY6aKioqqVq2KUomHAs+dOydTvAOXvHAtqaASH7BX89yAnFjiM59PUlUw2IfuONeWVUoYfXFKtgsmXrCdDf6JX86idfG9LvZqD96hspKw9+Bc18KqBUyqOCUXVyeZT79+/WS8FZ1ZPpKhpezmsCm8/GsUt0nB+C6DvRfjOiT0HzJFeJytCPbWnrurbG0WwWJzcsWbGWVDOAKJj2PRcaoYK0IDQ3ceJIINP6DpDhWBNsyX+DC7/DfUeJq1a9du27at+OU1G+uNjIzkbxSrczZ+qU7UKZo3NAFz8CQtr07gS3z5q96C7++xyX8ZGRnsT7HEZ2+llMlE9sgaNmzIbVHRuJgBlXxTj7YpU4wfC/KRHIFmoziCV2GSEp+7cI4TJ07IXvec4fzLFO+7xVWaTWWRnGZajqCGs2pT6ufMWKyReP63MjR61syoSi4wd/36dYHEV99uKJP4ksaNxZhxxo3NPUCG4rOwes7pFWXWSRL02bgnkF/IWfKQmzdvQhPDOPA34hLQp4qtExMoHTt2FFsnWB6xxF+1atXo18FjRRMYLQJmR5nEh6XirNaOHTtwFrQ1SC6BlcMW5NypUyfBdsFwCbbItFi7Xf0KrEOOHDnComr5JoVVaQGcY8ZsBeq5OvkLVsJhkcMC+ANSkrH48AFYpFn16tW5CQCath11+nE+AwcOlEmt+FlSUlK3bl2IUU4Xos+CSYRp5fsqyuQEN2zEgUooez2yiHHv3j3Z6+9LmYVXttoBu7eQQNwWZu3FhpqZju+++04yHzZ8zB+nU9ZrMF3H7zWUSXx1zBR7WYo7KX6g7E2ppCDUnoor8aEJatasCS8TTU4uJfHZ4JOKVWlZEDycRfYnq5Sc78tH2QpQaJwyqfAb5ulyEp+9T+BceTHMvnNhM6xaSDpt4q6OD/wZ7IXu5OcjuS4+aw/qSHzJczH7wpkG/kR4STi7z+6Y5Ex5ZVy8ePG9995jcWxoZp9++qnqqSfBwcGSa0qwGTzOzs6Se5V9twWGBm24fv36nGq5du0a/4kPGzYMDkB6erqKIo0cOVKmJGCMA048/C7W37Rq1Uow40e3CCQ+rvGdd9755JNP2Ep2bEY7fw6uWOKzJ67sObJXZPywGRWNS8Wqw7DmMsXcekE+kmtxMHGpjsQXn4uZV76xVl2fZeo5bIZh06ZN7Ds7X3311cKFC0tdQo4tPaz+FECNnjULMJUciBUvmqm+3VAx3VZ8IqbpOePGOgIVcFVdTeuEHnH69OlsqgYuRzA/gYF6aG1t3aRJE8HqkHFxcZL2x87OjjV8yb3i0DIx8fHx3377reQudLWCxRUEPH/+vH///pAXXLAEniDuG2citmzZUrlyZf68FDG7du2SKQlGVY2mFVi3bN26VfZ6b3v79m2xo4WCsb2FhYVsJps6yyaythYREcH+PHTokDhn/oJmylbUkb+K4uAGYrRpOxyCfpyDrXrUunVryZfeKDP2JiQksD+ZGyNY7Ud9OYFuUSYVfsPea/ElPrsuZS952EskftgMs/bi162qvxcEv132+vqkynoN5gqqI/HVMVNMJaoAKkiywFpScSW+XGEuZYr3+KiIYokfHR0tk4qg4mCR+tyTU6EetJT47A01P95AAFxGfv4qqgVrJ/zZveJ8uMklBpP4bFxw48aNyi6QA4ZSpuEixByPHj1CT4AWVbY+QEWgjjLQsX3++efod/lfEsBV16pVi/sTFmfQoEFVq1adPXu2ssU02EQ0zpkU8OTJEzj0bOJ8ixYtVHyeRlcIJD7o27ev7NVLdjZvmy90xBKfzYVStgw2m7bIr3gqGhczoJLfamD58IdbDCbx2VC9bm2fbkHFQ2/EltSAwp4/f76a7WLDhg0yxeQfNdcm1+hZs8VGJOcvsmkMfImvvt3QRuKzsfmQkJBSz6LaOkGfjRo1qmXLlhC7EKPIFiqnevXqaDviO48mD3e91Ng8DhWBOsro2LEjf/GThg0bVqtWTbAiCnOqcSvgQijLB0oFYg72h++1oh2hPPwpnn/++SceLi5W2Srv6HdkmnxDqswVWLewGD+UQf114ps3b470kydPVp0M3QGLsUlJSVEzZxUSn0V++/n5sT+1aTsckhIfHs5HH31Us2ZNZbWXNXkuQAXOBm6gYKqAPiQ+W4VGWfVjk8r4+Suz9sx0KAu1YvnwhxENI/GPHTsmK48vA1ZoiQ8bwXxZ1H4WG8OX+Kwna9eunWSe0Desn+O26E/iFxQUsO/yKpu5zy6QC/QsVeIrW/CO1UVuJq7BJD57x6rOC1b2UMSxj6XCptjCYoq/IaUm6kt81KsdO3Z06NChSpUqY8aMwalP80BX9P777/O3oGbGx8fDJqJ94gLFp2C3SzwTA04LHFG2ClizZs2URRnqHLHEZ/KradOmqIRid1Qs8dlrXP6yNnxYR8Vf36ZUiS9YWZXBaqDqWVwcupX4OBBb9DojosxAOkBvsRJ+8cUXaE0afUgIUoYtb8+97lONRs+aaRpx3Kr8VVwyvw9T325oI/FZwxcHAYtRbZ3Gjx8PbzM4OJgfo3Lq1KnPP/8ccoeLMywqKvL19a1Vq9aZM2dKPSNHGSQ+JHU8D7bOT/zrsCXSUXL+tEUO7O3Zs+dbb72FJgZhd+7cOc6msfnrqGZ8Qwepijvw8ccfo+aIrRm77eIPzojRsgLrFlh7uC7ooNUf/cGNZeJB8lNKHCtXrlQhJSVRIfHRE8l4gSjatB0OscTH3WDzIlRPx4epxB2DrGfN0M3NTZBAHxKfhdUp+4pLQECA7PX4Q9USX9maSKzk/Dn3hpH47HrfffddAzu6FVriyxWfS6hWrRrcOxZczpf4KDcbihOvNiV/tdwbP3JLfxJf/mpei2SfmpqaKns9cLlUif/BBx+IfVkWX/Htt99yb7IMJvHZ6sKNGjUq1UoyLaXOiBqfCxcu4CrQu6izFLEy1Jf42dnZ6KFRl5juREfIXx+aLafN38Jm8uXk5KC/ZANdggxh5cWBdOvXr2cTN6GnNVqGQnvEEl/+atkfFjAgWGVMLPHZnLMvv/xScgYFew/An7ZYqsTnzwTgaNWqFXYtW7ZMnXx0K/E1jWYxGBkZGezre5999tns2bPL9olKFtoLyylYxUISjZ41W9FYhdHgS3z17YY2Ev/u3buVK1eGu16q9VBtnZRFCMBcwOqamZk9fvz4xIkTv/76a/369cUTc1VTBokvQEWgDjpHNhMMShrlZKMkuOe//fZby5Yt4bGwZPBVOJvGuk7UEL6hQ5cKByYiIgKGCzZE8NKSrX8l/tahAJ1UYB0Cv0WmWJpd/UNwG5kJdXd3V1Z1IVeYedfoE+bKJD5uO1vdmPuMgzZth0Ms8dkrL8mV7/mw4Bw0NPZVY/HglD4kPpufKvmJXzicuNto4zdv3uQ2qpb44NChQ4JdeXl5NWrUgPfCj8IyjMSXKz49hi38ldkNQEWX+PJXATls6VDBuvgsBvr777/nP3i5Yio0jBeeJf9VlF4lPtPfsJuCQM9bt26hP8Au/ncWS5X4rKLzRz7Qe7FVWvnvSQ0m8Z8/f85G75BYYPehkvnLjWNv7dq1uW/glQoqX3h4OHQzTICWH2zXKFBHxQKXgkAdARD6gleWbM6o2DANHTpU8ivLBkBS4rOujok5wTpFkuviM68V1yXopNkLZXSZ/FtdqsRHexS8zmadBzo2fv4Gk/iwNugwYOvFo1lbt24VrDJhSHD2Tz75BN2DYGlqTWFT/KtXrz537lxxo4BC5WJt5Zo8a/gMMsWHbznhyIiJialatapA4qtvN7SR+PJXK37AYxQMu+bn5/NXZ9LUOnGgf0GrgcJ+6623OnfurHpwVxKNJH5cXFwbETj7O++8I94+YMAAiAZ0dnLFF1FwFs6QqrBy4kAdPnD2BN/1lCs+JgqZVep6OLqqwJqyb98+/pIvjKysLLaIGb+yqQMb92FjIoLPM4G1a9eyd7P8MUR1EEt83E+IYDbYgaJynb42bYdD0I8fP34cXS0EieT0Ej6oAKhRv//+e+PGjaERxRGq+pD46LDYjFvBimq4J2yiQnBwMH97qRIfV8pf5gHGjQUl8gP6VeSjc4nPVmJEzREsiV5SUjJt2rQyWBV1MAKJz0Yj2DMTSHw0AzYq+f777/fv3x+WEf0Z0sAQwxoKhk71KvHlr3QSRAM619mzZy9cuHDgwIFs4Q7+Y5arIfEdHBzQFeG2TJw4MT4+fsiQIazqo3dRMx/dSny5Yl48G/jB6aAFcatRNrRbXK8gB7ZAh2TsNZ8zZ85ABMOOfP7553y1UWbKEIsviWqJL4ZZbfFiMpAF+l7/XhmSEl/+KsZU8NVnuRKJD6+S9TH16tVDRYJ5woHt2rWTKabNCSYelCrxYVWhC/38/FBzYPtYAB6evmCBS4NJfPmrVadkihgPXNr8+fNHjhzJvkgvWQDDgIajk++jodvo2bMnu8CPPvoIVnHYsGFskT62MjR/vrVGz3rQoEEyxceGoVQWLFiA22hlZcW+AC0TBZuqaTe0lPh44mwQFN3n4MGD8ShnzJiB4uHUghzUtE4cEEPr16+HwoAD06JFC2VRBKWikcSHKpojAsYfTUC8fcOGDWwRGMjZCRMmqLlGu2qJL+b27dsy0VqKkuiqAmtKYmKiTBGLOGbMGHS+qMCoAOxzbMqWr1ANBDELeIPhsrCwgL5E8+nWrRtblh6gIWhq4VlnAbvXQAHctmrVqrHcUIEFX/Asc9vh4Pfj8PdYG/npp58k53wLjmVrxcp4k4n56EPiyxVTullEPryLyZMnwxCNHTuWrTmORyAYgFAt8XGxLVu2hI4KDQ1FPpGRkWywFU6LYDDRYBIftYUteApjgoqExgu9ChedjV9LrkihPUYg8eWKHprNmBFIfLnCVKEqMJeagQZgaWnJ/34YQ98SX65YAhYVSMajYcOG4tldpUp8tBMoYPZahwGJj+Yt0K+GlPhyxVNgq4lzwDzBjApWHli1apVM8Y5PnO2TJ0/QhsPCwtib3CZNmqDt6WqwRyOJzxaUkARtD/6hsr38tzEM+GOCF4jljjKJ/+eff8IZFjd4SYkvV/TWffv25Toh9sR79eolni9RqsRHYSCg+VmhLonXOzOkxJcr6gzrPzhgSUaNGlXqKJexsHfvXhhDNkeWAx0MvBrBkKf6zxptByaXfSiKwT6bKl5Rh6GO3dBS4rPyw3sRXGmHDh0E746UWSdYIVzptWvXzp49u3XrVnjskHTQi+h36tSp07t3by2XuNVroA4aBaTMwIED4acJvjqckJAgacegnGSKlRYl9woykb8K8FD/e2qGJzMzE4+brfjEgdpYtrUfGIWFhbAGnKZnoHeAzS/bNB7xp6/Qjpo3bx4dHS1pc8rWdjj4/XipC08JjmXTQ+HJ5+TkiHPWk8SXK96f2NjY8J/jRx99BN9VHMKuWuLDdOTn5zOXngHjgGKLF+U0mMSXK5oqnA028svRqFEjCCE9DQhWCImvPS9evIBc2L17Nwyx+iM0egLNb78CdBiaHitoJxcvXsRFnThxQvKjUeVCbm5ucnIy9MGpU6ckJ1GhEterVw8VS1Bm7sNyEKCo96XGdGqKRhIfhZEcySgV/qc35K8+WqGn79JVEKB+jh49mpSUhP/L4I/xDShszcGDBw8cOGCwD9qrA8QBesF9+/bhR3m9eNErjx49QmtFm8U1osaqCI9W/1mj7aenp8M6cV9XUE2pdkMn4ErT0tJQfggLyQ8RKrNObGlFBmQNxLS7u/vEiRORm05sr14lPoBdQv6Q+ILgnLCwsDJYObh2/EzwvD7//PNvvvlG+3ek+ubBgwd49HA4YWcEEZXacPXq1UOHDuHxodsy/DsKw7QdAey7hJLfsTYAaC/QcjAvsFfKFrJThkB237x5c+/evXDJlH2Z1PDApJw8eRJmKiUlRYe1VBITkfgmg+p18Y0FNttPvBT95cuXla0sqT3wzlWvTK8POnfuDEEguVwMwVCxLj5BGB5J6wTXDh4LBFxOTo4+hCw6dWVeh5rgWHFQOB+IBmWfDdIStnq1+h9TI0wAHx8fPHQDLxShE1Svi/+mQRK/YmEaEh9ud/v27WvXrl2hBmt1DlslUBzfQvAhiU9UKN4Q66Qrbt68WatWrQ4dOmg6mEoYL3joVapUqV+/fsV/byOGJD4fkvgVC9OQ+HLFyjN16tSxsrIyycgHuWIhnbp167Zp08YYjaAhIYlPVDRM3jrpCtwfc3Nz3Ctyh94cnj9/zlZY5lbwNC5I4vMhiV+xMBmJL1eE06GxVZxZBLrl0aNHuDqTmZepP0jiExUQ07ZOugL3B3eJGu8bQmRkpKenJ1uBwMvLq7yLU0ZI4vMhiV+xgN/8zjvvaPrpKIKosHz//feo0qQSCIIgKjJsmd0PPvhg1KhR5f7NsjKTnZ2NHkfwBfc3FpL4BEEQBEEQbzoVZ9kZQieQxCcIgiAIgiAIk4IkPkEQBEEQBEGYFCTxCYIgCIIgCMKkIIlPEARBEARBECYFSXyCIAiCIIyV4uLiAwcO7H6dBw8eCJIdO3ZstxTGm5IgVEMSnyAIgiAIY8XPz08m4uDBg4Jkbdq0EScz6pQEoRqS+ARBEARBGCtMEzdt2tSSx7lz5wTJQkJCLKUwxpRspJ/G9QnVkMQnCIIgCMJYYZpYrJX1xMuXL8+ePZubm2uY00nCvBoa1ydUQxKfIAiCIAiiFCDub968OWnSpLZt2zo7O2/ZsuXJkyflUhKS+IQ6kMQnCIIgCIJQxd27d+fNmwdxn5iYCGX/4MGDfv36BQcH79y50/CFIYlPqANJfIIgCIIgCGmePn36119/derUafTo0RkZGXLFGj74v6io6MiRI87OzoGBgTdu3Pjnn38MViSS+IQ6kMQnCIIgCIKQIC0tbciQIT169MjNzX358uWLFy+SkpKmT5/OJcCWJUuW9OrVa/Lkyc+fPzdMqUjiE+pAEp8gCIIgCOL/gHCHpg8JCXF3d9+1a9fTp0+Li4uvXLni5eU1evToM2fOCNLfvn07KioKiTdu3FhQUKDv4pHEJ9SBJD5BEARBEMaKzleQLCkpiY2N9fHxmTp16suXL7ElOzt7+PDh9vb2S5cuZVskOXnyZFBQkKOjY1pamq4KIwlJfEIdSOITBEEQBGGs6FDvwk9ITk62tLQcPXo0ZP2LFy/u3bu3du1aCwuL1atX3717t9QciouLd+7c6evrGxoaeunSJe2LJImB1wkljBSS+ARBEARBGCu6kvinT592cXHp27fvvn372JZ169ZBSUPMXL58WaOsHj9+PHPmzCZNmsTExNAHqojygiQ+QRAEQRDGivYSPysrC4q8Y8eOhw8fZkvdnzlzZtSoUV26dMnIyHj27FnZsr127drUqVM9PT337NlTXivoE28yJPEJgiAIgjBWtJT4x48fb9Wq1aJFi9hwe35+/vDhw21sbDZt2lRmcc/n6NGj7u7uI0eO1D4rgtAIkvhKYctjqZhYQxAEQRBE+aKlxF+6dKmbm9s///wDQT9r1iwXF5eoqKg7d+7osITZ2dnIVocZEoQ6vBES/8mTJ3v37oWnLtgO+X7+/Pndu3cL3qAVFhampKQsW7Zs3rx5iYmJhw8fxhYDlpcgCMLQFBcXHzhwYPfriMOI2eolYgyf8urVq7q9A4SRor3E9/b2hsR/+PDh9OnTdViv7t+/P3r06Nzc3Pz8fE9PT11lSxBq8kZI/GvXrjVu3NjX11ewHU166NCh33zzzfXr17mNFy9e7NGjx6efflq5cuX69evXqFHjq6++8vPzw3aDFpogCMKAwMrJRIhlE5NTFSTllStXdHsTCGNEe4nfqVMn9m1a3b63h/b47LPPzp8/r3OJr/N1QgmThCT+vxL/77//liva9qlTp1q3bt2gQYO4uDi48nfv3s3JyZk3bx4U/9dff52ZmVkexScIgtA7TCc1bdrUkod4VT62Wp8YA6esVasWrQtOMLRcQRIS39XVVR8fptWfxKd18Ql1IIn/fxL/2bNnTk5O9erVS05O5id78eLF5s2b0VA7d+786NEjw5WbIAjCUBjXStskcQhdAYnv4uJCEp8wPUji/5/ERzt89913Uezi4mJBypKSkgEDBnz11VcHDhwwUKGJNxh0NseOHRMHIZw6der69evcq2RU4JycnO3bt8+PjV27Zs3ly5eLiooMXliCKAdI4hC6AhLf3t6eJD5herxBEt/V1fX661y9erVPnz6cxGcBOevXr5fMJDk5uXLlynPnzn3x4oVhiv3s2TN9GB2i4nP//v2WzVuEDhvGr2z4bWdtExkRwWJGHz9+nLAooXnTphbt2/t16+bu6vrzDz8OGzL03r175VdwgjAQxvXOgajIQOLb2tqSxCdMjzdI4n/88cdmZmbteODPL774gpP4AQEBDRo0SE9Pl8wELkGVKlX++OOPkpISfRf45cuXt27dCg0NHT58eF5eHi3c+aYBid+sadMhgwcLJL61heX4ceOYxGf6fuaMGRcvXiwoKLh582ZiYmKbVq2g8qH+y6/sBEEQxgQkvoWFBUl8wvR4gyT+r7/+OnHixAmvA6HPSXy0wEaNGp0+fVoyE0goSPwxY8boW+Ln5uYmJCS4urrGx8fHxsa6u7svWbLk7t27ej0pUaEoVeI/ePDArE2bP8LD+UFlcAXXrVv3648/Je3cWR6lJgiCMD4g8du3b08SnzA93iCJX2osfnh4OH4ri7Y/d+4cJP6UKVPYGKo+ePr06Zo1a3x8fEJCQlgcNkTbpUuXcCe9vb3Xr18vniRAmCRM4vfv1y8nJyf3FfhtYdaeSfzVq1a1bNps69atggMLCwt/+/mXyIgIQ4Z4welF8fTXLgiCIFSg5QqSkPhmZmYk8QnTgyT+/0n8PXv21KhRIyYmRjLaPjY29r333lu9erU+SgiRlJmZGRAQ0KdPH1graH3+XvyZnJzs5+fXr1+/q1evUoC+ycMk/o8NG7Vp+Tv/X4Nvv2MS/4/wcPO27cTzcYuKipzsHczbmQmqkP64detW9OTJKNvsmBjdfg+SMDC00jZhpGi/Ln6LFi308X5efxKf5qIQ6kAS//8k/pMnT5o0afL7778jvSAlhPWPP/7Yvn373NxcnRcP4v6PP/5A+1+3bp2KFVGePXu2du3ajh07Tpw4kf+tLsL0YBK/a5eu+/buO7D/APuH321bteYkfod2ZtnZ2YIDUX9cnZyRTPDBZp3z8uVLaMFNmzY52tl38el8MCXFq2NHJwfHXbt26dagEAaDxgUJI+UNlPgEoQ4k8V/79BU0dJ06dTw8PHDIixcvsAX/Q4K7urrWrl2bDeEXFBToKiYBOmz58uVubm5i1Y7zQq4J3iegPFeuXJk0aZK9vf3ixYsNNlJLGJhSY/HnzZ33e7Pm4qAy1KhmTX4bNnSovmeM7N69269rV2j6tWvWMr/08ePHK1eudHZ06uHXfd++fTRH3Ogod4lfXFx88uTJ/oGBqFqhw4ZdvHBBxZAHvXMgOLSX+E2bNiWJT5geb7rEHzJkSL169Th5/fz58xUrVvz4449M6A8fPtzHxwdNtEGDBgkJCdgL4RIUFNS3b9/09HRtLAKkWEpKip+fX0hICBwMfuwNSoXyREdH+/v737p1S3wsEsPr6N+/f8+ePY8cOUJC3/QoVeLfvHmzbas2k/77X0ElPHz48M8//Lhhw4Y7d+5cOH9B5wu8IsMLFy6gYG4uLrNmzrxx4wbbzgn67OzsadOmQfrDzUAtNdgKs4T2lK/Eh5oPGz68yc+/DOgfNHBAcN/efVo2bRYcNABtQTJ9uTskRMVBe4n/888/k8QnTI83QuKjk5g0adLy5csF26FLIIb++OOPvLw8/vbTp0+Hh4f36NEDKh//T5gw4dy5c5xYgTpftWpVly5dcHVQWmUYrTx16hTke/fu3bdt2yaYQYt+Lj4+Hn5FVFTU7du3VWSCAzdv3oxiQOtDS2laBqIio86imVGRkb/88OOqlStZGtTDM2fO2Fpbuzg5wzPcsX17u9ZtZs6YocO1mB4+fBgzK8a8nVno0GHsxRdHUlLS3r17uT8zMjKGDBps0d58dkyMvkOGCF1RjqL5+fPnkRER1lZWW7duZfUZlhC/f2r8w5zZsyUPIYlPcJDEJwhJ3giJD/WD1is5SxVqCbvEMh3bHz16hGYJWSMeiUT6nJycWbNm2dnZrVmz5sGDB+oIfaS5c+fO7NmzXVxcEhMTBX4FurTDhw9369ZtyJAhZ8+eVWdOLTKEGwDzhGLExMRAzFF0hGmgjsRHux07eky7Nm2sLC0D+vZ1dXHFbxdnl8uXL8sVU7SPHz/e0cPD2cFxy5YtBQUF2pSnsLAQzrCXp6evT+fk5GTBiyMUbOHChY62dqHDhl24cIEVD8p+165dvt4+Xp4dN27cSAH6FZ9yFM2HDh5s0bTZksVL+BYMv2fNnGnWpo3ki0qS+ASH9hK/YcOGJPEJ0+ONkPj64/r16z169PD19d26davqFS1xl1etWuXl5TV27FiBuIeaP3nyJG6Xk5PTtm3byhDbAKEfHh7etWvXv/76Cz6JxpdBVDCgaeLj4/fs2SNQPInLl0MMcRshppEmZtas6MmTZ0yfgQomCE1+/PjxsqVLbayte3bvsX///jJULRySlpbm36ePnY1NwqIEFVFh586dCw4K6tDObNJ//8vZFBQA6t/ayqpXjx5Hjx4lF7QiU46iGU7gT40aP3r0SLAdBq11y5ao5OJDdF5aVE5Y5qtXr9KX44wO7SX+999/zyS+bmML9SfxaS4KoQ4k8bUFomfXrl3+/v6DBw9GexaLGJiM48ePo3n3798/NTX12bNn3C4kRncybdq0jh07JiQkKIs6VQeYJxi43r17u7q6nj17lmKg3yjY1HBlu3JycqZOnepoazdk8JDMzEw1J4vjwCtXrowdM8bB1g4uxK1bt0qtVKjMcCT8unVzc3ZZvXo18zZx1M2bN6MiIh3t7MeMHn358mUS+hWTCijxb9y4YWneYcqUKeJDdFta2M+VK1baWdtYWVjCoU1JTtZJtoRh0HIFSUj8+vXrow4UFBSgA123bp2u1v9Fd39BMWuc1sUnygWS+DoAkgVqBhrdxsZm9uzZf//9NxcenZGRMWHCBC8vr7179wpGQOF/Qwah2YeHh8Og6ESU4xQ7d+6EkYqMjGQBGwQhV1RFOH5Dhw61MGs/Oyam1CnahYWFCxcutLex7R8YeOzYMY3OxeaTWHWw6N+vX3p6OudRHDlypJ+/v72tbdyCOIrbqYCU40rbyiT+iRMnzNq0jV8YLz5EVxIH9fNwamrvnj1dnJz/XP3npUuX4hYssLGyGhg8MDc3lz5C8iYAif/555+z0Tf0m2PGjEHtWrNmjQ4HI/bv39+uXTsdvmMniU+oA0l8XZKdnT1q1CgfH59Vq1bl5eXNnDnTzc1t6tSpgsicfzuVw4cDAgJ69ep14MABnY+4w2HAqTt16gSVBq2m28wJ4wXKfvfu3V27dPF0d9+yeYtk3UAnlJSU5O7i2tnbB5WzbEELqNK3b98e98c4OAmjR426cOEC6yyRG/L06tjRzcV1165dNBOXYGzbtu3nH348c+aMYPu8uXNbNW/BLdzERycSJysra0p0tLWFZcS4cWgdrJYyf3hEaGjb1q1RABULdxKmATSQv7+/r68v6iGEfklJyalTp7p27Qqn9/jx41oKfTiK6I4tLCxGjhxpbm4Ob1YnrwhI4hPqQBJfx8BAoKOCvfj555/RpK9cucIfB8JvNPjx48d7e3tDSOkvbh4ngq4aOHCgjY0NdVEEnwcPHixfvtzWyrpv7978paLw4/Lly/37BXYwa78iMVHLGbosw/T09AH9g6wtrRYsWMDV9vz8/IRFi9q1aYseFLWUgsreWO7fv7961eq//voLVQKeJ6oK36VEbbS0sOjk4QGNNTIsbPu2bXyfUMt3Djg15LuLk3NI8EBUQm47aikzmMXFxdBPPt7eXp6e8EtpjpNpgzp29OhRPz+/wMDAq1ev4k9Ug3Xr1v3+++/ox8u2LhksG+yek5NTZGQki8I9ceLE4MGDIfd37NihpedAEp9QB5L4egGdk4uLy7179/gb8/Lypk2b5ubmFh0dbZjBdZwREp9mjxEC2JJQE6Ki7Gxs0P3AEUWvNn3aNHsbm/AxY8u2FKwynj59mpyc3NHDw8XJCVKJBWOwAP3Q0FAbK+voyZPRXkjov1GwBYs7urv7eHnv3bsXT3/nzp2//PBjUGB/uH9bt26NgzZycLSztmEfLcFGR3uHkIEDIZK0PDXOtWvXLjcXV5xaoLT++eefGTNmjAgNPX78ONsCnQcnxNrCEv7wkSNHtDw1UcGBI7dixQpvb2/IelhIuWIpi+nTp3fu3HnJkiXqf4Lm+fPnqampcBi6deuWnZ3NX6uHfd+tU6dOYWFhp06dKnNRSeIT6kASXy8IJD56jv379/v4+IwePfr06dN6VTP8HgsFsLa2JolPKOPQoUO9evZycXb2cHP379MHHYauvtws4M6dO/Hx8W1bt+7fr9+5s+fYWdDzpR46hPPaWltDdenjvERFA9bv4sWLI4YPt7exnTdvHhfEiO1QPH379LE07wA1b9He3L9vX/7nF+ATxi2Ic7S1GzpkSG5ubhmsKOpbVlaWX9eu9ra2W7dsFQzByBXGE4JsyKBBDrZ2CQkJ3DLEcIDH/fEHXA6oPcEXIQjTo7CwENIFKnzt2rVMnUPu+/v7BwQElBpYiwpz//79wMDAXr16JSuftI1TrFy5slWrVpGRkfAryjCkQhKfUAeS+HpBIPHRhtGZHTt2TB8r7wrYs2dPfn4++00SnyiVJ0+ejB83LmJ8hHiyo25B13j9+vWxY8ZYWVhGjB/PTQdH6xg5IiwqIlKvZycqArBIM2fMaNemzfDQUMn1/l6+jjjByZMnBw8abGdts2TJEo1CEG/fvv3fiRNbt/g9KjJSMrifX4b09PSg/v2dHR0TExO5jXAPAgP6dWjffumSpfRN8QqFzleQ/OeffzIzM4OCgmxtbQ8dOlSk4PDhw15eXv369bty5Ypk5YR/OHHiRGdnZ3T36kR2wYeMjo7u0aPHmjVr+EvtqQNJfEIdSOLrBclAHcPg7e3NLYFCEp8oFfRV0ZMnT582jY2sQ7vodRURZJ6Wlta7Z09HO7tzZ/8NpMZ5FT7GeP2dlFAHgU7as2eP4ONrYNTIkVC9KmoIvLjZs2c72jvY29iEDh0G0cNygBXCgc5Ozj179MCJNBU0fOCUogp19PDo5OF59OjRUrXU/fv3t2/f7uLk7Ne127lz59QcZ0GBN2/ejLN09e3KLQyFjdu2bXN3devS2Xffvn16euVFaIr+9O6GDRt8fX1DQkLgFsJUoubPnz+/a9eu06ZN46t81OetW7eit50yZYpqB1IMfImePXv6+/sfOXJE/RpVjutfEUYESXy9QBKfMBb4Eh8dFTTNpk2b9H1SOBJQXSzmgSR+BUGgkxbFx//erLlAc1i0Nx8VNlJSoKMiwfKYtzNzc3WdEBWFf508PCzM2p8+fRp78Yg93NziFy7UVWmLiopWrljRplWrwIB/R1WVJYPT4uPl5eTgyCL+NT1Lfn4+Wodlhw4oP7cQCu4J2ou14mUUf6ouUV7odUgbHSiMlbm5+eLFi9mK2KgV8fH/u5Ar/jxw4ICHh8eAAQPOnDlTNq8P9hAetZeXV1BQUFZWFn05hNAVJPH1Akl8wlgQSHxbK6u1a9YYsgAk8SsIWkr8u3fvtmvd5o/w8Nu3b7MtOTk5AX37urm4IBOocN3aQ1i5Xbt2wX9AeVydnefMns0fPUWtZhH/zo5OMbNmcUUqG8hqeGgoXJT5sbFscRXkD7UXNmKEg60d2k5ubi7JsnLEAFErqMCTJ0+2srJauHAh3EsWSIYqFx4e7uTktGHDBu1ffiLbuXPndu7cedasWdRrEzqBJL5eIIlPGAsk8QmGlhJ/2tSp5m3bnT17lr/x6NGjC+PitAnLUae0J0+e7B/Y397GNn7hQhT40aNHkydNQlHhb2gaNaGClOSUTh6eHm7u/DmXycnJ/n36Otk7rFu7llR+eWGYwHRULfiK3bt3t7OzW7ZsWWJiIrrXNWvW6HAWE+pVXl7e4MGD27Vrt2PHDuq7CS0hia8XSOITxgJJfIIhlvjNfm0CjX6cR5tWrZVJ/L69+/Tp1dtg4emC0kJmrVq5ylWxNpSrk0uXzr4pKSk6n1UC+bV161ZPN3dc7Llz/7swVGFh4eHDh91cXXHqrKws3Z6RUAdDzj198uTJ7t27GzduPGTIkIyMDD2dJTU1Ffnjfz3lT7whkMTXCyTxCWOBJD7BEEv87+p93azJb81/a8r9q//1N0zio9ocTk1dnJDATc+F6g3o619epWXA1vXs0SMqIlKvCxPn5+dPiIpq37bdlOhoLgQIP+BaDAoJ0d95CWUYfnkZfS9LABYtWpSUlKTXUxAmD0l8vUASnzAWSOITDLHEh6a/fv36DR5mbdpC4kPfTJ40CZp+1KhRvXv1OpiSIldIfP8+fQXBKni4egpfkVR1UF2ozOwbC1D5BQUFenqrgJaSlZXVxbeLk4Mjt/xrty5dSOKXCya5gqRqia/zdUIJk4Qkvl4giU8YCyTxCYb6sfj5+fkjQofn5uZiy/r16xOXL8eP0aNGOdrZs4/Rchw6eDAyIkIfy86UKvHv3r3bzz9AUB6ds3vXrmvXrrHfJPHLC5NcQVK1xDdJr4bQOSTx9QJJfMJYIIlPMAQ6SYXELyoqKlBwMOVg927ddu7YIVd8fbZZk9/mzpnDBckgWdiIEZYdOujDBJUq8SHum/z8iyFlH0l8QoeQxCe0hyS+XiCJTxgLJPEJSUpdUQcaOioiwtK8Q1pamlwhr/EQGzdoGDps2Izp06dNmTowOLjBt98terWCuG4hiU+YNiTxCe0hia8XSOITxgJJfEKSrVu39unVWzBvNThoQNyCBWyiIWpOSUnJn3/+adamTWFhofzVF828Onb07uTl1bFTV98u+/fv18eKmXIlsRkk8QmTgSQ+oT0k8fUCSXzCWCCJT2jKtWvXRgwfnp+fj987d+z4qfEPFWTaH0l8wmQgiU9oD0l8vUASnzAWSOITmlJUVBQZEfGvmE5K8u/TZ+mSJQZbDl81JPEJk4EkPqE9JPH1Akl8wlggiU+Ugby8vNWrVy9dunT7tu3FxcXlXZz/hST+m4lJriBJEp/QHpL4eoEkPmEskMQnGCagk0jiv5mYpN5VLfFNcp1QQueQxNcLJPEJY4EkPsEwAZ1EEv/NxASqrhj6ui2hPSTx9QJJfMJYIIlPMIxLJ0m+cyCJ/2ZiXFVXTUjiE9pDEl8vkMQnjAWS+ATDuHQSrYtPcBhX1VUTkviE9pDE1wsk8QljgSQ+wTAunUQSn+AwrqqrJtu2bTt69Gh5l4Iwbkji6wWBxEfHc+PGjaKiIgOcOjQ09OLFi+w3SXyiVEjiEwzj0kkk8QkO46q6pfLixYuSkpJHCvADJrq8S0QYKyTx9YJA4j958iQyMtLf3z8nJ0ffzTU7O5vzJUjiE6VSXhIf52KLqZPEryAYl04iiU9wGFfVVc2/dTg6unHjxr6+vj4+Po0aNYqPjxfLBhNY/4owACTx9YJA4qN9Pnz4cNmyZa6urrGxsbm5uYYpRl5eHkl8QjV8if/ixYtNmzZlZWXp9Yw4C3zdoMD+aCZykvgVBqaTZsyYsVuEWEkwhVGOKX/44QeS+ATDlFaQXLJkCWT94sWLYRiLi4s3btzYtGnTv/76S5DMlLwaQn+QxNcL0C7Nmzc/ffq0wPm+cuXK2LFjPTw81q5dq++4HZz65MmTv/3224kTJ/R6IsKo4Ut8A5wO4n7a1GnWllYjhg+/c+eOnCR+hQE6qVatWjIpxEqCKYxyT5mamsrfThKfMGpgjb29vYcPH/7ixQtuI/4MCgrib5GTxCfUgyS+XoAL3q5dO09PT/y4f/8+X+jDL0e31Lt3727dup0/f/7Zs2c6PztsQX5+fmxsrKurKx4BShIREZGbmyuwEQQhV3QqUZGRfl27ZWdn61XlP378eM2ff/p08vLx8tqyeQtrFDgj/N4unTt369r177//pipavrDRUDFioVwRUvr5+QnsJ0l8wqgpLCx0c3PjZtMxMjMzXVxcCgoK+Bu1l/hPnjxZtWrV0KFDb9y4QYbXVCGJr3sgr6Gqr169ClU9aNAgHx+flStXCqJloGw2bdqEXePHj4fE0eHZ0W4TExM7deo0YMAANkoKH2PSpEk414oVKwRmgiBu377taO/Qq2dPawvL6dOm3bx5U+enQG1PSUnx7dzZzcX1z9WrUUWZvkfXgjPaWluPGD4ioK9/B7P2CQkJKI/OC0C8IZDEJ4wadNCurq6ouvyN2dnZdnZ2ggX6tJH4T58+3bZtW/v27YOCgmJiYpDVjBkzWNgkYWKQxNcx0C5oLWPHjmV/FhcXHzp0qK+C8+fP831lpETTnTt3rpWV1bx58x49eqTlqSGkTp8+7e/vHxwcnJqaWlJSwu3CeY8dOxYSEuLl5YUfhgnJICo+qIQzZ8zo4dcdLujOnTu9O3bycHPfuGEj+gCd5I+Kh0oePnZs+7ZtJ0+a9PfffzNxD5W/ft26ju7uPbr5HThwAHUVZ9y/f7+rk3NHD4+kpCQ0HJ0UgHijIIlPGDUwmOijZ86cyd+4aNGifv36PXv2jG8Vyybx0fVfunQJuXXv3p1bdB/ifvr06ebm5kuWLNGV5ScqCCTxdczVq1fd3NwEExahnzZu3IjtuCHYxRf6aHLoioYOHdqlSxdInLJNjWXtNioqysnJaevWrcpaKQwELIK1tfWQIUPQ86E7LMO5CFPi2rVrVhaWENlyhdyH8l62bJmjvUPPHj1SkpO1dAVv3bo1b+48i/bmAX39UT9Zbqh1B1NS4FQ4OzpB5QtmpMAYJSxa5Obi2qd3bxSAXh8TGsGX+Hl5eWEjRujjrRRHQUHB+nXrucXLSeIT2hMTE9OuXTtYZvZnRkZG8+bNExMTYU6DgoJOnTrFtpdB4kN7wHkwMzPbsmULF+F26NAhWH5Y2gcPHiD/AQMG7Ny5U7dXRJQjJPF1CdrJggULwsLCJCPsc3NzR40a1alTp7i4OIGUR8+EbqlHjx6BgYGCOLxSQVbz5s3z9PScOHGiOh/bQre0cOHCzp07o7VT3M4bTuy82D69ej18+JC/8fLly5EREbbW1mNHjxF4pGoCJxO9SCcPDw83d1RsVttZ2D1ah42V9ZQpU7g+TAxOOmHCBBsrq7Fjxty5c4eEPqEmfIkP4YI/9bRIMVzTCxcu+Hb2tbe1vXjhAttIEr+8MKUVJFFpx40bZ2lpaW9v7+DgALk/ffp0VGMYVYhvLy8v+AB3797VSOKzsRsbG5s5c+YIooAgHqBJzp49i/yhW9LS0tzc3Hr16pWdnU2DgCYASXxdgltpZ2d35swZZQlKSkqgn4YPH96lSxd4z/zhdrTh+/fvr1mzBm170qRJ8AdK7ZzQbvfv3w+x/scff0A8qd8goZmgosaOHYvSwmoUFhaqeSBhSsAhdLC127plq3gX5HhmZmb/wMD2bdsuTkhQ/zvNOPDIkSOBAQF2Njbx8fFcDUd9nh8b2+b31oNCBl29erVU1Y584OuiAHbWNigAVVFCHaBRxowaHT52LGyj/s5y8uTJEaGh/9bwhQu5N12wwNaWVj5e3nl5efo7NSGJiS0vA/N4586dwMDAwYMHQxXwrSUsIUS5mZkZ+m5zc3N14tC2b98eHBwcFBT06NEjsahA5tAAPj4+0CRMukClLFmyBFsiIiJMw2t6kyGJr0vgbY8cObLUZNDie/bsQYsaMGBAenq6QO6gh8B9w97169cr66iQw+HDh0NCQry9vffu3VvmYU406a5duwYEBKSkpFCA/hsF6kzMrFneHTupEEOPHz/et2+fo709hAt+qJZNqD/Q8WPHjLG1th4zejRcWdadIJPdu3d7url7unukHkrVKNYTx6IVeLi59ezeHZnoVbcRJgBqoGV7c/N2ZqzG6tYzZKMwMPIOtrao59euXWM1HDIoLi7OycFxQP8gr44d8Q+nNsy3zAmGiUn8UkHHDfXfq1evtLQ0/qQ7PnB3s7KyOnXq5OjoeOTIEdWzm9BSNm/e7OTktHDhwrt378oVTQk6xM3NDRZYtxqRMCQk8XXG9evXO3TokJ2drWb6e/fuoWNwd3efMmVKQUEB372GgkfTTUxMFPvQSIaNEydORNNdvny59pE2ePxbtmzx8vIKDw+noIg3h39XabCxhaNYasqHDx/OmzsPwj0osD+qpaQriDTzY2MtzM2DBwQfP36c+2xt6qFD/fz9HWztFicsLts8E1T4f0PR5s6ztrQaEBQk/tYEQXBMiY4eOmQI+2CQrZU1PMMLr6JotGfp0qWuTs4hAwemKsKX2cYd27fDnejerdv2bdtYTHN8fLynu3vY8OFIpqtTE6oxrq+26SQlatq5c+ecnZ3HjRt39uxZwbG3b98ODQ2FQF+8eLH6r/fz8vKmTp1qZmYGaYFGhPqMU4SEhDg4OKSkpJA2MEZI4usGqJno6OjJkydrNBaONgONHhERAYW9du1aQSNHVgI1k5+fj24G7XbSpEmC5fa1AfkgZ5TfwsJiyZIlsA6kokyehEUJXX27qPkeFhX10qVL4/74w8by3/j4u3fv8s09fkPfu7m4wlfkwu5zc3NHjhhhZ2MzccIEbkS/zOAU0GphI0Y42NqiE1InjI1408jKyoK2RkXl/oTixxbUQPVHXsQ8e/bs6NGj3bv5oYavX7+eDc+XlJRcvXrVr2s3JwfHLZu3wH7yD0H9nBg1wc7aGv/TuIkBMMavtukkJWRAYmKitbU15BY6btS0e/furVq1ytbWNjIyEvVQ0zsJu3r69OkgBSdPnvxHAc4YEBAwduxYbkk0wlggia8b0Lo8PDzQNspwLJzs1NTUAQMGeHt779+/X7I/YLE9PXr06N+/P9qbnoJqzp8/P3ToUD8/v6SkJOqWTJi8vDxHOztIE42OQpWA1gkMCLBsbx4fH89f5jUzM5MbpMcPKP4OZu0HBgejReiwIiGrgykp3bp2g+ewcsUKCtAnOGASp02dOmhgiGDM8vr168FBQVYdLJYtW1aGhYnhzY4eNcqsTZuZM2Zw/nBBQQHchnZt2kRPnqxCRZ06dWro4CE2VtaLExaTMNI3FeFbbOWVEl7oyJEjnZ2dJ0yY0Lp160GDBonH9TUClhZSxMLCIioqiq2XX1xcvHDhwlatWs2bN0/9qVlEuUMSXzfExMRAHGujvNH9QFizgJlr165xWaHHys7OHjVqlK+vL1qdvsORnz59Ct8dxYDLAVOiLM6PMF5gvuMWLOjS2bdsa89DWK9ds8bNxbWzt49gmVfU4Z07dyJnT3eP9evXly0yp1Ty8/M3bdrk5ODg69M5PT2dgp4JuWKQxdK8Q3JysngXbOauXbucHJ26d+uGCqPmB8Uh7mNjY91dXUeFjeSifeAbb9261dPdvU+v3lBRpRp8mNO0tDS0lE4enocPH6ZFxwk9AZ1w8eLFhg0bLl26VFcr4cB9jYuLg+ewePFiNp5y5coV6BzJVkZUTEji64CcnBz41uxTsloCVTRjxgxPT8+ZM2fCV0aeERERHTt2nDNnjiHnGuJcS5YscXJywhNUsbghYYzAcDvY2m3btk2bTB48eDBn9mwLs/b9AwOZAIJnGNDX37KDBbZr/x23UikoKJg+bVrb1q3HjB6dmZmp79MRFZwp0dEDggaoTjN3zhwrC8uxY8aoHuNkSxjDifXy7Lh7925ue0pyCrZ4uLnv27dPo3dTkEcL4+IszS2GDB78999/q38gQagPfNfmzZsfPXqULUemq1f98EshQqKiokpKSlDtp02btnfvXp3kTBgAkvjagoY0adKk6OhoXWWIDgaaacyYMebm5lZWVuPHj8/IyCiXsJnr169PmTLF1dWVmrQpsWTx4u7d/LRfDe3ly5foSEJDQx3t7L08PR1t7SCeoLYNVlfRUs6fOwcfw9HeIWFRgmFOSlRArl696u7qeuF8KTNr2beWI8aPd7CxnTF9+r179wTxMzDmyKSfv7+zo9O6tWu55S9Rz8OGD3d3c4uNjS3zUM6/6xSPGeOBTObF5uTklC0TglAGJ/EfP37ct29fwddOtAHNBDX2hQJIAtIDRgRJfG25dOmSt7e3zoe64TFPmDABPUr5hsqgz1u3bh0eZTmWgdAhhYWFEBlr/vxTh3kit6a//rpjxw4d5qk+EPorVqzw7tipXM5OlDuQHQmLFvXv10/NCBz5v+PxyQODgzt6eKxcsYKv8ouKikaGjfwjPJzrFP9dh2DyZMsOFuPHjdPJe9ozZ85069LVzsZm48aN9GkhQodwEv/Ro0fQJPqYqkQS3+ggia8V6B5iYmLGjRuncyGOnKdOnbps2bJyn6e1c+fOsLCw8i0DoRP+jcKPi/Pq2FG3McHnz59v3rRpOUYgnDhxwosk/pvKgwcP7G1sNZUdjx8/3r9/v6e7e2dvn1OnTnHzUp48ecJ+I4HiC82eXbt0TU9P1+EKBwUFBZs3b/by7Ojfp8+xY8f+f3vnARVFlv7tVcdJO3lnd8ZdzxhRFMRAkpxzDoISRAQkJxEDICIoQ1AMoKgooCAGMCsGFEXMEQNG0DGBjumYR51dvp/cz/73dEPbNNUk3+f04dBFdVXR/d57n7f6BlqQhOCEllH8lJQUUvx2BCl+s6itrTU3N6+urub8yKT4BOfcu3fP0syc89vtpPhEK7IoM9NvnK9k3cPeLU6yeLGmmvqkyEjexJeocuH0gQEBVhYW+fn5nF7s/4E0O232bANdvRkJCTTeiWg+LaP4ycnJpPjtCFL8ZjF79uy5c+dK48ik+ATnFBYWjnRyYosXcggpPtFaIOrsbWx5c+FLACrYq1evRk6YYGNlvTx3eUVFRUR4uLmJ6bJly1BSpFr9/vnnn9XV1WwwyepVqwUm1yeIJkGKTwhDit8s0DZIafIQUnyCWx4/fuxgZ1e4di3nRybFJ1oF1I0Q8UD/AMmmf+UH7nKgvHykk/NwRaVJkZGIKE6uUEx2bN/u4+XlN86XeucTEtMCis8mFyHFb0eQ4rdRmq/4Dx482LZtW3GzSUxMRH2xfft2ge0lJSU0a357AVG0YvnyEQ4O0phFnhSfaBXQdJkaGe3gruNZdXX1KCdnCdYEbT6rCgqUhgxtfq5CfLS0jOJD6kjx2xGk+E3g+fPnFy9ePHPmzPXr16Vtt81U/EePHnl6en777bd/bzaff/75J598Irz9hx9+WCuFW8KENEDoBgUEFq4tlMbBSfGJVmHJ4sVjRntwOFz1/v37o93cHjx4wNUBxQeKrzh4CCk+ITEto/iJiYmk+O0IUvwPA8m+efNmfHz8L7/8IiMjM3DgwJ49ew4aNGj9+vUcTj0rfFKJFR8ZyMiRI+Hln376KX7+TQp8+eWXnTt3Hjx4cEVFhTT+faL5PHz4ENV9WVnZ4cOHEcAQF/FnFWwSkil+bW3tgfJygen58XTXrl1NnfCHFP8jBPEz0smJ2x41pPhE+4UUnxCGFP/DXL16VU1N7bvvvgsLC1u9ejUUJDMz08HB4auvvgoMDJRGz4e6Zij+tWvXrKysmIjD77t06SINxUfy0KlTJ/xiZ2fXksvuEuKAmEEt7DbKRXHoMDlZ2SGDFOxsbPLz89uU4q8rKtJUUz969Cj/Rjzt27NXUw9Fiv+xgQhfv369j7c3t5UPKT7RfmkZxZ85cyYpfjuCFP8DvH371tLSslu3boWFhfw2f+/eveDg4L///e+5ubnSGBErgeJjT8iWhYVF586dId9QcDk5uTlz5qxsBgUFBVFRUdbW1viFt3HRokVKSkpM8eH6SUlJNEqsTVFaWqo8THG0m/vp06cRqFVVVTHR0YpDhsxJS5NGrJLiEy3M8+fPrSwstxcXc3tYUnyi/UKKTwhDiv8Bdu/e/a9//SshIUHYYmtqanR0dCC7vHXOOUQCxT9+/DhKODNvgMzk0qVL/2s2u3btmjx5ssDGnTt3fvfdd+xEiKEtW7ZINi81wTl37tyxsbKC3//++++8jVCH2NjY4Uoq0uhYRYpPtDB5K1Z4uLtznq+S4hPtl5ZR/BkzZpDityNI8T8A/gu8RwcPHmzwr1OnTv3ll1/gu5yft6mKD79XV1dnzv3VV1/5+fndvn2bkytpcNJMCH1UVBQvnVBQUKitreXkdEQz2bp1q4Kc/IEDBwS2w5v1dXQT4uM5P6PEiq+hOry4uLiGj+3FxaT4RIOgzrl06RKC7c2bN0+fPuV8eYc6iRQf0lO+f7/Axdy6devw4cNNykBI8Ylm0jKKn5CQQIrfjiDFF8XLly9dXV379evXmL9u374dPp2cnMz5qZuk+Lt27RowYADrn4OUY+XKlRyOEGhsXny0ao6OjqyvP1x/zJgxUloigGgS69etUxgo12D9bmluMSEigvMe+RIr/hD5QWbGJo729ryHmYkJKT4hwNu3b/Pz8wMDAhEtBnr6/n5+a9esaeqYbHGQQPGfP38ONd+0aRP/xqVZWTpaWk36YpMUn2gmLaD4KInx8fGk+O0IUnxRoJDAYmHPAvN+8CgvL4fiJyYmcn5qMRUfrcjWrVuh9fBs2LaWlta+ffu47TMjYukrqFXfvn3Zjfxvvvlm8eLFNFN+q8MUH+Yh/Ccovr+vX4N/ag4SK76KomL89Om5Obm8B56S4hP8QOXfjSQZPGR8+PirV6/eu3dvanSMnraOr48P5xIjmeKjuK1fv55/4+JFizWGq5HiEy1Jyyj+9OnTSfHbEaT4ovjgXfzi4uKvv/46JSWF81OLo/js5ta///3vTp06ff75515eXrdu3eK8f6oIxce5Vq1a9eWXXzLL/9e//nX48GFuz040FSj+oAEDhceHQDgszMynTJ7M4TziDOqLT0iPyspKuf6yS7OyeFtQ7ZTv36+mrLJhwwZuz0WKT7RfeIqPmAwMDOTwS3U4Iooh4pkUv91Biv8BYmJi8B6VlZU1+Fe4b48ePXbv3s35eT+o+CjPS5YsYf1kfvrpp/nz53N+d5YhQvHr6sdxenh4sD5CrFN+YWFhST3Clnn69OmShmiZPT8SEKsQ7ry8PIHtsGco9YKMDM7PSIpPSA+/cb4OdnYCnd2hGtZWVp4eHq0+aSZT/MK1ha/5WLhgASk+0cLwFL+u/oYOJ8fEcTZv3hwcHDxnzpy39cTGxpLityNI8T8AnKNbt25wXOHe7RARdXV1FRWVR48ecX5e0YqPliAzM/P777/v1KmTvLz81q1bpddDRrTiAz09vQbnzsdVCexpbm7eint+JMA5vL28jAwMT5w4wQuempoaHy8vAz39O3fucH5GUnxCeliYmcdOnSpQDeLp2jVr5AcM5J82qvlIrPjWlpbeY714D1MjI1J8ooVB3d6zZ8/w8PAbN240/8v8ly9fXrx40d7ePiYmBr9gy9OnT0tLSwcNGmRiYlJVVUWx2i4gxf8Af/7557hx4z777LP09HTeWrYoPyhFY8eOhWQXFhZK47wiFP/FixfJycmff/75J5984uLicvnyZWlMds7jg4ofFRWFPAfXw9y6S5cuAwcONDAwOHLkiPCeBg3RMnt+PMBRHO3slIYqIg/Mzs5etnSphamZjqZWeXm5NE5Hik9IDyj+9Lg44e2wDdm+MtzOqyOx4k8YH7E8N5f38PUZR4pPtCQIXQsLCxhXWlqarq7uvHnzmjOtwtWrVwMDAx0cHKA3zC727t3r5OSELZs2bUKzghYWVkDT6LV9SPE/DJJja2vrr776ysPDY/78+Xl5eYmJiUZGRj/++GNcXJyUVgxtTPHxaeHsX3zxxT/+8Y8JEyZw++E1yAcVn7FgwQLeHfR+/foh8ZD2hRGNgZi5detWbk6OprqGiqLScCXlGQkJEHEpCYRkio9itWfPHoFvwPB069atTZ0shRS/A2NtaRU1ZYrAABJE+MKFC5WGDuN2Dnvqi0+0R1AcoAqpqalv3rzB75cuXQoKCnJzc9u2bVtT/QTWvnz5cujNxo0bHz58iC3Xr19PSEgwNjbet28f8w2cArV3cnKynp7eunXrpDF9LcEVpPhigUofZq+srNyzZ08ZGZkePXo4OjqWlZVx2xOUnwYVHx8VtB7JRv/+/YuKijicGVMEYir+48ePx4wZw5tD09LSsgXSD0IEiJy374FtnDlzZtGiRdI4kWSKz0AquIkP1qg0FVL8DkxGRoa6qmpVVRX/RqiwuurwuGnTuL3DQopPtEe2bNliYmIi0GmtoqLCxcUlJCQExi/OQdBeFBQUaGlpQehZZY6EAR5vYGCwePHiBufnwSkgJLq6urgATv4RgnNI8ZvAn3/+iTbg9u3bz5494zdvKBTnVbOw4tfU1AQGBn7++edInSFV3J5OBI0pPhvnyj+qtbq6mrf81hdffDFt2rSWSUIIcThx4oSVhWVlZSXnR26O4i9cuBCG9P8fcvLIQyQ4CCl+B+bmzZuweV+fcY8fP2bSjF/S58/X0tA4dOgQt+cixSfaHVeuXLG0tDx79qzwn+B2eXl5tra2EP3r16+LOAiq0MjISG9v74sXL8JnXrx4sW7dOkdHR7zw2rVrIiIZOfa5c+fc3Nzi4uLwS/P/HYJbSPGbBUIfJWfKlCmrVq3i9sgCio+2Z8yYMd9//z2SZrR5Uu18L0Bjis/GuQqMat25c2fXrl2Z5f/000+lpaUtdZmCCGcgROSEyPDQUM7zruYofm5OrqxMvz49euLRt2cvNq6rqZDid2BQ120vLjY2NFRVVMpIT1+xfLmWuoaBnj6SQ86rQVJ8on2BGJs4caLAymsCIEQTEhJMTU3z8/OFv/WqqamJjo42MDDYvn076+dz4cIFDw8P+AbqVTGLGOJ2w4YNOEhMTIxk38QSUoIUX0JQGM6cOZOUlGRlZbVs2TLeSFyu4Ff8W7du4Sy9evXKyclp+TagSYrPvtr7+9//ziy/Z8+et2/fbqkr/fDlfeSg7tbV1ELyw+1hm6P4+/fvVxwylCm+XH/Za9euSXAQUvwOz+XLl7ds2TIhIiIoIBAygUiWxso+Eij+n3/+uWfPHoFxhzdu3CgvL29SBkKKTzQVREtkZKSnp+cHwwZRihIUEBBgbGx87Ngx/sFO4eHh8+fPZ/3pr1696u/vb2dnt3LlSgmm1UcpSExMdHJygrfQUvdtBFJ8CTl16pSNjc3s2bOlNKicKX5eXl5VVZWFhYWuru6+ffs4X7RIHJqk+ACVBeoINlN+165d/fz8pDGp6AchxRfm9evX0VOiwsPCuD1scxQf6au2hgZT/OHKKjdv3pTgIKT4Hwl/1lNX3zdyrKfnlStXuD2+BIrPqKioyM3Nza5n1apVEkxhTIpPNBXUe15eXk3KdTdt2uTu7h4UFHT79m3+FBSBB9kwMzOD0jRzgR2UyrFjx3p4eJSVlXE1PT8hMaT4EoIk9caNG7z2Br8fPXoUv3B1fKb4sbGxampq3t7eojvSSZWdO3dOmTJFeLsIh7569eovv/yCv3733XcRERGtktCT4jdI5fnzVhaWHM4oCpsp3rYNdn6gvFyC+H/69Km+ji5TfDMTk7t37zb1CGicigoLra2saHj3xwPUwdfHZ0FGBrcOIbHil5SUyPaVYWGMdFeCQcCk+ESTqKqqsrS0PHXqVFNfiOZ427ZtBgYGy5Ytg1fgaWlpqZGR0YQJE65du8ZJ57eXL1/u3bvX0dERGcilS5dI9FsRUvzmgpw1JSVlxIgRS5Ys4bCXMxqJmJiYrl27JicnS2/eng+Cwpmfn+/k5HTy5EnoF//XCCIcGtXE+vXrNTQ08NqWHDbADyl+Y8ROjY2MmMCJTNy8eTNuWpyGmrqFmbmWhsaMhISmLq2FiDI2MGRuNM7Hp6kd3i5fvhw1JUpDdTj0KDUlRXoLwBFtjePHj+toakmQE4pAYsW/d+/egH79WRirKCpJkOuS4hPigxBFAwflkPgIsHnomaqq6oh6iouLObw8BuQhJydnzJgx8+fP5/zghJiQ4jeLQ4cOIVWdNWvWxYsXOVwyura2NiwszNraun///vgFT1s+D4aaP378OCkpyc7OzsfHR0tLS0dHx8zMDB/rli1bkJqbmJjAoTdv3tygxD9//hyVCJtrCL8LXz+2IHXh3e7CbngqfCjs9uzZMwmaTFL8xqisrNRUV4chNecgiEk0MDZW1oH+/hUVFZkLMxXk5LXUNWytrXNzcpo0U7K1pRVzI2QIYn7QiJOamprsZctMjYz9fX2rq6vxWoWBcrt27ZL0HyLaGagxwsPDY2NjObyJILHiP3r0aGB/WRbGqkrKpPiEVFm5ciWbBb85B0GUlpSUuLi4SHXub7QFo0ePltLxiQ9Cit8sUDbQKrB724jm33//vZkujvKwbNkyBweHRYsWQW2fPn06d+5cSHZ+fn5LTg7z8OHDoqIiSPy0adPu3r0LEceF4RosLS3l5eU///zzL7/8ks2cgwpizZo1e/fuvXLlCppGgbbt1atXERER3333XXZ2tsA7c/LkyX79+rH8Hm8gsoghQ4bcuHFD4EoOHz789ddfr169uqkNOSl+Y6BhiJ8+HWoumRvhw9qxY4ejvf0oZ2f8wj5WqImxoZGpkdHy5csd7OxGOjnt2bNHzKEj7m7uzI3mpM0RZ3/E2OpVq+xsbF2cR+7cuZO1c9evX1caOsxAV09gAnWiA3PhwgUrcwsO54GVWPEfP37MU3wDHV1SfEJKoNLesGGDlpYWJ4MA0QqPHTu2+ccRARxgzJgxUj0FIQJSfG54/vz50qVL7e3tJe53jlYBRdfGxgbv25kzZ3hCzBYtmjhxorOzM4RG2v1ecPxjx45BuENDQ4V7bKO4VlRUJCcnOzk5sVWuGF999ZWysjL+fX9//xkzZuzevRuyjv8I+4eEhGCH/v3744X8h0Ll0rNnT7YYE1wQiT6MX3jI5qFDhzp16iRBhx9SfBFcu3bN1tq6qT3yIdNnz54N8Pe3NLfIy8sTGEW9cuVKmV69I8dPuHPnTtaSLOwTFhKK0P2g6I8PDxdT8ZFqHj9+fLSbu72N7aqCVfwqBjeKmhKFC/D39aVO+R8JqGHCQsMy0jnokY8jnDt3zt/XT0VRKXZqbFO/OOVXfC9PzybNi4DQvXz5srWlldKQocL3OAiCH1TdaNqQ3HJyNLT10vZvUvzWhRSfAyCvdnZ2EyZMOH36tASNDcQFJTYoKAiae/DgQf4JrXi8ePGirKxsxIgRcOjKykpp9DlGe1lVVTVlyhQzM7PS0lIRuQr+xydPnuAy5s6dC7P/17/+xZsLn82i849//ENNTQ3vBlP8zz777LvvvnNzc0NDyDuItBU/KirKwMCAw3GlHYxpsdNCgoLF/IqWrVieOHOmgZ5+XOy0BmcyuXnzpoWp+VCFway3zKVLl959BLp6qSmpom84LcrMhBj1691HRNdSXMD9+/djoqO1NTWTk5IanHgHn7XSMMXev/SYk5bWWiNAiBYGjqKlrsFfsUhAdXV12uzZuppakyZO9B47FiFkZGCIaBQ/ilAfqimrMMVfmrVU/BfiyqfFxqopKSNoLUzNbK1tWmuWYaLtA1UIDQ3Nzc3lqn5D8XF3d+fkUI1Bit+6kOJzAORD4u4BqNDj4+NHjhyZl5f3wa93UcKzs7Ox86xZs5o6rlE09+7dS09Pt7a2zsjIaFJ7iWtGWhIbG2tkZPTtt9/yRF9JSQmBxRR/4MCBCQkJ2JiVlcV7obQVnxANFFxPS1ucHvkI79WrVpkaGo3z8q48X9lYXwJ8QAsyMmT7ysDC2c1I7Hn+3DlPjzHGhkbr1q1rbEmU8v37IUZDByns3r27wR1qamoWL15saWYe4O+PsGmsmCDzdB3lwsY74pgUMB8DqBInjI+ImzZNso8bddTaNWutLCxHOTufP38eobW9uHjQQLkR9g4jnZzwc9++fQ3ecxEAoR4cGMgUv6SkRJxTo1itXbPG3s4uKCCQfW3LpuVBJUmhSwjDGtNx48ZxOHHfgQMHXF1duTpag5Dity6k+JyBehmNweHDh69evSrO/i9evMjJydHV1Z0zZ47oNaL5wW7YeebMmdra2kVFRSg/zWwP0Eay+a2mTZtWWVkp2dFwVchVoGjR0dE9evT44osvvL29cShWK8nIyFy+fNnExASuz1u+tEHFv379+uu/QoovAN7qBgclN/X9wXueEB8fGBAgIvCwD1zZzcXF0tRsy5YtH3QdWIuayrt7mTFRUbx2CHG+fv16cxMTTw+PBifWRNThJZpq6sLrXr1Tru3bnRwc7W1sN27c+MG5CHft2sU0y9LcQkoLVhBtDVQaFmZmSD6b+sKdO3ciJp0cR6wrKuIvPqPd3HQ0tU6dOrVw4UJ9bZ2I8eM/WKWjECG/ZbG3Z88e0TvjXAhUR3t7pBD4hder5/Hjx0iGFQbKiZkkEB0b5I0IQgcHBxsbG1gyfi8uLpZgoIgIoPgjR44UZ0805fxf7COGxeyTTIrfupDicwaaAT8/P19fX57FNgaK7r59+5COh4aG4lUSLGiFl+AsOAJMGi2KBNMw19XLPQQa12xubn769GlO7g3gwhBPcP1jx47Vvb/x0Ldv3+fPnyP5+fnnn52cnFgfbmHF/+abb2xtbVHjOL9n1KhRxsbGf/vb30jxGajf02bPRkrGvxHv3tw5c9gb3iR+++03C1OzBo0Ex0RIhIWEWltapc+fL+ZQb3xGS7OyYDmDBsoVFBTwkgc2Eh0XaWVhGRE+/ty5c/wxzxRfX1eX/+sjvPb48eP+vr6W5uZZWVmIGXECAGdxsLNjphUWGirO/VeivYNYioudNis1VcyKFLshK/Ab52tiZLQ8dzliRmAHFKV+ffo62No9ffr00qVL0+PibG1s5s2dK7qjfMHKleIoPqJ9QkSErZXN4kWLBCaeQsxjo0yv3nraOh9sRIiODZrjGTNmdO/e3cvLKzIyEg394MGDOe93WlpaOmKEWIsGLl68GG7De4qW3c3NTZz7kqT4rQspPmegASgrK/vglAhoXQICAlA8Nm3aJJma88C51q9fDznGW93UZUHRukybNg0OvWbNGmksBc/gV3w8jYmJgcfn5OSgahBW/G+//RYJAH5xf4+HhwfSD7qLz+PKlStD5QfNnDGDfyPeZKUhQyX7fn9OWlpwUBD/coY4CJ7OiE8w0NWLnTr1woULTToslEhXS/vdvCK6egJzluM4ONq02Nh3HfRTUxG97MiwGVmZfob6Bqw4sAkx8T9iS/SUqKa6DnIMHO1dmiEnv3rVqlZZEJpoYZANGujpi5OIIupYt/upMTFINRvc59mzZx7u7oiirPeDQ5DujnIeqaOpJeKrJAQbG1KCVqDBHVDlIk/Q0tCYPHFiY1Xu5cuX4fc4zoTxEVTjfcwg8+zTp8+yZct4YYDYU1BQkGwR8caA4tvb24uz58KFC/nn3kGj4+zsTIrf9iHF5x4YkvAKPiiotbW16enphoaGeXl5Dx8+5KQGx0FwKOiduro6dPmDs3ayYYurV6+2tLTExeCSJL4MNHslJSWim1UBxUcjZ2pq+vPPP1dVVQkrPuvP84wPvGrPnj2k+DxEKz4+i6NHjyKHFP/u9dWrVw319Q8dOsSe4g1fvWq1tYWlr48PDiVBCorwS/r1V5levaEpAf7+wl/m4pjl5eVenp7Wlpbr1q3DDrdv3zYyMLQ0M6ur76uA0mFiZOTj7X3+/HkJLuDBgwcaw9XY/dRhg4fw/jWiA/P27duI8eOnRseIqCUePXpUvG2bjZX1mNEex44dE/2lZWFhoVx/2SGDFMr3l7MtqGa3FxfbWdt4enggoxB+OVN8hNyJEycE/oQgfzdbmpW1m4sr/ir6NlBocAiO079P38SZM5t5D4hov2RnZ3t5efHHM+pJ6JpwdDWHnTt32tjYiLMnKX47hRSfY65du+bt7b1p0yb+jVAuWDUsNiEh4datW9I4L5L7mJgYlCU0To3Nt4Ompbi4GJeBuqP5s26JMyulgOLX1dcpiDl3d/eysjKpDrcVJwNpd4hW/N27d6spq5ibmHq4u/v6jPMb5xvoHxA/fTqkubS09Py583fv3mWJE8Cr3tYzfdo0CD2ewunxEktTs9zc3OYshlJTU6M8TBGaoiAnX7h2bYMfHHLgnJwcC1MzHy8vXBusy3nECITEWE9PUxOT9evXN6ePTWpqKlN8PHDYpsYA60eH4BEedw63K2mIltmz44GCv3jRoiNHjvAHSXV1debChWfOnGnSoVDxmhkbN1atnTp1arSbm4GO3rqideLMPY/rsbOxQfw4Of6lGwMKTlpamr62dty0aQLfL6HOl+0r4+riKvDBHSgv9xs3zt7Wdvny5eL8I2ggZHr3eZctKAxu6ptAdBg8PDw8PT35t6CK9vf351bxd+zYYWlpKc6eUPx///vfWu/R0NAYNGgQKX7bhxSfY2BRKDY8q4BtV1ZWOjg4IAM+cOCANCa75IGma//+/ShOONfZs2f5z4WmFPYcGhqKigP78HfMkBjJFB9XNXPmzO+++27cuHHdu3enefGbBFP8AH//Mj6gg4Pl5aH4SJ8gGTy7ZY++vXr379N3gEy/gf1l5WUHDJaTVxw8RE1FdaSTE+x/zZo1eStWGBsYurm6mhobz0pNffDgQTNnGcfL4+Pi2NlVFJUuX77c2G6///777FmzcHbYDC7MxMho1qxZT548aeY3NhcqK1mO8e7f79krdurUJq0ohFBks0KVl5cL/AkN298aomX27HigNtDW0FiQ8ZeJ7ffs2aOmqrpy5comHQrJatKvv86ePVsgei9dupQQH29jZT1v7twm3V5BwozgQdlBRs0fP6wu9Ro71szYZNWqVbyu/MgiNNXUQ0NC2FNcxvXr14ODgpB44NTYTcyoxrkmT5rEotfKwhIJs/jXTHQYkpOTvb29+bdAKjQ1NblV/G3btqGhFGdPKD6cPvw9wcHBw4cPJ8Vv+5DiSwtU6BCyeLQuNjYoSBxOdCUatJrwNiMjo8TExKqqKjRI1dXVMCcrK6vs7GxO5J4hmeLX1d8JU1ZW7ty585dffkmK3ySY4ivIyWsMV/u/h+pwuEhjii/84Em/XH9ZhYFyOJrikKFBAYFwlOYvIcRAhgndYYYdFhIqIurwsR4/fnzsGE/vsWPPnz/PSdd5SBJvOS08BvaT3bplq/jxw5xbUVFRuK82kmSDhmiZPTseqKwQJxnp6fyBB7cerqyCIl9XHx78iD4aos7S3Jw3rzyibsnixTqamiHBwWLOcsbPw4cP7Wxs68eOD0TREN4BqTX/hDzIjZFIhIWG1tVH4Ls+mXr6UVOmnD59uqmn3rF9+xD5QSx6kSQ05ys1op2CprBPnz779+/nbTl48OAPP/zAbbWwefNmU1NTcfakjjrtFFJ8qXDv3r3Jkyfb2dllZGSgyWn5fuQ4aVpampOT07Rp0xwdHePi4iD63J5CYsXHu7Fnz54ePXqQ4jcVpvgTJ0RW83HhwoWhgxQaVvxf3vWWMTEygov4jvP18/WD7kyPi8PbjnfmzJkzv//++7Nnz2bOmJE2ezaHI1NxqEkTJ8HvcQ24pMyFmaKn5sQlxU+fztXZ6+qbQ54k4TIS4uPF/wKNKf7HcBO91RGt+CdPntTRfNcnQE9L297OLiY6umTXriPvOXr0KAKYv1cMqohJkZFTJk1++fIl/Nt5hJOTg+PevXslU2Qcbfny5QPqh25bW1oKjB1noO0sXPtuWn3XUS64mJFOzkhWUblZmJq5jByF60cFKMGpX79+7Whnz6J3QL/+27Ztk+AgRLsGkePu7q6rq7tlyxZkj6tWrRo4cGBmZia3LrFhwwZDQ0Nx9myO4nt4eNBQutaCFF8qQMVQOLmaiVIy0HyeOHFCRUUFog/jYVNVcog4Dv3HH38gBtTU1ARaWbwtyDqUlJRyc3Pr6r/UjomJsbGxEf5WGu/h0KFD0ciR4td9qC9+RUXF+NCwxJkzc3Jy8I8XbyveXlxcvn8/0gBIT2NvILanJCdzq/h19R0khioMZpqipqyCp43tKQ3FR0SNdHZ+N/+gji5iTMwpnBltSvFZT/2O2i+fKX5qSgpSzQfv2bhxo6qSMhQftRbLEht89P6lh4Kc3JjRHjFR0bxHUGCgkb5hWEioob7BokxRiaU4IGyMDY1wLgTSrNTUxo5WVVWVlpaGPERj+PBBcnIaw9ULCgqaOU1ZUWEh739XGjrs4IEDzTka0R55+PDhrFmzdHR0HBwchg8fvnr16lu3bnG75GVRUZG+vr44ey5atMjHx4f3FI2Oi4sLKX7bhxRfKkDFIKytPtYTF4BMY+TIkd26dRsxYkR2djaHFUQbd+g2fnmSIVrxUeEid2rqMlhSUnxcycTISJ6QoT1orDhIQ/HB0aNHE6bHizmhPj9tSvHb1MVwDlN8mLG1pRXvoa+jKz9g4AcVn/8BBR82eDBeaGFmrqetExE+vra2lpNeZ4Vr17JTKAyUa2z15br6lPL8+fMjHByCg4J5PYWaQ01NjY6mJu8fdHNx5fweDdHuOHXqlKenJ4cV9Zo1a7S0tMTZ8+zZs/zxj2vYvn27OFUrmqfRo0dz1QWUaCqk+FIBKmZtbS28qEoLgwswMjJCa4EUHJb/9ddfDxkyZObMmbi85i+L28Yduo1fnmRwPi9+ndQUH+zdu5fXW0ZWpt+SxYsbrOilpPg4F4587ty5hPgEgZVu4Y4LFixosOtFXRuz6jZ1MZzDFD9q8pRjx46deA/iRHmYIlN8uDssHz/5H/raulMmT543d25mZuaizEV4ZGdn79mz58aNG8+ePUMw79q1i6srRJBYmJmxGDY1Nn748KGInd1dXVlffE5In5/OU3y8S01d+YToeKCunj59+uTJkyXrACZMQUGBpqammDu/fPnS3d29fz0z/toGiYAUv3UhxZcKbUrxnz9/jqoBlqCoqPjJJ5907twZP318fLZs2dKY5YhDVFSUgYEB5+vtcUVHVXzFwUN+nZnIvxF1KJRo6dKlbU3xccDxYf837BW63+As9VJSfMa6devgiMGBQfyN4sIFCw309CsrKxt8CRv/2kZGu34Mit9YX3x8QAH+/oVr18Jub/Fx//79P/74o0FpePv2LbeKj9KxeNEiNsQF2cXUmBgRdsWt4uPf1NfRxVuBY967d48kiair770DtRDxhVKTyMvLQw0j/v6mpqZsvq+goCAxX8IGFdAShK0FKb5UaGuKX1ffVl26dAmFrUuXLqyU/vDDDyYmJvPnz0f70fG6yrXxDEQyXr58efTo0Rs3bvBvRNt/7NgxiSfXk57iA1yYXH9ZnuW7jnIRLhQtoPiD5eTXrlnDC/KFGQsMdPUaU/w2xces+BIckHPFr6uvRXU1tVgA9+vdZ9++fY3tya3ig/y8PNRgrPcd/3ZEciuO8iJal+rqagcHB06+1cnNzVVXVxd/f57iBwcHi/kSUvzWhRRfKrRBxWc8efIkKSnpn//8J2/67c8+++zHH3+cOHEi2pKOOqqPEIFUFf+PP/7w8fLi7zad9OuvAvmktBV/iPwgl5GjNNTUr1+/zjaS4rcR2oXig3lz5/IC2NLcvDG74lzx2dviN843ceZM/hkLkOfb2thy23IT7YjZs2dDMJo5PAP18JIlS8Sc3p7BFL9Tp06RkZFivgT64erqKtUVgQgRkOJLhTar+HX1zeqmTZuGDh0qsNQORH/UqFFZWVmi+5vyw1aQFUZ4YGXr7kmIQKqKX1e/nrGCvPz/N6SePVUVlQ4dPMh/Lmkr/rDBQ8r37zcxMgoNDmFlgRS/jYC6SE9Le+HChfySUVpaqqmusapglQQHlJLiX716VVlRkWf548PDG+yuw7niMwz09HHSLVu28LbsLimRlen34MEDzs9FtCKoCQUWCkQd1WBzzFaQLCoqkvhcOOyaNWsUFBS+/vrrkJCQiooKcV5lY2OD6ujbb78Vp0ZCy4Ky7OTkpKioGB8fz9X4AaJJkOJLhbas+IyzZ8/a2tp27dpVQPSHDBly/vz527dvHz58WHg+6SdPnpw6dYq3SCTr7y6McA/41t2TEIG0FR9RND4svF/vPmyO/MFy8vo6ullLlvBq/BZQfBQENIfDFAavKijA/0uK33aAarx8+ZJ/y+vXr7FRMiGQkuIjRBPiE/q8n94Her1r507h3aSn+IMGDDQ1Mrp27RrbQorfIXn27Jmvry//Fmdn5+3btze4871797S0tEpKSpp6FgQzqj4rKyvI9969e8PCwr7//vsBAwZkZmY+ffpU9GsnTpzYqVOnf//736LvyqOORaxGRkZqa2uvXLny3LlzSkpKAQEB8KKmXi3RTEjxpULbV/y6el9HIfzHP/7Bk+NPP/0U2TaayeTk5M6dO8P1BV5y4MCBfv36YR/2lPV3F0a4B3zr7kmIQNqKX1ffGi3IyNDS0ODNgSjbt98IB4f9ZWXQu//+97/z5s5NTkqSxqmZ4t+/fx/iGBYSoqOphbaHp/i4sNLSUvxSW1srTudmNGzV1dWV9Vy8eJGnoXgPa2pqLl++LNAH6UY9zXlj29TY37aPlBS/rn6dB1VFJd6NfKSpAjdc66Sp+OPDwzXU1CLGj2fpECl+hwSGzb+8FLC3txex8Nnx48dHjRrVpG+tz549GxwcDDnJy8tjYoDA7t2795w5cxITE+3s7LZu3frHH3809nLkG126dIHii6gtEZaLFy/GKVavXs3kErUiXvj1119379798OHD4l8t0XxI8aVCu1D8uvqu0rm5ubB2pvi9evViQ29nz56Np8KKf+jQIez80X6sHZIWUHzG9evXJ02cOPj9NJps5c4J4yPgysg2pWSxPMWvq2/MjAwMgoOCZ6WkMsWHr0+KnKg4dJiluUXctGm5OTlIABpbbQoSn/Trr0pDh8n07iPbp6+sjEx0VBQb+oxyFDkhcriSssB76DJyJLSPhri0GNJTfBAeGsbm1ZHtK4OfkyIjBSZjlZ7ip6Wlle/fryAvz7rrkOJ3SJji/48P0Yr/7sulhASIlji3J549e5aTk6Orq4uf/JHz3//+F0fo0aPHiRMnysvLR4wY4efnh98b7KB/+/btrl27Nqb4qAaROTg6OoaEhKBq5f8T9p8yZQrSA5wItSsNFm8xSPGlQntR/Lr6agKOpaGhgSS7oKCgrt75SPE/HlpM8evqZ1c4ffr0KOeR8rIDeKKvMVwtOSmJNxa2Obx+/frMmTOB/gHriorYDXV+xccWbFccPMTG6t36SlB8bHnx4kVVVdXRo0ejp0Q52NmPsHf44fvvEfwZ6elICXhlB63vSGdnbQ3NDRs2XLhwAUUGTa+musY4b+83b96Q4rcRpKr4qE7dXd3k+ssOkOmHuO3bs5ettQ2cm9fRSKqKjzTY39fPUE8f8sRTfAQwQrRJwoQQbWzKUaJ1QSUDBV/Mh4qKClN8GMXmzZuFb9iz+Wpg7SLmxEOtiNfa2dklJSUhKRXeE4ft2bPnmDFjEEsI5v3791tZWSHkfvvtN4E9792716Di4+mRI0dsbW2dnJwuX76MMwpfBurJ2NjYzp07f/PNN9B9GjLXMpDiS4V2pPiMO3fuZGVl8UyIFP/joSUVnwHDWLlypZmJCf9MO0b6BqtXr27OkCxEb0J8/FAFBRzNwtSMlT5+xa+rb+1CgoKwg66mlnBffHjPtWvXZGRkEPyqKirDlVUgVXhzYFfZy5apKinz94vF+5a9LBsJw9mzZ0nx2whSVfy6+llroVzGhoa8LmfQfaSsOCM++jlpaVlLlnB+Uqb4dfWTk5gaGU2IiNi6dStTfGxB2omwR5wfPHhQ9NzHiEO8EOm0x2iPhQsWHHq/P8IeiTH+LwHv37NnT7sYr9JhgOIbGxsX8qGhoYHPBVHn6+v76aef6ujo+Pv73717l79Nv379Oiy/wVmeEJMnTpzw8/ODeR84cEBEeCQmJqLSi46OZvug8kxJSYHDpKam8p+LKX7//v15io+YefjwYUhIiKOjI4KwQbnngUMhDcCJunTpgizig13/ieZDii8V2p3i19WXVVa8eYqPbP7eX4HiQIA+2o+1Q9Lyil9XH2y1tbXp8+drDFfj2ZJcf9mRTs4HDxwQGH/5QeA6Gzdu1NPSZoN62YBIbMGf8FNNRZX/i+lLly5ZmJkbGxpduHChwaOxEa6bNm26ePHiuqKi6XFxaMNC0YbZ2Qv0UoX6V1VVoXzxFB+/vOVjlLMzKX5LIm3FZ6B6R3kZLCfPS1DlZQfEx8Xdvn2bk0KERHfHjh28EY08xQfIjWX7ykRNnsIUH//v5s2bkRubGhvraGr5+/kFBwWdP38ekSmwfjmuebSbu6qSEq6zcG3hGPfRGqrDC9euxQXjRDig0pChAn6GdCJx5szm/zuEmDTWFx/6Dr9nnWk7der0xRdfqKmp5efns9Eg+JRzc3PR0AssZHnt2jW01BYWFqWlpSK61zOuXr0Kce/Tpw9vah0EBioulh6gQLFoZIoPm2dxXlNTk5mZqa2tnZCQIBBvjXHq1Cl2DwUgn0Fu2ZR3iGgypPhSoT0qPg+e4vfo0aPvX+nevTvql4/2Y+2QtIri805def78lMlTeJaPx6ABchMnREKvxWkwsM/u3btdR41i64+yh4qiYubCTDZp9I0bNzZs2CDQwh06eHDb1m2NVXzCk9jcuXPHzsYG6Udjl8EUX05Wdnx4eMT48bwHsgue4rPOtWK+M4RktIzi19ULEIzKz9dvmMJgFnUyvXorDh6St2JFM6t9xLO7q5uCnDwOxbbwKz5MKzoqCn7P3xcfcYWsGFqP14aFhI7z9kHm7ObiiiNAELEd+wQFBpoZm6A4sPuv2H/+vHnIUqCJpPhthMYU/9atWz/99NM333zTuXNn/rnj5OTkoBlnz559+PDhnDlzYNvsexh84ikpKebm5snJyQLDRUQQFRWF/EFRUZG/Cw0OePjw4XHjxrm5ueFQUHxYAQ4LqThw4AAcfe7cuZcuXWrSv7l3797v6ztDAllZ2aVLl9Ks+dKDFF8qdAzFnzx5chofqETCwsJQ13y0H2uHpBUVn/Hq1at9+/aNHOE0oF8/Zkt9e/VSGqa4cOFCEe0TLruioiI0JIT/ZiocK3LCBFhLc7oaCyv+9evXTY2NXUaOauwlTPEHyPQb+1cUhwxlio8jZGVlQZj27NkjPBetCBob+0s0SIspPgOhC18xNjTs36fv/w/dnr1G2Dts3LhRdI8FYVD6bt++HegfwMsZDHT12AAVfsWvq1/cVF1FVcRw23fdqcv2b9q0adLEiaqKSmVlZchR1VWHL8rM5N8N4lhYWIiTkuK3ERpTfNR1qGFOnjwZHR3tVY+JicmXX37JLLlr1669evWKiIj4+eefi4qKtm/f7ujoGBQUBLFrUjX47Nmz7t27w/LR0Av8CcUqNzcXh0Ua4OzsHBIS4lrPsWPHJKhp8e8gOH/44Qd2/cOGDePNBktwDim+VOgYin/27Nk//wqbNPOj/Vg7JK2u+LgAqNLDhw/z8/P1dXR5d/Txi6O9/YYNGwTu8WD/J0+ezJ0zB6LDk3vZvjKj3dzhds2/Uy6s+DjdGA8PZycn4SvHtaGRE90XHw3YWE/PuGnTlmZluY5yETFFhjgXQ4ighRWfgU9/8aJFFqZmvGjs17sP9BoCJGY0Pnr0aE5a2nBlFb6ePwNDQ0LZfE3xcdOL/xozp06dCgsJgZOJPizeDeg+YnJGQoKmuoZwzzR2eUzxFQbK5a1YUbByJe+hoTqcFL8lwScl8BmdOXOmwWGpyO7279+/e/du5P8LFixQU1P7dz3dunXz8PCQ2LzT09NR20C+169fLxy6NTU1WVlZrD8PEonmiCMqfE9Pz86dO8vKyiJ1qa2t5a85Ud/SlDtcQYovFTqG4tNw24+BVld8nHf2rFlLlizBlaCux8Woqw7nuY5cf9lRzs4HDx5knW1QW61etdrEyIh33xQ6hafw5g8aj5gIWzUubGp0tLmJ6Z07d/j3rKiosLKwQBMrWvFPnz7tM9YLDSS2rCooaNJbTYrfJFpF8evqI+T69eszZ8z4v4Wce/REGEdNiULuKsK3UDnv2L7d3sa2L9+6WiOdnHfs2MFht67pcXEmhkaNjW5kio8LGKqgMExhMO8h07s3FB8Xj0J369atu3fvUoeKNgjiBPUJIv/FixdKSkrNWRamurpaQUEBFY68vDzr6CgATpSamspJ+UJQTZ48+erVq8grkFTwL94cHR0tvOgEIRmk+FKBFJ9oL7QFxRdY3fb48eP+vr5sasL/3wNnyNCw0NDS0lKP0R7934+pxUNBTh5XzltumRMaXG0KDafyMMV5c+eyUWVsts2wkLDB8oPQGokzow722bpli7urWzHdxZcaraX4DNjw0aNHAwMCefEJb1ZTUc3JyREe74gQQlC5jBzFS1bx0NHUysnOaWonnw+CwqWnpd3YvLRM8RUHD0EO8AcfJvUddX777TcfL6/wsDCXUaOyl2Vze2EEhyBslJWVjx071pyDxMbGdunSpVOnTr6+vsJdChHhcIM9e/Y05xQCzJs3D6eDV/Cmb5oyZUpT+/cTjUGKLxVI8Yn2QhtU/Lr6/sQQ+tFubjwBkunVW0VRkSdDQxUGBwUEoiVoma90cZHp8+cPV1YZ7eZe8K4Xw8pRzs6qikorVqz4YEcdpvhVVVXBgUF4FRxO/LuhpPhNonUVPyUpeePGje9yua1bLUzNeKE7sL+so539iRMneFNF3b59OyE+Xo2vZ84Q+UFz0tIam+WpmVRUVGioDkfQ8m+E0MfHxc2dM1d0X3zkJ9iHDRXwHjuWelC0WThRfBzkP//5D+qczz//fO3atQJ/lZLi//zzz97e3iEhIWwLKT6HkOJLhfau+GlpaZ07dxZW/IMHD/bv3z8pKYm7ayRambap+AyE7uJFi3Q0Nfv27IXHYDk51jPHzsZ29+7dH5wJjlvgZyUlJSHBISYoVIaGQYGBSEKY8eAn/GnK5MkCXTKQFSzIyMB/gYaT9bsoKyvT0dQSf11SUvwm0bqKj3QuPCyM/f7kyZMFCxaoq/7fcJEBMv0QM9Cjlfn5QxUUeD1z5GUH+PqMg9NIbzkqxJ6DnR0EnddXB1vy8/PlZAcgJxGt+CiebL2InOzsiPHjaVaoNgsnio/Pd+nSpWwgrIyMjECHGSkpfq9evWpqajQ1NTMzM3EBpPgcQoovFdq74u/YscPHx0eg53Fd/ey50dHRmzdv5u4aiVamVRT/xYsXO3fuZKYrQvHr3i+tMj4sbLiS8hB5eSMDwyVLlnDV7V4CkFc8q0cgwYBcCqccb+qpv38fyIbNoQHW0tAQf2VHUvwm0eqKL7C67dmzZydPmjR0kAJP9IcNHsKb4BXSj3wPiWILrAGEKn2QnNxIp3erdN26dSs1JUVXSyt6ShQLUdEz6qCKCAoI1NbQ8PIc26T5oIiWhBPFr6ufQExJSYlZvq6uLqpf3p+kp/iIsZUrVyoqKsI6mOI/evTo0KFDH8x7cbU5OTkHDhzgtV8I75MnT/J2QF2N+rM5iyq2a0jxpUK7Vnzio6KFFR8SBu+BMehr67CviUQrPgMWcvjw4TWrV1++fLnd3Uesra0d6eSU9OuvuHjPMWOmTY0Vv7M1KX6TaGuKX8cWf6isdBn1lz73eCD+s5YsabG8GpdRUlIyISLC1tpGV1Nr7JgxSxYvZkkprmHdunXTYmMFLmb2rFm8cSP4E4LWUE+fN1s/0dbgSvHBzJkzu3Tpgprns88+y8jI4Hk2h4p/48aN27dv1/EpPiw8PDx8xIgRUEcoPoIzKCjIxcXFyclpzZo1FRUVN2/e5K/8kQOMGTPGzMxMVVVVR0fH2NiYDcpKT0/X1NTk7Xbq1Kmff/65wdV/PwZI8aVCKyo+f9ZLik98kHdDL1JnRU6YIO37czjR1atXE+LjDXT1pkbH1NTUsFh99uxZWEjojIQEcY4g1SuUErhs/LMzE2bA/5bn5jbpfW5w7C/RGC0/L/61a9d43a4aVHwG9llXVKSjqSnTu89QhcETJ0SijZBez5zGwPsDDbp48aJAq48QFb4Ytt55THT0qlWr2FNLM/Pc3NyWu1yiKXCo+NDrnj17shv5sPytW7ey7ZwoPg6+bNkyOTk5Dw8PXDNP8fGnCxcuDB06VFFRkddRB9vLysoSExODg4N1dXUjIyNnzJjx22+/vXnzBr8jAWAz/yCe/f39vb29ccCkpKQBAwbwTnf06NFOnTo1Nta8w0OKLxVaRfFRfZeUlKA65g3mI8UnRICqlvUQQJVtbmIa4O9/+vRpKQ2nQxDCbq3MLXx9fFDnshDFuU6dOuXn62thYlpaWiqN80oArTbVfmlJxUe+OnnSJDUV1bVr1rAtIhSfgRKXmpJ68ODBdpSsQu/cXd0y0tPT58+3MDOX0oBgovlwqPiIz7y8PHYjH8AiDh06dP/+fSj+ypUrUUNKfIVoa0xNTb/44gscFvZ59uxZfsUHO3fu7Nq1q3BffJQdpNPITiMiImbOnImL+emnn/in2nzy5Am7bUSKzw8pvlRoYcVHWN+5c2f8+PGOjo5o3nj3Y0jxiQZh9emmTZtGu4/+bz0PHjyImjxFU11jVmpqdXU1hwry6tUr1NrOjiMc7OzWFRXx8k+cJenXX7U1NafFxiJQ2470UN+Y9gsUPzUlJT8/nzd3jTRAuOIUNlbWyIrPnTvH6lsYxgh7h4jwcOmdt1V48eIFcpLgwKCMjAzetIZEG4RDxQcwCk1Nzb+9B7pvbGwcHh6enZ2NkGjqF1Co3t8tD+Lj88knn7ADysnJsUWgT506tWzZMt6e8NGsrKwGZ+Xn5/Hjx4MHD0aGIPwnKP4PP/ww/j0uLi6k+BwekBT/HVB8MzOz2traFjjX3bt3ly5dCrnPzMxkk3bz/oQLMDAwIMUnGOzr+Fu3bnm4j0aI3r9//8SJE7yAQW179OhRSL+1peXy3FzUoc3UbjbS1NfHx9jAcMGCBaznJY6JGmf58uVWFhZjRnucPHmyra2nQ4rfHmGzOiK89+3bZ6CrGzE+ArHH+VkQvUhTba1tPEaPLt9fzhMdJLFjx4xxGTlqx/btnJ+0LdB2MnCiMbhV/Lr6e0D6+voqKipfffUVz/W/+OKL7t279+vXLycnp6ys7OrVq6Jjg/XP9Pb2/uc//8mOMGDAgJiYmHv37jXn2tA8KSkpXbx4UfhPUPxevXpVvAfZOFN8lNYjR47s37+ftUQfCaT4UgEZMMpGYGCgVC3/7du3GzZssLCwQIE5f/68QGLN7us7Ozu38NyCRJulqLCwtLT0xYsXE8ZH8HoXCIBoQVA5OTo62NlvLy6WeBUeZJ6/JibqaGrFTZt27do11gzgaDi4va3dSCdntB9tMzJJ8dsRbJwD/L6kpATxxjZCKVJTUuxsbJJ+/ZWr5hy1K3QhKDDQwsxsUWYmu8vIZpMM8Pe3MDNfsXy5+BMlEQTncK74jOfPnxcVFWVkZDg5OX366ae83ju8m/G+vr5RUVEohm/evBGQENTwS5cuxT689GDy5MnV1dXNvyoo/nfffbedL6N+8OBBUFAQVL6xjjpr1qzBDunp6eHh4S0/DKa1IMXnEoT4jRs32ILSly5dWrRokbW1dXZ2djMTVmFQmN9NSxIU5OHhcfjwYQFVwulWrFiBUy9ZsgS/0w2Yj5zK8+eLi4sRBsuWLnV2HIGQuHXrlohiz7RpaVaWkYEh9IWNbRLzXHjtkydP1q9f72jv4Obqum/fPta5H0e4cuWKj5eXiZERKv2W+YJLMkjx2xFoqoMDg3bv3o0AO3PmDP+fYORjx4wxMTZGVtnMZBJFJiU5WU9LG/kqb5AGjpk2e7ahvkF83HTEdnOOTxDNR0qKzwOuj3bh5MmTo0ePNjIygjvyRL9z584//vgjtgQEBGzbtu3QoUMoMnv27JGXl//888+xQ9euXW1tbcvKyrj6zhbHgWH6+PigecJTZNfR0dGurq64yMYUv6qq6ubNmzt37vTy8vp4VnAjxeeShw8fmpmZ8Q8Gx+9IW5H+opnhamZW+Nn06dNHjRqVl5cnUGBwinXr1iHQAwMDafGIjxwU7B07djx79gyebWxgePHiRdSDkydNErNXIqIXdWL0lCiYTWpKivAiCQ2+pKSkZLT7aBsr65UrV/K8Cg1D4oyZ+to6sVOnCkx81gZpU4pPY3+F+V89W7duXZCRgaY6LS1txowZDe6JIgDPsLGy8nB3r6yslOArqUePHq1YvtzG0irA791gdDatJD6OzZs3Ozk4eI8dC6NqrTXjCIIfaSs+A60J6x5z+PDh7OxsqMjf//73Tz/9FJbPM/7vv/9eT0+PjanF9mHDhgm7SvOprq5m02WOGzfOwsKiV69eR44cwfbU1NTBgwfzdsMbgjSDZQLnz59HcjJ27NiPp8yS4nPA6Xrq6m8pbdmypaKigv+v0O7du3d7eHh4enpeuXJF4vQRrRp0LTc3V1tbe+7cuQhZ/i+bcFhEvK+vL0504MABqY42I9oybOz106dPIfQmRkbbtm1D3To+PHxqdAzaAGh3kwwb++/du9dj9Gg7G9s1q1c35po45uXLl6dMmmRpbgHlYt9l1dUnvfn5+SPsHbzGjOXwFo5UaVOK36Yupi2A8F62dCnqOuSfFiamApVtgyCG0+fP19XSQoYp/u12BPDBAwfcXd3sbW3Xrl3L2w6/QXEw1DfYuHHjx3MvkGj7tIDio1DMmzePf9JMFAFU8rdu3YqPj7e2tlZUVOQNqAU9evRAc8C/eBa3oJlDu4OSiHqAN0IXp7t27RpvHwjYpUuX0PScO3fu+fPnT548iY6OXr16tZQuqa1Bii8hiPUXL14wZUHuaGxszObPYXeYhPdH8Vu3bp2jo2NSUpIEg7vZtCQ+Pj4hISFo2wR6kmFLYmKinZ1dYWEhyX0HAB/i0qVLkRnyx9K7Nefz8g6Ul/NvPHToEPRl3tx58+fN37plK2ISr/Xx8po9ezab4MzcxBSVWm1tbW5OrsSxAUlau2aNpbk5jAemLhDhf/75Z3Fxsb62ToCfP69uxT6lpaWjnEfaWFqtX7++HckQs+o5c+aUCCGc4bC77NLbk3VjJcUHq1etQolAVPv7+v6amIgadeHChTU1NeK8FiH622+/BQUEWpiaIVMVPdcZdoY3+Hh7W1lYrCpYxetmifQgJirKwc4uMzOTLbJDEG2HFlB8lD4ou4h58W/evAkJycrKUlFR8fX1lXh6TWkwZcqUuLg4vD/+/v4fT886UnwJedcRMy2NNb3v1gdNScnLyxP9EuwGAUpNTTU1NYXAie9baJz8/PxcXV03b94s0KkUTwsKCuzt7adPny6NGSSIVuHBgwdKiorj/zoqCL8b6RtMj4tjXzI+ffo0YXq8jqamrqaWkYGhga6etobmSCdnxNi5c+cM9PQOHDjw6NEjdze3nOxsNj6kmVd148aNlOQU5AyTJk68cOEC74A4+KZNm1AW2NxN2F5ZWRkZMQF7zp8/v91NXxAaGvrtt9/+rSGEVZvlA9Le8+DBg1L8h1sK4XsfwjdE/scH23L//v2M9HRE8o4dO2ytbVA0EHv6Orri9BwTZt++feO8vZ0cHNcVFTV4LwYZFxJmjeHDo6Oirl69yjairC3NyjLUNxgfFs7JYEGC4JyWUXxxlr5iN0AlnqpBSsC4YPne3t7trklqDqT4f+Ht27fQlGfPnjXmQ4jaixcv4q+sM+jo0aPZl1BQbTHnpsQpcISgoCAo+5EjR0QsdclGPc6bN09fXx8ej8+Jv01CvOLlHh4egYGBkPt20QWCEBNxFD8lOVm+v+zSrKUs60Ns7C8rg+iPHOGEsJkaHe3v68vWluI294O+hwQH62ppzUlLE569+N69e9iuo6kVHhbWfkeDsDVlhRFeZbYF9kQl09YaSwm4cuUK0lGBUJw5YwbihP3OqrvICZEILT1tbfxMTkpCVllbW2thZrZlyxaEveeYMb8mJqLOvHXrlsTfCz158mT1qtV2NjY+Xl5nzpzhr+px5Ijw8S4jR12orGRDp1DNIlVGmbK1sTl08JC0V4AmCImRnuKjbEJv2JzLzV/dlmhJOqziIxxhwPHx8cLfyaLNgDdv3ryZfyOq8p07d0ZFRSHJGzt27OTJk7GDcMuKN8vR0RGVfl19iYqNjU1KSpLg8tCu7NixA4IeHBzc2HqBsCW2kJvwCMWzZ88GBAS4u7sXN2NaQ6LN8kHFhwxpqWskxMcLfPolJSUKcvJIPi9fvjzW01NKtyvYajiuo1wc7O3hXsx7YE7r1q2zsbJ2+1DuSnyEnD9/vk+Pnhf/WtchwhFF7HeE9Ah7B9h8+vz5ixctykhPN9DTMzM2+e2331AVW1lYsmnEgoOCEGnNvx4kCTiRvrbO1JgY/rsziFveN6WnT5/GFRrqG2Qvy27jY8QJQkqK/+bNm7y8PBgRjk+K3+7osIoPDZo/f36nTp3gOgJ/qqio6NmzJzyetwUy7efnh409evRwcHCAxON96d69OxSc9bksLS2FyrBaHr94enqy+5ds8SDJrhBHQ7JRUFBgYGCQmpqKQwm0Isg6qqur+R0OO2C3zMxMKyurnJycu3fvSnZqoo3DFD8kKOjx48dP3oOCCulhip+VlaWqpLRr1y6BF0JQhikMnjp16tu3b+/cuSNVL8FlsN4LYaGhS5cu9fXxMTU2XrFiBX2hRAgjWvERt/5+fiOdnVHf8oL2XYccbR0nBwc4t4+X97y5c1+9evX06VOuLgknOnfuXEhwCPLSvBUrUOh4f0LZSUlONjUympGQgGr245lFm2i/QBVUVVW3b9/OVbjCQEpKSlxdXcPDw5kIQXvi4uJI8dsRHV/xhcdVnDlzhl/x0WYgiLt165aUlASR+m89eFOQrf744482Njb4vaqqSldXl33LjNZo4sSJS5Ys4cSfcJDff/8dxcbNzW3jxo0iGjA23biTk1NUVJRwPkB0JJjiD5aTN9DV43/IyvRjih83bZqOppZwDxzIkK21jZaGRsuMukZJuX37dkJ8vKW5RXJSUk1NDckQ0SBM8S9UVvL3tucp/t69e5WGDtteXCzwqiWLFw9XUobro5LcXVIijewRpWnz5s0WZuZuLq6s307WkiV2NrZTJk/uGEMgiA4Pat3S0lL8zMnJUVFRyczMbOb3tyz7hZO4u7sfOXIEheLt27e7du3S0tLy8fFpvz0wP0JI8euysrKg8vB7ASvCEaZPn965c+fCwkI8Xb16dWBgIPtKly1rxaFko/zs37/fy8vLwcEBRUt4CNqpU6cg9+PGjdu3bx/1zOnwMMV3sLNbmZ9fsHIle+B36A5T/Gmxsfo6umyuX35evXplbWmpMVytJSdWQtOC01HOSYiAKT7ywOxl2bwH0lGm+Bs3bhw0YOCzZ88EXnXz5k3EeUpysrQv7/79+6sKVqHEvfvewHEEhKltLr1MEAJUVVW9u+kTF8eeQnjmzJljaWlZUlIiWW/J2tpamI+jo+Py5ctxBFTs1dXVERERnp6eOCbdxGlfdHzF582KwOPs2bM8xX/69Cny1F9++aXBqVvx2uHDhysrK0PBEeswbOTHCHEEvTTuJyF/QBGysLBAcUVBZSfCL4mJifb29jt37hRzRC/R3vlgX/zcnBxVReUdO3YIvBARojRkaNSUqHY0SSXxMcAUPzAgEMHJexjq6YtWfMSziZHR9Pf6Im2uXbu2ds0a6H7LnI4gJOby5cvr169HoxAeHo7anr+lgDbcuHHDzc0tMDBQuDOnCFDcCgsL1dTUIG9QIxzn9u3bGRkZ2LJs2TLqgdke6eCK/7e//S0/P7+Uj71792ZnZ//8889M8a9fv66urm5gYNDgQV69eoVyIiMjw772On78uL+/PyeDvUTw+++/48pdXFwWLVo0d+5cGxub5ORk0RM5Ex2MDyo+dhAebssWl1WQk9+2bVtrXDVBNApT/LNnz/7BR2hICFP8TZs2QfGFuyleuHBBT1sH9WFrXDJBtEXKy8tPnToFJRgxYgREH3LS4J11lKaysjJtbW0fH5+bN2+KnjQZhfHKlSvOzs5xcXEopNiCfHvHjh1WVlbp6ek0UWz7peMrfu/evfvzISsr26tXr65duzLFr6ysHDBgQHBwcIMHgTONGzful19+OXPmTF19d5o7d+60wNLHOBHatrCwsAkTJuAKKXv+2BBn0sz0+fOVhg7Lzclh1ffjx4+3bNlibGDo7+snPJclQbQuoofbnjx5UktDI3vpMoG13hYuWKCuqvpRzWNNEI2BYrJu3brnz58bGhpWVFRUVVU1Nh0fD7h7RkaGubl5SkpKYyIBuYetmZmZFRcXswLI1tl0cXEhuW/vdHDF79SpU15eXulfycnJ6datG1N8NDz9+vULDQ1t8CAIdwR6jx49hOeubgEaWyiX6PBA8VWVVSZERAgovqmRUUJ8PFP8J0+ezElLg+XbWtuEBAePdndXGjLU18dHgrWTCULaiFZ8hPTMGTOMDAx37drFi/mSkpIhcoMC/P2pGiQ6Hnfv3uV37mfPnvE6CEDiL1++fKGeixcvvnz5sqioCEXj3r17Dg4ONTU1O3bsWLZsmZgnQoGCqXt6elpbW2/btk2gO9zmzZsNDAzw8/fff2eLQHt5eenp6ZWXl3M4exXRWnR8xRcebsvfFx8Brampqa+v3+BBXrx4MWrUKOQAtbW1Ur9ignjP69evUaGfOXNGQG727dtXWT8nCXuKFuLatWvLc3OjJk9Jm5126tQpmo2eaJt8cF78V69eTYqMHK6sEhQYGBIUjIe6qir+Sn0UiQ5JWFjYzZs3eU83bdq0cuXKuvr77pDsH3/8cfLkyeHh4d9+++348eMh+oaGhsgB0tLSoqOjJTvj0aNHcVJXV1d+KVq+fDlbKBqZQFJSkqOjY2ZmJnUc6DB8jIrPP6MOlMjPz+8///lPgyuAIhlQUFAwMjKi20gEQRASA5vx8hwr0OUme1k2lIX3FHKzYcMGD/fR7m5unh4eJSUlNMEA0VFpTPFnzZqlrKx84MABWMfbt2+hK+rq6tDu/Px8KDjKyL179yQ+KV6+ceNGFxcX5Am8JYMePXqEs1taWkZERDTWs59op3zsig+2bt3arVs3lDeBNwKJbEhICI4gPG8JQRAEQRCEZEA5bty4wVsjAuYNxYdeOzk5zZkzh3/P2bNn+/r63r9/f8+ePZzcbYTq4BSKioozZ84sKiqysrKC3Eu8iCfRliHFf9cpYurUqT/++KOXlxfy2gf1XLhwISAg4Pvvvw8ODqY7SQRBEARBcAXUok+fPrLv+c9//gPFf/jwobW1tcB4qurqalNTU857rLFRto6Ojlu3bqVVIDoqHVnx582bB8UXXomtoqKCX/Hr6hdqRlI7dOjQr7/+WllZWUVF5csvvxw4cCByXG7fHYIgCIIgPnJCQ0OTkpIWvycgIACK/+TJE3t7e4H7kr/99puVlVWDS/cQhGg6rOL/73//q6qqWr9+vfCocPzDO3bsOHnyJP/G169fV1ZWFhQUpNSTn5+PTIDWDyIIgiAIglsa7IsPb3FycoqJieHfc/r06UFBQTQgkJCADqv4koFS9Gc9VJwIgiAIgpAGjQ233bJly6BBg44dO/bmzZvXr1/v3r0bT8vLy1vvSol2DCk+QRAEQRBEyxEVFcU/wdT27dsLCwvr6u8zbtiwwcjIqFu3bt27dzc2NsafWu8yifYNKT5BEARBEETLcfHixVevXvGe3rt3r6amhvf07t27K1asKCgoePDgQWtcHdFBIMUnCIIgCIIgiA4FKT5BEARBEARBdChI8QmCIAiCIAiiQ0GKTxAEQRAEQRAdClJ8giAIgiAIguhQkOITBEEQBEEQRIeCFJ8gCIIgCIIgOhSk+ARBEARBEATRoSDFJwiCIAiCIIgOBSk+QRAEQRAEQXQoSPEJgiAIgiAIokNBik8QBEEQBEEQHQpSfIIgCIIgCILoUJDiEwRBEARBEESHghSfIAiCIAiCIDoUpPgEQRAEQRAE0aEgxScIgiAIgiCIDgUpPkEQBEEQBEF0KDhX/P8Hy55Dy6z4AKMAAAAASUVORK5CYII=" alt="CH20 p.40原圖，供結構與衍生化核對" width="760" />

</details>

**條件：**類固醇酯的位置異構次序需用 Q039 原圖及指定方法的經驗輸入，不從單一 OH 數強推。

**易錯：**「ortho 一定最極性、para 一定最不極性」不能普遍成立。

**閉卷自問：**chlorophenol 三異構物題選 adsorption，代表 RP 分配一定不能分開嗎？

<details>
<summary>收起答案與最短理由</summary>

不代表。Q025 是題本最適原理配對；實際鍵結相也能透過選擇性分離位置異構物。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q025|Q025｜111-1 #36]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q039|Q039｜110-1 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q061|Q061｜107-2 #13]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q096|Q096｜103-1 #35]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f03|F03]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f06|F06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f20|F20]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l07|同題複習卡]]；來源與用途站见本節掛載。

## L08｜矽膠接上 C18 後，為何仍可能拖尾？

^hplc-c-l08

**先問：**矽膠接上 C18 後，為何仍可能拖尾？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「鍵結基團、殘餘矽醇基、pH 與峰形」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「固定相選擇與拖尾候選原因」。

**短鏈：**殘餘表面與帶電分析物作用 → 保留不均／拖尾 → 封端或調整條件。

bonded phase（鍵結相）以共價鍵把基團接在矽膠上；沒有反應完的 Si–OH 仍可能與分析物作用。矽醇基解離為 Si–O⁻ 時，可吸引質子化胺 BH⁺。endcapping（封端）用小型矽烷試劑遮蔽殘餘作用位點，減少部分次級作用。

**立即用一次：**C18 可以分析鹼性藥物；看 pH、相穩定性及峰形。拖尾要查表面作用，也查過量進樣或樣品溶劑。

**條件：**高 pH 會威脅一般矽膠；封端不等於所有高 pH 都安全。聚合物核心須查溶劑膨潤與產品範圍。

**易錯：**Si–O⁻ 不是自由 OH⁻；含碳率不是殘餘矽醇基已封端百分率。

**閉卷自問：**aminopropyl、cyano、diol 出現時，能只由名稱宣告全是正相嗎？

<details>
<summary>收起答案與最短理由</summary>

不能。這些極性相可在 NP、RP 或 HILIC 等條件下使用，必須連同移動相判別。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q004|Q004｜113-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q018|Q018｜112-1 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q027|Q027｜111-1 #29]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q043|Q043｜109-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q055|Q055｜108-2 #12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q064|Q064｜107-2 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q088|Q088｜104-2 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q090|Q090｜104-1 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q102|Q102｜102-1 #35]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f04|F04]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f05|F05]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f21|F21]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|同題複習卡]]；來源與用途站见本節掛載。

## L09｜酸與鹼改 pH，保留為何常往相反方向？

^hplc-c-l09

**先問：**酸與鹼改 pH，保留為何常往相反方向？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「分析物為酸或鹼、pKa、移動相 pH 與 RP 模式」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「酸鹼題的保留方向」。

**短鏈：**pH 改解離比例 → 疏水保留改變 → tR 方向改變。

弱酸 HA 在 pH 上升時較多變 A⁻；弱鹼以 BH⁺ ⇌ B 討論，pH 上升時較多變成中性 B。常規 RP 中中性態通常比離子態保留強，所以酸升 pH 常較快，鹼升 pH 常較慢。

**立即用一次：**aspirin pKa 3.5：pH3→5 時酸解離增加，C18 tR 縮短；pentycaine pKa8.1 升 pH 則中性比例增加，不能拿來縮短 tR。

**條件：**近似要排除離子對、離子交換、溶解度或表面作用主導；同時保護樣品與管柱。

**易錯：**同一句「升 pH 會較快」不能同時套給酸與鹼。

**閉卷自問：**bupivacaine 從 pH9 改為 pH5，常規 RP 能延長 tR 嗎？

<details>
<summary>收起答案與最短理由</summary>

通常不能；變成較多 BH⁺，常縮短保留。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q024|Q024｜111-1 #30]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q034|Q034｜110-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q049|Q049｜109-1 #34]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q052|Q052｜108-2 #9]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q074|Q074｜106-1 #36]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q099|Q099｜102-2 #34]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c03|C03]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c04|C04]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09|同題複習卡]]；來源與用途站见本節掛載。

## L10｜pKa 附近的 pH 改變，為何特別值得注意？

^hplc-c-l10

**先問：**pKa 附近的 pH 改變，為何特別值得注意？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「pH 區間、pKa 及中性／離子態保留假設」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「變動大小的近似判斷」。

**短鏈：**比較區間與 pKa → 解離比例變化 → 判題定保留變化。

Henderson–Hasselbalch 式把 pH−pKa 變成兩態比。每差 1 個 pH，兩態比差 10 倍；pH=pKa 時各半。接近 pKa 時，中性比例對 pH 變動更敏感，遠離時常已幾乎在同一態。

**立即用一次：**ibuprofen pKa4.4：四個一單位區間中，4→5 跨過 pKa，題本選最大影響。procaine pKa9 在 pH8→7 兩端都以 BH⁺ 為主，Q007 選影響最小。

**條件：**比較不同藥物的 tR 改變還需要中性態、離子態各自保留；只靠 pKa 的大小不是精確數值證明。混合溶劑 pKa／pH 要同尺度。

**易錯：**ACN 加到乙酸緩衝液後的 pH，不能用「中性溶劑稀釋酸」一概推斷。

**閉卷自問：**弱鹼 pKa9，pH8、7 的 B:BH⁺ 各多少？

<details>
<summary>收起答案與最短理由</summary>

1:10、1:100；中性比例是 1/11、1/101。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q007|Q007｜113-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q041|Q041｜109-2 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q045|Q045｜109-2 #39]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q053|Q053｜108-2 #10]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f23|F23]]。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c03|C03]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c04|C04]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l10|同題複習卡]]；來源與用途站见本節掛載。

## L11｜移動相比例，怎樣轉成沖提強度？

^hplc-c-l11

**先問：**移動相比例，怎樣轉成沖提強度？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「模式、溶劑種類及明確的比例順序」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「較強／較弱沖提與 tR 順序」。

**短鏈：**先認強溶劑 → 換成分率 → 比保留方向。

eluotropic power（沖提力）指溶劑在特定固定相上帶出分析物的能力。NP 常增加能競爭矽膠表面的較極性溶劑；RP 常增加有機相比例；HILIC 常增加水比例。它不是只把介電常數或極性指數排大到小。

**立即用一次：**水:MeOH＝1:5 的 MeOH 分率5/6，高於1:3的3/4、1:2的2/3、1:1的1/2；題定C18下1:5最快。

**條件：**比例需看清先後，如 ACN/water 和 water/ACN 相反；溶劑種類改變也改選擇性，不能只看總有機百分率。

**易錯：**別把 NP 的強溶劑序直接套給 RP；甲醇、乙腈的氫鍵能力也不同。

**閉卷自問：**C18 題：ACN/water 30:70 與70:30，哪個通常較快？

<details>
<summary>收起答案與最短理由</summary>

70:30，ACN 多，RP 沖提較強。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q005|Q005｜113-2 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q021|Q021｜111-2 #30]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q023|Q023｜111-2 #36]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q035|Q035｜110-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q038|Q038｜110-1 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q067|Q067｜107-1 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q083|Q083｜105-2 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q085|Q085｜105-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q089|Q089｜104-2 #38]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f02|F02]]。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c01|C01]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|同題複習卡]]；來源與用途站见本節掛載。

## L12｜縮短分析時間，和改善分離，是同一件事嗎？

^hplc-c-l12

**先問：**縮短分析時間，和改善分離，是同一件事嗎？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「等度／梯度、流量、柱長、溫度與 Rs」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「有品質條件的操作調整」。

**短鏈：**改變通過時間或保留 → 讀 tR／峰寬／峰距 → 比時間與分離品質。

isocratic（等度）保持相組成；gradient（梯度）隨時間改變組成。RP 常增加有機相由弱到強沖提。提高流量、使用較短柱或較強沖提常加快，但可能犧牲分離；降低梯度斜率常讓近鄰峰更有機會分開。

**立即用一次：**同端點10%→70%有機相，10 min斜率6百分點/min；延至15 min斜率4百分點/min。Q084選延長1.5倍作較慢梯度。

**條件：**升溫常降黏度與背壓，保留與選擇性的方向取決於方法熱力學；題本常用加快的經驗，不可普遍化。

**易錯：**快並不證明 Rs 合格；梯度越慢也不保證每一組峰都更好。

**閉卷自問：**RP 增加水比例，能否當成一般縮短 diclofenac 分析時間的方法？

<details>
<summary>收起答案與最短理由</summary>

不能；常減弱沖提、延長保留，Q042 的反向選項是水增加。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q042|Q042｜109-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q084|Q084｜105-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q086|Q086｜105-1 #38]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f24|F24]]。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c02|C02]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c11|C11]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l12|同題複習卡]]；來源與用途站见本節掛載。

## L13｜陽離子交換樹脂為何帶負電？

^hplc-c-l13

**先問：**陽離子交換樹脂為何帶負電？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「固定基團電荷、分析物電荷、pH 與競爭離子」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「IEC 的保留與沖提方向」。

**短鏈：**相反電荷吸引 → pH／競爭鹽改作用 → 不同 tR。

ion-exchange chromatography（離子交換）名稱依「被交換的分析物」命名。陽離子交換相帶負電，抓陽離子；陰離子交換相帶正電，抓陰離子。提高沖提液中競爭離子常促使分析物離開；pH 同時影響分析物及弱交換基團。

**立即用一次：**–SO₃⁻ 是強陽離子交換；–COO⁻ 也抓陽離子，只是常屬弱陽交換。lysine 在題定升 pH 沖提中較能維持正電，最後出。

**條件：**強／弱指基團解離的 pH 行為，不是柱子分離一定強／弱。離子強度 I 與單一離子樹脂選擇性不同。

**易錯：**I 大不等於分析物總會被抓更強；原子序不在 I 的定義式內。

**閉卷自問：**陰離子在一般陽交換相會比有可比吸引的陽離子早還是晚？

<details>
<summary>收起答案與最短理由</summary>

通常早；同號／不保留者較早，仍看其他作用。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q016|Q016｜112-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q019|Q019｜112-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q072|Q072｜106-2 #32]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f07|F07]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f08|F08]]。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c05|C05]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l13|同題複習卡]]；來源與用途站见本節掛載。

## L14｜離子對試劑要與誰帶相反電荷？

^hplc-c-l14

**先問：**離子對試劑要與誰帶相反電荷？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「分析物在 pH 下的電荷及試劑疏水端」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「離子對試劑選擇與相對 tR」。

**短鏈：**反號作用／表面吸附 → 增加有效疏水保留 → RP 更能留住離子。

ion-pair chromatography（離子對）常在 RP 加入帶電且有疏水端的試劑。它可與分析物形成對離子作用，也可吸附於固定相造成動態離子交換。入門用「反號電荷＋疏水端」抓題意，實際不必完全等同中性離子對單一機制。

**立即用一次：**苯乙酸在能形成陰離子的條件下，用帶正電 tetrabutylammonium；酸性條件的苄胺 BH⁺ 用帶負電 alkylsulfonate。相同試劑類型中較長烷鏈常留更久。

**條件：**分析物須在方法條件下帶所需電荷；試劑濃度、吸附與柱平衡也會影響結果。

**易錯：**cationic ion-pair agent 是正電試劑，不是必然拿來抓正電分析物。

**閉卷自問：**四丁基銨可以與丁胺 BH⁺ 作題目的反號配對嗎？

<details>
<summary>收起答案與最短理由</summary>

不適合，兩者同正電；丁酸 A⁻ 才是該選項的對象。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q009|Q009｜113-1 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q014|Q014｜112-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q022|Q022｜111-2 #31]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q044|Q044｜109-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q057|Q057｜108-2 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q062|Q062｜107-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q080|Q080｜105-2 #12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q098|Q098｜102-2 #33]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f09|F09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f25|F25]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14|同題複習卡]]；來源與用途站见本節掛載。

## L15｜分子篩的大分子，為何反而先出？

^hplc-c-l15

**先問：**分子篩的大分子，為何反而先出？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「水動力尺寸、孔隙大小及有效分離範圍」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「SEC 的尺寸排序」。

**短鏈：**大者少進孔 → 可走體積較小 → 較早流出。

size-exclusion chromatography（尺寸排斥、分子篩）理想上藉可進入孔隙的體積分離。大分子進不了小孔，較直接走柱外空隙；小分子進孔較多，晚流出。分離的是溶液中的水動力尺寸，分子量對照校正仍受分子形狀影響。

**立即用一次：**hyaluronic acid 高分子分布題選 SEC。小胺基酸 phenylalanine 比大 collagen 能進更多孔，不能說小者一定先。

**條件：**選適當孔徑範圍並抑制次級吸附；GFC常水相，GPC可有機相。不是所有SEC固定相都不帶電或只用水。

**易錯：**大分子先出不是因為抓得更強；也不是全化學中只有SEC能有這種先後。

**閉卷自問：**兩個分子都大到完全不能進孔，SEC能保證分開嗎？

<details>
<summary>收起答案與最短理由</summary>

不能；都在排斥極限附近，需換孔徑範圍或其他方法。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q031|Q031｜110-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q091|Q091｜104-1 #36]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f10|F10]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l15|同題複習卡]]；來源與用途站见本節掛載。

## L16｜HILIC 為何用高有機相，卻留住親水物？

^hplc-c-l16

**先問：**HILIC 為何用高有機相，卻留住親水物？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「親水表面、高有機／少量水相及電荷條件」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「HILIC 的模式與題圖次序」。

**短鏈：**親水層／表面作用 → 親水物較易保留 → 加水常較快沖出。

hydrophilic interaction liquid chromatography（親水性交互作用層析）用親水固定相及富有機的水混合移動相。分析物可分配入表面富水層，也可有吸附或離子交換作用，所以常呈接近正相的親水保留。ZIC-HILIC 只是兩性離子相的一類。

**立即用一次：**Q008原圖的短→長為phenylalanine、tyrosine、threonine、serine、arginine；峰D是serine。題定HILIC加水常減少保留，與常規RP方向相反。

**條件：**需要足夠水形成與平衡相關層、溶解緩衝鹽；不是100%有機就一定最好。保留序依具體相、pH與鹽。

**易錯：**Ascorbic acid不是thiol；GSSG是disulfide，不把三者統稱硫醇。

**閉卷自問：**HILIC可含帶電固定基團，強酸／強鹼分析物是否可能另有離子交換作用？

<details>
<summary>收起答案與最短理由</summary>

可能，這就是Q011選D的原因。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q008|Q008｜113-1 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q011|Q011｜112-2 #28]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f11|F11]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l16|同題複習卡]]；來源與用途站见本節掛載。

## L17｜鏡像異構物，靠什麼產生保留差異？

^hplc-c-l17

**先問：**鏡像異構物，靠什麼產生保留差異？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「對映異構物與可作用的對掌環境」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「對掌性方法的可用性」。

**短鏈：**與手性環境作用不同 → 自由能／保留不同 → 對映峰分開。

enantiomers（對映、鏡像異構物）在非手性環境多有相同物性。可用手性固定相、手性移動相添加物，或先與手性試劑衍生成非對映異構物。三點作用模型包含氫鍵、π作用與立體限制，是辨識教學模型，不是「三點成面」即證明分離。

**立即用一次：**Pirkle、cyclodextrin 是題本配對；cetrimide 是一般陽離子對試劑，並不提供所需手性。Labetalol四種組態是兩對對映體，不是四者互為鏡像。

**條件：**普通C18本身沒有手性識別；手性serine添加仍須具體方法驗證。手性crown ether確實可作分離相。

**易錯：**Q017 的未限定crown ether不能外推成所有冠醚都不具對掌分離。

**閉卷自問：**要直接分離D/L-alanine，題本Pirkle與裸silica、ODS相比選誰？

<details>
<summary>收起答案與最短理由</summary>

Pirkle；本題原印alanine前缺字，D/L由題意與舊講義補充，不冒充原印。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q003|Q003｜113-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q017|Q017｜112-1 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q030|Q030｜111-1 #40]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q079|Q079｜106-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q100|Q100｜102-2 #37]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f12|F12]]。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17|同題複習卡]]；來源與用途站见本節掛載。

## L18｜衍生化，是把分析物的哪個弱點補起來？

^hplc-c-l18

**先問：**衍生化，是把分析物的哪個弱點補起來？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「原分析物的偵測／分離弱點及反應產率」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m03|M03]]使用「衍生物的分離與偵測」。

**短鏈：**接上合適基團 → 改偵測或保留 → 可辨識的產物訊號。

derivatization（衍生化）是把分析物反應成另一種可分析形式。可導入UV發色基或螢光基、改善分離，或在特定反應下改善穩定性。它增加反應步驟，須核對反應完整度、回收、產物穩定性、空白與過量試劑。

**立即用一次：**neomycin與fluorodinitrobenzene反應後可UV偵測；題定silica條件下降低極性、減少過強表面作用，避免拖尾。Q097的「增加管柱作用」錯。

<details>
<summary>原圖輔助：比較結構／反應</summary>

<img src="data:image/png;base64,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/ri+qqqqqspaenEcx7j0asveZV39BEEIBoOhUOjMM88866zTACArK8swwDRtv1/kOM4iVrdu3dhXAgEPY7DRNCsQ8CSTQcuyIpEIpaDrRJbls846a9CgQW63u2XLllOnTkUk777z4dh7xiqKsm7dplWrVufn5yNgdnagrCzi8XhYNm6HDh3mz5/bv3//8ePHU0qeffbZp59+WtO0eDzJapxqhCAI7CFm8QLWgJznGRsnTwnYts16FhsGcbkERHQGn3U3c+5sLeABQFVVQRAczuIUjzhHR48e3atXL0pBUfjjjz+udevWmkavuOKKK6+8+PjjB4TDYdOEiy66qFu3bn6/3KVLu9dfez0cDns8MpM7n2+X25+wImtIJS/ziMjqvVRV9Xg86W3aNU1jowH/gfvsIMUeE/tawdWcdFGFiHZn5tdg0H/yySffe++9s2fPHjBggCjKdfRsEwTOMCxFkVq3bvn888+fcsopX3/99eLFi+fMmW2aFhMkURQFQWBenNp6TkuSxLL6S0pKEHH9+vUVFYlRo0Y98eTj3bt3HzjwxL/+mn/DDdd3bN+xQYMGzrfYs8Wmktzc3OHDh3/00UevvPJ6jx7/+/DDD//+++9BgwYVFW91uVxZWQGXS1BcUsAXuOyyS1atWuPz+TmOcyvu/v0HjBkzhuPw5ptvbtG8xbnnnv3555+aplmvXjYAxGIxQkleXp7f72VX+q8DWAW2TXmO93q9sixHo1GXS4hGk8EsLwDjCAdJUnjeAuArbR3K3qe9gqYlvV6v055I0wwAUBSF4yA3N/uCCy7IysrSddPjkU855RRJ4gChQYP6/fsPDgYDzz//vCzDlVde6fYAAOg6ueKKSwgBVTU9HjkUing8Hmcq30k4kRSe55kwM4JjJvOMEi4ej/v9fkfmD0PsfbGHnYgJcQgc8/wiQM1a17apKPKNGjUKBALTp08nhFAKul5XJwxFkVhpKgD069fn+OOPtSwCyDMqW8ZX8a8lOqZp5ufnEAK6rrMlX06O76abbli4cP61113tcrnYpDDu8SeDQdGyQZLAJlRxicABxyNwIMvc1VdftW3b1tFjriuoV2jb9pgx15122qm//z41NzcXABChfv2CRo0bFBUVPf30k9nZuTfccMNTTz153ejrFi1aJAicP+B9/PFHW7RooarJXr16WRZIErRt23bASQMs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fCymRyIRRVFisZjf72czqeDk6zimOOJk7/FIhkHcbjErK+uP+X/897//FQQhHAm3aN6iffv2+fn5mzZvmjFjhqIqfp8fANxut22bV1xx+XfffXf55ZeOHDly164dpqnruur1ul0uAOA9nrRo1FNcXGSYxqZNmzhOiEQiXre3rKysuLgqEAgQArt3F6dnpHq9blEU2SzLsk3V1ZIqOXkOTdSHAgAnC9pRhiyLFRVVGelppkmLiopMy7z++uvPOeecqqrwtm070tIyKAXLIlVVMZ/PV1UV3rx5q66bhOLo0ZdOnnyvptHevXtv3LgpeQpjoIkqUbB3BO4JVp8M1ktsxc7SNLpcLpbiXpZlZyXPBqFz5rHCEWdNMUV1uQRKYevWrY0bNf7tt9+WLFkyYfyEdevXzZs3b926df379S8rK0Nq3XHHHQCwc+fOtLS03Nzchx56qLik+M033+zevXtOTk44HK6srCQEKioiL730+l133bVq1SpZkj/44IO1a9euW7dOklyapuXmpD399NOdOnV95JFH5/wylxIAAI7jCUE219bho9XMonFsKYGxekHg3W53p46dsrOzJ02aFA6H3W63pmmCIEydOvXqq68ePXr0559/HggEDMOQJfmnn376z3+mXHXVVRs3bnS73V6vlwWlUkoJAURgCeEJIdUe7ohWszjuwER31kVsipQkzufzeb1e9l6c+ZTVgD+mjT3yZO/3e4EDjoe09BRR4lPTgjm5WZ06nyRJgqYrBfXycvOyFTVqmJYgcsFAMDMzc+vWrbIst27datK9k8KRcElJSe/evU899dQWLVtMn/7eDz/8cN3113Ec165dO0JIgwYN0tNdgUAgHA3n5+cvXLjqow8/eeWVV2bM+HHduvWqagACsUEQpFqSmh0mnLfIcicJgiCK4mGUMagrUAqBgE9RDEEASmnz5s0ff/zxjz76aPny5RnpWSzNbnlZJVKO2GgadjgUrawImZb954KFL7/06scffaoqeocOHRxtMyRVcYF4lRWoSfnH4FH/qXCmQUb2hABTADNf5oS49I/osaMxTGMx1e/3nn322Rs2bMjOzna7XZ06dercubOu6y1btuzXr196ejrPQ5cuXVq1bpGXl3vttdc2atRI140HH5y0bt0627br18+95557BEG4//77RVEcMXzEhAkTLMs69dRTysrKmjYt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" alt="CH20 p.40原圖，供結構與衍生化核對" width="760" />

</details>

**條件：**不是所有衍生化都降低極性或提高穩定性。柱前／柱後位置依目的；柱後反應常為增加偵測響應。

**易錯：**導入缺乏發色基的醣，不會自動解決無UV訊號。

**閉卷自問：**有合適ELSD能直接測未衍生化醣，是否必須先衍生化？

<details>
<summary>收起答案與最短理由</summary>

不必；先比較直接法與反應步驟的收益及誤差。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q002|Q002｜114-1 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q097|Q097｜103-1 #36]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f13|F13]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l18|同題複習卡]]；來源與用途站见本節掛載。

## L19｜UV 和 DAD 怎樣把流出物變成訊號？

^hplc-c-l19

**先問：**UV 和 DAD 怎樣把流出物變成訊號？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m03|M03]]取用「分析物吸收、選定波長及校正」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「吸光度訊號及有限的光譜證據」。

**短鏈：**光吸收隨流出改變 → 吸光度峰／光譜 → 定量或支持比對。

UV/Vis detector 量光吸收。DAD（diode array detector，光二極體陣列）可取得一段波長的吸收資訊，對多種吸光成分及光譜比對有用。量測吸收需要分析物在條件下有足夠發色性；UV不是全通用。

**立即用一次：**混合物各有不同吸收波長，Q093選DAD；mannitol沒有可供常規直接UV靈敏測定的強發色基，Q073排UV。

**條件：**UV常見氘燈供UV、鎢燈供可見；具體光源隨儀器。DAD光譜／峰純度支持專一性，但非未知結構唯一證明。

**易錯：**看得見吸收峰不等於已知道藥物身分；改波長也可能改響應因子。

**閉卷自問：**aspirin題選「UV通常氙燈」為正確敘述嗎？

<details>
<summary>收起答案與最短理由</summary>

題本不選。常見UV來源為氘燈；氙燈常見於螢光激發，仍看產品。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q029|Q029｜111-1 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q093|Q093｜103-2 #35]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f14|F14]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l19|同題複習卡]]；來源與用途站见本節掛載。

## L20｜螢光選擇性，為何常比單純 UV 高？

^hplc-c-l20

**先問：**螢光選擇性，為何常比單純 UV 高？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m03|M03]]取用「激發波長、發射波長及分析物螢光特性」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「螢光訊號與適用分析物」。

**短鏈：**能被激發且放出螢光 → 選發射光 → 較少背景干擾。

fluorescence detector（螢光偵測）先用激發光，再讀另一波長的發射光。不是所有會吸收的分子都有效放螢光，增加這道條件常帶來較高選擇性。剛性與共軛有利於部分分子，但不能保證每個剛性分子都發螢光。

**立即用一次：**Riboflavin（B2）與aflatoxins題本選HPLC-fluorescence；若分析B1，有方法先氧化成thiochrome再測，不能一概說未處理B1就是同樣的天然螢光配對。

**條件：**靈敏度取決於化合物、量子產率、淬熄、波長、基質與儀器；必背排序只是題本常用比較。

**易錯：**sensitivity是低量能不能辨；selectivity是能否分辨目標與干擾；robustness是小幅條件變動仍穩定。

**閉卷自問：**UV相較FL，本題給robustness、selectivity、sensitivity，選何優勢？

<details>
<summary>收起答案與最短理由</summary>

Q046選robustness較佳；不是UV在所有方法都更靈敏。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q033|Q033｜110-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q036|Q036｜110-1 #26]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q046|Q046｜109-2 #40]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q082|Q082｜105-2 #33]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f14|F14]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f17|F17]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l20|同題複習卡]]；來源與用途站见本節掛載。

## L21｜電化學、PAD 與電導，讀的是同一種量嗎？

^hplc-c-l21

**先問：**電化學、PAD 與電導，讀的是同一種量嗎？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m03|M03]]取用「可氧化還原基團、電位控制或離子導電」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「電流或電導訊號與方法配對」。

**短鏈：**選電位測電流／量離子導電 → 分清機制與訊號 → 選適用偵測。

HPLC的ECD是electrochemical detector（電化學），常量分析物在電極氧化還原形成的電流。PAD是pulsed amperometric detection（脈衝安培偵測），變換電位並量電流，能更新表面、用於醣等。電導偵測量溶液導電，常用於離子層析的無機離子。

**立即用一次：**Adrenaline有catechol可氧化，Q095選電化學；氯離子Q060選ion chromatography，常配抑制型電導，不直接指定PAD。

**條件：**電流常nA；電導常µS。電極、溶劑、pH、鹽與電位窗口要相容。糖在適當鹼性／電極PAD條件可檢測。

**易錯：**GC的electron capture detector也縮寫ECD，但它是電子捕捉，與液相電化學不同。

**閉卷自問：**題目問非HPLC檢測器，electron capture和electrochemical如何選？

<details>
<summary>收起答案與最短理由</summary>

排electron capture，它是本題的GC電子捕捉配對。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060|Q060｜107-2 #12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q078|Q078｜106-1 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q095|Q095｜103-1 #11]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f08|F08]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f26|F26]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l21|同題複習卡]]；來源與用途站见本節掛載。

## L22｜沒發色基，怎麼選 RI、ELSD 或 CAD？

^hplc-c-l22

**先問：**沒發色基，怎麼選 RI、ELSD 或 CAD？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m03|M03]]取用「分析物揮發性、移動相與是否梯度」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「不靠發色基的讀數選擇」。

**短鏈：**折射差／殘留微粒／粒子電荷 → 訊號 → 適用範圍與校正。

RI比樣品流與參考流折射率，需穩定溫度與組成，梯度易改基線。ELSD霧化流出液、蒸發移動相，再讀殘留粒子散射。CAD也先生成粒子，再以corona discharge（電暈放電）產生帶電氣體，讀粒子電荷的電流。

**立即用一次：**未衍生化醣、PEG、非離子界面活性劑題選ELSD；梯度題排RI。UDCA缺乏強常規UV吸收，題本選ELSD。

**條件：**ELSD/CAD要求分析物相對不揮發且移動相、添加物相容；不可用大量不揮發鹽。可配梯度但響應仍可隨組成變動，須校正。

**易錯：**「通用」表示不局限發色基，並非所有物質、條件、濃度都相同響應。

**閉卷自問：**分析物比移動相更容易揮發，ELSD可靠保證可測嗎？

<details>
<summary>收起答案與最短理由</summary>

不能，分析物可能一起蒸發，殘留粒子不足。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q001|Q001｜114-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q013|Q013｜112-2 #36]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q028|Q028｜111-1 #31]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q051|Q051｜109-1 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q063|Q063｜107-2 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q073|Q073｜106-2 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q075|Q075｜106-1 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q092|Q092｜103-2 #30]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f15|F15]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f17|F17]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22|同題複習卡]]；來源與用途站见本節掛載。

## L23｜峰面積，怎麼變成可信的濃度？

^hplc-c-l23

**先問：**峰面積，怎麼變成可信的濃度？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m03|M03]]取用「校正、稀釋、樣品面積與內標加入時點」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「濃度、單位與可補償的誤差」。

**短鏈：**用標準建關係 → 外標面積／內標比值 → 回算濃度及品質。

external standard（外標）以已知濃度建立面積關係，再回算樣品。internal standard（內標）加入固定量的另一個成分，用分析物／內標面積比校正；若注入量等共同乘法誤差同時影響兩者，比值可以抵消。內標須穩定、不反應、可辨別且適用於該檢品。

**立即用一次：**乳酸內標題選丙酸；tR宜近但峰不能重疊。若要補償萃取損失，內標要在該步驟前加入且經歷相近回收。

**條件：**不保證所有偵測器誤差、基質或回收偏差都抵消。R²高不夠，還看殘差、準確度、精密度、範围、專一性等。

**易錯：**MIC10、疑慮50µg/mL是題目資料，不當成臨床用藥建議；檢量範圍需涵蓋關鍵區域，非越寬越好。

**閉卷自問：**標準比值1對應10µg/mL，樣品比值2且截距0，原稀釋4倍，原濃度多少？

<details>
<summary>收起答案與最短理由</summary>

測得20µg/mL，乘4＝80µg/mL；前提同內標濃度及已驗證比例關係。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q006|Q006｜113-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q015|Q015｜112-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q066|Q066｜107-1 #13]]。

<details>
<summary>更多同型題</summary>

[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q068|Q068｜107-1 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q076|Q076｜106-1 #32]]

</details>

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f18|F18]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f27|F27]]。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c06|C06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c07|C07]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c08|C08]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23|同題複習卡]]；來源與用途站见本節掛載。

## L24｜小粒徑提高效率，為何同時要更高壓？

^hplc-c-l24

**先問：**小粒徑提高效率，為何同時要更高壓？

**掛載：**[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m02|M02]]取用「粒徑、柱長、內徑、F／u與板高」→本節→[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-m04|M04]]使用「效率與壓力的有條件比較」。

**短鏈：**細粒減少路徑／質傳展寬 → H下降 → 同L時N增，但阻力增。

UHPLC是超高效液相的通稱，UPLC是題本常用名稱及商標系統用語。粒徑變小可減少多路徑與質傳展寬，常容許較高線性速度；壓力需求上升。Van Deemter簡式H=A+B/u+Cu，H是板高；總板數N=L/H。

**立即用一次：**同L，H由20變10µm，N加倍；若L也減半，N可不變。相同黏度、柱長與線性速度的近似下，dp減半背壓約4倍。

**條件：**B係數與溶液縱向擴散相關，細粒不直接改變它；改u仍會改B/u項。F相同但內徑變小，u會改，效率不一定上升。

**易錯：**固定相粒徑≠柱內徑；短柱≠總板數一定增；1.7µm只是歷史例子。

**閉卷自問：**Q101問細粒不直接降低哪種展寬，選B/u所代表的什麼？

<details>
<summary>收起答案與最短理由</summary>

縱向擴散；注意不代表換u後B/u的數值也固定。

</details>

做題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q012|Q012｜112-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q020|Q020｜111-2 #27]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q101|Q101｜102-1 #30]]。

必背配對：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f19|F19]]。

紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c09|C09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c12|C12]]。

回跳：[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l24|同題複習卡]]；來源與用途站见本節掛載。

## 全章分類：不要把不同軸混成互斥名單

^hplc-c-methods

| 分類軸 | 本章項目 | 為什麼不能混在同一排 |
|---|---|---|
|主要保留機制|adsorption吸附、partition分配、IEC、SEC、手性作用；可兼具多作用|鍵結相也可兼具表面與分配，HILIC也可兼IEC|
|固定相／移動相配置|NP、RP、HILIC|名稱須看兩相和比例，不只一個基團|
|加試劑／改分子|ion-pair、derivatization|離子對是相中试劑；衍生化是化學反應|
|沖提程序|isocratic等度、gradient梯度|可套於多種模式，不是新的固定相|
|硬體效率|HPLC、UHPLC／題本UPLC|細粒與系統壓力／展寬，不另決定酸鹼保留方向|
|偵測與定量|UV、DAD、FL、EC、PAD、conductivity、RI、ELSD、CAD；外標／內標|分離決定何時出，偵測決定如何看见，校正決定怎么回算|

| 模式 | M01用途 | M02條件與作用 | M03量／單位 | M04判讀及回查 |
|---|---|---|---|---|
|P01 正相 NP|按表面作用比較分離|極性固定相（如裸silica）；相對低極性移動相。 吸附／極性表面作用；較強表面作用者常晚。|tR與峰面積，先給軸及校正。 tR用min；面積依偵測器積分。|低極性者常先出；增加合適強溶劑常縮短保留。 [[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05\|L05]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07\|L07]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]|
|P02 逆相 RP|一般小分子／題定蛋白疏水差異|C18/C8/phenyl等疏水相；常水＋有機相。 疏水保留為主，可兼有表面次級作用。|tR、k′；定量讀校正面積。 tR用min；面積依偵測器積分。|中性疏水者常晚；有機相增加常較快，酸鹼另判。 [[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06\|L06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10\|L10]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12\|L12]]|
|P03 離子交換 IEC／IC|可帶電物與無機離子|帶電交換相；控制pH與競爭鹽。 反號電荷作用；鹽與解離改保留。|tR；電導／電流或其他相容偵測。 tR用min；面積依偵測器積分。|依被交換離子命名；競爭鹽常促沖提。 [[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13\|L13]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21\|L21]]|
|P04 離子對 RP|改善可離子化物的RP保留|RP相＋反號、具疏水端的試劑。 對離子與表面動態作用，可增加離子物保留。|相對tR、分離與校正響應。 tR用min；面積依偵測器積分。|先看分析物電荷，再選反號；同族較長尾常更留。 [[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]|
|P05 尺寸排斥 SEC|高分子尺寸與分布|孔徑適當、抑制次級吸附；水相或有機相依方法。 水動力尺寸決定可進孔的體積。|流出時間／體積、尺寸校正。 tR用min；面積依偵測器積分。|大者少進孔先出；超出孔徑範圍者難分。 [[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15\|L15]]|
|P06 親水作用 HILIC|親水物在RP留不住時的候選|親水相＋富有機、含水移動相。 富水層分配＋吸附／可能IEC。|tR；pH、含水與鹽需紀錄。 tR用min；面積依偵測器積分。|親水者常更留，水增加常強沖提；不是普通RP。 [[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16\|L16]]|
|P07 對掌性分離|對映異構物比例／分離|手性固定相／添加物，或手性衍生化。 不等的手性作用造成保留差。|對映峰的tR、Rs和各自面積。 tR用min；面積依偵測器積分。|非手性C18不自動分；冠醚需具有手性辨識。 [[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17\|L17]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18\|L18]]|

### 圖3｜全章方法分類與大小循環對照圖

<details>
<summary>展開向量圖</summary>

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="4400" viewBox="0 0 1900 4400" role="img" aria-labelledby="hplc3_g3_title hplc3_g3_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="hplc3_g3_title">HPLC｜全章方法分類與大小循環對照</title><desc id="hplc3_g3_desc">高效能液相層析教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊；藍線表示圖4液體流路，灰線表示訊號／分析資訊。座標曲線依各子圖標示。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="4400" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH20 / HPLC / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">HPLC｜全章方法分類與大小循環對照</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">先看分類軸，再讓每種模式走同一個 M01 → M02 → M03 → M04。</text>
<rect x="50" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="71" y="246" font-size="27" font-weight="600" fill="#24343f">M01｜先定問題</text>
<text x="71" y="288" font-size="23" font-weight="400" fill="#24343f">目的與檢品</text>
<polyline points="470,262 506,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="506.0,262.0 494.6,268.2 494.6,255.8" fill="#61717a"/>
<rect x="510" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="531" y="246" font-size="27" font-weight="600" fill="#24343f">M02｜準備與測量</text>
<text x="531" y="288" font-size="23" font-weight="400" fill="#24343f">製樣、作用與條件</text>
<polyline points="930,262 966,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="966.0,262.0 954.6,268.2 954.6,255.8" fill="#61717a"/>
<rect x="970" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="991" y="246" font-size="27" font-weight="600" fill="#24343f">M03｜讀訊號</text>
<text x="991" y="288" font-size="23" font-weight="400" fill="#24343f">量、單位與處理</text>
<polyline points="1390,262 1426,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1426.0,262.0 1414.6,268.2 1414.6,255.8" fill="#61717a"/>
<rect x="1430" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1451" y="246" font-size="27" font-weight="600" fill="#24343f">M04｜核對結論</text>
<text x="1451" y="288" font-size="23" font-weight="400" fill="#24343f">判讀、限制與品質</text>
<rect x="50" y="365" width="1800" height="245" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="406" font-size="27" font-weight="600" fill="#9e771c">分類軸先分開｜名稱不是同一層的互斥選項</text>
<text x="72" y="454.34" font-size="24" font-weight="400" fill="#24343f">保留機制：吸附／分配／IEC／SEC／手性作用，可有多重作用。</text>
<text x="72" y="488.42" font-size="24" font-weight="400" fill="#24343f">相配置：NP／RP／HILIC；加試劑／改分子：離子對／衍生化。</text>
<text x="72" y="522.5" font-size="24" font-weight="400" fill="#24343f">程序：等度／梯度；效率硬體：HPLC／UHPLC；讀數：偵測器＋校正。</text>
<rect x="50" y="680" width="1800" height="365" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="70" y="723" font-size="29" font-weight="600" fill="#24343f">P01｜正相 NP</text>
<rect x="70" y="753" width="410" height="270" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="92" y="794" font-size="27" font-weight="600" fill="#9e771c">M01｜先定問題</text>
<text x="92" y="842.34" font-size="23" font-weight="400" fill="#24343f">表面作用差異</text>
<text x="92" y="875" font-size="23" font-weight="400" fill="#24343f">L05、L07、L11</text>
<polyline points="480,879 510,879" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="510.0,879.0 498.6,885.2 498.6,872.8" fill="#61717a"/>
<rect x="510" y="753" width="410" height="270" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="532" y="794" font-size="27" font-weight="600" fill="#286c68">M02｜準備與測量</text>
<text x="532" y="842.34" font-size="23" font-weight="400" fill="#24343f">極性固定相（如裸silica）；相對低</text>
<text x="532" y="875" font-size="23" font-weight="400" fill="#24343f">極性移動相。</text>
<text x="532" y="907.66" font-size="23" font-weight="400" fill="#24343f">吸附／極性表面作用；較強表面作</text>
<text x="532" y="940.32" font-size="23" font-weight="400" fill="#24343f">用者常晚。</text>
<polyline points="920,879 950,879" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="950.0,879.0 938.6,885.2 938.6,872.8" fill="#61717a"/>
<rect x="950" y="753" width="410" height="270" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="972" y="794" font-size="27" font-weight="600" fill="#326991">M03｜讀訊號</text>
<text x="972" y="842.34" font-size="23" font-weight="400" fill="#24343f">tR與峰面積，先給軸及校正。</text>
<text x="972" y="875" font-size="23" font-weight="400" fill="#24343f">時間min；積分面積依偵測器。</text>
<polyline points="1360,879 1390,879" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1390.0,879.0 1378.6,885.2 1378.6,872.8" fill="#61717a"/>
<rect x="1390" y="753" width="410" height="270" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="1412" y="794" font-size="27" font-weight="600" fill="#356844">M04｜核對結論</text>
<text x="1412" y="842.34" font-size="23" font-weight="400" fill="#24343f">低極性者常先出；增加合適強溶劑</text>
<text x="1412" y="875" font-size="23" font-weight="400" fill="#24343f">常縮短保留。</text>
<rect x="50" y="1075" width="1800" height="365" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="70" y="1118" font-size="29" font-weight="600" fill="#24343f">P02｜逆相 RP</text>
<rect x="70" y="1148" width="410" height="270" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="92" y="1189" font-size="27" font-weight="600" fill="#9e771c">M01｜先定問題</text>
<text x="92" y="1237.34" font-size="23" font-weight="400" fill="#24343f">疏水性／一般小分子</text>
<text x="92" y="1270" font-size="23" font-weight="400" fill="#24343f">L06、L08、L09、L10、L11、L12</text>
<polyline points="480,1274 510,1274" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="510.0,1274.0 498.6,1280.2 498.6,1267.8" fill="#61717a"/>
<rect x="510" y="1148" width="410" height="270" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="532" y="1189" font-size="27" font-weight="600" fill="#286c68">M02｜準備與測量</text>
<text x="532" y="1237.34" font-size="23" font-weight="400" fill="#24343f">C18/C8/phenyl等疏水相；常水＋有</text>
<text x="532" y="1270" font-size="23" font-weight="400" fill="#24343f">機相。</text>
<text x="532" y="1302.66" font-size="23" font-weight="400" fill="#24343f">疏水保留為主，可兼有表面次級作</text>
<text x="532" y="1335.32" font-size="23" font-weight="400" fill="#24343f">用。</text>
<polyline points="920,1274 950,1274" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="950.0,1274.0 938.6,1280.2 938.6,1267.8" fill="#61717a"/>
<rect x="950" y="1148" width="410" height="270" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="972" y="1189" font-size="27" font-weight="600" fill="#326991">M03｜讀訊號</text>
<text x="972" y="1237.34" font-size="23" font-weight="400" fill="#24343f">tR、k′；定量讀校正面積。</text>
<text x="972" y="1270" font-size="23" font-weight="400" fill="#24343f">時間min；積分面積依偵測器。</text>
<polyline points="1360,1274 1390,1274" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1390.0,1274.0 1378.6,1280.2 1378.6,1267.8" fill="#61717a"/>
<rect x="1390" y="1148" width="410" height="270" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="1412" y="1189" font-size="27" font-weight="600" fill="#356844">M04｜核對結論</text>
<text x="1412" y="1237.34" font-size="23" font-weight="400" fill="#24343f">中性疏水者常晚；有機相增加常較</text>
<text x="1412" y="1270" font-size="23" font-weight="400" fill="#24343f">快，酸鹼另判。</text>
<rect x="50" y="1470" width="1800" height="365" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="70" y="1513" font-size="29" font-weight="600" fill="#24343f">P03｜離子交換 IEC／IC</text>
<rect x="70" y="1543" width="410" height="270" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="92" y="1584" font-size="27" font-weight="600" fill="#9e771c">M01｜先定問題</text>
<text x="92" y="1632.34" font-size="23" font-weight="400" fill="#24343f">帶電物與無機離子</text>
<text x="92" y="1665" font-size="23" font-weight="400" fill="#24343f">L13、L21</text>
<polyline points="480,1669 510,1669" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="510.0,1669.0 498.6,1675.2 498.6,1662.8" fill="#61717a"/>
<rect x="510" y="1543" width="410" height="270" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="532" y="1584" font-size="27" font-weight="600" fill="#286c68">M02｜準備與測量</text>
<text x="532" y="1632.34" font-size="23" font-weight="400" fill="#24343f">帶電交換相；控制pH與競爭鹽。</text>
<text x="532" y="1665" font-size="23" font-weight="400" fill="#24343f">反號電荷作用；鹽與解離改保留。</text>
<polyline points="920,1669 950,1669" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="950.0,1669.0 938.6,1675.2 938.6,1662.8" fill="#61717a"/>
<rect x="950" y="1543" width="410" height="270" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="972" y="1584" font-size="27" font-weight="600" fill="#326991">M03｜讀訊號</text>
<text x="972" y="1632.34" font-size="23" font-weight="400" fill="#24343f">tR；電導／電流或其他相容偵測。</text>
<text x="972" y="1665" font-size="23" font-weight="400" fill="#24343f">時間min；積分面積依偵測器。</text>
<polyline points="1360,1669 1390,1669" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1390.0,1669.0 1378.6,1675.2 1378.6,1662.8" fill="#61717a"/>
<rect x="1390" y="1543" width="410" height="270" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="1412" y="1584" font-size="27" font-weight="600" fill="#356844">M04｜核對結論</text>
<text x="1412" y="1632.34" font-size="23" font-weight="400" fill="#24343f">依被交換離子命名；競爭鹽常促沖</text>
<text x="1412" y="1665" font-size="23" font-weight="400" fill="#24343f">提。</text>
<rect x="50" y="1865" width="1800" height="365" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="70" y="1908" font-size="29" font-weight="600" fill="#24343f">P04｜離子對 RP</text>
<rect x="70" y="1938" width="410" height="270" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="92" y="1979" font-size="27" font-weight="600" fill="#9e771c">M01｜先定問題</text>
<text x="92" y="2027.34" font-size="23" font-weight="400" fill="#24343f">改善離子物RP保留</text>
<text x="92" y="2060" font-size="23" font-weight="400" fill="#24343f">L14</text>
<polyline points="480,2064 510,2064" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="510.0,2064.0 498.6,2070.2 498.6,2057.8" fill="#61717a"/>
<rect x="510" y="1938" width="410" height="270" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="532" y="1979" font-size="27" font-weight="600" fill="#286c68">M02｜準備與測量</text>
<text x="532" y="2027.34" font-size="23" font-weight="400" fill="#24343f">RP相＋反號、具疏水端的試劑。</text>
<text x="532" y="2060" font-size="23" font-weight="400" fill="#24343f">對離子與表面動態作用，可增加離</text>
<text x="532" y="2092.66" font-size="23" font-weight="400" fill="#24343f">子物保留。</text>
<polyline points="920,2064 950,2064" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="950.0,2064.0 938.6,2070.2 938.6,2057.8" fill="#61717a"/>
<rect x="950" y="1938" width="410" height="270" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="972" y="1979" font-size="27" font-weight="600" fill="#326991">M03｜讀訊號</text>
<text x="972" y="2027.34" font-size="23" font-weight="400" fill="#24343f">相對tR、分離與校正響應。</text>
<text x="972" y="2060" font-size="23" font-weight="400" fill="#24343f">時間min；積分面積依偵測器。</text>
<polyline points="1360,2064 1390,2064" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1390.0,2064.0 1378.6,2070.2 1378.6,2057.8" fill="#61717a"/>
<rect x="1390" y="1938" width="410" height="270" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="1412" y="1979" font-size="27" font-weight="600" fill="#356844">M04｜核對結論</text>
<text x="1412" y="2027.34" font-size="23" font-weight="400" fill="#24343f">先看分析物電荷，再選反號；同族</text>
<text x="1412" y="2060" font-size="23" font-weight="400" fill="#24343f">較長尾常更留。</text>
<rect x="50" y="2260" width="1800" height="365" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="70" y="2303" font-size="29" font-weight="600" fill="#24343f">P05｜尺寸排斥 SEC</text>
<rect x="70" y="2333" width="410" height="270" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="92" y="2374" font-size="27" font-weight="600" fill="#9e771c">M01｜先定問題</text>
<text x="92" y="2422.34" font-size="23" font-weight="400" fill="#24343f">高分子尺寸與分布</text>
<text x="92" y="2455" font-size="23" font-weight="400" fill="#24343f">L15</text>
<polyline points="480,2459 510,2459" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="510.0,2459.0 498.6,2465.2 498.6,2452.8" fill="#61717a"/>
<rect x="510" y="2333" width="410" height="270" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="532" y="2374" font-size="27" font-weight="600" fill="#286c68">M02｜準備與測量</text>
<text x="532" y="2422.34" font-size="23" font-weight="400" fill="#24343f">孔徑適當、抑制次級吸附；水相或</text>
<text x="532" y="2455" font-size="23" font-weight="400" fill="#24343f">有機相依方法。</text>
<text x="532" y="2487.66" font-size="23" font-weight="400" fill="#24343f">水動力尺寸決定可進孔的體積。</text>
<polyline points="920,2459 950,2459" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="950.0,2459.0 938.6,2465.2 938.6,2452.8" fill="#61717a"/>
<rect x="950" y="2333" width="410" height="270" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="972" y="2374" font-size="27" font-weight="600" fill="#326991">M03｜讀訊號</text>
<text x="972" y="2422.34" font-size="23" font-weight="400" fill="#24343f">流出時間／體積、尺寸校正。</text>
<text x="972" y="2455" font-size="23" font-weight="400" fill="#24343f">時間min；積分面積依偵測器。</text>
<polyline points="1360,2459 1390,2459" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1390.0,2459.0 1378.6,2465.2 1378.6,2452.8" fill="#61717a"/>
<rect x="1390" y="2333" width="410" height="270" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="1412" y="2374" font-size="27" font-weight="600" fill="#356844">M04｜核對結論</text>
<text x="1412" y="2422.34" font-size="23" font-weight="400" fill="#24343f">大者少進孔先出；超出孔徑範圍者</text>
<text x="1412" y="2455" font-size="23" font-weight="400" fill="#24343f">難分。</text>
<rect x="50" y="2655" width="1800" height="365" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="70" y="2698" font-size="29" font-weight="600" fill="#24343f">P06｜親水作用 HILIC</text>
<rect x="70" y="2728" width="410" height="270" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="92" y="2769" font-size="27" font-weight="600" fill="#9e771c">M01｜先定問題</text>
<text x="92" y="2817.34" font-size="23" font-weight="400" fill="#24343f">保留親水分析物</text>
<text x="92" y="2850" font-size="23" font-weight="400" fill="#24343f">L16</text>
<polyline points="480,2854 510,2854" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="510.0,2854.0 498.6,2860.2 498.6,2847.8" fill="#61717a"/>
<rect x="510" y="2728" width="410" height="270" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="532" y="2769" font-size="27" font-weight="600" fill="#286c68">M02｜準備與測量</text>
<text x="532" y="2817.34" font-size="23" font-weight="400" fill="#24343f">親水相＋富有機、含水移動相。</text>
<text x="532" y="2850" font-size="23" font-weight="400" fill="#24343f">富水層分配＋吸附／可能IEC。</text>
<polyline points="920,2854 950,2854" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="950.0,2854.0 938.6,2860.2 938.6,2847.8" fill="#61717a"/>
<rect x="950" y="2728" width="410" height="270" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="972" y="2769" font-size="27" font-weight="600" fill="#326991">M03｜讀訊號</text>
<text x="972" y="2817.34" font-size="23" font-weight="400" fill="#24343f">tR；pH、含水與鹽需紀錄。</text>
<text x="972" y="2850" font-size="23" font-weight="400" fill="#24343f">時間min；積分面積依偵測器。</text>
<polyline points="1360,2854 1390,2854" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1390.0,2854.0 1378.6,2860.2 1378.6,2847.8" fill="#61717a"/>
<rect x="1390" y="2728" width="410" height="270" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="1412" y="2769" font-size="27" font-weight="600" fill="#356844">M04｜核對結論</text>
<text x="1412" y="2817.34" font-size="23" font-weight="400" fill="#24343f">親水者常更留，水增加常強沖提；</text>
<text x="1412" y="2850" font-size="23" font-weight="400" fill="#24343f">不是普通RP。</text>
<rect x="50" y="3050" width="1800" height="365" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="70" y="3093" font-size="29" font-weight="600" fill="#24343f">P07｜對掌性分離</text>
<rect x="70" y="3123" width="410" height="270" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="92" y="3164" font-size="27" font-weight="600" fill="#9e771c">M01｜先定問題</text>
<text x="92" y="3212.34" font-size="23" font-weight="400" fill="#24343f">分離對映異構物</text>
<text x="92" y="3245" font-size="23" font-weight="400" fill="#24343f">L17、L18</text>
<polyline points="480,3249 510,3249" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="510.0,3249.0 498.6,3255.2 498.6,3242.8" fill="#61717a"/>
<rect x="510" y="3123" width="410" height="270" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="532" y="3164" font-size="27" font-weight="600" fill="#286c68">M02｜準備與測量</text>
<text x="532" y="3212.34" font-size="23" font-weight="400" fill="#24343f">手性固定相／添加物，或手性衍生</text>
<text x="532" y="3245" font-size="23" font-weight="400" fill="#24343f">化。</text>
<text x="532" y="3277.66" font-size="23" font-weight="400" fill="#24343f">不等的手性作用造成保留差。</text>
<polyline points="920,3249 950,3249" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="950.0,3249.0 938.6,3255.2 938.6,3242.8" fill="#61717a"/>
<rect x="950" y="3123" width="410" height="270" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="972" y="3164" font-size="27" font-weight="600" fill="#326991">M03｜讀訊號</text>
<text x="972" y="3212.34" font-size="23" font-weight="400" fill="#24343f">對映峰的tR、Rs和各自面積。</text>
<text x="972" y="3245" font-size="23" font-weight="400" fill="#24343f">時間min；積分面積依偵測器。</text>
<polyline points="1360,3249 1390,3249" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1390.0,3249.0 1378.6,3255.2 1378.6,3242.8" fill="#61717a"/>
<rect x="1390" y="3123" width="410" height="270" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="1412" y="3164" font-size="27" font-weight="600" fill="#356844">M04｜核對結論</text>
<text x="1412" y="3212.34" font-size="23" font-weight="400" fill="#24343f">非手性C18不自動分；冠醚需具有手</text>
<text x="1412" y="3245" font-size="23" font-weight="400" fill="#24343f">性辨識。</text>
<rect x="50" y="3540" width="875" height="650" rx="18" fill="#e8e1f2" stroke="#685185" stroke-width="2"/>
<text x="72" y="3581" font-size="27" font-weight="600" fill="#685185">不是新模式｜操作、硬體與反應</text>
<text x="72" y="3629.34" font-size="24" font-weight="400" fill="#24343f">等度：組成固定；梯度：隨時間改。RP增有機常強沖提，HILIC加水常強沖</text>
<text x="72" y="3663.42" font-size="24" font-weight="400" fill="#24343f">提。</text>
<text x="72" y="3697.5" font-size="24" font-weight="400" fill="#24343f">衍生化：改分析物，使分離／偵測更適合；核對產率與空白。</text>
<text x="72" y="3731.58" font-size="24" font-weight="400" fill="#24343f">UHPLC：細粒與相容高壓／低展寬系統；粒徑不決定NP或RP。</text>
<text x="72" y="3765.66" font-size="24" font-weight="400" fill="#24343f">外標／內標：校正面積或比值，並不提供新的固定相。</text>
<text x="72" y="3799.74" font-size="24" font-weight="400" fill="#24343f">L12、L18、L23–24</text>
<rect x="975" y="3540" width="875" height="650" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="997" y="3581" font-size="27" font-weight="600" fill="#326991">辨識對照｜偵測與選項限制</text>
<text x="997" y="3629.34" font-size="24" font-weight="400" fill="#24343f">UV／DAD：吸收；FL：有效螢光。</text>
<text x="997" y="3663.42" font-size="24" font-weight="400" fill="#24343f">EC／PAD：電流；電導：離子導電。</text>
<text x="997" y="3697.5" font-size="24" font-weight="400" fill="#24343f">RI：折射差，通常等度。ELSD／CAD：非揮發粒子，需可蒸發移動相。</text>
<text x="997" y="3731.58" font-size="24" font-weight="400" fill="#24343f">LC-MS可量部分無發色基物；GC-FID/TCD/electron capture是選項對照，不當</text>
<text x="997" y="3765.66" font-size="24" font-weight="400" fill="#24343f">本章核心LC偵測。</text>
<text x="997" y="3799.74" font-size="24" font-weight="400" fill="#24343f">L19–22；圖4詳讀物理量。</text>
<text x="50" y="4332" font-size="20" font-weight="400" fill="#61717a">P1檢品與目的；P2原理與條件；P3裝置與讀數；P4判讀與限制。每個核心模式都保留這四個面向。</text>
<text x="50" y="4368" font-size="20" font-weight="400" fill="#61717a">原題：CH20 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

</details>

獨立圖檔：[[藥物分析_高效能液相層析法HPLC_全章方法分類與大小循環對照圖_v3_0.svg]]


### P01｜正相 NP的四個檢查面向

^hplc-c-p01

| 面向 | 可用資訊 |
|---|---|
|P1 目的與檢品|依方法表用途；要有本模式可利用的分析物差異|
|P2 原理與條件|極性固定相（如裸silica）；相對低極性移動相。 吸附／極性表面作用；較強表面作用者常晚。|
|P3 裝置與讀數|選相容LC柱與偵測；tR與峰面積，先給軸及校正。 tR為min；面積依偵測器積分|
|P4 判讀與限制|低極性者常先出；增加合適強溶劑常縮短保留。 條件不足就不強排唯一序|

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|L05]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|L07]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；代表原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q021|Q021｜111-2 #30]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q025|Q025｜111-1 #36]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q035|Q035｜110-2 #39]]。

### P02｜逆相 RP的四個檢查面向

^hplc-c-p02

| 面向 | 可用資訊 |
|---|---|
|P1 目的與檢品|依方法表用途；要有本模式可利用的分析物差異|
|P2 原理與條件|C18/C8/phenyl等疏水相；常水＋有機相。 疏水保留為主，可兼有表面次級作用。|
|P3 裝置與讀數|選相容LC柱與偵測；tR、k′；定量讀校正面積。 tR為min；面積依偵測器積分|
|P4 判讀與限制|中性疏水者常晚；有機相增加常較快，酸鹼另判。 條件不足就不強排唯一序|

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06|L06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|L09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10|L10]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|L12]]；代表原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q005|Q005｜113-2 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q010|Q010｜112-2 #27]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q023|Q023｜111-2 #36]]。

### P03｜離子交換 IEC／IC的四個檢查面向

^hplc-c-p03

| 面向 | 可用資訊 |
|---|---|
|P1 目的與檢品|依方法表用途；要有本模式可利用的分析物差異|
|P2 原理與條件|帶電交換相；控制pH與競爭鹽。 反號電荷作用；鹽與解離改保留。|
|P3 裝置與讀數|選相容LC柱與偵測；tR；電導／電流或其他相容偵測。 tR為min；面積依偵測器積分|
|P4 判讀與限制|依被交換離子命名；競爭鹽常促沖提。 條件不足就不強排唯一序|

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13|L13]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21|L21]]；代表原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q016|Q016｜112-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q019|Q019｜112-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060|Q060｜107-2 #12]]。

### P04｜離子對 RP的四個檢查面向

^hplc-c-p04

| 面向 | 可用資訊 |
|---|---|
|P1 目的與檢品|依方法表用途；要有本模式可利用的分析物差異|
|P2 原理與條件|RP相＋反號、具疏水端的試劑。 對離子與表面動態作用，可增加離子物保留。|
|P3 裝置與讀數|選相容LC柱與偵測；相對tR、分離與校正響應。 tR為min；面積依偵測器積分|
|P4 判讀與限制|先看分析物電荷，再選反號；同族較長尾常更留。 條件不足就不強排唯一序|

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|L14]]；代表原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q009|Q009｜113-1 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q014|Q014｜112-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q022|Q022｜111-2 #31]]。

### P05｜尺寸排斥 SEC的四個檢查面向

^hplc-c-p05

| 面向 | 可用資訊 |
|---|---|
|P1 目的與檢品|依方法表用途；要有本模式可利用的分析物差異|
|P2 原理與條件|孔徑適當、抑制次級吸附；水相或有機相依方法。 水動力尺寸決定可進孔的體積。|
|P3 裝置與讀數|選相容LC柱與偵測；流出時間／體積、尺寸校正。 tR為min；面積依偵測器積分|
|P4 判讀與限制|大者少進孔先出；超出孔徑範圍者難分。 條件不足就不強排唯一序|

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15|L15]]；代表原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q031|Q031｜110-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q037|Q037｜110-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q050|Q050｜109-1 #37]]。

### P06｜親水作用 HILIC的四個檢查面向

^hplc-c-p06

| 面向 | 可用資訊 |
|---|---|
|P1 目的與檢品|依方法表用途；要有本模式可利用的分析物差異|
|P2 原理與條件|親水相＋富有機、含水移動相。 富水層分配＋吸附／可能IEC。|
|P3 裝置與讀數|選相容LC柱與偵測；tR；pH、含水與鹽需紀錄。 tR為min；面積依偵測器積分|
|P4 判讀與限制|親水者常更留，水增加常強沖提；不是普通RP。 條件不足就不強排唯一序|

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16|L16]]；代表原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q008|Q008｜113-1 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q011|Q011｜112-2 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q043|Q043｜109-2 #32]]。

### P07｜對掌性分離的四個檢查面向

^hplc-c-p07

| 面向 | 可用資訊 |
|---|---|
|P1 目的與檢品|依方法表用途；要有本模式可利用的分析物差異|
|P2 原理與條件|手性固定相／添加物，或手性衍生化。 不等的手性作用造成保留差。|
|P3 裝置與讀數|選相容LC柱與偵測；對映峰的tR、Rs和各自面積。 tR為min；面積依偵測器積分|
|P4 判讀與限制|非手性C18不自動分；冠醚需具有手性辨識。 條件不足就不強排唯一序|

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|L17]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18|L18]]；代表原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q003|Q003｜113-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q017|Q017｜112-1 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q030|Q030｜111-1 #40]]。

### 固定相材料與修飾｜必背配對要連條件

| 材料／修飾 | 來源常用配對 | 本版限制 |
|---|---|---|
|裸silica／silanol|NP吸附；氫鍵等表面作用|Si–OH不同於Si–O–Si桥；實际含水與活性需控制|
|aminopropyl／cyanopropyl／diol|醣／界面活性劑、親水選擇性|也可在其他相條件用，不只NP|
|C18／C8／phenyl|ODS常用RP；C8較短鏈；phenyl芳香選擇性|配體密度、孔徑、殘餘位點及样品决定保留|
|styrene＋DVB|常見交聯IEC樹脂骨架|不是所有IEC唯一材質|
|SO₃⁻／COO⁻|強陽／弱陽交換|名稱依抓住的陽離子|
|季銨正電／可質子化胺|強陰／弱陰交換|弱相須看pH保持帶電|
|agarose／dextran／polyacrylamide|舊列親水soft gel SEC材料|孔徑、機械穩定及次級作用決定適用|
|交聯polystyrene／alkylated dextran／controlled-porosity glass|舊列rigid gel材料|剛性不等於一律親脂或只準水相；玻璃珠表面可修飾|
|Pirkle／cyclodextrin／手性冠醚|對掌識別相|非手性冠醚不自动具有該能力|

### 九種偵測條目｜先問被量到的物理量

^hplc-c-detectors

| 名稱 | 真正讀的量與常見單位 | 必要分析物／條件 | 梯度／限制 | 題本用途與回查 |
|---|---|---|---|---|
|UV/Vis|吸光度；AU/mAU|足夠UV/Vis吸收；常用氘燈UV、鎢燈可見|可用適當梯度，核對溶劑截止與基線|小分子有發色基；非全通用；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l19\|L19]]|
|DAD|多波長吸收／光譜|UV/Vis吸收；同時取一段波長|須核對基線、共流出與峰純度限制|不同吸收波長混合物；光譜支持辨識；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l19\|L19]]|
|Fluorescence|發射光強度；RFU等|有效螢光；激發及發射波長均相容|常可梯度；防淬熄與組成效應|B2、aflatoxins；部分物先衍生化；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20\|L20]]|
|Electrochemical|氧化還原電流；nA等|可電化學反應且電位／電極適合|選適合溶劑、鹽與電位；電極污染需查|adrenaline、catechol、部分thiol/VitC；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21\|L21]]|
|PAD|脈衝電位下的電流|電極表面可再生；適用反應窗口|不同於電導；醣常用鹼性IC條件|醣及polyol等可用；非普通氯離子指定法；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21\|L21]]|
|Conductivity|離子導電；µS等|離子可導電；背景控制／常用抑制器|IC方法及背景匹配|氯等無機離子IC常用；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21\|L21]]|
|RI / RID|折射率差；RIU等|分析物流與參考流有可測折射差|一般等度；嚴格控制溫度|醣／聚合物等；一般不配梯度；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]|
|ELSD|殘留微粒散射；相對訊號|非揮發分析物、可蒸發相／添加物|可適當梯度；不可大量不揮發鹽|醣、PEG、UDCA、脂質與界面活性劑；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]|
|CAD|帶電氣膠的電流|蒸發相、非揮發分析物；corona充電|可適當梯度；響應與組成需校正|無發色基的較廣分析範圍；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]|

本章把電導另外列出，所以共有九個條目；UV與DAD分列功能，不表示原理互不相關。ELSD/CAD是消耗樣品的氣膠路徑；串接其他偵測器須按流路與相容性，不把九台當一串全部接上。

### 圖4｜儀器與操作考點圖

<details>
<summary>展開向量圖</summary>

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="3490" viewBox="0 0 1900 3490" role="img" aria-labelledby="hplc3_g4_title hplc3_g4_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="hplc3_g4_title">HPLC｜儀器流路與操作考點</title><desc id="hplc3_g4_desc">高效能液相層析教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊；藍線表示圖4液體流路，灰線表示訊號／分析資訊。座標曲線依各子圖標示。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="3490" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH20 / HPLC / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">HPLC｜儀器流路與操作考點</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">藍實線是液體；灰實線是訊號／資料；紅虛線是分析者回查。所選偵測器只有一個方法路徑。</text>
<rect x="50" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="71" y="246" font-size="27" font-weight="600" fill="#24343f">M01｜先定問題</text>
<text x="71" y="288" font-size="23" font-weight="400" fill="#24343f">目的與檢品</text>
<polyline points="470,262 506,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="506.0,262.0 494.6,268.2 494.6,255.8" fill="#61717a"/>
<rect x="510" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="531" y="246" font-size="27" font-weight="600" fill="#24343f">M02｜準備與測量</text>
<text x="531" y="288" font-size="23" font-weight="400" fill="#24343f">製樣、作用與條件</text>
<polyline points="930,262 966,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="966.0,262.0 954.6,268.2 954.6,255.8" fill="#61717a"/>
<rect x="970" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="991" y="246" font-size="27" font-weight="600" fill="#24343f">M03｜讀訊號</text>
<text x="991" y="288" font-size="23" font-weight="400" fill="#24343f">量、單位與處理</text>
<polyline points="1390,262 1426,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1426.0,262.0 1414.6,268.2 1414.6,255.8" fill="#61717a"/>
<rect x="1430" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1451" y="246" font-size="27" font-weight="600" fill="#24343f">M04｜核對結論</text>
<text x="1451" y="288" font-size="23" font-weight="400" fill="#24343f">判讀、限制與品質</text>
<rect x="50" y="410" width="420" height="205" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="72" y="451" font-size="27" font-weight="600" fill="#326991">儲液瓶</text>
<text x="72" y="499.34" font-size="24" font-weight="400" fill="#24343f">相組成、pH與鹽</text>
<text x="72" y="533.42" font-size="24" font-weight="400" fill="#24343f">防分層／析鹽</text>
<polyline points="470,510 506,510" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="506.0,510.0 494.6,516.2 494.6,503.8" fill="#326991"/>
<rect x="510" y="410" width="420" height="205" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="532" y="451" font-size="27" font-weight="600" fill="#326991">Degasser</text>
<text x="532" y="499.34" font-size="24" font-weight="400" fill="#24343f">去氣泡</text>
<text x="532" y="533.42" font-size="24" font-weight="400" fill="#24343f">減少流量／基線異常</text>
<polyline points="930,510 966,510" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="966.0,510.0 954.6,516.2 954.6,503.8" fill="#326991"/>
<rect x="970" y="410" width="420" height="205" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="992" y="451" font-size="27" font-weight="600" fill="#326991">Pump</text>
<text x="992" y="499.34" font-size="24" font-weight="400" fill="#24343f">設定F體積流量</text>
<text x="992" y="533.42" font-size="24" font-weight="400" fill="#24343f">壓力由阻力形成</text>
<polyline points="1390,510 1426,510" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1426.0,510.0 1414.6,516.2 1414.6,503.8" fill="#326991"/>
<rect x="1430" y="410" width="420" height="205" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="1452" y="451" font-size="27" font-weight="600" fill="#326991">Injector</text>
<text x="1452" y="499.34" font-size="24" font-weight="400" fill="#24343f">控制進樣體積</text>
<text x="1452" y="533.42" font-size="24" font-weight="400" fill="#24343f">防溶劑不匹配與過載</text>
<rect x="1430" y="740" width="420" height="225" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="1452" y="781" font-size="27" font-weight="600" fill="#286c68">Guard column</text>
<text x="1452" y="829.34" font-size="23" font-weight="400" fill="#24343f">截留污染、保護分析柱</text>
<text x="1452" y="862" font-size="23" font-weight="400" fill="#24343f">粒徑與相按產品相容性</text>
<rect x="970" y="740" width="420" height="225" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="992" y="781" font-size="27" font-weight="600" fill="#286c68">Analytical column</text>
<text x="992" y="829.34" font-size="23" font-weight="400" fill="#24343f">不同模式與保留機制</text>
<text x="992" y="862" font-size="23" font-weight="400" fill="#24343f">dp粒徑、dc內徑、L柱長</text>
<rect x="510" y="740" width="420" height="225" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="532" y="781" font-size="27" font-weight="600" fill="#286c68">Selected detector</text>
<text x="532" y="829.34" font-size="23" font-weight="400" fill="#24343f">只走已選且相容的偵測路徑</text>
<text x="532" y="862" font-size="23" font-weight="400" fill="#24343f">流出物變成可量訊號</text>
<rect x="50" y="740" width="420" height="225" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="72" y="781" font-size="27" font-weight="600" fill="#286c68">廢液／收集</text>
<text x="72" y="829.34" font-size="23" font-weight="400" fill="#24343f">依偵測器是否耗樣</text>
<text x="72" y="862" font-size="23" font-weight="400" fill="#24343f">ELSD/CAD不作普通無損前端</text>
<polyline points="1850,510 1877,510 1877,690 1640,690 1640,740" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1640.0,740.0 1633.8,728.6 1646.2,728.6" fill="#326991"/>
<polyline points="1430,850 1390,850" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1390.0,850.0 1401.4,843.8 1401.4,856.2" fill="#326991"/>
<polyline points="970,850 930,850" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="930.0,850.0 941.4,843.8 941.4,856.2" fill="#326991"/>
<polyline points="510,850 470,850" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="470.0,850.0 481.4,843.8 481.4,856.2" fill="#326991"/>
<rect x="1020" y="1045" width="830" height="215" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="1042" y="1086" font-size="27" font-weight="600" fill="#9e771c">Data system｜資料處理，不是液體出口</text>
<text x="1042" y="1134.34" font-size="24" font-weight="400" fill="#24343f">收取隨時間的訊號 → 積分／校正／峰寬 → tR、含量、Rs及品質。</text>
<text x="1042" y="1168.42" font-size="24" font-weight="400" fill="#24343f">L03、L23–24；單位與處理錯誤回M03。</text>
<polyline points="930,925 950,925 950,1155 1020,1155" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1020.0,1155.0 1008.6,1161.2 1008.6,1148.8" fill="#61717a"/>
<rect x="50" y="1045" width="865" height="215" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="1086" font-size="27" font-weight="600" fill="#9e771c">控制條件｜對應部件而非一律找幫浦</text>
<text x="72" y="1134.34" font-size="24" font-weight="400" fill="#24343f">波長 → 偵測器；溫度 → 柱溫控制；注入量 → 進樣器。</text>
<text x="72" y="1168.42" font-size="24" font-weight="400" fill="#24343f">F／壓力 → 泵及阻力；Q058只把pump連到tR。</text>
<text x="50" y="1370" font-size="31" font-weight="600" fill="#24343f">M03 的九種讀數條目｜先問分析物能改變什麼</text>
<rect x="50" y="1420" width="580" height="375" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="72" y="1461" font-size="27" font-weight="600" fill="#326991">UV / Vis</text>
<text x="72" y="1509.34" font-size="24" font-weight="400" fill="#24343f">吸收，AU／mAU</text>
<text x="72" y="1543.42" font-size="24" font-weight="400" fill="#24343f">須足夠發色性。常見UV氘燈、可見鎢燈。</text>
<text x="72" y="1577.5" font-size="24" font-weight="400" fill="#24343f">不是通用。L19</text>
<rect x="660" y="1420" width="580" height="375" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="682" y="1461" font-size="27" font-weight="600" fill="#326991">DAD</text>
<text x="682" y="1509.34" font-size="24" font-weight="400" fill="#24343f">多波長吸收／光譜</text>
<text x="682" y="1543.42" font-size="24" font-weight="400" fill="#24343f">支持比對與峰純度，不單獨唯一確認未知結構。</text>
<text x="682" y="1577.5" font-size="24" font-weight="400" fill="#24343f">L19</text>
<rect x="1270" y="1420" width="580" height="375" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="1292" y="1461" font-size="27" font-weight="600" fill="#326991">Fluorescence</text>
<text x="1292" y="1509.34" font-size="24" font-weight="400" fill="#24343f">激發後讀發射光</text>
<text x="1292" y="1543.42" font-size="24" font-weight="400" fill="#24343f">B2／aflatoxins常考；需有效螢光與相容波長。</text>
<text x="1292" y="1577.5" font-size="24" font-weight="400" fill="#24343f">L20</text>
<rect x="50" y="1825" width="580" height="375" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="72" y="1866" font-size="27" font-weight="600" fill="#326991">Electrochemical</text>
<text x="72" y="1914.34" font-size="24" font-weight="400" fill="#24343f">電極反應電流，nA等</text>
<text x="72" y="1948.42" font-size="24" font-weight="400" fill="#24343f">Adrenaline／catechol可用；選電位與電極。</text>
<text x="72" y="1982.5" font-size="24" font-weight="400" fill="#24343f">不是GC電子捕捉。L21</text>
<rect x="660" y="1825" width="580" height="375" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="682" y="1866" font-size="27" font-weight="600" fill="#326991">PAD</text>
<text x="682" y="1914.34" font-size="24" font-weight="400" fill="#24343f">脈衝電位下的電流</text>
<text x="682" y="1948.42" font-size="24" font-weight="400" fill="#24343f">糖／polyol可用並更新電極表面。</text>
<text x="682" y="1982.5" font-size="24" font-weight="400" fill="#24343f">不是電導。L21</text>
<rect x="1270" y="1825" width="580" height="375" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="1292" y="1866" font-size="27" font-weight="600" fill="#326991">Conductivity</text>
<text x="1292" y="1914.34" font-size="24" font-weight="400" fill="#24343f">導電訊號，µS等</text>
<text x="1292" y="1948.42" font-size="24" font-weight="400" fill="#24343f">無機離子IC常用；氯常配抑制型電導。</text>
<text x="1292" y="1982.5" font-size="24" font-weight="400" fill="#24343f">L21</text>
<rect x="50" y="2230" width="580" height="375" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="72" y="2271" font-size="27" font-weight="600" fill="#326991">RI / RID</text>
<text x="72" y="2319.34" font-size="24" font-weight="400" fill="#24343f">分析流與參考流的折射差</text>
<text x="72" y="2353.42" font-size="24" font-weight="400" fill="#24343f">控制溫度與組成；一般不配梯度。</text>
<text x="72" y="2387.5" font-size="24" font-weight="400" fill="#24343f">L22</text>
<rect x="660" y="2230" width="580" height="375" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="682" y="2271" font-size="27" font-weight="600" fill="#326991">ELSD</text>
<text x="682" y="2319.34" font-size="24" font-weight="400" fill="#24343f">霧化 → 蒸發 → 殘粒散射</text>
<text x="682" y="2353.42" font-size="24" font-weight="400" fill="#24343f">非揮發物＋揮發相；可適當梯度。</text>
<text x="682" y="2387.5" font-size="24" font-weight="400" fill="#24343f">糖／PEG／UDCA。L22</text>
<rect x="1270" y="2230" width="580" height="375" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="1292" y="2271" font-size="27" font-weight="600" fill="#326991">CAD</text>
<text x="1292" y="2319.34" font-size="24" font-weight="400" fill="#24343f">霧化 → 蒸發 → 粒子充電</text>
<text x="1292" y="2353.42" font-size="24" font-weight="400" fill="#24343f">電暈氣體帶電，讀粒子電荷電流。</text>
<text x="1292" y="2387.5" font-size="24" font-weight="400" fill="#24343f">相容性與校正不可省。L22</text>
<rect x="50" y="2690" width="875" height="540" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="72" y="2731" font-size="27" font-weight="600" fill="#b72d4a">M02 回查｜峰形、漂移與管路異常</text>
<text x="72" y="2779.34" font-size="24" font-weight="400" fill="#24343f">拖尾／峰寬：查殘餘silanol、負載、樣品溶劑、流路展寬；不是只靠封端一</text>
<text x="72" y="2813.42" font-size="24" font-weight="400" fill="#24343f">招。</text>
<text x="72" y="2847.5" font-size="24" font-weight="400" fill="#24343f">tR漂移：核對F、配液、pH、溫度與平衡。</text>
<text x="72" y="2881.58" font-size="24" font-weight="400" fill="#24343f">高壓：查黏度、粒徑、堵塞與相容性；不任意升壓。</text>
<text x="72" y="2915.66" font-size="24" font-weight="400" fill="#24343f">移動相與萃取：均相配液≠兩相除基質。</text>
<rect x="975" y="2690" width="875" height="540" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="997" y="2731" font-size="27" font-weight="600" fill="#b72d4a">M03／M04 回查｜訊號與結論</text>
<text x="997" y="2779.34" font-size="24" font-weight="400" fill="#24343f">梯度基線：RI一般不適合；ELSD/CAD亦需組成響應校正。</text>
<text x="997" y="2813.42" font-size="24" font-weight="400" fill="#24343f">無訊號：查發色性／螢光／可電極反應／揮發性，不先宣告無分析物。</text>
<text x="997" y="2847.5" font-size="24" font-weight="400" fill="#24343f">含量不符：核對內標加入時點、校正範圍、稀釋與回收。</text>
<text x="997" y="2881.58" font-size="24" font-weight="400" fill="#24343f">九台不是整串液路；毀樣與支路依方法。</text>
<polyline points="50,2780 22,2780 22,690 1180,690 1180,740" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1180.0,740.0 1173.8,728.6 1186.2,728.6" fill="#b72d4a"/>
<text x="50" y="672" font-size="22" font-weight="400" fill="#b72d4a">峰形／漂移不符 → 修正條件，回M02再測</text>
<text x="50" y="3422" font-size="20" font-weight="400" fill="#61717a">操作配對與歷史數值見F01；高pH、溶劑與溫度上限查具體產品，不把舊恆溫槽100–150°C當通用設定。</text>
<text x="50" y="3458" font-size="20" font-weight="400" fill="#61717a">原題：CH20 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

</details>

獨立圖檔：[[藥物分析_高效能液相層析法HPLC_儀器與操作考點圖_v3_0.svg]]


### 辨識對照｜出現在選項，不當本章核心方法

| 選項 | 如何辨 | 本章接點 |
|---|---|---|
|GC-FID／TCD／electron capture|氣相偵測配對；樣品與氣化條件須適用|Q028、Q063、Q078中排除不相容配對|
|LC-MS|質譜可偵測不具發色基物；須能在介面／游離條件生成可量離子|Q073 mannitol的MS選項可行，不冒稱此章完整教MS|
|LC-IR|原理可作特定分析，但本題不是UDCA最佳常规配對|Q092保留選项，細部方法未提供|
|原子吸收／配位滴定|元素原子吸收或金屬配位；不同分析對象|Q060氯離子方法辨識|

## 公式總表與紙筆重建

^hplc-c-formulas

| 紙筆家族 | 問哪個量／式的身分 | 母式 | 單位與前提 |
|---|---|---|---|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c01\|把二元比例換成分率]]|知道哪一個強溶劑比較多，才能判tR方向。；定義|$\phi_B=\frac{V_B}{V_A+V_B}$|$V_A,V_B$同體積單位；$\phi$無單位；$100\phi$為%。 按題目列出的溶劑順序；以給定體積比作配方比較，不當嚴格熱力學體積加成。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c02\|保留體積、時間與k′]]|分清通過時間和真正保留，並用F作時間換算。；定義＋近似操作比較|$V_R=F t_R,\qquad V_0=F t_0,\qquad k^{\prime}=\frac{t_R-t_0}{t_0}$|$F$ mL/min，$t$ min，$V$ mL；$k^{\prime}$無單位。 體積流量與所量流路對應；用同保留體積比較F時採等度且保留性質不變。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c03\|弱酸兩態比與中性比例]]|把pH方向說成可以紙筆核對的解離比。；平衡模型、活度近似|$\mathrm{pH}=\mathrm{p}K_a+\log\frac{[A^-]}{[HA]},\quad r=10^{\mathrm{pH}-\mathrm{p}K_a},\quad f_{HA}=\frac1{1+r}$|pH、pKa、r與比例均無單位；方括號為同濃度單位。 同溶劑、可用同尺度pKa與pH；以濃度代活度；單一弱酸與普通RP中性態較強保留。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c04\|弱鹼兩態比與pH敏感區]]|避免把酸的方向套給鹼，並重建Q007近似。；共軛酸平衡模型|$\mathrm{pH}=\mathrm{p}K_a+\log\frac{[B]}{[BH^+]},\quad r=10^{\mathrm{pH}-\mathrm{p}K_a},\quad f_B=\frac r{1+r}$|pKa是BH⁺的酸解離常數對應值；各比無單位。 單一弱鹼、同尺度pKa與pH；跨不同藥物ΔtR需兩態保留，不只比較fB。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c05\|離子強度，濃度要乘電荷平方]]|將I與樹脂吸附選擇性分清，不用原子序替代電荷。；定義|$I_c=\frac12\sum_i c_i z_i^2$|$c_i$ mol/L，$z_i$電荷數無單位；$I_c$ mol/L。 所有離子均列入，濃度按解離化學計量；例中近似完全解離。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c06\|外標直線回算]]|從面積找到測定溶液濃度，先扣空白／截距。；校正模型|$S=a c+b,\qquad c=\frac{S-b}{a}$|$S,b$為面積單位；$c$ µg/mL；$a$為面積單位/(µg/mL)。 同分析物、波長、進樣體積和已驗證線性範圍；b用校正的截距。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c07\|內標比值回算]]|用已驗證的比值關係補償共同注入變動。；校正模型|$R=\frac{A_X}{A_{IS}}=a\frac{c_X}{c_{IS}}+b,\quad c_X=c_{IS}\frac{R-b}{a}$|面積比R與濃度比無單位；a、b為本比值模型係數；c同µg/mL。 兩峰分開、內標濃度已知、共同變動且關係驗證；先于欲補償步驟加IS。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c08\|稀釋與每錠含量]]|把測定溶液濃度送回原萃取液，最後才算藥品含量。；質量守恆與定義|$c_0=D c_{meas},\qquad m=c_0V_E,\qquad \%label=\frac{m}{m_{label}}\times100\%$|$D$無單位；$V_E$是定容萃取體積，mL；µg/mL×mL=µg；1000µg=1mg。 一錠定容萃取、量測在校正範圍，已驗證回收；D只算實際後續稀釋。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c09\|單峰N與柱板高H]]|比較柱效率時，不把總板數和單位長度品質混為一談。；近高斯模型＋定義|$N=16\left(\frac{t_R}{W_b}\right)^2=5.54\left(\frac{t_R}{W_{1/2}}\right)^2,\qquad H=\frac{L}{N}$|$t_R,W$同時間單位，N無單位（常記plates）；H與L同長度單位。 Wb採基線切線宽、W1/2為半高寬；兩者係數不可混。以總tR算此常用N，不用扣t₀時間。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10\|兩峰解析度Rs]]|既看峰距又看寬度，才能判斷是否足夠分開。；近高斯與指定寬度模型|$R_s=\frac{2(t_{R2}-t_{R1})}{W_{b1}+W_{b2}},\qquad R_s=\frac{1.18(t_{R2}-t_{R1})}{W_{1/2,1}+W_{1/2,2}}$|tR與W用同時間單位；Rs無單位。 先依時間排序tR2>tR1；寬度定義配正確係數。约1.5是常用教學基線分離参考，實际系统適用性依方法。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c11\|梯度斜率與時間比例]]|讀懂「延長1.5倍」改的是同端點變化速度。；程序定義|$g=\frac{\phi_f-\phi_i}{t_G},\qquad \frac{g_2}{g_1}=\frac{t_{G1}}{t_{G2}}\;(\Delta\phi\;\text{相同})$|φ若以%表示，g為百分點/min；若分率则min⁻¹。 線性梯度、端點與F相同；真正柱內梯度還有延遲體積與重平衡。|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c12\|粒徑、內徑、流量與壓力的比例]]|分清三種不同尺寸／速度，避免UPLC題推錯。；多孔床近似模型|$\Delta P\propto\frac{\eta L u}{d_p^2},\qquad u\approx\frac{F}{\varepsilon A_c},\quad A_c=\frac{\pi d_c^2}{4}$|η黏度；L、dp、dc長度同量綱；u長度/時間；F體積/時間；ε無單位。 粒形、孔隙率、流動條件可比，定L、η與u比較粒徑；定F、ε比較內徑。|

### 圖5｜公式與誤差判讀總表

<details>
<summary>展開向量圖</summary>

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="3870" viewBox="0 0 1900 3870" role="img" aria-labelledby="hplc3_g5_title hplc3_g5_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="hplc3_g5_title">HPLC｜公式、讀譜與誤差判讀</title><desc id="hplc3_g5_desc">高效能液相層析教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊；藍線表示圖4液體流路，灰線表示訊號／分析資訊。座標曲線依各子圖標示。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="3870" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH20 / HPLC / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">HPLC｜公式、讀譜與誤差判讀</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">先問哪個量，選定義／模型，再讀單位與條件；錯誤回到具體步驟。</text>
<rect x="50" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="71" y="246" font-size="27" font-weight="600" fill="#24343f">M01｜先定問題</text>
<text x="71" y="288" font-size="23" font-weight="400" fill="#24343f">目的與檢品</text>
<polyline points="470,262 506,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="506.0,262.0 494.6,268.2 494.6,255.8" fill="#61717a"/>
<rect x="510" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="531" y="246" font-size="27" font-weight="600" fill="#24343f">M02｜準備與測量</text>
<text x="531" y="288" font-size="23" font-weight="400" fill="#24343f">製樣、作用與條件</text>
<polyline points="930,262 966,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="966.0,262.0 954.6,268.2 954.6,255.8" fill="#61717a"/>
<rect x="970" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="991" y="246" font-size="27" font-weight="600" fill="#24343f">M03｜讀訊號</text>
<text x="991" y="288" font-size="23" font-weight="400" fill="#24343f">量、單位與處理</text>
<polyline points="1390,262 1426,262" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1426.0,262.0 1414.6,268.2 1414.6,255.8" fill="#61717a"/>
<rect x="1430" y="205" width="420" height="115" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1451" y="246" font-size="27" font-weight="600" fill="#24343f">M04｜核對結論</text>
<text x="1451" y="288" font-size="23" font-weight="400" fill="#24343f">判讀、限制與品質</text>
<rect x="50" y="365" width="1200" height="680" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="75" y="410" font-size="29" font-weight="600" fill="#24343f">EX01讀譜示意｜位置、寬度與面積分工</text>
<polyline points="130,495 130,850 1145,850" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1145.0,850.0 1133.6,856.2 1133.6,843.8" fill="#61717a"/>
<text x="150" y="485" font-size="23" font-weight="400" fill="#326991">訊號（示意相對響應）</text>
<polyline points="130,850 130,858" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="123" y="890" font-size="23" font-weight="400" fill="#24343f">0</text>
<polyline points="275,850 275,858" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="268" y="890" font-size="23" font-weight="400" fill="#24343f">1</text>
<polyline points="420,850 420,858" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="413" y="890" font-size="23" font-weight="400" fill="#24343f">2</text>
<polyline points="565,850 565,858" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="558" y="890" font-size="23" font-weight="400" fill="#24343f">3</text>
<polyline points="710,850 710,858" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="703" y="890" font-size="23" font-weight="400" fill="#24343f">4</text>
<polyline points="855,850 855,858" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="848" y="890" font-size="23" font-weight="400" fill="#24343f">5</text>
<polyline points="1000,850 1000,858" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="993" y="890" font-size="23" font-weight="400" fill="#24343f">6</text>
<polyline points="1145,850 1145,858" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="1138" y="890" font-size="23" font-weight="400" fill="#24343f">7</text>
<text x="1087.0" y="924" font-size="23" font-weight="400" fill="#24343f">時間／min</text>
<polyline points="652.0,849.9161343430244 652.725,849.8976942174429 653.4499999999999,849.8755111446242 654.1750000000001,849.8488963240601 654.9,849.8170493952799 655.625,849.7790434232662 656.35,849.7338084408331 657.075,849.680113515525 657.8000000000001,849.6165473301688 658.525,849.5414972924817 659.25,849.4531272204542 659.975,849.3493536868186 660.7,849.2278211479409 661.425,849.0858760299868 662.15,848.9205399980917 662.875,848.7284826922468 663.6,848.5059942762485 664.325,848.2489582126594 665.05,847.9528247464065 665.7750000000001,847.6125856512449 666.5,847.2227508654394 667.225,846.7773277139996 667.95,846.2698034827331 668.6750000000001,845.6931321720912 669.4,845.0397263139074 670.125,844.301454779097 670.85,843.4696475365205 671.575,842.5351083397211 672.3000000000001,841.4881363163502 673.025,840.3185574120839 673.75,839.0157665941481 674.475,837.5687816469126 675.2,835.9663092914665 675.9250000000001,834.1968242311777 676.65,832.2486615650907 677.375,830.1101228204432 678.1,827.7695956351533 678.825,825.2156868723131 679.55,822.4373686738787 680.275,819.4241366632749 681.0,816.1661791908466 681.725,812.6545561873954 682.45,808.8813858557112 683.175,804.8400370952766 683.9000000000001,800.5253252290961 684.625,795.933708292528 685.35,791.063480861034 686.075,785.9149621462316 686.8,780.4906748867016 687.525,774.7955114106809 688.25,768.8368831604124 688.975,762.6248499500609 689.7,756.1722252871497 690.4250000000001,749.494654226336 691.15,742.610660447315 691.875,735.5416595570964 692.6,728.3119360100072 693.325,720.9485815136255 694.0500000000001,713.4813933400725 694.775,705.94273158205 695.5,698.3673350718418 696.225,690.7920964070638 696.95,683.2557972853812 697.675,675.7988061259912 698.4,668.4627407315774 699.125,661.2900995027478 699.85,654.3238654395327 700.575,647.6070878330282 701.3,641.1824471471821 702.0250000000001,635.0918090993641 702.75,629.3757743538509 703.475,624.0732305317009 704.2,619.2209134033411 704.925,614.8529841589145 705.65,611.0006295417248 706.375,607.6916913809139 707.1,604.9503316733112 707.825,602.7967388471916 708.5500000000001,601.2468802018293 709.275,600.3123047688548 710.0,600.0 710.725,600.3123047688548 711.4499999999999,601.2468802018293 712.1750000000001,602.7967388471919 712.9000000000001,604.9503316733114 713.625,607.6916913809142 714.35,611.0006295417252 715.075,614.8529841589145 715.8,619.2209134033411 716.525,624.0732305317009 717.25,629.3757743538509 717.9749999999999,635.0918090993641 718.7,641.1824471471826 719.4250000000001,647.6070878330288 720.1500000000001,654.3238654395334 720.875,661.2900995027484 721.6,668.4627407315774 722.325,675.7988061259912 723.05,683.2557972853812 723.775,690.7920964070638 724.5,698.3673350718411 725.225,705.9427315820507 725.95,713.481393340073 726.6750000000001,720.9485815136262 727.4,728.3119360100072 728.125,735.5416595570964 728.85,742.610660447315 729.5749999999999,749.494654226336 730.3000000000001,756.1722252871509 731.0250000000001,762.6248499500615 731.75,768.836883160413 732.475,774.7955114106815 733.2,780.4906748867016 733.925,785.9149621462316 734.65,791.063480861034 735.375,795.933708292528 736.0999999999999,800.5253252290961 736.825,804.8400370952769 737.5500000000001,808.8813858557115 738.2750000000001,812.6545561873957 739.0,816.166179190847 739.725,819.4241366632749 740.45,822.4373686738787 741.175,825.2156868723131 741.9,827.7695956351533 742.625,830.1101228204429 743.35,832.248661565091 744.075,834.1968242311779 744.8000000000001,835.9663092914666 745.525,837.5687816469126 746.25,839.0157665941481 746.975,840.3185574120839 747.6999999999999,841.4881363163502 748.4250000000001,842.5351083397212 749.1500000000001,843.4696475365205 749.875,844.301454779097 750.6,845.0397263139074 751.325,845.6931321720913 752.05,846.2698034827331 752.775,846.7773277139996 753.5,847.2227508654394 754.2249999999999,847.6125856512449 754.95,847.9528247464065 755.6750000000001,848.2489582126594 756.4000000000001,848.5059942762485 757.125,848.7284826922469 757.85,848.9205399980917 758.575,849.0858760299868 759.3,849.2278211479409 760.025,849.3493536868186 760.75,849.4531272204542 761.475,849.5414972924817 762.2,849.6165473301689 762.9250000000001,849.680113515525 763.65,849.7338084408331 764.375,849.7790434232662 765.1,849.8170493952799 765.8249999999999,849.8488963240601 766.5500000000001,849.8755111446242 767.2750000000001,849.8976942174429 768.0,849.9161343430244" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="695.5,698.3673350718416 681.0,850" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polyline points="724.5,698.3673350718416 739.0,850" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polyline points="710.0,600 710.0,850" fill="none" stroke="#326991" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<text x="686.0" y="580" font-size="25" font-weight="400" fill="#326991">X</text>
<polyline points="738.9999999999999,849.9043931510478 739.7249999999999,849.883371407885 740.4499999999998,849.8580827048715 741.1749999999998,849.8277418094285 741.8999999999999,849.791436310619 742.625,849.7481095025236 743.3499999999999,849.6965416225496 744.0749999999999,849.6353294076986 744.8,849.5628639563926 745.5249999999999,849.4773069134292 746.2499999999999,849.3765650313179 746.9749999999999,849.2582632029732 747.6999999999998,849.1197161086526 748.425,848.9578986741849 749.15,848.7694155978246 749.8749999999999,848.5504702691613 750.5999999999999,848.2968334749233 751.3249999999999,848.0038123624317 752.0499999999998,847.6662202109035 752.7749999999999,847.2783476424192 753.4999999999999,846.833935986601 754.2249999999999,846.3261535939596 754.9499999999999,845.7475759703157 755.675,845.090170676184 756.3999999999999,844.3452879978545 757.1249999999999,843.5036584481705 757.8499999999999,842.5553981916333 758.5749999999998,841.4900235072822 759.2999999999998,840.2964754006393 760.0249999999999,838.9631554497759 760.75,837.4779739173289 761.4749999999999,835.8284110774804 762.1999999999999,834.001592592272 762.925,831.9843796235428 763.6499999999999,829.7634741842037 764.3749999999999,827.3255400153054 765.0999999999999,824.6573390240752 765.8249999999998,821.7458830344375 766.55,818.5786002882217 767.275,815.1435157961334 767.9999999999999,811.4294442775655 768.7249999999999,807.4261940536311 769.4499999999999,803.1247798755112 770.1749999999998,798.5176422886157 770.8999999999999,793.5988707611705 771.6249999999999,788.3644274534829 772.3499999999999,782.8123681815788 773.0749999999999,776.943056846704 773.8,770.7593693708399 774.5249999999999,764.2668830081768 775.2499999999999,757.4740468028708 775.9749999999999,750.3923289430701 776.6999999999998,743.036336827352 777.4249999999998,735.4239058180244 778.1499999999999,727.5761529099406 778.875,719.51749189509 779.5999999999999,711.2756070514083 780.3249999999999,702.8813829255339 781.05,694.3687884076834 781.7749999999999,685.7747140035377 782.4999999999999,677.1387619819004 783.2249999999999,668.5029899040543 783.9499999999998,659.911608905336 784.675,651.41063898363 785.4,643.0475244339982 786.1249999999999,634.8707134331332 786.8499999999999,626.929206601068 787.5749999999999,619.2720801296527 788.2999999999998,611.9479897477881 789.0249999999999,605.0046623732762 789.7499999999999,598.4883827633912 790.4749999999999,592.4434828061391 791.1999999999999,586.9118412798089 791.925,581.9324019411627 792.6499999999999,577.5407176775668 793.3749999999999,573.7685281742422 794.0999999999999,570.643378107575 794.8249999999998,568.1882822857988 795.5499999999998,566.4214434300857 796.2749999999999,565.3560274364945 797.0,565.0 797.7249999999999,565.3560274364945 798.4499999999999,566.4214434300854 799.175,568.1882822857984 799.8999999999999,570.6433781075746 800.6249999999999,573.7685281742415 801.3499999999999,577.540717677566 802.0749999999998,581.9324019411617 802.8,586.9118412798089 803.525,592.4434828061391 804.2499999999999,598.4883827633901 804.9749999999999,605.0046623732751 805.6999999999999,611.9479897477869 806.4249999999998,619.2720801296515 807.1499999999999,626.9292066010667 807.8749999999999,634.8707134331318 808.5999999999999,643.0475244339982 809.3249999999999,651.41063898363 810.05,659.9116089053346 810.7749999999999,668.5029899040528 811.4999999999999,677.1387619818988 812.2249999999999,685.7747140035362 812.9499999999998,694.3687884076819 813.6749999999998,702.8813829255323 814.3999999999999,711.2756070514067 815.125,719.51749189509 815.8499999999999,727.5761529099392 816.5749999999999,735.4239058180231 817.3,743.0363368273506 818.0249999999999,750.3923289430688 818.7499999999999,757.4740468028696 819.4749999999999,764.2668830081757 820.1999999999999,770.7593693708399 820.925,776.943056846704 821.65,782.8123681815788 822.3749999999999,788.3644274534819 823.0999999999999,793.5988707611696 823.8249999999999,798.5176422886149 824.5499999999998,803.1247798755104 825.2749999999999,807.4261940536303 825.9999999999999,811.4294442775648 826.7249999999999,815.1435157961334 827.4499999999999,818.5786002882217 828.175,821.7458830344369 828.8999999999999,824.6573390240748 829.6249999999999,827.3255400153049 830.3499999999999,829.7634741842032 831.0749999999998,831.9843796235424 831.7999999999998,834.0015925922717 832.5249999999999,835.82841107748 833.25,837.4779739173289 833.9749999999999,838.9631554497756 834.6999999999999,840.2964754006391 835.425,841.490023507282 836.1499999999999,842.5553981916332 836.8749999999999,843.5036584481704 837.5999999999999,844.3452879978544 838.3249999999999,845.090170676184 839.05,845.7475759703157 839.775,846.3261535939596 840.4999999999999,846.833935986601 841.2249999999999,847.2783476424191 841.9499999999999,847.6662202109034 842.6749999999998,848.0038123624316 843.3999999999999,848.2968334749232 844.1249999999999,848.5504702691613 844.8499999999999,848.7694155978246 845.5749999999999,848.9578986741849 846.3,849.1197161086525 847.0249999999999,849.2582632029732 847.7499999999999,849.3765650313179 848.4749999999999,849.4773069134292 849.1999999999998,849.5628639563926 849.9249999999998,849.6353294076985 850.6499999999999,849.6965416225496 851.375,849.7481095025236 852.0999999999999,849.791436310619 852.8249999999999,849.8277418094285 853.55,849.8580827048715 854.2749999999999,849.883371407885 854.9999999999999,849.9043931510478" fill="none" stroke="#685185" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="782.5,677.1387619818995 767.9999999999999,850" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polyline points="811.4999999999999,677.1387619818995 826.0,850" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polyline points="797.0,565 797.0,850" fill="none" stroke="#685185" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<text x="773.0" y="545" font-size="25" font-weight="400" fill="#685185">Y</text>
<polyline points="420,520 420,850" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<text x="390" y="540" font-size="23" font-weight="400" fill="#24343f">t₀=2</text>
<polyline points="681.0,940 739.0,940" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="681.0,932 681.0,948" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="739.0,932 739.0,948" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="685" y="976" font-size="23" font-weight="400" fill="#24343f">0.4</text>
<polyline points="767.9999999999999,940 826.0,940" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="767.9999999999999,932 767.9999999999999,948" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="826.0,932 826.0,948" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="772.0" y="976" font-size="23" font-weight="400" fill="#24343f">0.4</text>
<text x="75" y="1020" font-size="22" font-weight="400" fill="#61717a">tR=4.0、4.6 min；Wb=0.4 min（基線切線寬）；面積不由峰高替代。</text>
<rect x="1300" y="365" width="550" height="680" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="1322" y="406" font-size="27" font-weight="600" fill="#326991">讀到資料之後，才算</text>
<text x="1322" y="454.34" font-size="24" font-weight="400" fill="#24343f">k′X=(4−2)/2=1</text>
<text x="1322" y="488.42" font-size="24" font-weight="400" fill="#24343f">Rs=2×(4.6−4.0)/(0.4+0.4)=1.5</text>
<text x="1322" y="522.5" font-size="24" font-weight="400" fill="#24343f"></text>
<text x="1322" y="556.58" font-size="24" font-weight="400" fill="#24343f">X面積24，校正S=2c+4</text>
<text x="1322" y="590.66" font-size="24" font-weight="400" fill="#24343f">c=(24−4)/2=10 µg/mL</text>
<text x="1322" y="624.74" font-size="24" font-weight="400" fill="#24343f"></text>
<text x="1322" y="658.82" font-size="24" font-weight="400" fill="#24343f">曲線高度與面積是示意；不按24積分單位繪</text>
<text x="1322" y="692.9" font-size="24" font-weight="400" fill="#24343f">製。</text>
<text x="1322" y="726.98" font-size="24" font-weight="400" fill="#24343f">同tR不是唯一身分證據。</text>
<text x="1322" y="761.06" font-size="24" font-weight="400" fill="#24343f">L03、L23；C02、C06、C10</text>
<rect x="50" y="1130" width="580" height="400" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="1171" font-size="27" font-weight="600" fill="#9e771c">C01 比例</text>
<text x="72" y="1219.34" font-size="24" font-weight="400" fill="#24343f">φB=VB/(VA+VB)</text>
<text x="72" y="1253.42" font-size="24" font-weight="400" fill="#24343f">問哪個強溶劑更多；1:5→5/6。</text>
<text x="72" y="1287.5" font-size="24" font-weight="400" fill="#24343f">φ無單位；先讀配方順序。M02→04</text>
<rect x="660" y="1130" width="580" height="400" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="682" y="1171" font-size="27" font-weight="600" fill="#326991">C02 時間／體積／k′</text>
<text x="682" y="1219.34" font-size="24" font-weight="400" fill="#24343f">VR=F×tR；V₀=F×t₀</text>
<text x="682" y="1253.42" font-size="24" font-weight="400" fill="#24343f">k′=(tR−t₀)/t₀</text>
<text x="682" y="1287.5" font-size="24" font-weight="400" fill="#24343f">F mL/min、t min、V mL；k′無單位。等度近似。</text>
<text x="682" y="1321.58" font-size="24" font-weight="400" fill="#24343f">M03</text>
<rect x="1270" y="1130" width="580" height="400" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="1292" y="1171" font-size="27" font-weight="600" fill="#685185">C03 弱酸</text>
<text x="1292" y="1219.34" font-size="24" font-weight="400" fill="#24343f">pH=pKa+log([A⁻]/[HA])</text>
<text x="1292" y="1253.42" font-size="24" font-weight="400" fill="#24343f">fHA=1/(1+10^(pH−pKa))</text>
<text x="1292" y="1287.5" font-size="24" font-weight="400" fill="#24343f">pKa−1：HA=10/11；普通RP酸升pH常快。M02→</text>
<text x="1292" y="1321.58" font-size="24" font-weight="400" fill="#24343f">04</text>
<rect x="50" y="1565" width="580" height="400" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="1606" font-size="27" font-weight="600" fill="#9e771c">C04 弱鹼</text>
<text x="72" y="1654.34" font-size="24" font-weight="400" fill="#24343f">pH=pKa+log([B]/[BH⁺])</text>
<text x="72" y="1688.42" font-size="24" font-weight="400" fill="#24343f">fB=r/(1+r)，r=10^(pH−pKa)</text>
<text x="72" y="1722.5" font-size="24" font-weight="400" fill="#24343f">pKa−1：B=1/11；pKa是BH⁺值。M02→04</text>
<rect x="660" y="1565" width="580" height="400" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="682" y="1606" font-size="27" font-weight="600" fill="#326991">C05 離子強度</text>
<text x="682" y="1654.34" font-size="24" font-weight="400" fill="#24343f">I=½Σ cᵢzᵢ²</text>
<text x="682" y="1688.42" font-size="24" font-weight="400" fill="#24343f">列全部離子，電荷要平方。</text>
<text x="682" y="1722.5" font-size="24" font-weight="400" fill="#24343f">0.1M CaCl₂：I=0.3M。不是保留常數。M02</text>
<rect x="1270" y="1565" width="580" height="400" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="1292" y="1606" font-size="27" font-weight="600" fill="#685185">C06 外標</text>
<text x="1292" y="1654.34" font-size="24" font-weight="400" fill="#24343f">S=a×c+b；c=(S−b)/a</text>
<text x="1292" y="1688.42" font-size="24" font-weight="400" fill="#24343f">先扣截距再除斜率。</text>
<text x="1292" y="1722.5" font-size="24" font-weight="400" fill="#24343f">校正範圍、單位與回代要一致。M03→04</text>
<rect x="50" y="2000" width="580" height="400" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="2041" font-size="27" font-weight="600" fill="#9e771c">C07 內標</text>
<text x="72" y="2089.34" font-size="24" font-weight="400" fill="#24343f">R=AX/AIS=a(cX/cIS)+b</text>
<text x="72" y="2123.42" font-size="24" font-weight="400" fill="#24343f">cX=cIS×(R−b)/a</text>
<text x="72" y="2157.5" font-size="24" font-weight="400" fill="#24343f">兩峰可分；共變且已驗證，才補偿誤差。M03→04</text>
<rect x="660" y="2000" width="580" height="400" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="682" y="2041" font-size="27" font-weight="600" fill="#326991">C08 原樣含量</text>
<text x="682" y="2089.34" font-size="24" font-weight="400" fill="#24343f">c₀=D×c測定；m=c₀×VE</text>
<text x="682" y="2123.42" font-size="24" font-weight="400" fill="#24343f">µg/mL×mL=µg；1000µg=1mg。</text>
<text x="682" y="2157.5" font-size="24" font-weight="400" fill="#24343f">VE是定容萃取體積；V₀另指未保留體積。M03→</text>
<text x="682" y="2191.58" font-size="24" font-weight="400" fill="#24343f">04</text>
<rect x="1270" y="2000" width="580" height="400" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="1292" y="2041" font-size="27" font-weight="600" fill="#685185">C09 效率／展寬</text>
<text x="1292" y="2089.34" font-size="24" font-weight="400" fill="#24343f">H=A+B/u+Cu；N=L/H</text>
<text x="1292" y="2123.42" font-size="24" font-weight="400" fill="#24343f">N=16(tR/Wb)²；半高係數5.54。</text>
<text x="1292" y="2157.5" font-size="24" font-weight="400" fill="#24343f">H與L同長度單位，u是線性速度。</text>
<text x="1292" y="2191.58" font-size="24" font-weight="400" fill="#24343f">B不直接改，B/u仍隨u變。M02→04</text>
<rect x="50" y="2435" width="580" height="400" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="2476" font-size="27" font-weight="600" fill="#9e771c">C10 分離</text>
<text x="72" y="2524.34" font-size="24" font-weight="400" fill="#24343f">Rs=2ΔtR/(Wb1+Wb2)</text>
<text x="72" y="2558.42" font-size="24" font-weight="400" fill="#24343f">半高寬另用係數1.18。</text>
<text x="72" y="2592.5" font-size="24" font-weight="400" fill="#24343f">峰距用差、寬度用和；同時間單位。M03→04</text>
<rect x="660" y="2435" width="580" height="400" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="682" y="2476" font-size="27" font-weight="600" fill="#326991">C11 梯度</text>
<text x="682" y="2524.34" font-size="24" font-weight="400" fill="#24343f">g=(φf−φi)/tG</text>
<text x="682" y="2558.42" font-size="24" font-weight="400" fill="#24343f">端點同，時間1.5倍→g為2/3。</text>
<text x="682" y="2592.5" font-size="24" font-weight="400" fill="#24343f">%作數值則g為百分點/min，非每分鐘增加幾倍。</text>
<text x="682" y="2626.58" font-size="24" font-weight="400" fill="#24343f">M02→04</text>
<rect x="1270" y="2435" width="580" height="400" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="1292" y="2476" font-size="27" font-weight="600" fill="#685185">C12 壓力與速度</text>
<text x="1292" y="2524.34" font-size="24" font-weight="400" fill="#24343f">ΔP∝ηLu/dp²；u≈F/(εAc)</text>
<text x="1292" y="2558.42" font-size="24" font-weight="400" fill="#24343f">同u細粒減半→壓力約4倍。</text>
<text x="1292" y="2592.5" font-size="24" font-weight="400" fill="#24343f">內徑減半同F→u約4倍；dp≠dc。M02→04</text>
<rect x="50" y="2940" width="875" height="660" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="72" y="2981" font-size="27" font-weight="600" fill="#b72d4a">錯在條件／操作 → 回M02</text>
<text x="72" y="3029.34" font-size="24" font-weight="400" fill="#24343f">先認NP／RP／HILIC，不把水多一律叫強沖提。</text>
<text x="72" y="3063.42" font-size="24" font-weight="400" fill="#24343f">先酸／鹼再判pH；混合溶劑pKa與pH須同尺度。</text>
<text x="72" y="3097.5" font-size="24" font-weight="400" fill="#24343f">細粒、內徑、柱長與F/u各自獨立列條件。</text>
<text x="72" y="3131.58" font-size="24" font-weight="400" fill="#24343f">I增加常使競爭沖提更強，不是tR必定變大。</text>
<text x="72" y="3165.66" font-size="24" font-weight="400" fill="#24343f">修改後重新取得必要資料，再到M04。</text>
<rect x="975" y="2940" width="875" height="660" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="997" y="2981" font-size="27" font-weight="600" fill="#b72d4a">錯在讀數／推論 → 回M03或M04</text>
<text x="997" y="3029.34" font-size="24" font-weight="400" fill="#24343f">校正漏b：扣截距；原液稀釋：乘D。</text>
<text x="997" y="3063.42" font-size="24" font-weight="400" fill="#24343f">峰高≠面積；tR≠含量；N≠兩峰已分離。</text>
<text x="997" y="3097.5" font-size="24" font-weight="400" fill="#24343f">Wb與W½係數分開；Rs峰距差、寬度和。</text>
<text x="997" y="3131.58" font-size="24" font-weight="400" fill="#24343f">R²高不夠驗證；內標不是所有誤差都抵消。</text>
<text x="997" y="3165.66" font-size="24" font-weight="400" fill="#24343f">未提供資料不编造新tR、LOD或唯一身分。</text>
<text x="50" y="3802" font-size="20" font-weight="400" fill="#61717a">公式分類：C01/02/05/08部分為定義與守恆；C03/04平衡；C06/07校正；C09/10/12模型；C11程序定義。</text>
<text x="50" y="3838" font-size="20" font-weight="400" fill="#61717a">原題：CH20 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

</details>

獨立圖檔：[[藥物分析_高效能液相層析法HPLC_公式與誤差判讀總表_v3_0.svg]]


這十二類是教學練習C01–12，與102筆來源Q分開。先說要算什么、為何選式，再代入；不用計算機求任意對數。pH只用差0、±1、±2；來源7.9／8.1／4.4先畫區間判斷，不做按鍵教程。

### C01｜把二元比例換成分率

^hplc-c-c01

**問什麼／選式理由：**知道哪一個強溶劑比較多，才能判tR方向。

**式的身分：**定義。

$$
\phi_B=\frac{V_B}{V_A+V_B}
$$

**符號與單位：**$V_A,V_B$同體積單位；$\phi$無單位；$100\phi$為%。

**條件：**按題目列出的溶劑順序；以給定體積比作配方比較，不當嚴格熱力學體積加成。

**自編紙筆題：**C18水:MeOH為1:5與1:3，哪個MeOH分率較大且通常較快？

**整理／代入／約分：**① 標出強RP溶劑MeOH是後項。② 1:5→5/(1+5)=5/6；1:3→3/4。③ 交叉乘：5×4=20>3×6=18。④ 5/6較大，題定下沖提較強。

**結果與驗算：**1:5的MeOH較多、tR通常較短。

**最小變式：**NP DCM:hexane=2:1和1:2，哪個較強？

<details>
<summary>變式答案與理由</summary>

DCM為該NP二元中的較強溶劑；2/3>1/3，2:1較強。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q005|Q005｜113-2 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q021|Q021｜111-2 #30]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q023|Q023｜111-2 #36]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q038|Q038｜110-1 #32]]。

### C02｜保留體積、時間與k′

^hplc-c-c02

**問什麼／選式理由：**分清通過時間和真正保留，並用F作時間換算。

**式的身分：**定義＋近似操作比較。

$$
V_R=F t_R,\qquad V_0=F t_0,\qquad k^{\prime}=\frac{t_R-t_0}{t_0}
$$

**符號與單位：**$F$ mL/min，$t$ min，$V$ mL；$k^{\prime}$無單位。

**條件：**體積流量與所量流路對應；用同保留體積比較F時採等度且保留性質不變。

**自編紙筆題：**F=1 mL/min，t₀=2 min、tR=6 min。求V₀、VR、k′；F加倍的同體積近似tR？

**整理／代入／約分：**① V₀=1×2=2 mL，VR=1×6=6 mL。② 保留額外時間6−2=4 min。③ k′=4/2=2。④ 若VR仍6 mL，新tR=6/2=3 min，新t₀=1 min。

**結果與驗算：**V₀=2 mL、VR=6 mL、k′=2；新tR=3 min。

**最小變式：**流量加倍、t₀與tR同時減半，k′會減半嗎？

<details>
<summary>變式答案與理由</summary>

不會；(3−1)/1=2。若相性質不變，時間尺度改而相對保留不變。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02|L02]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|L03]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|L12]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q058|Q058｜108-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q074|Q074｜106-1 #36]]。

### C03｜弱酸兩態比與中性比例

^hplc-c-c03

**問什麼／選式理由：**把pH方向說成可以紙筆核對的解離比。

**式的身分：**平衡模型、活度近似。

$$
\mathrm{pH}=\mathrm{p}K_a+\log\frac{[A^-]}{[HA]},\quad r=10^{\mathrm{pH}-\mathrm{p}K_a},\quad f_{HA}=\frac1{1+r}
$$

**符號與單位：**pH、pKa、r與比例均無單位；方括號為同濃度單位。

**條件：**同溶劑、可用同尺度pKa與pH；以濃度代活度；單一弱酸與普通RP中性態較強保留。

**自編紙筆題：**弱酸pKa4，pH3與5的A⁻:HA及HA比例各多少？

**整理／代入／約分：**① pH3−pKa4=−1，r=1/10，所以A⁻:HA=1:10。② HA有10份，總11份→10/11。③ pH5−4=+1，r=10，A⁻:HA=10:1。④ HA=1/11。⑤ pH升高，中性HA下降，RP常較快。

**結果與驗算：**pH3：HA10/11；pH5：HA1/11。

**最小變式：**pH=pKa時，解離態為50%還是100%？

<details>
<summary>變式答案與理由</summary>

兩態比1:1，酸解離態與中性態各1/2；不是全解離。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|L09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10|L10]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q024|Q024｜111-1 #30]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q034|Q034｜110-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q041|Q041｜109-2 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q099|Q099｜102-2 #34]]。

### C04｜弱鹼兩態比與pH敏感區

^hplc-c-c04

**問什麼／選式理由：**避免把酸的方向套給鹼，並重建Q007近似。

**式的身分：**共軛酸平衡模型。

$$
\mathrm{pH}=\mathrm{p}K_a+\log\frac{[B]}{[BH^+]},\quad r=10^{\mathrm{pH}-\mathrm{p}K_a},\quad f_B=\frac r{1+r}
$$

**符號與單位：**pKa是BH⁺的酸解離常數對應值；各比無單位。

**條件：**單一弱鹼、同尺度pKa與pH；跨不同藥物ΔtR需兩態保留，不只比較fB。

**自編紙筆題：**pKa9的弱鹼，pH8與7的B:BH⁺、fB各多少？

**整理／代入／約分：**① pH8：r=1/10，B:BH⁺=1:10，fB=1/11。② pH7：r=1/100，B:BH⁺=1:100，fB=1/101。③ 差=1/11−1/101=(101−11)/1111=90/1111，约0.081。④ 兩端以離子態為主。

**結果與驗算：**中性B約從9.1%降到1.0%；普通RP保留常減。

**最小變式：**同一弱鹼從pH=pKa改成pKa−1，fB如何改？

<details>
<summary>變式答案與理由</summary>

1/2降至1/11；變動較遠低於pKa的區間明顯。不用算10^0.1等非整數。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|L09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10|L10]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q007|Q007｜113-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q045|Q045｜109-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q049|Q049｜109-1 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q074|Q074｜106-1 #36]]。

### C05｜離子強度，濃度要乘電荷平方

^hplc-c-c05

**問什麼／選式理由：**將I與樹脂吸附選擇性分清，不用原子序替代電荷。

**式的身分：**定義。

$$
I_c=\frac12\sum_i c_i z_i^2
$$

**符號與單位：**$c_i$ mol/L，$z_i$電荷數無單位；$I_c$ mol/L。

**條件：**所有離子均列入，濃度按解離化學計量；例中近似完全解離。

**自編紙筆題：**比較0.1 M NaCl與0.1 M CaCl₂的濃度式I。

**整理／代入／約分：**① NaCl：Na⁺0.1、Cl⁻0.1；I=½(0.1×1+0.1×1)=0.1 M。② CaCl₂：Ca²⁺0.1、Cl⁻0.2。③ I=½(0.1×4+0.2×1)=½×0.6=0.3 M。

**結果與驗算：**CaCl₂的I=0.3 M，是該NaCl例的3倍。

**最小變式：**I變3倍，分析物在IEC上的tR一定變3倍嗎？

<details>
<summary>變式答案與理由</summary>

不一定；I不是保留常數，競爭離子、電荷、選擇性與pH另決定保留。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13|L13]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q016|Q016｜112-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q019|Q019｜112-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q072|Q072｜106-2 #32]]。

### C06｜外標直線回算

^hplc-c-c06

**問什麼／選式理由：**從面積找到測定溶液濃度，先扣空白／截距。

**式的身分：**校正模型。

$$
S=a c+b,\qquad c=\frac{S-b}{a}
$$

**符號與單位：**$S,b$為面積單位；$c$ µg/mL；$a$為面積單位/(µg/mL)。

**條件：**同分析物、波長、進樣體積和已驗證線性範圍；b用校正的截距。

**自編紙筆題：**校正S=2c+4，样品S=24。求c，驗算回原式。

**整理／代入／約分：**① 要算c，重排c=(S−b)/a。② c=(24−4)/2=20/2=10 µg/mL。③ 回代2×10+4=24。④ 不直接24/2，否則漏截距。

**結果與驗算：**10 µg/mL，回代一致。

**最小變式：**同式S=44，c是20還是22µg/mL？

<details>
<summary>變式答案與理由</summary>

(44−4)/2=20 µg/mL；44/2=22漏扣截距。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|L03]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|L23]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q006|Q006｜113-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q015|Q015｜112-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q076|Q076｜106-1 #32]]。

### C07｜內標比值回算

^hplc-c-c07

**問什麼／選式理由：**用已驗證的比值關係補償共同注入變動。

**式的身分：**校正模型。

$$
R=\frac{A_X}{A_{IS}}=a\frac{c_X}{c_{IS}}+b,\quad c_X=c_{IS}\frac{R-b}{a}
$$

**符號與單位：**面積比R與濃度比無單位；a、b為本比值模型係數；c同µg/mL。

**條件：**兩峰分開、內標濃度已知、共同變動且關係驗證；先于欲補償步驟加IS。

**自編紙筆題：**R=0.5(cX/cIS)，cIS=4µg/mL，樣品AX=300、AIS=200，求cX。

**整理／代入／約分：**① R=300/200=3/2=1.5。② cX/cIS=1.5/0.5=3。③ cX=3×4=12 µg/mL。④ 若兩面積同減半，150/100仍1.5。

**結果與驗算：**12 µg/mL；共同注入減半比值不變。

**最小變式：**AX減半而AIS没變，比值仍可抵消嗎？

<details>
<summary>變式答案與理由</summary>

不能；這不是共同乘法變動，比值也減半，須查不同回收／干擾等原因。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|L23]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q006|Q006｜113-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q066|Q066｜107-1 #13]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q068|Q068｜107-1 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q076|Q076｜106-1 #32]]。

### C08｜稀釋與每錠含量

^hplc-c-c08

**問什麼／選式理由：**把測定溶液濃度送回原萃取液，最後才算藥品含量。

**式的身分：**質量守恆與定義。

$$
c_0=D c_{meas},\qquad m=c_0V_E,\qquad \%label=\frac{m}{m_{label}}\times100\%
$$

**符號與單位：**$D$無單位；$V_E$是定容萃取體積，mL；µg/mL×mL=µg；1000µg=1mg。

**條件：**一錠定容萃取、量測在校正範圍，已驗證回收；D只算實際後續稀釋。

**自編紙筆題：**一錠萃取定容100mL，再稀釋4倍，測得100µg/mL；標示50mg，求每錠與標示百分率。

**整理／代入／約分：**① 原萃取液c₀=4×100=400µg/mL。② m=400×100=40000µg。③ 除1000得40mg。④ 40/50×100%=80%。⑤ 逆核：40mg/100mL=400µg/mL，再除4=100。

**結果與驗算：**40mg/錠；題設標示百分率80%。

**最小變式：**稀釋後濃度較小，回原液用乘還是除D？

<details>
<summary>變式答案與理由</summary>

乘D；若把100再除4，會與實際稀釋方向相反。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|L23]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q015|Q015｜112-2 #39]]。

### C09｜單峰N與柱板高H

^hplc-c-c09

**問什麼／選式理由：**比較柱效率時，不把總板數和單位長度品質混為一談。

**式的身分：**近高斯模型＋定義。

$$
N=16\left(\frac{t_R}{W_b}\right)^2=5.54\left(\frac{t_R}{W_{1/2}}\right)^2,\qquad H=\frac{L}{N}
$$

**符號與單位：**$t_R,W$同時間單位，N無單位（常記plates）；H與L同長度單位。

**條件：**Wb採基線切線宽、W1/2為半高寬；兩者係數不可混。以總tR算此常用N，不用扣t₀時間。

**自編紙筆題：**tR=4min，基線寬Wb=0.4min，柱L=160mm。求N與H。

**整理／代入／約分：**① tR/Wb=4/(4/10)=10。② N=16×10²=1600。③ H=160/1600=0.1mm。④ 同L若H減半，N=3200；若L也減半，N仍1600。

**結果與驗算：**N=1600；H=0.1mm。

**最小變式：**短柱H較小，是否總N一定大？

<details>
<summary>變式答案與理由</summary>

不一定；N=L/H，L縮短與H下降要一起算。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|L24]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q012|Q012｜112-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q020|Q020｜111-2 #27]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q101|Q101｜102-1 #30]]。

### C10｜兩峰解析度Rs

^hplc-c-c10

**問什麼／選式理由：**既看峰距又看寬度，才能判斷是否足夠分開。

**式的身分：**近高斯與指定寬度模型。

$$
R_s=\frac{2(t_{R2}-t_{R1})}{W_{b1}+W_{b2}},\qquad R_s=\frac{1.18(t_{R2}-t_{R1})}{W_{1/2,1}+W_{1/2,2}}
$$

**符號與單位：**tR與W用同時間單位；Rs無單位。

**條件：**先依時間排序tR2>tR1；寬度定義配正確係數。约1.5是常用教學基線分離参考，實际系统適用性依方法。

**自編紙筆題：**tR1=4.0、tR2=4.6min，兩個基線寬都0.4min，求Rs。

**整理／代入／約分：**① 峰距4.6−4.0=0.6min。② 寬度和0.4+0.4=0.8min。③ Rs=2×0.6/0.8=1.2/0.8=3/2=1.5。④ min互消，正值。

**結果與驗算：**Rs=1.5；依方法判準與實际峰形再核對。

**最小變式：**只把兩峰tR和寬度同時減半，Rs如何改？

<details>
<summary>變式答案與理由</summary>

比例同縮，Rs不變；時間變快不自动提高分離。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|L03]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|L12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|L17]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|L24]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q014|Q014｜112-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q030|Q030｜111-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q042|Q042｜109-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q084|Q084｜105-2 #39]]。

### C11｜梯度斜率與時間比例

^hplc-c-c11

**問什麼／選式理由：**讀懂「延長1.5倍」改的是同端點變化速度。

**式的身分：**程序定義。

$$
g=\frac{\phi_f-\phi_i}{t_G},\qquad \frac{g_2}{g_1}=\frac{t_{G1}}{t_{G2}}\;(\Delta\phi\;\text{相同})
$$

**符號與單位：**φ若以%表示，g為百分點/min；若分率则min⁻¹。

**條件：**線性梯度、端點與F相同；真正柱內梯度還有延遲體積與重平衡。

**自編紙筆題：**10%→70%有機相，tG從10變15min，兩個g與比例？

**整理／代入／約分：**① 差70−10=60百分點。② 原g=60/10=6百分點/min。③ 新g=60/15=4。④ 新/原=4/6=2/3。⑤ 不是乘1.5；慢梯度可能改善近鄰分離但需實測。

**結果與驗算：**6變4百分點/min；斜率是原2/3。

**最小變式：**時間縮成0.5倍，同端點斜率變多少？

<details>
<summary>變式答案與理由</summary>

變2倍；tG在分母，與時間反比。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|L12]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q042|Q042｜109-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q084|Q084｜105-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q086|Q086｜105-1 #38]]。

### C12｜粒徑、內徑、流量與壓力的比例

^hplc-c-c12

**問什麼／選式理由：**分清三種不同尺寸／速度，避免UPLC題推錯。

**式的身分：**多孔床近似模型。

$$
\Delta P\propto\frac{\eta L u}{d_p^2},\qquad u\approx\frac{F}{\varepsilon A_c},\quad A_c=\frac{\pi d_c^2}{4}
$$

**符號與單位：**η黏度；L、dp、dc長度同量綱；u長度/時間；F體積/時間；ε無單位。

**條件：**粒形、孔隙率、流動條件可比，定L、η與u比較粒徑；定F、ε比較內徑。

**自編紙筆題：**dp減半而其他保持，ΔP倍數？若dc減半、F相同，u倍數？

**整理／代入／約分：**① dp在平方分母：1/(1/2)²=4，ΔP約4倍。② dc減半→截面積1/4。③ F相同u约4倍，不是維持原速度。④ 要保持u，F约改1/4；效率需另看H(u)與系统展寬。

**結果與驗算：**dp減半同u：壓力约4倍；dc減半同F：u约4倍。

**最小變式：**dp減半且u加倍，模型壓力變几倍？

<details>
<summary>變式答案與理由</summary>

2÷(1/2)²=8倍；仍須系統額定壓力允許。

</details>

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02|L02]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|L24]]；來源任務：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q012|Q012｜112-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q020|Q020｜111-2 #27]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q101|Q101｜102-1 #30]]。

## 102 筆來源題：原題、題圖與逐題判讀

^hplc-c-bank

依CH20出現順序編Q001–Q102；原文年度與題號保留，跨年重複考點仍保留每一筆。原題只整併換行、正規化相容字，移除可辨識手寫標記；没有把來源題換成自編題。題圖在下方真正內嵌，不依賴外部圖檔。所有「題本答案」與「編輯推論」分開列；本次沒有官方答案表。

### Q001｜114-1 #28｜ELSD與梯度

^hplc-c-q001

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.1。

**原題：**下列有關蒸發式光散射檢測器(evaporative light-scattering detector)之敘述,何者錯 誤?

(A) 與折射率檢測器(refractive index detector)相同,不適合梯度沖提

(B) 靈敏度比螢光檢測器(fluorescence detector) 差

(C) 適合無顯著紫外光吸收之物質, 如醣類與脂類的分析

(D) 為通用型的高效液相層析檢測器

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**ELSD與梯度；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**ELSD不靠移動相的固定折射率 → 蒸發後量粒子散射 → 可用相容梯度；A把RI限制套給ELSD。

**其他選項／關鍵錯選：**B是題本常用靈敏度比較；C的醣／脂類無強UV吸收可用ELSD；D的通用是相對概念。

**條件／易錯與來源边界：**ELSD的梯度響應仍需校正，不等於完全不受組成影響。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|L22]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22|R22]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f14|F14]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f15|F15]]。

</details>

### Q002｜114-1 #29｜衍生化的目的

^hplc-c-q002

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.1。

**原題：**高效液相層析分析時如需進行衍生化,下列考量何者錯誤?

(A) 衍生化須同時具有高產率與穩定性佳的特點,分析方法的回收率與精確度才會理想

(B) 如果欲檢測缺乏發色團的化合物,可以試圖導入醣分子以提高水溶性,加速分析時間

(C) 極性大的胺基醣苷類抗生素衍生化後,可以用正相的矽膠層析管進行分析

(D) 如果有其他適當的偵檢器可以使用,衍生化通常不會被選擇用於分析

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**衍生化的目的；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**無發色團 → 要導入能吸光／發螢光的基團；導入普通醣只改水溶性，沒有解決光學偵測弱點，選B。

**其他選項／關鍵錯選：**A要求產率與穩定性合理；C可用衍生化改善silica分離；D有合適直接法時常可省反應。

**條件／易錯與來源边界：**衍生化也可為分離或特定穩定性目的，不必只為UV。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18|L18]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l18|R18]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f13|F13]]。

</details>

### Q003｜113-2 #29｜手性與離子對

^hplc-c-q003

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.2。

**原題：**以HPLC 分析光學異構物時,下列何者最不適用?

(A) 使用Pirkle type 管柱

(B) 使用cyclodextrin 管柱

(C) 使用C18 管柱,在移動相中添加serine

(D) 使用C18 管柱,在移動相中添加cetrimide

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**手性與離子對；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**鏡像分離需要手性識別 → cetrimide是一般陽離子對試劑 → 不提供該差異，選D。

**其他選項／關鍵錯選：**A的Pirkle、B的cyclodextrin可供手性相；C的serine提供手性添加物候選。

**條件／易錯與來源边界：**添加serine不自動保證任何對映體都分開，須有具體方法；本題C不等於一律作共價衍生化。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|L17]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17|R17]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f12|F12]]。

</details>

### Q004｜113-2 #32｜固定相的適用性

^hplc-c-q004

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.3。

**原題：**關於HPLC 固定相的敘述,下列何者錯誤?

(A) C18 無法用於鹼性化合物之分析

(B) 苯基矽烷矽膠具選擇性分析芳香環化合物的特性

(C) 胺丙烷基矽膠可用於界面活性劑的分析

(D) 四級銨鹽常為強陰離子交換樹脂的作用基團

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**固定相的適用性；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**C18能分析鹼性物 → 看解離、疏水性、表面及穩定性 → A的「無法」錯。

**其他選項／關鍵錯選：**B的phenyl有芳香選擇性；C的aminopropyl有界面活性劑方法；D的季銨正電抓陰離子。

**條件／易錯與來源边界：**「沒有酸鹼之分」也過度簡化，酸鹼條件會影響保留與峰形。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|R08]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f05|F05]]。

</details>

### Q005｜113-2 #33｜RP水醇比例

^hplc-c-q005

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.3。

**原題：**以C18 管柱分析C6H5CH2NH2 時,以水及甲醇為移動相,在下列何種體積比例(水: 甲醇)下沖提,其滯留時間最短?

(A) 1:5

(B) 1:3

(C) 1:2

(D) 1:1

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**RP水醇比例；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**C18是RP → MeOH越多通常越強沖提 → 1:5的MeOH=5/6最高 → tR最短A。

**其他選項／關鍵錯選：**B=3/4、C=2/3、D=1/2，均小於5/6；比例前項是水。

**條件／易錯與來源边界：**不是只比數字5與3，必須先認比例中的哪個溶劑。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|R11]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c01|C01]]。

</details>

### Q006｜113-2 #40｜內標的適用範圍

^hplc-c-q006

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.4。

**原題：**有關HPLC 含量測定之內標(internal standard),下列敘述何者錯誤?

(A) 加入內標是為了消除注入量及檢測器的誤差

(B) 內標宜與分析物結構近似

(C) 內標的濃度,宜與分析物相近

(D) 內標一旦確定,可一體適用於不同檢品分析

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**內標的適用範圍；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**IS須配合特定分析物、基質與步驟 → 不能一個內標一體適用 → D錯。

**其他選項／關鍵錯選：**B結構相近、C濃度可比是合理選擇；A用語「消除」依題本採用，但實際只是可補償共同誤差。

**條件／易錯與來源边界：**IS不會消除所有偵測器或回收誤差，須驗證並在欲補償步驟前加入。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|L23]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23|R23]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f18|F18]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c06|C06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c07|C07]]。

</details>

### Q007｜113-1 #28｜pKa區間與變動

^hplc-c-q007

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.4–5。

**原題：**以逆相層析法同時分析bupivacaine（pKa 8.1）、pentycaine（pKa 8.1）、prilocaine（pKa 7.9）及procaine（pKa 9.0），若將移動相的pH值從8降低為7，對於下列何者的滯留時間影響最小？

(A) bupivacaine

(B) pentycaine

(C) prilocaine

(D) procaine

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**pKa區間與變動；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**pH8→7：pKa9的procaine兩端已多為BH⁺ → 中性比例1/11降到1/101 → 題本選影響最小D。

**其他選項／關鍵錯選：**A/B的pKa8.1接近區間上端；C的7.9落在區間內，題本認變動較大。

**條件／易錯與來源边界：**跨不同藥物的精確ΔtR還需各自兩態保留；只靠pKa能作本題近似，不能作普遍定量結論。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10|L10]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l10|R10]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c04|C04]]。

</details>

### Q008｜113-1 #35｜HILIC原圖峰D

^hplc-c-q008

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.5–6。

**原題：**以HILIC 層析管(性質類似正相管柱)分析下列五種胺基酸,其層析圖(如下)中波峰 D 是何種胺基酸?

<img src="data:image/png;base64,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" alt="Q008原題圖，CH20 PDF p.5" width="760" />

(A) serine

(B) tyrosine

(C) threonine

(D) phenylalanine

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**HILIC原圖峰D；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**先讀原圖A–E的位置 → 題定HILIC短→長為Phe、Tyr、Thr、Ser、Arg → 峰D為serine，選A。

**其他選項／關鍵錯選：**B tyrosine對峰B；C threonine對峰C；D phenylalanine對峰A；arginine為峰E但非選項。

**條件／易錯與來源边界：**這是該HILIC例的經驗次序，不假定所有pH及柱相都一致。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16|L16]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l16|R16]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f11|F11]]。

</details>

### Q009｜113-1 #38｜離子對與解離

^hplc-c-q009

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.6。

**原題：**下列何者不適合以離子對-層析分離法(ion-pairing chromatography)進行分析定 量? ①CH3CH2CH2CH2NH2 ②CH3CH2CH2COOH ③CH3CH2CH2CH2OH ④ (CH3CH2)4N+Br-

(A) ①

(B) ②

(C) ③

(D) ④

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**離子對與解離；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**選不適用者 → ③butanol在一般方法條件不顯著成離子 → 缺少反號配對依據，選C。

**其他選項／關鍵錯選：**①胺可質子化；②酸可解離；④季銨本身帶正電，都可在相應條件下用離子對。

**條件／易錯與來源边界：**一般醇難解離，不等於化學上永遠不能成alkoxide；本題不採極端強鹼條件。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|L14]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14|R14]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f09|F09]]。

</details>

### Q010｜112-2 #27｜C18同族次序

^hplc-c-q010

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.7。

**原題：**以高效液相層析法分析 amylbenzene、propylbenzene 及toluene 的混合物,若以 C18 管柱為固定相,甲醇和水的 混合溶液為移動相,則下列敘述何者錯誤?

(A) 增加移動相中的甲醇含量會降低此三者的capacity factor(K')

(B) 提升層析管柱的溫度,會使capacity factor(K')降低

(C) 移動相中加入0.1% 的乙酸,此三者的capacity factor(K')幾乎不變

(D) 滯留時間由長到短依序為 toluene、propylbenzene、amylbenzene

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**C18同族次序；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**同族中性烷基苯 → 烷鏈較長疏水保留較強 → 長→短應amyl>propyl>toluene，D顛倒。

**其他選項／關鍵錯選：**A提高MeOH常降k′；B升溫降k′是題本經驗情境；C少量乙酸不明顯改中性物解離。

**條件／易錯與來源边界：**升溫不保證所有分析物k′都降低，還要看分離熱力學。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06|L06]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06|R06]]。

</details>

### Q011｜112-2 #28｜HILIC多重作用

^hplc-c-q011

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.7–8。

**原題：**下列有關親水性交互反應層析法(hydrophilic interaction liquid chromatography, HILIC)之敘述,何者正確?

(A) 其分離機制與逆相層析類似

(B) 極性較高的化合物較不易滯留

(C) 移動相的水含量愈多,化合物愈慢被沖提出來

(D) 強酸性或強鹼性化合物皆有可能發生離子交換的反應

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**HILIC多重作用；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**HILIC可含帶電表面／分析物 → 除親水層分配外可有IEC → D正確。

**其他選項／關鍵錯選：**A把HILIC說成普通RP；B親水／極性物一般更留；C水增加常強沖提而較快。

**條件／易錯與來源边界：**HILIC不是只有分配一種機制，也不是所有柱都是ZIC。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16|L16]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l16|R16]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f11|F11]]。

</details>

### Q012｜112-2 #32｜粒徑與內徑

^hplc-c-q012

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.8–9。

**原題：**對於高效液相層析法(HPLC)的描述,下列何者錯誤?

(A) 固定相充填劑的粒徑愈小,分離效果愈佳

(B) 層析管柱長度變為2 倍,則滯留時間約變為2 倍

(C) 流速相同時,減小層析管柱內徑可提高分離效果

(D) 固定相粒徑愈大,分離的最佳線性流速(linear velocity)愈低

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**粒徑與內徑；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**題本指定C錯 → 同F減內徑會提高u，但效率需看速度與柱外展寬 → 不能保證分離改善。

**其他選項／關鍵錯選：**A細粒常降低H；B同u、組成、柱性質時L兩倍tR約兩倍；D較大粒徑通常最佳u較低。

**條件／易錯與來源边界：**原題「流速」沒分F與u，是重要歧義；A/B也各有前提，不把C的反面背成小內徑必較差。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|L24]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l24|R24]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f19|F19]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c09|C09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c12|C12]]。

</details>

### Q013｜112-2 #36｜無發色基偵測

^hplc-c-q013

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.9。

**原題：**下列何者可用於檢測不具發色基(chromophore)的分析物?

(A) diode array detector

(B) fluorescence detector

(C) evaporative light scattering detector

(D) UV/Vis detector

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**無發色基偵測；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**不具發色基 → A/D吸收、B螢光均缺直接訊號依據 → C ELSD量非揮發粒子可用。

**其他選項／關鍵錯選：**DAD本質也是光吸收；FL除非分析物有效發光或另作衍生化。

**條件／易錯與來源边界：**選ELSD仍須分析物不易揮發、移動相可蒸發。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|L22]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22|R22]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f15|F15]]。

</details>

### Q014｜112-2 #38｜離子對保留方向

^hplc-c-q014

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.9–10。

**原題：**以逆相層析分析具離子化特性之待測物,於動相中加入離子對試劑時,下列敘述何者錯 誤?

(A) 可增加解析度

(B) 以靜電力形成離子對

(C) 離子對試劑的低極性端與固定相,以凡得瓦力相互作用

(D) 分析物的滯留時間變短

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**離子對保留方向；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**離子物加合適疏水離子對試劑 → 常增加RP有效保留 → D的tR變短錯。

**其他選項／關鍵錯選：**A可能改善分離；B是入門的反號電荷模型；C疏水端可與RP相作用。

**條件／易錯與來源边界：**實際也可有試劑吸附造成動態IEC；解析度增加不是每個條件都保證。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|L14]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14|R14]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f09|F09]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]。

</details>

### Q015｜112-2 #39｜檢量範圍

^hplc-c-q015

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.10。

**原題：**某抗生素之最低抑菌濃度(MIC)為10 μg/mL,當血中濃度高於50 μg/mL 時有肝毒 性之疑慮。若欲使用HPLC 監測其療效濃度時,下列測試濃度範圍何者最恰當?

(A) 0.01~10000 μg/mL

(B) 0.1~1000 μg/mL

(C) 1~100 μg/mL

(D) 20~50 μg/mL

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**檢量範圍；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**需涵蓋10與50µg/mL周圍 → C的1–100涵蓋上下關鍵區又較集中 → 題本選C。

**其他選項／關鍵錯選：**D 20–50漏掉10附近；A/B跨太多數量級，未必能用同一有效校正範圍。

**條件／易錯與來源边界：**題設MIC與毒性數值僅用於此分析範圍題，不作治療判斷。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|L23]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23|R23]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f18|F18]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f27|F27]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c06|C06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c08|C08]]。

</details>

### Q016｜112-2 #40｜陽交換與pH

^hplc-c-q016

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.10。

**原題：**用陽離子交換層析法分析選項之胺基酸時,若將動相的pH 值緩緩提升,則最後沖提出 者為何?

(A) glutamic acid(C5H9NO4)

(B) leucine(C6H13NO2)

(C) threonine(C4H9NO3)

(D) lysine(C6H14N2O2)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**陽交換與pH；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**陽交換抓正電 → pH上升逐步減少正電 → lysine側鏈胺較能保留正電 → 最後D。

**其他選項／關鍵錯選：**glutamic acid側鏈為酸；leucine及threonine沒有額外強鹼性側鏈。

**條件／易錯與來源边界：**以題定胺基酸pH沖提條件作比較；完整次序會依pH、鹽及相改變。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13|L13]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l13|R13]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f08|F08]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c05|C05]]。

</details>

### Q017｜112-1 #34｜冠醚條件

^hplc-c-q017

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.11。

**原題：**使用高效液相層析法時,下列何者無法達到分離鏡像異構物的目的?

(A) 移動相中加入對掌性修飾劑

(B) 以對掌性試劑衍生化分析物

(C) 將cyclodextrin 修飾至固定相上

(D) 將crown ether 修飾至C18 管柱上

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**冠醚條件；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**題本選D；普通未具手性的crown ether修飾不自動提供鏡像識別。

**其他選項／關鍵錯選：**A手性添加物、B手性衍生化、C cyclodextrin均有可行辨識機制。

**條件／易錯與來源边界：**冠醚若本身具手性，可作CROWNPAK等分離相；D措辭未限定，不能把題本答案外推成所有冠醚不能分離。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|L17]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17|R17]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f12|F12]]。

</details>

### Q018｜112-1 #39｜常用RP基團

^hplc-c-q018

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.11。

**原題：**下列逆相液相層析固定相之修飾基團,何者最常用?

(A) CN

(B) diol

(C) n-octadecyl

(D) NH2

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**常用RP基團；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**最常用RP鍵結烷基 → 十八碳n-octadecyl=C18/ODS → C。

**其他選項／關鍵錯選：**CN、diol、NH₂是較極性基團，可在不同模式用，但不是本題最常見疏水配對。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|R08]]。

</details>

### Q019｜112-1 #40｜IEC基團與命名

^hplc-c-q019

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.11–12。

**原題：**有關離子交換層析的敘述,下列何者錯誤?

(A) 固定相係styrene 和divinylbenzene 之聚合物

(B) divinylbenzene 之含量與交聯程度有關

(C) 含磺酸根官能基者屬於陽離子交換型

(D) 含羧酸根官能基者屬於陰離子交換型

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**IEC基團與命名；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**COO⁻帶負電 → 抓陽離子 → 屬弱陽交換，D把名字顛倒。

**其他選項／關鍵錯選：**A是常用styrene/DVB樹脂例；B交聯與DVB相關；C SO₃⁻是強陽交換。

**條件／易錯與來源边界：**不是所有IEC相都必用styrene樹脂；矽膠鍵結及其他核心也可用。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13|L13]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l13|R13]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f07|F07]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c05|C05]]。

</details>

### Q020｜111-2 #27｜UPLC粒徑

^hplc-c-q020

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.12。

**原題：**相較於HPLC,利用UPLC(ultra-high-performance liquid chromatography)進行 acetaminophen 的不純物分析時,下列敘述何者錯誤?

(A) UPLC 管柱充填物之粒徑較大

(B) 同管柱長度下,UPLC 有較大的理論板數

(C) UPLC 系統需要較大的幫浦壓力

(D) UPLC 具更高的工作效率

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**UPLC粒徑；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**UHPLC常用較小粒徑 → 同L降低H而提高N → A的較大粒徑錯。

**其他選項／關鍵錯選：**B已給同L可比較效率；C阻力與壓力通常增；D能以較高速度達有效分離。

**條件／易錯與來源边界：**只有適合的柱、流路、壓力及柱外展寬控制，才能取得預期收益。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|L24]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l24|R24]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f19|F19]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c09|C09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c12|C12]]。

</details>

### Q021｜111-2 #30｜NP混合比例

^hplc-c-q021

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.12。

**原題：**在矽膠層析中,以二氯甲烷(A)與正己烷(B)混合溶媒為移動相,在下列何種體積比 例(A:B)下,移動相之極性最大?

(A) 10:1

(B) 2:1

(C) 1:2

(D) 1:10

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**NP混合比例；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**矽膠NP → DCM比hexane較極性／較強沖提 → DCM分率10/11最高 → A。

**其他選項／關鍵錯選：**B=2/3、C=1/3、D=1/11；都較低。

**條件／易錯與來源边界：**只用比例作同一二元體系比較，不把它當線性溶劑強度常數。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|R11]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c01|C01]]。

</details>

### Q022｜111-2 #31｜弱酸與正電試劑

^hplc-c-q022

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.13。

**原題：**C6H5CH2COOH 如以離子對-逆相層析分離法進行分析定量時,移動相加入下列何者, 其滯留時間最長?

(A) C7H15SO3 -

(B) (CH3)4N+

(C) (C4H9)4N+

(D) Cl-

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**弱酸與正電試劑；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**苯乙酸可帶負電 → 選正電季銨 → 四丁基銨比四甲基銨更疏水 → 最長C。

**其他選項／關鍵錯選：**A/D帶負電不是該陰離子的反號；B也正電但烷鏈較短。

**條件／易錯與來源边界：**須有足夠苯乙酸解離與合適試劑濃度；碳鏈規則只比同族。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|L14]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14|R14]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f09|F09]]。

</details>

### Q023｜111-2 #36｜RP保留最長

^hplc-c-q023

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.13。

**原題：**以C18 管柱層析分析檢品,水(A)及甲醇(B)混合液為移動相,下列何種體積比例 (A:B),其檢品之滯留時間(retention time)最長?

(A) 2:1

(B) 1:1

(C) 1:2

(D) 1:3

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**RP保留最長；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**C18 RP → 水最多是較弱沖提 → 2:1的水分率2/3最高 → 保留最長A。

**其他選項／關鍵錯選：**B水1/2；C1/3；D1/4。題目問最長，與Q005問最短相反。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|R11]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c01|C01]]。

</details>

### Q024｜111-1 #30｜aspirin酸鹼方向

^hplc-c-q024

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.13–14。

**原題：**以C18 管柱進行aspirin(pKa = 3.5)的高效液相層析分析時,下列何者正確?

(A) C18 管柱為正相的固定相

(B) 紫外光檢測器的光源通常為氙燈

(C) 以0.05 M 乙酸/乙腈(85:15)為移動相,若pH 值由3 提高至5,則滯留時間縮短

(D) 提高移動相中乙腈的比例時,滯留時間延長

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**aspirin酸鹼方向；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**aspirin是弱酸 → pH3→5解離增加 → RP保留常減少 → C正確。

**其他選項／關鍵錯選：**A C18屬RP；B常用UV氘燈而非以氙燈作該慣用配對；D增加ACN常較快。

**條件／易錯與來源边界：**氙燈也可存在某些光學儀器，題本「通常」不能當所有產品排除條件。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|L09]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09|R09]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c03|C03]]。

</details>

### Q025｜111-1 #36｜位置異構物原理

^hplc-c-q025

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.14。

**原題：**下列何種層析原理最適於分離chlorophenol 之三種異構物(o-、m-、p-)?

(A) partition

(B) adsorption

(C) ion-exchange

(D) size exclusion

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**位置異構物原理；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**位置異構物的表面作用與可接近性可不同 → 題本最適配對adsorption → B。

**其他選項／關鍵錯選：**C主要看離子電荷；D主要看水動力尺寸；A也可能在實際RP方法提供異構選擇性。

**條件／易錯與來源边界：**只保留本題最佳配對，不宣稱partition絕對不能分位置異構物，也不硬背普遍o>m>p。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|L07]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l07|R07]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f06|F06]]。

</details>

### Q026｜111-1 #39｜正逆相切換溶劑

^hplc-c-q026

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.15。

**原題：**NH2 管柱可用在正相及逆相分離,下列何者為正逆相切換時最適用的沖提液?

(A) ethyl acetate

(B) dimethylformamide

(C) water

(D) ethanol

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**正逆相切換溶劑；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**切換要讓兩套溶劑互通且柱相容 → ethanol為題本可兼用的醇 → D。

**其他選項／關鍵錯選：**A非慣用水相RP溶劑；C水不適合直接銜接部分低極性NP相；B不是該題推薦過渡。

**條件／易錯與來源边界：**實際依全部溶劑互溶與柱建議沖洗，不能只因含OH就任意替代。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04|L04]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04|R04]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f02|F02]]。

</details>

### Q027｜111-1 #29｜聚合物相容性

^hplc-c-q027

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.15。

**原題：**關於HPLC 層析管柱的敘述,下列何者錯誤?

(A) 利用封端(endcapped)方法,可增加充填物對高pH 溶液的穩定性

(B) 相較於矽石,以有機聚合物為核心的充填物在高pH 下有更好的穩定性

(C) 相較於矽石,以有機聚合物為核心的充填物對高親脂性移動相有更好的穩定性

(D) 將矽石顆粒表面的羥基置換成烷基可增加其穩定性

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**聚合物相容性；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**題本對聚合物與高親脂移動相的比較選C為錯；溶劑可導致特定聚合物膨潤，不能一律更穩。

**其他選項／關鍵錯選：**A/D表面鍵結與封端可改善部分穩定性；B不少聚合物相較耐高pH。

**條件／易錯與來源边界：**各選項都依材料；不把C的反面改寫成所有聚合物都被非極性溶劑溶掉，封端也不保證通用高pH穩定。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|R08]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f05|F05]]。

</details>

### Q028｜111-1 #31｜未衍生化醣

^hplc-c-q028

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.15。

**原題：**使用高效液相層析法分析未經衍生化的醣類分子時,最適合使用下列何種檢測器?

(A) 火焰離子化檢測器(flame ionization detector)

(B) 電子捕捉檢測器(electron capture detector)

(C) 蒸發光散射檢測器(evaporative light scattering detector)

(D) 螢光偵測器(fluorescence detector)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**未衍生化醣；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**未衍生化醣缺強發色／螢光 → ELSD讀粒子不依這些基團 → C。

**其他選項／關鍵錯選：**A火焰離子化與B電子捕捉是題本GC偵測器；D缺足夠直接螢光。

**條件／易錯與來源边界：**適當方法下糖可PAD；本題選項沒有PAD，不宜說糖不能電化學檢測。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|L22]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22|R22]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f15|F15]]。

</details>

### Q029｜111-1 #32｜UV的通用性

^hplc-c-q029

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.16。

**原題：**關於HPLC 檢測器的敘述,下列何者錯誤?

(A) 紫外光檢測器(UV)為高靈敏之通用型檢測器

(B) 蒸發光散射檢測器(ELSD)可用於醣類的分析

(C) 電化學檢測器(ECD)常運用於選擇性的生物檢品分析

(D) 螢光檢測器之光源通常為氙燈

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**UV的通用性；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**UV須有足夠吸收 → 不是通用型 → A錯。

**其他選項／關鍵錯選：**B糖可ELSD；C可反應生物分析物用電化學；D螢光常用氙燈激發。

**條件／易錯與來源边界：**「有發色基」也須波長、靈敏度與基質合適。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l19|L19]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l19|R19]]。

</details>

### Q030｜111-1 #40｜三點模型

^hplc-c-q030

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.16。

**原題：**以HPLC 分析鏡像異構物時,鏡像異構物一般必須與具掌性(chiral)之靜相至少有幾點 接觸方具良好分離效 果?

(A) 1

(B) 2

(C) 3

(D) 4

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**三點模型；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**題本三點辨識模型 → 不等手性作用可產生保留差 → 至少3點C。

**其他選項／關鍵錯選：**A/B不符合此題的三點教學配對；D不是該模型的最少點數。

**條件／易錯與來源边界：**3點模型可包括立體排斥，不是純粹三點成平面的幾何證明。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|L17]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17|R17]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f12|F12]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]。

</details>

### Q031｜110-2 #29｜玻尿酸分離

^hplc-c-q031

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.16。

**原題：**玻尿酸(hyaluronic acid)為多醣類化合物,其分離純化以下列何者最適當?

(A) 正相液相層析法

(B) 離子交換層析法

(C) 逆相液相層析法

(D) 分子篩層析法

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**玻尿酸分離；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**高分子多醣要依尺寸分離／純化 → SEC提供可進孔體積差 → D。

**其他選項／關鍵錯選：**A/B/C可有特定其他分離用途，但這題給玻尿酸高分子而未給可用電荷或疏水差異。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15|L15]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l15|R15]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f10|F10]]。

</details>

### Q032｜110-2 #31｜低極性與C18

^hplc-c-q032

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.17。

**原題：**以相同之移動相進行逆相液相層析分析低極性檢品時,檢品滯留時間最長之層析管為 何?

(A) C18 管柱

(B) C8 管柱

(C) cyano 管柱

(D) diol 管柱

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**低極性與C18；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**同移動相且低極性物 → 可比C18有較強疏水保留 → 最長A。

**其他選項／關鍵錯選：**B C8烷鏈較短；C/D較極性，相同題定下不選最長。

**條件／易錯與來源边界：**比較要有可比鍵結密度、孔徑與柱尺寸；不能因此推出高極性物在C8必定最長。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06|L06]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06|R06]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f05|F05]]。

</details>

### Q033｜110-2 #32｜偵測器選擇性排序

^hplc-c-q033

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.17。

**原題：**下列HPLC 所使用之檢測器,其偵測化合物之選擇性由高至低排序,何者正確?①紫外 光檢測器(UV) ② 電化學檢測器(ECD) ③蒸發光散射檢測器(ELSD) ④折射率檢測 器(RID)

(A) ②①③④

(B) ①②③④

(C) ②④①③

(D) ①②④③

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**偵測器選擇性排序；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**四台中題本選擇性順序ECD>UV>ELSD>RI → ②①③④ → A。

**其他選項／關鍵錯選：**B/D把UV置於ECD前；C把RI放在ELSD與UV之前，不合題本順序。

**條件／易錯與來源边界：**FL若加入此教材序通常在ECD前；選擇性不是檢出最低量的靈敏度。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20|L20]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l20|R20]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f14|F14]]。

</details>

### Q034｜110-2 #38｜弱酸適用pH

^hplc-c-q034

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.17。

**原題：**某弱酸性藥物之pKa=4,用逆相高效液相層析分析時,最適當之動相pH 值為何?

(A) 8

(B) 3

(C) 6

(D) 7

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**弱酸適用pH；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**弱酸pKa4 → pH3中性HA占10/11 → RP有足夠保留且較少解離 → B。

**其他選項／關鍵錯選：**A8、C6、D7都高於pKa而多為A⁻；可能太早流出。

**條件／易錯與來源边界：**這是選項中的方法候選，不是所有弱酸的最適pH恆為pKa−1。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|L09]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09|R09]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c03|C03]]。

</details>

### Q035｜110-2 #39｜NP沖提序

^hplc-c-q035

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.17–18。

**原題：**在正相液相層析中,下列何者為溶劑沖提能力由大至小之順序?

(A) 甲醇、乙酸乙酯、二氯甲烷、正己烷

(B) 乙酸乙酯、二氯甲烷、甲醇、正己烷

(C) 乙酸乙酯、甲醇、二氯甲烷、正己烷

(D) 甲醇、乙酸乙酯、正己烷、二氯甲烷

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**NP沖提序；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**題本NP沖提強度序MeOH>ethyl acetate>DCM>hexane → A完全符合。

**其他選項／關鍵錯選：**B/C把MeOH次序移後；D將hexane置於DCM前。

**條件／易錯與來源边界：**這是矽膠常用經驗序，不把它當純溶劑極性指數的普遍排行。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|R11]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f02|F02]]。

</details>

### Q036｜110-1 #26｜B2螢光配對

^hplc-c-q036

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.18。

**原題：**利用HPLC 定量飲料中之維生素B2(riboflavin)含量時,下列何種偵測器有最好的選 擇性?

(A) UV detector

(B) fluorescence detector

(C) evaporative light-scattering detector

(D) refractive index detector

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**B2螢光配對；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**B2具可用螢光 → 激發與發射雙條件排除背景 → 最佳選擇性FL，B。

**其他選項／關鍵錯選：**A UV亦可有吸收但選擇性較低；C/D較廣泛響應，不能借此保證B2專一性。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20|L20]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l20|R20]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]。

</details>

### Q037｜110-1 #28｜多模式辨識

^hplc-c-q037

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.18。

**原題：**關於高效液相層析法之應用,下列何者正確?

(A) 使用粒徑篩析(size-exclusion)層析法時,苯丙胺酸的滯留時間比膠原蛋白短

(B) 相較於苯甲酸,苯甲醛更不易滯留在矽膠管柱上

(C) 氧化鋁通常用作離子交換充填劑的基礎材料

(D) 使用逆相管柱分離時,benzene 比amylbenzene 的滯留時間更長

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**多模式辨識；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**裸silica較強吸附benzoic acid → benzaldehyde較早 → B。

**其他選項／關鍵錯選：**A小胺基酸比collagen可進更多SEC孔，通常較晚；C alumina常是吸附相，不是該常用樹脂骨架；D benzene比amylbenzene在RP較早。

**條件／易錯與來源边界：**分子大小、電荷、疏水性三把尺不要混在同一句。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|L05]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05|R05]]。

</details>

### Q038｜110-1 #32｜強RP移動相

^hplc-c-q038

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.18–19。

**原題：**採用C18 管柱分析betamethasone 時,下列移動相何者可使分析物的滯留時間最短?

(A) methanol-water(30:70)

(B) methanol-water(20:80)

(C) acetonitrile-water(30:70)

(D) acetonitrile-water(70:30)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**強RP移動相；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**C18 RP → D含70%ACN，比其他配方強沖提 → betamethasone最早。

**其他選項／關鍵錯選：**A/B MeOH比例低；C僅30%ACN；題本溶劑種類與比例同時指向D。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|R11]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c01|C01]]。

</details>

### Q039｜110-1 #33｜五類固醇原圖

^hplc-c-q039

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.19。

**原題：**下圖5 個皮質類固醇化合物利用C18 層析管,以甲醇/水(75:25)為移動相沖提, 則下列何者的滯留時間排第3 位?

<img src="data:image/png;base64,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zJcdmOISeABpqArpvEajEU5SQoher5dIJMh7bNWq1caNG3///XeYt3fv3r179+7EiROxjcN9PGvWrP3798+bN2/8+PHDhg2rXLlyaGgoknEQriQeXA3WyfXr15csWXLu3Ln69esvXLgQy4lhGJ1Ox+Px4C5AcTibzRYSErJ06dJVq1YtW7bszp07derUadSoUVRUFLrV399fp9NZrVY4kWEtXrt2bfny5ceOHatbt+7SpUvLlStHCFGr1UAl4tAAzY5tdtq0aZ07d164cOGyZcsOHDjwwQcflCxZEtpEJpMhbIU1PH/+/H379nG53MGDBycmJmKTi4qKat++PYLgOKlVqlTp448/Lq7xghJn/5WBxO12m81mbB5wieB4PmLEiJ9//tkblH38+HGBQFCpUiVM1ipVqlSsWLFVq1bLly+fPn161apVO3ToULJkyRIlSmAluLzE6XSeOHFizZo1aWlpNWvW7NixY4UKFYA9oCEH7NywYfHN4MGDk5OTly9f/tNPP61evXrMmDFhYWGlS5cWiURly5a9du2av78/yDo4HM758+d///3327dvV69evUePHlWqVMFW4XK5cNwhHhMMJ2K73V6tWrWVK1ceOnRozZo1kydPbty4cZcuXcLCwuDDoTFGNps9bNiwTz75BI1gh3C73QkJCVFRUVKp1Gg0AoRTqlSpsLAwhCXByeNyue7cubNr1y6HwzFmzBgED/bu3Xv48GG45h89etS9e/eXGkcoEYwXy8OLQm1k2P5wi61atapx48b9+/cnhAQFBVWqVOnixYtbtmzBPlRcQVGz2SyRSADdAXIJqB4601h/xWXjFVAXFBG1wikTvONnwJ4BqoABgmbA7cCNmpubi1FmPNxKZcqUycnJyc3NFYvFgD8plcqAgAC73R4TE6NUKg8ePIiDCzAqd+/evXnzJiLhjx8/hikAG8tsNgOpEhkZmZubq9VqlUoliCguXLjw4MGDFi1aEELgiTWbzQ0aNJg4cSIeIysra9GiRfDEqlQqDoeDGjgU04GOemMKnZLfItQjl8sTEhL8/f1p8B2BppIlSzocjhYtWvj7++/du/fAgQMcDkehUCxZsgSlNXFkw0GpcePGderUWbJkydSpU2vWrNmpU6dmzZohJx42LJw8jx8/3rx58/79+4OCgr766qtGjRrhSaBhYaRTGLjb7Yb94nA4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" alt="Q039原題圖，CH20 PDF p.19" width="760" />

(A) betamethasone

(B) betamethasone 21-valerate

(C) betamethasone 17-valerate

(D) betamethasone 17,21-dipropionate

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**五類固醇原圖；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**按原圖與題本短→長5藥次序 → 第3為betamethasone17-valerate → C。

**其他選項／關鍵錯選：**A betamethasone第2；B21-valerate第4；D17,21-dipropionate第5；prednisolone第1非選項。

**條件／易錯與來源边界：**17與21酯位置次序需記此方法；碳數或OH數相同，不能單憑這兩點強推。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|L07]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l07|R07]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f20|F20]]。

</details>

### Q040｜109-2 #27｜RP常用溶劑

^hplc-c-q040

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.19。

**原題：**以 C18 HPLC 分析 prednisolone 和 betamethasone 時,下列移動相溶劑何者不適 用?

(A) 甲醇(methanol)

(B) 乙腈(acetonitrile)

(C) 氯仿(chloroform)

(D) 四氫呋喃(tetrahydrofuran)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**RP常用溶劑；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**題本是一般含水RP常用移動相 → MeOH/ACN/THF皆常見 → chloroform不適用該慣用配對，C。

**其他選項／關鍵錯選：**A/B/D與水在常用範圍混溶且有RP方法。

**條件／易錯與來源边界：**不能說所有RP或特殊LC永遠禁止chloroform；要看完整配方與材質。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04|L04]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04|R04]]。

</details>

### Q041｜109-2 #28｜ibuprofen影響最大

^hplc-c-q041

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.20。

**原題：**下列 pH 值變動,何者對 ibuprofen(pKa 4.4)在逆相層析法的滯留時間有最大的影 響?

(A) pH 2 → pH 3

(B) pH 4 → pH 5

(C) pH 6 → pH 7

(D) pH 8 → pH 9

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**ibuprofen影響最大；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**ibuprofen弱酸pKa4.4 → pH4→5跨過主要解離區 → 中性比例變動最大 → B。

**其他選項／關鍵錯選：**A2→3兩端多中性；C6→7與D8→9兩端多離子，變動較小。

**條件／易錯與來源边界：**以此題同一分析物、近似兩態RP保留模型作比較。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10|L10]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l10|R10]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c03|C03]]。

</details>

### Q042｜109-2 #29｜時間調整反向題

^hplc-c-q042

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.20。

**原題：**利用逆相層析建立 diclofenac 的不純物分析方法時,下列何者無法減少分析時間?

(A) 增加移動相流速

(B) 增加移動相中有機溶劑之比例

(C) 增加移動相中水相之比例

(D) 增加移動相之梯度變化速度(斜率)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**時間調整反向題；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**問「無法減少」 → RP水增加常減弱沖提 → tR不縮短 → C。

**其他選項／關鍵錯選：**A加F可加快通過；B加有機相常更強；D更陡梯度常更快。

**條件／易錯與來源边界：**A/B/D仍要核對不純物峰Rs與檢出能力，時間短不等於方法好。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|L12]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l12|R12]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f24|F24]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c11|C11]]。

</details>

### Q043｜109-2 #32｜C8/C18題本爭議

^hplc-c-q043

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.20–21。

**原題：**下列有關逆相層析與正相層析之敘述,何者錯誤?

(A) 強陰離子交換樹脂可用於逆相層析

(B) 甲醇可用於正相層析與逆相層析

(C) HILIC 管柱分離效果通常較接近正相層析

(D) 相較於 C18 管柱,高極性樣品在 C8 管柱之滯留時間較短

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**C8/C18題本爭議；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**題本選D，並在說明宣稱高極性物在C8更晚；這是本版保留的題本答案身分。

**其他選項／關鍵錯選：**B MeOH可用不同模式；C HILIC親水保留常接近NP；A只有兼具疏水與交換作用的混合模式相等情形可與RP並論。

**條件／易錯與來源边界：**科學上不能單憑C8/C18名稱普遍推高極性物tR。可比相C8通常疏水保留較弱；A措辭也過寬。本題需保留爭議，不編成必然定律。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|R08]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f21|F21]]。

</details>

### Q044｜109-2 #38｜經典離子對試劑

^hplc-c-q044

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.21。

**原題：**下列何者非用於離子對-逆相液相層析之離子對試劑?

(A) sodium heptanesulfonate

(B) ammonium acetate

(C) tetrabutylammonium chloride

(D) sodium decanesulfonate

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**經典離子對試劑；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**經典RP離子對須有合適疏水端 → ammonium acetate通常是緩衝鹽 → B。

**其他選項／關鍵錯選：**A/D為帶負電的烷基磺酸鹽；C四丁基銨為帶正電的疏水季銨。

**條件／易錯與來源边界：**緩衝離子也可影響保留，不代表acetate完全不參與任何離子相互作用。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|L14]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14|R14]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f09|F09]]。

</details>

### Q045｜109-2 #39｜pH8.4與缺字動相

^hplc-c-q045

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.21。

**原題：**下列四個藥物使用 C18 管柱進行液相層析,若以 acetonitrile : ㄑ-HCl(60:40, v/v;pH=8.4)為動相,則那一個藥物之滯留時間最短?

<details>
<summary>展開缺字原印截圖</summary>

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABAAAAAEKCAIAAAAD3LAVAAAACXBIWXMAAA7EAAAOxAGVKw4bAACaNklEQVR4nOy9e7hNVf/3v8h2PuecRwhFSSjJqRxDSN2OFSF0oFLRtxNXhR4U7lKEUEkqd1Tu6kZ0k2OFipKcCSF8EYW0ntdvfS7jN8zTmmvtvbHbn9cf+1p7zjHnHHPMcXi/5xyHSDQc//M///N//+//DRlYURRFURRFUZQ04f/8n//zv//7v2l4wkjIcGoAFEVRFEVRFOXsowZAURRFURRFUTIRagAURVEURVEUJROhBkBRFEVRFEVRMhFqABRFURRFURQlE5H2BuBAODAAQ4cODRlYURRFURRFUZQ04bLLLktjA1AuHDfFCBlYURRFURRFUZQ0oXr16toFSFEURVEURVEyCzoGQFEURVEURVEyEWoAFEVRFEVRFCUToQZAURRFURRFUTIRagAURVEURVEUJROhBkBRFEVRFEVRMhFqABRFURRFURQlE6EGQFEURVEURVEyEWoAFEVRFEVRFCUToQZAURRFURRFUTIRagAURVEURVEUJROhBkBRFEVRFEVRMhFqAKInT578OhX89NNP5lS//fbbxnj8+eefjgisXbv25ptvPnHihL1x27ZtcU/l5tdff/W8x/Hjxw8ZMiStUmzOnDlE2L1969atNWvWPHLkSJiTPPXUUyNHjnRsfDFGQpGZMWPG22+/7d7+3nvvvfTSS2HOwEP8T4J8++23CUUyI9K1a9fXXnvNc9cff/zRokWLlStXhjkP2bJatWrHjx93bN+1a1eHDh3i5pYlS5Y8++yznrvuvffeESNGRGMZb9SoUWEiI1BO77///n379oU/xEBmmzJlSkCAMWPG9OnTJ6Fzks4vv/xyEpER9uzZ82PikAieZ/vll1+uv/56/sa9LlXZxx9/PHv27KRjHp6+fft61gw8js6dOwcfSwVLcxPyQj/88MMll1yyefPmhKOopJr169fzsNxNpJIcP//8M+l56NChcx0R5TwlYxiAw4cPIzpRsa+88grtTbBo4H4++OCDsWPHvvXWW4iPuCdHNEdSwY033mhONWvWrLjhKZNUcLYe+u9//8t2RJUdq0svvTSJyDzyyCOe99igQYP+/fuTMnlCY2phfmw9EyROmTJl5Pfu3btxUPJ7/vz5xOG7776zA+/d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BgzImzevnIGbIqoOr+UwAPfddx//tm7d2rM3F7GaPn36tddea99+lSpVsHCeiRmMDJV+8803A8LItTyHlzzxxBPsGjFihL3xjTfeYCP5Non4KIqiKIqipJ4MYACKFy9+6aWX+u295pprkFNffvml/Nu0aVP+nTp1qmdgtsfVXlu3biXM5ZdfPmzYMLRvu3btRo4cye86deqwPVu2bOhvd+CBAwdmz54d8XrTTTehnu1d9sk9DUDPnj3ZmDNnTnT2qFGj0Itt2rQR5fr88887oicdTkQBE3L06NEchZheu3atBJCRpqVKlUK8cjjpLB6mRo0a9gw8Mm5VjJPjXu6///4CBQrgZ1566aW+ffvmypWL7bfffrsjJnfeeSfbixQpgo4n2nfddVeOHDncie/5+OTq9957LymGYePHiy++iHEqV66cRN42DLYBeOGFF/iN//HzeKRtJDYet0OHDjyIwYMHSw7Jly+f8UghOXToEOcpXLhwwCcdaNasGefnjty7HnnkEXb169fP3kg02NipU6eEIqMoiqIoipJWnO8GYN26daIUPffK7I22vpw2bRpbrr/+es/wyEr2duzYMeCKooPz5s2LCP7iiy/sXShUdqGnzWT2EhhtirJfs2aN+zxxDcDLL7/MlrJly27cuNEO+dlnn6Gns2TJYrwNfPDBBwQmYo73zXv37jWz1M+ePRtXYE+3v2/fPnmdb8+V6WcAsDFlypSxp+tZsmSJfG2wX8yPHTtWPonY9yIhEfRmtnu/xydX50YqV65sa32ktgzmRr6bjcYAiLepUqXKgQMHoj4QH6yI3W3pzz//JD9wICbN7yhPxowZw1H9+/cPDvbUU09FYmPQHdtPnTolg1KIj2NXhQoVSpQokVBkFEVRFEVR0orz3QB89NFHSChUsufehx56iL1Dhw41W44dO5YvXz42+nVJZ2+NGjUCrig6GNC4jl1IOumoM2vWLEdgRzePaDgDcPz48WLFirHFvW4UPP300+xq3769uXqlSpXY4u5mE5d77rmHA4cNG2a2+BkAwEI4DpfvKuYlN9EuXrw4Wt/heaKnO/yYkH6PT67OGcyHCwN+ICUl5YILLsDVyBYxALli8MN9SFzeffddDrzxxhsTOuqyyy7jKIcxc0O6EWFHhsF1kOZinNyDUlq3bs32I0eOJBQfRVEURVGUNOF8NwCTJ09G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" alt="Q045原印缺字，CH20 PDF p.21" width="920" />

</details>

(A) prilocaine(pKa 7.9)

(B) bupivacaine(pKa 8.1)

(C) morphine(pKa 8.4)

(D) procaine(pKa 9.0)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**pH8.4與缺字動相；按原題的正確／錯誤／最長／最短／無法问法回答。

**原印答案：**空白。**題本說明／編輯推論：**D（procaine），不是冒稱原印D。

**最短完整解題鏈：**pH8.4下pKa9的procaine較多BH⁺ → 題本說明指其極性／離子態較多、RP較早 → 編輯選D。

**其他選項／關鍵錯選：**A/B pH高於pKa，中性比例較高；C pH=pKa近各半。

**條件／易錯與來源边界：**◆答案欄空白，不能稱原印答案D；動相名印作「ㄑ-HCl」缺漏，保留原圖，不自行填成Tris。跨藥物精確tR仍需兩態保留資料。

**答案身分：**原印◆答案空白；題本說明列procaine，編輯推論D；動相名稱缺字。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10|L10]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l10|R10]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c04|C04]]。

</details>

### Q046｜109-2 #40｜UV耐變性

^hplc-c-q046

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.22。

**原題：**相較於螢光光譜分析法,UV 光譜分析法之優勢為下列何者?

(A) robustness 較佳

(B) selectivity 較佳

(C) system suitability 較佳

(D) sensitivity 較佳

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**UV耐變性；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**UV只需吸收等基本設定，FL還受激發、發射及淬熄等影響 → 題本選耐變性robustness A。

**其他選項／關鍵錯選：**B選擇性與D靈敏度是題本FL優勢；C system suitability是整個方法按規定檢查，不是單憑偵測器名勝出。

**條件／易錯與來源边界：**實際robustness要試驗小幅條件變動，教材排序不是通用性能保證。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20|L20]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l20|R20]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f14|F14]]。

</details>

### Q047｜109-1 #8｜非慣用RP溶劑

^hplc-c-q047

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.22。

**原題：**下列何者不是逆相層析法常用之溶媒?

(A) methanol

(B) acetonitrile

(C) ethyl acetate

(D) tetrahydrofuran

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**非慣用RP溶劑；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**一般含水RP慣用MeOH、ACN、THF → ethyl acetate不屬此組常用配方 → C。

**其他選項／關鍵錯選：**A/B/D是題本常用RP溶媒。

**條件／易錯與來源边界：**「不是常用」不是「任何特殊RP配方都不可用」。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04|L04]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04|R04]]。

</details>

### Q048｜109-1 #10｜一律給分註記

^hplc-c-q048

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.22。

**原題：**下列何檢品之分析一般不用HPLC?

(A) vitamins

(B) nonsteroidal anti-inflammatory drugs

(C) aminoglycoside antibiotics

(D) heparin sodium

**另印給分註記：**（E）一律給分（題本另列的給分註記）。

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**一律給分註記；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**（E）一律給分；保留另印註記，未取得官方公告。

**最短完整解題鏈：**題本另列(E)一律給分 → 本題依來源給分註記保存，不指定A–D中唯一正確化學答案。

**其他選項／關鍵錯選：**A vitamins、B NSAIDs、C aminoglycosides及D heparin sodium都有可考慮的LC方法。

**條件／易錯與來源边界：**未取得官方公告；不得稱已核對官方一律給分，也不以此題證明肝素不能HPLC。

**答案身分：**題本列(E)一律給分；沒有另核對官方給分公告。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|L01]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l01|R01]]。

</details>

### Q049｜109-1 #34｜弱鹼升pH方向

^hplc-c-q049

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.23。

**原題：**Pentycaine(pKa 8.1)使用逆相層析管柱分析,當動相組成為Tris-乙腈(4:6)(pH 8.5)時,其滯留時間為 26 分鐘。下列方法何者無法減少 pentycaine 的滯留時間?

(A) 提高乙腈比例

(B) 提高分析溫度

(C) 提高緩衝溶液pH 值

(D) 改用酸性緩衝溶液

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**弱鹼升pH方向；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**弱鹼pKa8.1 → 升pH中性B比例增加 → 常增加RP保留 → 無法縮短為C。

**其他選項／關鍵錯選：**A加ACN常強沖提；B提高溫度是題本加快情境；D酸化增BH⁺常加快。

**條件／易錯與來源边界：**26 min是來源初始條件；改pH未給新k′，不能精確計算新tR。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|L09]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09|R09]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c04|C04]]。

</details>

### Q050｜109-1 #37｜四種保留機制

^hplc-c-q050

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.23。

**原題：**下列有關液相層析之敘述,何者正確?

(A) 靜相為silica gel 時,極性較小的成分先沖提出

(B) 靜相為ODS 時,極性較大的成分先沖提出,此稱為正相分離

(C) 靜相為陽離子交換樹脂時,檢品中的陽離子比陰離子更快沖提出

(D) 靜相為分子排斥性的充填劑時,分子較小的化合物滯留時間較短

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**四種保留機制；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**silica是極性吸附相 → 較少表面作用的低極性物常先出 → A。

**其他選項／關鍵錯選：**B ODS方向合理但名字應RP；C陽交換通常留陽離子；D SEC小者常較晚。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|L05]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05|R05]]。

</details>

### Q051｜109-1 #38｜梯度非離子物偵測

^hplc-c-q051

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.24。

**原題：**以高效能液相層析法分析非離子性界面活性劑時,如使用梯度法沖提,下列何者為最適 當之偵測器?

(A) fluorescence detector

(B) UV-visible detector

(C) refractive index detector

(D) evaporative light scattering detector

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**梯度非離子物偵測；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**非離子界面活性劑缺有效光學基團且要梯度 → ELSD可用 → D。

**其他選項／關鍵錯選：**A需有效螢光；B需強吸收；C RI通常受梯度組成影響而不適合。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|L22]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22|R22]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f15|F15]]。

</details>

### Q052｜108-2 #9｜中性物與pH

^hplc-c-q052

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.24。

**原題：**以HPLC 分析中性待測物,下列動相之條件何者對其滯留時間影響最小?

(A) 流速

(B) pH 值

(C) 黏稠度

(D) 組成

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**中性物與pH；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**中性待測物在該pH不解離 → pH對自身電荷影響小 → B。

**其他選項／關鍵錯選：**A流量、D組成直接影響時間；C黏度與運輸條件可相關，須分F與壓力設定。

**條件／易錯與來源边界：**表面解離或溶劑改變仍可能影響中性物，不說pH完全沒作用。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|L09]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09|R09]]。

</details>

### Q053｜108-2 #10｜混合溶劑pH

^hplc-c-q053

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.24。

**原題：**配製液相層析之動相時,乙酸緩衝液中加入乙腈時,會使其pH 值產生下列何種變化?

(A) 增加

(B) 減少

(C) 不變

(D) 隨乙腈加入之百分比增加而降低

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**混合溶劑pH；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**題本記載乙酸緩衝液加入ACN後pH增加 → 保存A；混合溶劑需實測及一致尺度。

**其他選項／關鍵錯選：**B/C/D都不符合本題記載；不以單純強酸稀釋公式推此題。

**條件／易錯與來源边界：**乙酸／乙酸根同比稀釋比值可不變；ACN另改活度、pKa與電極讀數。題目未給完整比例與量測基準，不能普遍定量外推。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10|L10]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l10|R10]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f23|F23]]。

</details>

### Q054｜108-2 #11｜silica結構比較

^hplc-c-q054

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.25。

**原題：**有關液相層析法的敘述,下列何者正確?

(A) 溫度不會影響滯留時間

(B) 靜相為silica gel 時,benzyl alcohol 比benzoic acid 的滯留時間短

(C) 逆相層析法的動相為低極性的有機溶劑

(D) 動相的組成不影響滯留時間

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**silica結構比較；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**題定裸silica對COOH作用較強 → benzoic acid較晚，benzyl alcohol較早 → B。

**其他選項／關鍵錯選：**A溫度可能影響；C一般RP是水＋有機的相對較極性相；D組成會改沖提力。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|L05]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05|R05]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f03|F03]]。

</details>

### Q055｜108-2 #12｜C18全名

^hplc-c-q055

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.25。

**原題：**下列何者為逆相層析所用之C18 管柱充填劑?

(A) octadecyl silane-bonded silica particles

(B) octyl silane-bonded silica particles

(C) phenyl silane-bonded silica particles

(D) silica particles

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**C18全名；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**C18是18碳octadecyl鍵結相 → octadecyl silane-bonded silica → A。

**其他選項／關鍵錯選：**B octyl是C8；C phenyl為另一選擇相；D裸silica為常用NP吸附相。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|R08]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f05|F05]]。

</details>

### Q056｜108-2 #33｜丁烷丁醛丁酸

^hplc-c-q056

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.26。

**原題：**下列三種化合物a:CH3CH2CH2CH3;b:CH3CH2CH2CHO;c:CH3CH2CH2COOH 以矽膠 管柱(silica gel column)配合適當溶媒進行分離,其滯留時間(tR)值關係為何?

(A) a>b>c

(B) b>a>c

(C) a>c>b

(D) c>b>a

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**丁烷丁醛丁酸；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**題定silica表面作用 → 丁酸c強於丁醛b強於丁烷a → tR c>b>a → D。

**其他選項／關鍵錯選：**A/B/C都把最弱作用的烷烴放得太晚，或将酸錯排。

**條件／易錯與來源边界：**這是同骨架題定比較；不是任意不同碳數的官能基全排序。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|L05]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05|R05]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f03|F03]]。

</details>

### Q057｜108-2 #34｜四丁基銨對象

^hplc-c-q057

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.26。

**原題：**下列何者最適合加入tetra-n-butylammonium hydroxide 於動相中,以C18 管柱進行 層析分析?

(A) CH3CH2CH2CH2NH2

(B) CH3CH2CH2COOH

(C) CH3CH2CH2CH2OH

(D) C6H5Cl

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**四丁基銨對象；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**試劑四丁基銨帶正電 → 需要陰電分析物 → butyric acid可解離為butyrate → B。

**其他選項／關鍵錯選：**A胺在酸性帶正電；C醇一般不顯著解離；D氯苯中性。

**條件／易錯與來源边界：**含OH不等於都有足夠解離可作此離子對。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|L14]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14|R14]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f09|F09]]。

</details>

### Q058｜108-2 #38｜幫浦角色

^hplc-c-q058

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.26–27。

**原題：**高效能液相層析儀所使用的泵(pump),其功能與下列何者有關?

(A) 檢測波長

(B) 滯留時間

(C) 層析溫度

(D) 檢品注入量

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**幫浦角色；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**幫浦送移動相，F改變通過時間 → 對應tR → B。

**其他選項／關鍵錯選：**A波長屬檢測器；C溫度屬柱溫控制；D注入量屬進樣器。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02|L02]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l02|R02]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f01|F01]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c02|C02]]。

</details>

### Q059｜108-1 #11｜軟膏基質萃取

^hplc-c-q059

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.27。

**原題：**下列何種溶劑組合最適合用於去除hydrocortisone 軟膏之基質?

(A) water-chloroform

(B) water-n-butanol

(C) acetonitrile-hexane

(D) MeOH-hexane

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**軟膏基質萃取；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**軟膏油性基質需分相處理 → MeOH與hexane可分配藥物／油性成分 → 題本最佳D。

**其他選項／關鍵錯選：**A/B也可能分相但不是題本推薦藥物回收組合；C雖可兩相，不能僅有分相就稱同樣最適。

**條件／易錯與來源边界：**需驗證hydrocortisone回收率、萃取次數與層的取用；別把任意分層當去基質成功。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04|L04]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04|R04]]。

</details>

### Q060｜107-2 #12｜氯離子與IC

^hplc-c-q060

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.27。

**原題：**測定檢品中氯離子濃度時,配合適當偵測器使用,下列何種方法最適宜?

(A) 配位滴定法

(B) 原子吸收光譜法

(C) 氣相層析法

(D) 離子層析法

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**氯離子與IC；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**Cl⁻為無機陰離子 → 離子交換分離再偵測 → IC，D。

**其他選項／關鍵錯選：**A配位滴定通常測金屬配位；B原子吸收通常測元素原子；C常規GC不直接適合氯離子。

**條件／易錯與來源边界：**常用IC＋抑制型電導。PAD是另一電流法，不能把「氯→IC」偷換為「氯必→PAD」。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21|L21]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l21|R21]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f08|F08]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f26|F26]]。

</details>

### Q061｜107-2 #13｜嗎啡類最短

^hplc-c-q061

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.27–28。

**原題：**以ODS 管柱在pH 8.0 之緩衝溶液下進行高效液相層析分離時,下列何種嗎啡類化合物 的滯留時間會最短?

(A) morphine

(B) normorphine

(C) ethylmorphine

(D) 3-O-benzylmorphine

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**嗎啡類最短；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**題定pH8與ODS比較嗎啡類 → normorphine缺N-methyl、較親水 → 最短B。

**其他選項／關鍵錯選：**A morphine、C ethylmorphine、D benzylmorphine在該題較疏水／較晚。

**條件／易錯與來源边界：**精確排序同時受pKa與相作用；此處保存來源同條件比較，不跨pH一律外推。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|L07]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l07|R07]]。

</details>

### Q062｜107-2 #32｜苯乙酸離子對

^hplc-c-q062

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.28。

**原題：**以離子對-逆相層析法(ion-pairing chromatography) 進行苯乙酸(C6H5 CH2 COOH)之分析定量時,動相加入下列何者可使待測物之滯留時間 最久?

(A) C7 H15SO3 Na

(B) (CH3 )4 NCl

(C) (C4 H9 )4 NCl

(D) C5 H11SO3 Na

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**苯乙酸離子對；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**苯乙酸陰電態配正電季銨 → 四丁基銨較四甲基銨疏水 → C最留。

**其他選項／關鍵錯選：**A/D烷基磺酸鹽帶負電；B正電但較短。

**條件／易錯與來源边界：**選项(CH₃)₄NCl與(C₄H₉)₄NCl按鹽提供的陽離子判，不拿Cl⁻當疏水配對者。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|L14]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14|R14]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f09|F09]]。

</details>

### Q063｜107-2 #34｜PEG配對

^hplc-c-q063

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.28。

**原題：**Polyethylene glycol 類聚合物之定量分析,下列何種層析法與檢測器之配對最適當?

(A) 氣相層析法-電子捕獲檢測器

(B) 氣相層析法-熱傳導檢測器

(C) 高壓液相層析法-紫外光檢測器

(D) 高壓液相層析法-揮發光散射檢測器(ELSD)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**PEG配對；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**PEG聚合物不易常規GC直接分析且弱UV → HPLC分離、ELSD讀粒子 → D。

**其他選項／關鍵錯選：**A/B是GC配對但不合此直接定量條件；C没有足夠強UV基團。

**條件／易錯與來源边界：**PEG分布也能SEC；本題是在方法與偵測器配對中選D。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|L22]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22|R22]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]。

</details>

### Q064｜107-2 #37｜醣類固定相

^hplc-c-q064

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.29。

**原題：**下列那個層析管柱最適用於醣類分析?

(A) ODS 管柱

(B) aminopropyl silica gel 管柱

(C) 陽離子交換管柱

(D) 陰離子交換管柱

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**醣類固定相；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**題本常見糖分離相為aminopropyl silica → B。

**其他選項／關鍵錯選：**A常規C18對未衍生化親水糖保留可能不足；C/D依其他條件也可有糖方法，不是化學上均不能用。

**條件／易錯與來源边界：**anion-exchange＋PAD是有效醣分析組合，原題單選採B不能當排除所有其他方法的證明。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|R08]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f04|F04]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f26|F26]]。

</details>

### Q065｜107-1 #10｜已知蛋白親脂序

^hplc-c-q065

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.29。

**原題：**使用ODS 管柱分析4 種蛋白質(I-IV),其親脂性大小為I>II>III>IV,以一般蛋白質 之分析條件進行梯度沖提而得到適當分離,則滯留時間最長者為:

(A) I

(B) II

(C) III

(D) IV

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**已知蛋白親脂序；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**題已給疏水性I>II>III>IV且RP梯度分離適當 → 最親脂I最晚 → A。

**其他選項／關鍵錯選：**B/C/D題定疏水性較小；不另用分子量重排。

**條件／易錯與來源边界：**蛋白在RP可能變性，方法須適用；此題已限定可取得適當分離。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06|L06]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06|R06]]。

</details>

### Q066｜107-1 #13｜內標相近tR

^hplc-c-q066

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.29。

**原題：**有關液相層析法所使用的內部標準品之敘述,下列何者正確?

(A) 比待測成分的分子量小

(B) 與待測成分有相近的滯留時間

(C) 不具紫外光或可見光的吸收

(D) 能與待測成分發生化學反應

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**內標相近tR；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**IS與分析物需经歷相近條件且峰能分辨 → tR相近但不重疊 → B。

**其他選項／關鍵錯選：**A不必總分子量較小；C須能被所選偵測器偵測；D不應與分析物反應。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|L23]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23|R23]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f18|F18]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c07|C07]]。

</details>

### Q067｜107-1 #34｜RP溶劑強度

^hplc-c-q067

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.30。

**原題：**①Acetonitrile ②water ③tetrahydrofuran ④methanol 用於逆相液相層析法,其溶 劑強度(solvent strength)由大至小順序為何?

(A) ①③④②

(B) ②①④③

(C) ③①④②

(D) ④①②③

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**RP溶劑強度；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**題本RP強度THF>ACN>MeOH>water → ③①④② → C。

**其他選項／關鍵錯選：**A把ACN置THF前；B把水排最強；D把MeOH排THF前。

**條件／易錯與來源边界：**溶劑種類也改選擇性，不保證同百分率時每個分析物都同一保留次序。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|R11]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f02|F02]]。

</details>

### Q068｜107-1 #39｜乳酸內標

^hplc-c-q068

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.30。

**原題：**以高效液相層析法分析生物檢體中的乳酸(CH3 CH(OH)COOH)濃度時,下列何種化 合物為最適當之內部 標準品?

(A) 丙醛(C2 H5 CHO)

(B) 丙酸(C2 H5 COOH)

(C) 丁酸(C3 H7 COOH)

(D) 甲基乙二醛(CH3 COCHO)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**乳酸內標；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**乳酸是小羧酸 → 選結構與方法行為可比的丙酸 → B。

**其他選項／關鍵錯選：**A丙醛與D二羰基不同；C丁酸較長一碳，相較B較不相近。

**條件／易錯與來源边界：**實際還須樣品本底不干擾、峰分開及回收相似；相似結構不是唯一標準。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|L23]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23|R23]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f18|F18]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c07|C07]]。

</details>

### Q069｜107-1 #40｜THF互溶

^hplc-c-q069

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.30。

**原題：**下列何者與水之互溶性最佳?

(A) tetrahydrofuran

(B) ethyl acetate

(C) chloroform

(D) diethyl ether

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**THF互溶；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**THF的氧可接受水的氫鍵、常與水混溶 → A。

**其他選項／關鍵錯選：**B ethyl acetate、C chloroform、D ether不如THF與水完全混溶。

**條件／易錯與來源边界：**不叫「似氫鍵」；同理ACN也可接受氫鍵，不能以無OH就判不混水。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04|L04]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04|R04]]。

</details>

### Q070｜106-2 #2｜室溫兩相

^hplc-c-q070

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.31。

**原題：**下列何種溶劑組合在室溫下會分成兩相?

(A) water-ethanol

(B) water-tetrahydrofuran

(C) methanol-n-hexane

(D) methanol-chloroform

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**室溫兩相；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**室溫常用二元組合 → MeOH/n-hexane常分成兩相 → C。

**其他選項／關鍵錯選：**A water/ethanol、B water/THF、D methanol/chloroform一般可混溶。

**條件／易錯與來源边界：**溫度、比例與鹽會改互溶；題本以通常室溫條件比較。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04|L04]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04|R04]]。

</details>

### Q071｜106-2 #31｜silica官能基

^hplc-c-q071

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.31。

**原題：**於矽膠(silica gel)管柱層析,以適當比率之正己烷-二氯甲烷為沖提液,下列何者滯 留時間最長?

(A) C6 H13OH

(B) C4 H9 COCH3

(C) C3 H7 OC3 H7

(D) C5 H11CHO

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**silica官能基；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**類似六碳骨架 → alcohol的OH與silica作用較強 → C₆H₁₃OH最留，A。

**其他選項／關鍵錯選：**B ketone、C ether、D aldehyde有不同表面作用，題定下不及醇。

**條件／易錯與來源边界：**此題不能證明所有含OH的大／小分子都比所有酸或胺保留長。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|L05]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05|R05]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f03|F03]]。

</details>

### Q072｜106-2 #32｜磺酸強陽交換

^hplc-c-q072

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.31。

**原題：**以含SO3H 基團之樹脂為固定相,係指何種層析?

(A) strong cation exchange

(B) strong anion exchange

(C) weak cation exchange

(D) weak anion exchange

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**磺酸強陽交換；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**SO₃H在廣pH下可為SO₃⁻ → 負電抓陽離子 → strong cation exchange A。

**其他選項／關鍵錯選：**B/D抓陰離子須正電相；C弱陽交換常用COOH/COO⁻。

**條件／易錯與來源边界：**SO₃⁻叫磺酸根，不是SO₄²⁻硫酸根。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13|L13]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l13|R13]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f07|F07]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c05|C05]]。

</details>

### Q073｜106-2 #35｜mannitol偵測

^hplc-c-q073

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.32。

**原題：**使用液相層析法分析製劑中的甘露醇(mannitol)時,下列何種偵測器不適用?

(A) 紫外光偵測器

(B) 蒸發光散射檢測器

(C) 質譜儀

(D) 折射率偵測器

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**mannitol偵測；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**mannitol無強常規UV發色基 → 直接UV不適用題定方法 → A。

**其他選項／關鍵錯選：**B ELSD量粒子；D RI量折射差；C適當LC-MS可檢測。

**條件／易錯與來源边界：**不把缺UV改寫成所有偵測器都不能用；衍生UV是另一方法。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|L22]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22|R22]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f17|F17]]。

</details>

### Q074｜106-1 #36｜bupivacaine延長題

^hplc-c-q074

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.32。

**原題：**使用逆相層析法分析bupivacaine(pKa 8.1),動相組成為乙腈/0.1 M Tris(pH 9.0)(8:2),bupivacaine 在一分鐘內被沖提出,下列何種作法無法延長bupivacaine 的滯留時間?

(A) 降低乙腈的比例

(B) 使用更長的管柱

(C) 將緩衝溶液改為乙酸(pH 5.0)

(D) 降低流速

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**bupivacaine延長題；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**問無法延長 → 酸化弱鹼增加BH⁺ → 常縮短RP保留 → C。

**其他選項／關鍵錯選：**A降ACN減弱沖提；B加長柱增路徑；D降F延長通過時間。

**條件／易錯與來源边界：**三種改動所改的是k′、柱路徑與時間尺度，不要全稱疏水性變大。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|L09]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09|R09]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c02|C02]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c04|C04]]。

</details>

### Q075｜106-1 #37｜較廣偵測範圍

^hplc-c-q075

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.33。

**原題：**下列使用於液相層析法的偵測器中,何者偵測範圍最廣?

(A) fluorescence detector

(B) UV-visible detector

(C) evaporative light scattering detector

(D) electrochemical detector

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**較廣偵測範圍；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**四選項中ELSD不要求光吸收、螢光或可電極反應 → 偵測範圍較廣 → C。

**其他選項／關鍵錯選：**A/B/D各有必要分子特徵；範圍廣不代表檢出最低量最佳。

**條件／易錯與來源边界：**ELSD仍受揮發性與相容性限制；不是所有物質等響應。

**答案身分：**題本106-1第一處#37（p.33）。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|L22]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22|R22]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f15|F15]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f17|F17]]。

</details>

### Q076｜106-1 #32｜內標tR距離

^hplc-c-q076

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.33。

**原題：**在層析法作定量分析選用的內部標準品(internal standard),下列何者錯誤?

(A) 安定性宜佳

(B) 其結構宜與分析物相似

(C) 其滯留時間應與分析物儘量遠離

(D) 與分析物不產生化學反應

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**內標tR距離；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**IS應與分析物行為相近、tR近而峰分開 → 盡量遠離不恰當 → C。

**其他選項／關鍵錯選：**A安定、B結構相似、D不反應均合理。

**條件／易錯與來源边界：**相近tR與峰重疊不同；不能用共流出來計兩個獨立面積。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|L23]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23|R23]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f18|F18]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c06|C06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c07|C07]]。

</details>

### Q077｜106-1 #37′｜RP模式辨識

^hplc-c-q077

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.33–34。

**原題：**有關逆相層析法的敘述,下列何者正確?

(A) 矽膠為常用之充填劑

(B) 靜相的極性較動相低

(C) 動相之極性由低至高

(D) 靜相為巨孔樹脂

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**RP模式辨識；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**一般RP疏水固定相低於含水移動相的極性 → B。

**其他選項／關鍵錯選：**A裸silica是NP；C RP梯度常增有機而非由低至高極性；D巨孔樹脂並非普通RP定義。

**條件／易錯與來源边界：**本題與Q075共用題本106-1#37，本版以#37′辨識；A若指矽膠核心而已需再分鍵結與裸表面。

**答案身分：**題本106-1第二處#37（p.33–34），本版加′辨識，不更改年份。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06|L06]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06|R06]]。

</details>

### Q078｜106-1 #38｜ECD縮寫

^hplc-c-q078

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.34。

**原題：**下列何者非高效能液相層析法之偵測器?

(A) UV-visible detector

(B) fluorescence detector

(C) electron capture detector

(D) electrochemical detector

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**ECD縮寫；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**electron capture是GC電子捕捉 → 非題定HPLC檢測器 → C。

**其他選項／關鍵錯選：**A UV、B FL、D electrochemical可與HPLC配合。

**條件／易錯與來源边界：**相同ECD縮寫一定先展開英文，不能只看字母選。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21|L21]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l21|R21]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f26|F26]]。

</details>

### Q079｜106-1 #40｜alanine題缺字

^hplc-c-q079

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.34。

**原題：**欲直接分析異構物 -alanine, -alanine,應選用下列何種靜相?

<details>
<summary>展開缺字原印截圖</summary>

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA/IAAADmCAIAAAD5ryl/AAAACXBIWXMAAA7EAAAOxAGVKw4bAABa9UlEQVR4nO29d3gVxcP+nRBCQktI6MgPQ2/SQRGBUBKlqXRUihQF6UXxSxEvpD1IkSrVgIqISBMQpQWkBkKLtFBCCSRAEoQntJCQ8t7vmct5ht09m00IHA7f+/NHrpzZ2Z3Z2T0zn9kzM+tywRr/+c9/xo8fbzEyIYQQQgghJEuoVavW//7v/6alh0tNa7Rp06Zt27YWIxNCCCGEEEKyhHr16lnS+nRjCP7zn//8z//8j8XIhBBCCCGEkCzh//2//0etJ4QQQgghxLmh1hNCCCGEEOL0UOsJIYQQQghxeqj1hBBCCCGEOD3UekIIIYQQQpweaj0hhBBCCCFOD7WeEEIIIYQQp4daTwghhBBCiNNDrSeEEEIIIcTpodYTQgghhBDi9FDrCSGEEEIIcXr+K7Q+ISFhwYIFqampN27c+PXXXzVb//rrr7Zt22b64L/88suMGTMytEubNm327t1ruCk4OPiLL77IaB5u3bo1ZsyY2NhY8fHEiRODbWzfvt3iETp16rR582YrMY8ePTp//nx9+JEjR/ZmhLNnzxoePykp6d1339VsjYuLQw7v378vQ86cOdOlS5d0c4vCnD59uiZwlo30T/VZgVM+efLk+fPnHZ0RJyMqKgrlFh8f7+iMOAe4zd57772NGzdajP/HH3+oH1GLRjxOSkoKKlVNoOHlOHz48OYM8vfff8vdHz16dPgJOHfunDzUvXv3ItIjOTlZk3/cZqiUUICGBfXpp59evHjRYqmagOYJVevKlSvtRUANHxoa+v3333/22We7d++2F23cuHFz5841TwtFGhYWNmXKlCVLltiLs3///r59+1rJOSHk+eF50XrZPNjLDZqQXbt2LV68GJXasWPHMnTwUaNGlStXDs3Shg0b3Nzcfv/9d3XrsGHD6tevn4k8C958880BAwZkaJfChQv/9ttvhpug9cjh5cuXM3RAOD2O+eDBA/ER1fFbb71VpkyZevXqWTzCyy+/jIK1t/Xu3bs7duzAxX3llVdcXFxw2MjISE2c8uXLu7q6uj1OtmzZEB9/NeEI7Ny5s2FaDx8+xNYDBw6ogSgQBKr3BjoGHh4e6Z4XUkH3RhNYtWrVmTNnprvvM0OcXeXKlZ9qKpDgatWqtWrVCi36U03omfHhhx+i3FavXv1UU5k0aZKfn9+mTZueairPhtGjRxcvXjwxMTHdmOHh4Z6entBHGYJvnMvj4PsIS9YELliwQH80VEcuGUStH27evJnR3VWQujzUunXr0o2PbwrMXi2lv/76C+GomvSnhsYIm65cuQLpf2gN2T3AP3v27Fm0aFGfPn1QKeE4qLS/+eab27dv497+4IMPOnTogPalTp06pUuXxuVAhHz58tWuXbtr165r1661d+06deqkVnpoOnH3Llu2bNasWcOHD+/YsWOtWrVQebq7uzdo0GDOnDn2jvPLL7+89NJLakibNm3y2wG5sncclTNnzvz888+4SVatWnX9+nUruxBCMsTzovXQLFGlGj5m2LdvX6lSpdSat2HDhqh8rRwZrVH27Nnl0/Fx48Z5e3urD1cqVaqEQJMjoLMRZoeDBw+icpw+fbq9CP/884/+gCZaD0qWLDlhwgQrpybA9fPy8tJ76uHDh1FQaJ6tHESj9egCzZ8/H21A+/btha+j0Jo3b442wN5zKUTTt+hCBfTNIZoxK1qP3e11D0SI/Ki5idGMiePrtR63jfVieTY8G61HIy2+O1nyZPF54NloPW5spAKReqqpZCEwJzc72OtmCwIDA9Xj7N69O2/evEOGDBEf8WVEPZNsQ3yJpNYjRRFes2ZNe1rft2/fZB1I8eOPP9aHo7TV+iE1NfWmHVBVotNlb6tA/QEBNVvUv+zcuROZ37BhQ9TjIAPfffed+n000foBAwYEBASk2aoai90Mf39/sS862NWrV69Xr17Pnj3h619//bU8LBR8ypQp33777dKlS3/99VcU4DvvvHPnzh17Fx0Vtce/oLrGJZYft27d2rJlS/QNcJBu3bp9+eWXqOqPHDmSbu9Or/VNmzZt3br17zpQCOh4mB9t48aNousiwS03cODAF+YpAyHPCc+F1p87d87T0zNXrlyGWg89Rd0ENf/ss882b96MuqZu3bqI+corr8jn0/a4du1a8eLF1afpaCFQC6MmTUlJwcdTp07hUOoPvnpQn3rbIUeOHKhA7W0FP/74o/6AqtaPGDFCswsqO5ysJtDeoJ0020/ARYsWRXOl34SC+uijj8yLSKDR+hs3boinXKNHj16+fDmabZSb+RGehtYnJSXdsHHo0CEEnj179sa/rF+/HoUvP2qy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Dro9OAK+NWI4luHrqBo2bDhNB3pKFrU+NDQUJSnWViKEPA2etdaLlRPTRfqEeKalLhsiEa11unP1NOupiyHUasOD9r5u3bqzZs2CQJgf6mmshCOAXMJBYZYy5Oeff86ZMydaU/PkBDExMZ6engsXLtRvGj58uDpAVnL79u127drJjxqtR/U9cOBANf4zGFsvpkDotb569eryx5B169ahWOTHU6dOuei0vlChQmi60NigWOTY+oSEBFxlNN6yUUcHslevXnIvFDjkI92zsw6aRrE8a/fu3dWx2mLUirnWi7cOFylSBPeJKhNi5Maz13ox18Kw35jlWD93jXBfunQJAoou+owZM3B7y2hz5sxxlNaLRW/0L6nIEKgEMjQjecqUKfI1dvhqoJ6UxxlriuHPlV9//TW+Nfhuullm4sSJ6hHQqfby8tJMcBI49i2zArR/NWrUwGUSb2sSZFrr0auU79LOkyePudajgsLtKhbn1Wg9MqD+vAz1L1mypBqir+2bNGnSqVMndbVl1JwZ0vo020xWOdAua98yKwgJCcExJ02aZCUyISQTPGuth+vYG74iZrZ99dVX+F8OuRZtuX7lMhwnf/78cFn9io0azLUexylRogRqGSTq6uoaGhpqcqinp/WNGjV65ZVX5Lw6XBI/Pz/rP7tDHOFnmuUIBV26dOnatavhXuoMOVXrk5KSvL29NUtb2NP6W7duadYwFiMf4Nb6tY3RhmkCW7durTmg1HpkD1KC+6FKlSpyRSDkChddfhTPfuD66gwEdcaCOmUWuiMXpfnxxx9xjurI/m+//bZ+/frG5ZspcArIGwpWMwN7x44d6Wo9dAchmhdAAgiWQ7RerNSZK1euZ/DTufVz1wj35MmTXWxrzmh2HDNmjKO0XqzU+Ywlpm/fvvInKVw4sagr6j25yFW/fv3UugLfApOXK9epU0czUujChQuaq7N06VKTN1KJKVKGL3p7HrQevUH0ITWLtGZO61euXKl5jYn68N7waf2yZcvEPxqt12DldVT16tXT/PgjBuGk2VbakauioeuLyln8j36IydSUp6H1hJCnjYPfMqvZ10X3OioxVL158+aayJs2bUK4+rzZHuZaj+OItz7h//bt26u/w+pB3lAnGr5WVlKmTJmMan18fDzqSjQtefLkQety8ODBN998E62pxVUC1qxZgxTVJ/0qDRs2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" alt="Q079原印缺字，CH20 PDF p.34" width="920" />

</details>

(A) Pirkle phase

(B) silica gel

(C) ODS

(D) ion-exchange resin

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**alanine題缺字；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**按題意是鏡像alanine直接分離 → 需手性相 → Pirkle A。

**其他選項／關鍵錯選：**B裸silica、C普通ODS、D一般IEC不自動提供手性識別。

**條件／易錯與來源边界：**原印兩個-alanine前均缺字。本版保留題幹與原截圖，D/L來自旧講義與鏡像題意推论。

**答案身分：**原印兩處-alanine前均缺字；舊講義與題意補充D/L，不冒充原印。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|L17]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17|R17]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f12|F12]]。

</details>

### Q080｜105-2 #12｜VitaminC陰離子

^hplc-c-q080

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.34–35。

**原題：**為增加維他命C 在逆相層析管柱的滯留時間,可於動相中加入下列何者?

(A) 陽離子對試劑(cationic ion-pairing agent)

(B) 陰離子對試劑(anionic ion-pairing agent)

(C) 鹼性緩衝液

(D) 提高有機溶媒比例

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**VitaminC陰離子；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**ascorbic acid可失H⁺成ascorbate負電 → 正電離子對加有效RP保留 → A。

**其他選項／關鍵錯選：**B同負電不合反號；C升pH使酸更解離，常不延長普通RP；D加有機常更快。

**條件／易錯與來源边界：**VitaminC是烯二醇內酯，原解說用COO⁻錯誤，答案A不因此改變。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|L14]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14|R14]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f25|F25]]。

</details>

### Q081｜105-2 #32｜RP保留方向

^hplc-c-q081

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.35。

**原題：**下列有關逆相層析分析之敘述,何者正確?

(A) 動相之極性增加,則檢品滯留時間縮短

(B) 極性較大之化合物,滯留時間較短

(C) 固定相為高極性物質

(D) 動相溶媒為非極性

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**RP保留方向；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**RP疏水相 → 題定較極性物較不留 → B。

**其他選項／關鍵錯選：**A水／極性提高常較弱沖提而延長；C相為高極性是NP；D低極性移動相不是常規含水RP描述。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06|L06]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06|R06]]。

</details>

### Q082｜105-2 #33｜aflatoxins配對

^hplc-c-q082

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.35。

**原題：**微量多環芳香烴化合物如aflatoxins 之分析,下列何者層析法與檢測器之配對最適當?

(A) 氣相層析法-熱傳導檢測器(TCD)

(B) 氣相層析法-火燄離子型檢測器

(C) 高壓液相層析法-螢光檢測器

(D) 高壓液相層析法-紫外光檢測器

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**aflatoxins配對；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**aflatoxins有可用螢光且適合LC → HPLC-FL最佳題本配對 → C。

**其他選項／關鍵錯選：**A/B為GC配對；D UV可測部分條件，但本題微量與選擇性優先FL。

**條件／易錯與來源边界：**aflatoxins是雜環真菌毒素；保留原題「多環芳香烴」用語，不在正文將其分類為一般PAH。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20|L20]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l20|R20]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]。

</details>

### Q083｜105-2 #35｜等比例RP強度

^hplc-c-q083

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.35–36。

**原題：**以逆相層析管柱進行分析時,下列那個動相的沖提強度最大?

(A) 水

(B) 水/甲醇 1:1

(C) 水/乙腈 1:1

(D) 水/四氫呋喃 1:1

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**等比例RP強度；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**相同1:1有機/水比例 → 題本RP強度THF>ACN>MeOH>water → D。

**其他選項／關鍵錯選：**A純水最弱；B MeOH與C ACN不及題本THF配方。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|R11]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c01|C01]]。

</details>

### Q084｜105-2 #39｜梯度1.5倍

^hplc-c-q084

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.36。

**原題：**逆相層析法的梯度沖提中,層析管柱相同下,下列何者最能改善分離結果?

(A) 流速不變,沖提時間縮小為0.5 倍

(B) 流速不變,沖提時間增長為1.5 倍

(C) 流速增加至1.5 倍,沖提時間縮小為0.5 倍

(D) 流速減少至0.5 倍,沖提時間縮小為0.5 倍

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**梯度1.5倍；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**同梯度端點且F不變 → 時間1.5倍使斜率為2/3 → 題本較佳分離選B。

**其他選項／關鍵錯選：**A/C加快梯度；D雖減F但時間又縮半，不能僅看流慢就保證分離。

**條件／易錯與來源边界：**未給各峰選擇性及新Rs；這是一般優化候選，不是所有方法必然改善。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|L12]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l12|R12]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f24|F24]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c10|C10]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c11|C11]]。

</details>

### Q085｜105-2 #40｜NP低極性溶劑

^hplc-c-q085

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.36。

**原題：**下列使用於正相層析法的動相中,何者極性最小?

(A) toluene

(B) hexane

(C) acetonitrile

(D) dichloromethane

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**NP低極性溶劑；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**NP溶劑極性比較 → hexane最小 → B。

**其他選項／關鍵錯選：**A toluene、C ACN、D DCM比hexane在該溶劑比較中較強極性／作用。

**條件／易錯與來源边界：**極性與固定相沖提力相關但不同概念；此題直接問溶劑極性。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|R11]]。

</details>

### Q086｜105-1 #38｜梯度沖提方向

^hplc-c-q086

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.36。

**原題：**下列關於液相層析法移動相的沖提力(eluotropic power)的敘述,何者錯誤?

(A) 在逆相層析中,水的沖提力最小

(B) 在正相層析時,移動相在氯仿中逐漸增加甲醇比例,可加大沖提力

(C) 在逆相層析時,乙腈-水作移動相,逐漸增加乙腈比例,可加大沖提力

(D) 在逆相層析採梯度沖提時,一般以漸增移動相極性之方式進行

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**梯度沖提方向；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**RP梯度一般增有機相作更強沖提 → D「漸增極性」反向。

**其他選項／關鍵錯選：**A water最弱、B NP加MeOH更強、C RP加ACN更強，均合題本情境。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|L12]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l12|R12]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f24|F24]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c11|C11]]。

</details>

### Q087｜104-2 #32｜hexanol苯己烷

^hplc-c-q087

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.37。

**原題：**① n-Hexane ② n-Hexanol ③ Benzene 以正相高壓液相層析法分析時,其滯留時 間之大小順序為何?

(A) ① > ② > ③

(B) ② > ③ > ①

(C) ① > ③ > ②

(D) ③ > ① > ②

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**hexanol苯己烷；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**題定silica作用：hexanol的OH最強，benzene居中，hexane最弱 → ②>③>① → B。

**其他選項／關鍵錯選：**A/C/D都錯置醇或烷烴。

**條件／易錯與來源边界：**苯有π與可極化性但永久偶極為0；不能把「不飽和鍵」一概當較大永久極性原因。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|L05]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05|R05]]。

</details>

### Q088｜104-2 #37｜KOH處理silica

^hplc-c-q088

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.37。

**原題：**KOH-impregnated silica gel 適用於分析下列何種化合物?

(A) 鹼性化合物

(B) 酸性化合物

(C) 中性化合物

(D) 兩性化合物

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**KOH處理silica；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**題本KOH處理silica配對鹼性化合物 → A；用合適表面條件減少部分強酸鹼作用與拖尾。

**其他選項／關鍵錯選：**B/C/D不是該表列最佳對象。

**條件／易錯與來源边界：**這是指定處理方法配對，不把固體KOH處理等同所有LC用強碱流动相都安全。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|R08]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f04|F04]]。

</details>

### Q089｜104-2 #38｜三配方強度

^hplc-c-q089

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.37。

**原題：**以ODS 管柱分析prednisolone 時,則下列三種移動相之相對沖提力大小順序為何? ① acetonitrile/water (40:60) ② acetonitrile/water (50:50) ③ acetonitrile/ tetrahydrofuran/water (50:10:40)

(A) ① > ② > ③

(B) ② > ① > ③

(C) ③ > ② > ①

(D) ③ > ① > ②

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**三配方強度；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**RP：③含50%ACN+10%THF、水40%；②50%ACN、水50%；①40%ACN、水60% → ③>②>① → C。

**其他選項／關鍵錯選：**A/B/D與題本有機種類及比例指向相反。

**條件／易錯與來源边界：**THF也改選擇性，混合配方不可只用平均極性指數保證相同分離。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|L11]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11|R11]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c01|C01]]。

</details>

### Q090｜104-1 #33｜silanol與siloxane

^hplc-c-q090

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.38。

**原題：**下列何者為正相液相層析固定相之官能基?

(A) Siloxane

(B) Silanol

(C) n-Octyl

(D) n-Octyldecyl

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**silanol與siloxane；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**裸silica表面Si–OH為silanol → 正相極性作用 → B。

**其他選項／關鍵錯選：**A siloxane是Si–O–Si橋；C n-octyl與D原印n-Octyldecyl均非該題silanol配對。

**條件／易錯與來源边界：**不要把siloxane桥自身當成一定RP；須看表面配體。D印字也與常见octadecyl不同，保留原文。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|R08]]。

</details>

### Q091｜104-1 #36｜玻尿酸方法

^hplc-c-q091

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.38。

**原題：**下列何者最適合用來分離高分子醣類聚合物(如hyaluronic acid)?

(A) 分子篩層析法

(B) 離子交換層析法

(C) 正相液相層析法

(D) 逆相液相層析法

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**玻尿酸方法；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**高分子玻尿酸按溶液尺寸分離 → SEC／分子篩 → A。

**其他選項／關鍵錯選：**B/C/D需另有可用電荷或疏水差異，未是此題最適配對。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15|L15]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l15|R15]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f10|F10]]。

</details>

### Q092｜103-2 #30｜UDCA偵測

^hplc-c-q092

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.38。

**原題：**檢驗Ursodeoxycholic acid(UDCA)的含量,下列何種分析方法較適當?

(A) HPLC-UV detector

(B) HPLC-fluorescence detector

(C) HPLC-ELSD

(D) HPLC-IR detector

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**UDCA偵測；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**UDCA弱常规UV且無適合直接FL依據 → 不靠發色基的ELSD → C。

**其他選項／關鍵錯選：**A直接UV相較不理想；B須有效FL；D IR不是本題較適合的常规LC含量偵測。

**條件／易錯與來源边界：**不宣稱任何UV方法絕不可能測UDCA；旧說明的精確ε值來源未核對，正文不據此給定LOD。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|L22]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22|R22]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]。

</details>

### Q093｜103-2 #35｜DAD多波長

^hplc-c-q093

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.39。

**原題：**以液相層析法分析含有不同吸光波長的多種化合物的檢品時,下列何者為最適合的檢測 器?

(A) UV detector

(B) Electrochemical detector

(C) Fluorescence detector

(D) Diode array detector

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**DAD多波長；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**多成分各不同吸光波長 → DAD同時取得一段吸收資訊 → D。

**其他選項／關鍵錯選：**A一般單波長UV不及該題多波長需求；B/C讀其他特征。

**條件／易錯與來源边界：**DAD不單独證明未知結構或保證没有共流出。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l19|L19]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l19|R19]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]。

</details>

### Q094｜103-1 #8｜DMF互溶

^hplc-c-q094

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.39。

**原題：**下列溶劑組合何者在室溫下不會出現分層現象?

(A) Acetonitrile/n-Hexane

(B) Methanol/n-Hexane

(C) Water/Chloroform

(D) Water/N,N-Dimethylformamide

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**DMF互溶；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**水與極性醯胺DMF可混溶 → 不分層D。

**其他選項／關鍵錯選：**A ACN/hexane、B MeOH/hexane、C water/chloroform是題本分層組。

**條件／易錯與來源边界：**DMF是N,N-dimethylformamide，官能基為醯胺，不是醛。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04|L04]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04|R04]]。

</details>

### Q095｜103-1 #11｜adrenaline電化學

^hplc-c-q095

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.39。

**原題：**下列那種偵測器對於adrenaline 可提供最好的偵測靈敏度?

(A) 折射率偵測器(RI detector)

(B) 紫外光偵測器(UV detector)

(C) 蒸發光散射檢測器(ELSD)

(D) 電化學偵測器(EC detector)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**adrenaline電化學；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**D。

**最短完整解題鏈：**adrenaline具catechol氧化還原基團 → 電極電流靈敏 → EC detector D。

**其他選項／關鍵錯選：**A RI靈敏度較低；B UV與C ELSD在題定比較不及選定電化學。

**條件／易錯與來源边界：**“最好”是該化合物與相容電化學條件，非所有分析物都優于MS/FL。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21|L21]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l21|R21]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f16|F16]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f26|F26]]。

</details>

### Q096｜103-1 #35｜benzylmorphine

^hplc-c-q096

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.40。

**原題：**以ODS 管柱在pH 8.0 之緩衝溶液下進行液相層析時,下列何種嗎啡類化合物之滯留時 間最長?

(A) Codeine

(B) 3-O-Benzylmorphine

(C) Morphine

(D) Normorphine

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**benzylmorphine；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**題定ODS與pH8 → O-benzyl增加疏水芳香部分 → 3-O-Benzylmorphine最晚B。

**其他選項／關鍵錯選：**A codeine、C morphine、D normorphine在原例較早。

**條件／易錯與來源边界：**benzyl=CH₂–phenyl（苄基），不是tolyl（甲苯基）；使用原圖校對。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|L07]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l07|R07]]。

</details>

### Q097｜103-1 #36｜neomycin原反應

^hplc-c-q097

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.40。

**原題：**下圖為分析neomycin 所進行的衍生化反應,如衍生產物以silica gel 管柱分析,則下列 何者非此衍生化之優點?

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAVIAAAGVCAIAAAAjWu60AAEAAElEQVR4nOxddbwU1Rc/09v7kvfobml/AiYgggIidiCKgQ12Yjd2dwsqNoqBgQEoSHd3vN7e6XvP74+7b1heCUiz3898lmXf7OzMnTn3nHviezhEhAwyyOBwAr+/TyCDDDLY18iIfQYZHHbIiH0GGRx2yIh9BhkcdsiIfQYZHHbIiH0GGRx2yIh9BhkcdsiIfQYZHHbIiH0GGRx2yIh9BhkcdsiIfQYZHHbIiH0GGRx2yIh9BhkcdsiIfQYZHHbIiP2BD5r2mkEGewAZsf9X0GQyDgChUMTQiaFTQLAtsEywTACERNwABABIJjX2BcsigBAOR9nnatIEAOc9+9yyiG0B4zqwLGKaJvuuYRi2bQJQSm0ACkBNS0ck7H1G+DPYI+D2FM1GbcfhOG6PHH8/IaVpdd2WZRfPASEgCAAIpgmyDJpOZZnXNMPnU4ADAEAKpkkURQAATbPcbgkAbBtEEcrKwvn52c6HAGBZKAgcAgoCBwCqqno8HgDQtKTb7dY0TRAEWRbZzqZlSqLCccI+H4QMDjVktP2/gBACAIIg8DwAwHvvfTBr1gLgQJbhr7/mP/fccyUlFZZlAYCq6omEatv4zjvvXnLJFYmE4XZLFRWxRx99cunSZQDwyCOPDhgw+OSTT+nXb+Cff/4djap333331Km/CzwHCO+++/4bb7xVVlYBADwvAvCKooiiCMBTCqZpy5LrIJ9DMzhggLWA1o4a9ye1oLbjHyzQdRUxdRWGTuoXNh73+HOmgcTCG8bcmZfbcN7cpcRGpKmtojzWu9fxANJLL76OFH+a8huAtGlj0SMPP9G4UYt2bTv17TNAEj3HHdtv1sx5iuy75+4HkaKhk969juvRveeKFavYb6WNHNF13TR1REKItR+GIINDDuJuTBPszWGieRRFAQBCSDwezwpmJRIJQRAIwW3bSkxLr1evXv369XkeIpGkz+cVRfB4PCUlZQF/1g033NS6dVu32wPAV1SEX3jhpWOOOeaVV16RZXnWrFlvv/22orgJIYZhrFu3uaKiIhaLA4Db5bUtQERKqSBymqb5/V5FUQghALyqqj6fb38PSQYHP2qbD2rT3g6qqP1dMg0OIiQSMURimiYiIkVZ8vCcwnPuhg1aACiKHFi+bJ2hU8tMaXtiY8cO3Xt0Pzo3p8HAAUOXLlmjyIG33vxQlvwffvCpYxREI3rRthCAAqDwnNK0SSsAqU3rjpFw0tkHKZaWhGybIqJhZPR8BnsMu6ntDxNVDwBerx8ANE2VJMm2ITc3t3XrNi1btkwkEgsXLtR1vUGDwqKiom3btpWXl3fq1Ck3N9+leLp36/7Qg49cddVV7737gWnajRo2MS3bMomaRErptm3bksmkx+MB4I89+tjC+vWys7N//vlnvz9YUlIyY8YaVVXz8/NPOOHoYDBIbBR4DikHCHC4jHoGexm1zQe1KXnLsmzbrlHhH6pIJBLsjWWiz5v1/HMvM1U89q77mzdrs27t5ptvuqN+YRMA6emnXkKKTRq1vXLUDbGINfCkYZIQAHDP/Guhx5U78qKrTR2R4I/f/yFwvqm//C2LwbF3PowEdQ179TyhVcuOr7/2XtMmrQL+3DatOy5dsoqZD0jRthApqqq+f4cig0MDtXry+VogiqIgCOz9f9H5WFPAr8YP9xIQUdd1AGCvAGCapqqqVc6EUvB6vQCACMDRQNBn2Qb7UzKZ8Pv9lNLi4tK33npnzOgbpk2bFolo/oCX49EfEJ9/4VngKACVZOGee8dO+OjDY487/q6xD5w8aMDpZ5zWrn0bjsfc3FzTBEUBl8slSVI4HD7//PNff/31NWvWmKZpWcgiCGykKc3E7TPYA9hlI39PAXd0DbL/IuLeXj5g5SKF4zhBEJgDwrIsnudlWZZlmVJKCDFN0+v1IqJhmG63oqo6AHg8rptuuumEE04wLTsRV++8886CgkKPx/Piiy9++OGHkydPvvTSS4NB92233cKWBvn5+Z9//umaNeuysgJjxowpLKw3fvxHq1evfPyxx0877dTc3Jx77rln6GlDZAUIgccff3zhwoXnnHPWvHnzXnrppRNPPDE3N0eS2OCAquput8vrde/VwcngMMEeS9c5WGCaJrNZqn9uWZZpmh6PR1EUTdPcbreu6y6XCxB03ZZlkRcgFksEAilfumFYxEaPRx479sHJkydfecXVpw07NRj0ezyKYdhut1hUVF6/fh7L8Ckvj+blBaEydYfBsoBSynGcJKWmu6lTp5133nljxoweOXJko0aFyaRhWnp2dtA5SVmW98k4ZXAo47BL15Fl2ZF5XdcjkQgAJBIJWZa9Xm92draiKLZtu91uALBtqqkWpWzJA5RCIOCjlFZUVFAKlmW5XLKm2T/88MOSJUv++OOPZ555xudTeAHcbhE4KCjIAw4EAXTDzMsLsvmVUKu0NGRaNgAgUkXhZZlDBETQdfLOO2+XlZdOmjRp7Nixc+bO8/qU7OygZRFCiKZpGZnPYI9gP2t75mCASqt73/wix3FskUwIkSTJ+ZOu64ZhBINBpurZh5QAXzk3mpZdmSpLdd10uVzsr3PnLlm7Zn1pafkpg05q1qyRTQzbpswgt20bkSPE4jiB4zBdbm2biiIPCKZJZZlny/YNGzd4vd7i4mK/39+iRTNCCCKxbepyyZWq/rCbqTPY49hvYs+iAOwVADiOYz5Cnt+7jzUTHkKIIKSS28vKyiilPp+Pue4ikYjf7xcEYcWKFX5/cMXyVU2bNmvVqilwYNs0mYz7/V7DMNxur6qqLsUTiyVFUXYpEseBIIBp24lEbNWqVYhYUFDQokWL9J9mrgS3281xnG3bzDPKqnRC4Yjf75ckobS0PC8vp6ysrKAgPxqNBoMpCz+ZTHq93ozYZ/BfkBK3/SX2TM9XF/t9o/Nt2+Y4Ttd1RVEefPDBeDz+6KOPut3uGTNm3HTTTS+99FLXrl2vueaaX36ZmohrhYWFRx7Z48abru/c+QgAYPU5hKBlWS7FpaqWxyNFI+bGjZu//37ytBm/lJUVlZaWlpeXDx069Morr2zfvn29evXSJxpd1y3L8vv9iJyum263ommG2604pzdixPAePXqMGTPGtlP2BQLats1zoiBI1S8ngwx2Ekzc9pvqYHIupOE/RgR3Eixch4iCIHi9XlEUFy5cPHPmP4ZhIYJhWAsXLl69eu0999z3wQfjB50y5IUXXqhXr/C999//beofum4CgKrqALymGTwvrl+/efny5Y8++vQRRxwxYMCARx55ZMWKFTwvDht2hqrqH3888aSTBo4b9+TWrUW6bgLwhmHpuulyeXy+AKXAcZzbrZSWlrrdCqU0FotZlgVAXS7Xiy++GA6HZVkklCTVpG3bkijtzTk6Exo8jCDWGDNDRObxZtLofIiIe9YI32fq3YHL5QIASZIsi0iSQCmIgrxl87a//5plmubPP/8iS+758xa98sorZ5913tNPP+NyCSedNLBPnz5ffPHl9ddfGwknlyxZsmjRounTp2/atGn58uWmaXfq1Omcc8/q0rlbs+ZNOnfu6PW5w+Hw++9/eMEFF+Tn53/wwQdffTVpxIgRI0aMaNWqBSFMdDnTtFwuGQDq1csDoDwPiESSBAAoKCgoLi5OJBK5ubm6prFwIACI4i4PPqUp34Sum+znAAARbdtkfo3KB8AR+8wiYn+itpm9bjFhsrkz0sQ5GSDVk3gopYZhmKaZXkLHAtr/MT1ov4NdrqrqhmGxZLvTh53tUnwAksC7fN7cgD//ilGjAZRXX3lH17C4KGwa+MjDTzVq2DIS1rZsLjuiYw8Axe3KOv+8kd9+81NZacwyMRG31CRBik5y/uBBpw06ZShSXLF8zfnnjQAQ8/PqP/Xkc+yv8Zimqak0e9PU4/EoInG2t956g+dhxoxpiMQwNERi22bl6y5D0wznfSgUisVi7EcJsSzLME0d0WJbUo3ugSHO4D+gjsrXOmpemGzufBVMrVN7jTPHIZCKzyZTl0uRJBEACAGfz1evXr2Jn0z86aefrr76SssyZFnmOb6kpESSID8/SxBg9uxZubnZPp+rYcO8Dz98f/OmjeFwxYQJ7w4ceFIg4BNF8HpFl4sHAEGAUCgGADfccMPPP//8zz/z2rZt+dFHH8ydM/f8889/5plnOnXq9tJLr1FKXS4xHk9SSiVJkSQFgAfgdd20LNKhwxGUwpIlywB4WXaxPwHwiLsz/qxkkBA0DCs7O9vv9xuGIUkKz4uiKHIcZ5ipvMP0uEYGBxd2STZ3TewPGXBcKt01Eom63e7s7OwhQ4b063fciSeeqChKs2bNevfu/corr8yfv6SkpPyrryZ9Penr008fZhhWcXF5164dGzYsEEWeue5ZIh0AWBYaBuE4yMoKaJrVunXrjh07rl+/nv2pa9fODzzwwHffffe///1v9JjRp5566j//zPN5vWzRVGn5s2wi8cgjj8zPL1i8eLFlkfTTrp5l9K9gRxAEThA4RZEYgRdzLtq2zY7J8zyhBAAkUan7aBnsL3C1wPmrsyfT53Ufra6c/CqSf2jMAjwPhBDbpgAAHLg9SqNGjQoKCgxDtyx0u93BYDA/P/fLLz9v0qTJkf/r3qhRw4tHjmjVsuXpZ5wmSWJh/TwAMC2LfZ3nAThABMsmPM8pihAOx3ke3G4pEAi0adNm/PjxmmbxPMfzkJXl69r1iHfeeeOP3/+oqKjo2avnuede8MvPv2ua4XG7CEFDJ4FAQOC5eDzZu9cxa9as07UUDx8iB7vlzpMkQRIFXbNDFTH2X5awxBKQGS+QJCqAPCGYyfk/2OHY/HXvxrHk0Opf3mGnQ0LgHSAiIoeYYrCbP29xcXHxwIEnIUJFRXjDhg1NmzYtKMj54YepFRVlCxbM73hE+1NOOaWwsB4AUAqUUse1ZhgWAChKmm2MYJpU13WO41588cWxd49dumRphw5tNM1yuSTLorZtezxyNJr87LPPPvzww02bNg0ZMmT48OFdu3YlhCSTSb/f73ZLL7/8+quvvjplypSGDQsoBUJQkjjbBnEXzXDToJLEI6ZmqOLiUk3TCgsLnXihYWiMSsS2bcbh9d9HOIPdRm2KujYZxDSXfLrM/4thWJtLr4qPYdd9Ewc6LMuyrO0eykRcR4q6ZjOXGyWVXBfsr4lEMplERNu22XcNI+UnY8XIqqqqqoqIatJ0SDJ+/206gPjxR5+FKmLOh4ZO2BtNtZDiU08+7/NmA0gPPzQuGlF1jZSVRpDirJnzAv7cBfOX2hZSkiq/NY1dvxEUkwmD+RrvuvNeWfIA8I0bN5006Vt2CdFolDF2UWo79GEZ7C/U5rqrg+0m3bFn2zYrLan7V3Z2asdDpWIHEQ3DYEMmCDwi2Da1LOL1KppmMcJMQiAe1wAgFlMBIBaLud1uj8cTj8cFQbBtWxAE5v1yZla3283yeRkrrqZZloWtW7cGgBkzZmRn+52jyTKvaZZtg8slapp1881jpk2bdtedd73xxhtdunR54403AMCyoLCwMBaPhcNh07Q5LhWEE4RdNvUpBY9Hjse1u+6668UXXxw6dOi4ceMKCwtHjRr1yy9TAUCWZUlSAIAZ/BkcmKhtOqi+JxPsfzlclWlmZ2aj2qaondx5f4Okbduh6yZiis3C0IlpUEe7appm2zabQVmCHXuDiIlEgr1xPqEE2XfZduqQ03v3Oi4STjh6nv3VifPZVupHN20sumjEZQBSu7advvpycjymN2/W5sknnkOK4VCC7ZxMGJQgpTtszEvv/Bdx++e2za4C4zFdFNz33P1APKYhxVBFrF27DpdeenkioSIiU/uWZR0CAdpDFVVYbZhrRtd1R7E79iYi7qy2x8rpAf9tnnDK4x3AjjXz6RPKzkxjBwjY+tyybMtCUeSZf569KorC8zxT74ZhiKJoGIaiKJRSr9erKEpFRQXbLRqNcxyYpkkIUAq2DaNHj966dWtZWRlUmgY8v32RxhbtiYSqaXbjxoWvv/76N5O+6dChwyWXXHLVVVet37B+6dKlxcUVpmlu3VqaSBg8zyeTejKppm8MiUQykUgmk2oioSYSyVgsHo1Go5H45s3FggCzZ8+2iX3UUUexO+XxeIYNGzZjxgxWLyTLMiIyl/6+H/kMdhtVnPk1OvZrhIiV/BbVj1jbd6oLPMfVkNufvsOBCmYjpZ51yyIut4iYYqwzDMLzvGkxgg23quqKogQCAQCQZQUAotG4oiiyLOfk5FIKqqoGg37LRI9HYRdtGFa/fn0ppfPmzWvVqhkTqnS2HNumsszLsgcA4nHN7XafeurJXbt2mTNnzv333w+A773/7vr16wKBwOrVq/1+f3qpknOb2athGOmuHWfhV69ewYsvvszmLFXVCKGEgKII8VhS4Le7BxMJ1efzmKbJ3HsZHGioLYnGeR7Sp+x/nb45WlkMU0WM6xZ7Z13hsGsRQtKfQueYTv3JAYPqyyEeACyL2LbtdiuIgBQIQZ7nUufOASComu5xu4CDrVtKGjYqqCiP5uYFAcEmVBR44IDYIAgQj2t+v9tJiTUMcvbZZ/M8/+mnn0oSzwaVVdfzPFgWmqbp9SmMHpMS4AUABIpAbJw2/Y/nn3sxFC6XRKWktKigXn2mlqFaFBcAXC6XE3NNF/vs7LzHHnusfv2c/PwGXbt2nTLle56Hf/6Z17NXzzvvuPPue+7yeFyQlsObwYGJKkrUMfgFQWAfkso+LrATLFWHp9hXyT9PPe+MSyceT0qSxNLXNdWyLMvr9bCL2LatrEGDfMOggsDHYvHy8jKXy92kSX1CIBaLZ2f7EVNqPB7XvF43z4Ntw1NPPXX33XcvW7asTZtUES6lqXwhROB4IITouqkoEs+Luq4ici6XbJo2z4NhWIzMx7IsRM4wDJ/XW+OdsSzkOI7nU9KLCJQCIogiFBWF6tfPeeutD6+66oo+ffoIgjBr1qxWrVp++eWX9erVc7nEDCHvgY8qkuyY2+klM7DTxjUP1UR9Z77JrM30mrkq3935Q+1b/Hs6iiiKTsnKm2+++eKLL2maEY/rGzZsvffee2fOnCtJ/AMPPNioUaO27dodc8wxH374iSBAdrY/GlWj0SQhoGkWk/lwOC6K0Lx5c0ScPn06c7uyqYENDMdDIpGglHq9blEUeR5cLpfbrQiC4HYrkiQ5Mi+KoiyLfr+XUiAEmO+AWQ0MksSJ4naNzTIIRREsC+rXzykpiVx++YgZM2Z07NjRsqwXX3xx0qRJTZo0cLlEAKAULIuwvOA9PN4Z7CFUkXmoppt3Ka1W3I3E+zok/MCT850BBQBWvwQATh5LPJ58//33XS73DTfcJEninDnz3n7n3SZNms2Y8fcTTzx17LHHNm7ceMWKFZdcctn69Rvvvfd2WXbJMh+PJ2RZrlzAc4RAkyZNmjVr9vPPP59xxhnBoI+QFJeeaVJZ4X0+HwA1DM2h8RRFESBVWWEYNsdx7BMAzrapKNSchuFMAezViflJEiBCXl4WAPTo0b1Tpy4AVFEkQYBoNOlyuSRJIJRIksCK/zI4wFFFqzs+tSpu9bolka+y07/KbfW1ZfVT2clD7Q/waW92WMtW5qiBbduWRSgFv9+rqmooFNqyZQtbLYuCGI1GX3rppVatWr366quvvfbaxx9/3Lhx4y+//HLLljJKqSCAIIiKIkejyVAolpXl0zS9efPmoiguWLAgkUgQsp302jRNSoE1HVAUxefzeTweURRpGuEXz/Mul0sURRY1FATBMciZnDsbk/P0jcGyABEEASKRpCjC779PfeihhzgO4nEtGPQqisDzwNpsa5qRyc09wFFjdMwx+Ku8rwPbH/2dNBJq3Ke27+7MAaueKAJSQJp6D7CDKbsnwKdviBzbJEkSBIGZ05IkqGrCsiyXW968eWu79h3q5Reed/4FNqGrVq7ZuqXo4osuadO6qaFbwUB2j+7/i8eSWzZvc7vEhQtXqKoaCkW8Xq/L5QYAn89FKT744EOrVq1euXKVKAKjzUskDJ/PpWsm6zuww/nxPABIkkQplaQUtYYsy8xbBwDAgWFapmUhAMcDx1i5uNTGPnH+y6YAQiAY9FoW8jz31ltvVoQqPF4Xocj2YX5+t1vJZOwc4EjXtQyOiy39/b/K3YHovU0tfZmoVzrJ9ihqvmrDSNWfIqLP55MkyTAMQeCuu/aau++++7JLL/G4PEk1bhErFC7fti0czJLdbndpWTHHcdk5wQULlo8cObJ///5//fWXKILHI8Vimm1DTk7O4MGDKdINGzaUlUUIAZ4Hl0sBAI+nViZc5+6yxEy7EuzWKoqkKBLPA8vHRKx1TS6IQChSJBwPksx17da5XkHe9OnTBYGjlNo2tW3K5h1K4cDzv2aQQq2JN4yOEQBqSZ+pEftf7HfGyth7y4UqEyfTrolEgv03Eok0b978oYceuO320cOGDdX0ZOvWLXv1POqjj8YXFW8FgHnz52zbtiUrO+D3e7v3aH/HHbeFQqGRIy++8MKRZWXhQMAtisBx4PMpffv0+eGH791ul2GY7IpsGwCAdQOvvgHwHCfwvCgIkiBIoiizNzzPU0o1TVNVlZFwVrcXqoBSKooCABCChYX1mjVrNmHCBACQJIEQwvM8K0lCxN1g78lg34CrCbDjA7zzXr39dpvTc37S/gvO8nJP2/a1wol1OyRToijath0Oh9u0aWPbViIRN01EpKLId+/ebfToa23bOuOMYYMHn3bBBed5vZ7HHnukXr38cDhx7rlnzJs39+WXX54/f36HDh1uvvn2des2GYZhmvTMM8/84ssvvF4X0/DMza7rtlALEGuog+QqMzRYjQBzRpimmUwma7s6QlCSBI4DVmkPAMccc8z06dOLikoAQFEk5zlJTx/M4KAAC5zvTjpsbcbDnkV1GqAqzTMra4x2SFZPvd8ncPKZndK6WCw2ceLEZ599XtMMYmMiob76yptr165Hin/8Me3WW+7s2bP36OtuLCkpS50kxXhMs0yMx7RVK9ddMeoaALFefoOPJnxKbPxt6jQA8YfvfzYNGo0kWfkd62xJSA2vtoW2TYmNlFUEVu7JSgCdMWRlRXVcF2PUojTVKtuyyJw581wuz4cfTkhvoe1k9WdwgKNKQZ6qqv/6DFTHviDMxpqIsVl6T3osgJ2PbVFFEQDAspBSKssCt0ctEqwp6AAAjNCaUqqqqs/nAwDWhSYcDufl5Zlmirg6kUgoituJdbHPGX9+IBBkR9U12+USEWHRoqWjR49esGDBEUccMWLEiPfee69bt26vvfZS2snUep5VTpDSVKm/rKSMfABQFMWJPtRWX82c/JpmyLIsCJxhWJqmtWvX7qSTTnrhhReys4POpQEAISkOggwONDCfDhOS9DeMK4k5pHc+drZvxB5Ya2wAEARBFAWOA9umHMc5TkdEYKrGNGxmBrPqWEWRawlU7/bJ/Etgk5XZsOZTPp+PECIIXCKhUmoHAlkAlHHaV0oIH49H/f4gAAXgw+FwVla2k28virxt02+//fbJJ59ctGhRMpkMBoNffPFFhw4d/H6/ZVlqUjdNs8a29Yyog60+cLtxRLw+N3PsSZLk8/n8fr/X6/1XWVVVnSXhsr5al1566Zw5c7777rvWrVsyBuH/MKIZ7AukS3u68FfGnqRdKqPaF2LP2sU5zG2SJPF8rWJv6LbHI3McsOp3l8u1q3wydaMOsU/vgQUAuq6zxBunNY3zhgkex3HMHcBcayzSTinP86DrpqLItk0kSdB107KsZ555Zvz48Rs2bFAUJZlMKooiCIKqqgJflzPfCcZUro8oRerxuBBR0zRRFPv27TtmzJghQwbVdhA2zogoinwkEsvKCgDApEnfnnXWWX/++WfPnj0Nw3C7FcsigiBk0vIPFjiSz0pCd5X7dHfE3rKsytQxcJq9sNUFx3GOVxkRGUMrU1ZsUeoQ7yuKlP5ERqPxYNCvaQZSXpIkSlP+J5fLJckcIqiq5rR5ZqEsxni/97GrKSw1i46mGWvXrl22bFlpaSnP8x6PRxAEQgixazlKzSKIsizzAiSTSULIfffdV1JS0rZt25NOOumiiy763/96QGXCPyv1STfgnUIAALAs0rZt2yuvvPL2229lLbQty5ZlsUpzngwOVeyy2FdZRjJhhjSuZbbsZGoTK+sHECESiXIcFwwGmIXP/M/5+bkAYJo2IcTtVtSkSQhbw1BEFEVRlmVR4thDTEiqqYMjEpTp1r2LPSP2qWNRANieQqfrplJLE9valmmWhbwAbN1x1VVX/fLLL6NGjRo3bhwiPvDAA+ecc06LFi14HiyLcBzHAnLpmtwwLI7jZFm89NLLo9HohAkTWAFCMql5PO4DMa8yg72AXZYZR8yYx5sZGCzczZhY3W63y+Vi3WM5jkMETbU01Qz4gwF/QNesRFy3LUoJcCBQAuFQPBqJExsBARH9fhdrCysIgiiKzE/BatFYNTgzK+LxOIs57+Hx2GvQNE3XdUIsZx7BypBhjaiSe+tsksRpqqEmTZ/Xc+cdYymBE47vO2vm7JtvuvXDDyace875L734yuZNRZIo2BZVkyZburNxYuYV0/+nnnrq33//vWLFCvZzoihaVi2GRwaHHnbJ7+8gmUzG43HH28R89TWyMlkmmgZ1GCktEw2dbCeopMgIp5CmyCcNnera9h0oQcOwDMOiFFnAKRrd3rllX5FAkZ1+3SnUwDVGd+61kpmLkhQVV738BpddeiXj21qyeMWVV1wLIPbuddxvU6eVl0WQYlFRCRu3WCzhtMeJxRJr1673ev3PP/8iYmpgETGdUzSDQxi7rC0R0bZtWZZZlMu2bVVVTdNkxj/P8/F4XFVVtrNpmqZpShLHcZBI6NFokiWlsxw1y0KWKw4AiCmeAFnmFIV3rE1KQZZFWRY5Dpi/mi3payQP3Gvgd/q1VjjNxaDSm0gpZeNm27ZNaJVXikAprfpaOUqWRZkLZcSIEUuXLi0tDXk8cqtWrV577aWff/o5FAoNHDjw+uuvnzlzTmFhPTZWfr/X5ZITCVVVdb/fW1BQ0Lx588mTJ6uqzrytUEnVkMEhj90xkimlbHnP1LvP55Nlmed59l+/3+/xeBjFHwDv8cisMtzncwWDXif3ThRBkjhmfMZiaiyW9PlcAGCayCTatsE0Kcvbc2Q8mUyyJQDrFb8HBmBfgVXUVmE+kiRJTIGv8srzjMKkyiu43VIkkmDlA6ZJTzrppHXr1s2bNw8AZFmwLDz++OP/+uuvd999d/PmzYMHDz7rrHNmzJjBflFVdZ/P4/G4dN30et39+/f/559/tmzZwrrlQBXC/wwOYeyGheBwxTr29oYNGzRNYya3bdtsHZvaO8UJb6tJi5G9s/8m4gZS3Lyp2NBpmsGfdNYCkXCCcdcjoq6bFRVhRNy4cSMiaprG7GTGXb/XQXd6+9cjUcosICfZjlK7xm1Hht/tVL+pMUkZ/DRUEW/erM0F51+MFHWNpJ9M0bbycY8/7fcHGzZsfP31N27Zsg0RQ6FIcXEp++np0//yev3jx3+EiKwmZy+NXwYHGnZH2zs2IaNbLCkpe/fd95cuXc7zvKrqEyd+NmHCx9FoHADUpJlMmgBQVlb2/vvvT5z4uWFQAFi4cOHYsWNXrlz3yiuvvPnmm5RCNKp+9dXkjz76CBHmzVt8//0PDB48eNiw08eNe3rWzLnlZaH77n0AKTRp0sQwrA8+GP/JJ58mEqrH49lj819t2KVAR+07W5blhPorK94o1NXbjK9pA69XYZy8hkFM05QkqW3btvPnzy8tDStK6m4mk2YyaRYW5t50002///bn8ccf//rrr59zzjmff/6lLMsFBfmsF9gxx/TOy8ubP38+YqpJ3kFlP2XwH7Cr84SjE1ihmGWRWTPnNqjf5KYbb2NK5uKLLuc5pbiogul2SpAS3LqlvGuXnuefN9IykRJ88okXAJRvJk1p1bJjfl6jP36faZn46CNP5+Y0WLd263HH9vd5c6+79sYxo2/1uIOnDztn6q/TAKRoRDUNRIr9TzzlwuGXpGu2WFSlFGNR9V/PfyfbAWy/XgsdI4VdS9W2OTv+iVKnvmAXGg/XdJ5Vt3RrIuU8pRiP6fPnLQFQfpryBztPNUnYG5b2H49p27aWzpg+66orr/N6gh3ad/504pdOOcCkr787skcv1nWH5fxncDhglxNfBYEzTea9A0DgBd7tdguCUF5esWHD1mRSU1U9JycvGMzmOIjFjEBAAQCe5yORyJw5c0pLKxRFWb58uSzJhJBYLBaNRm+++eYvvviC2Q5z585duHDhY489NmrUKFmGBg0axOPxSCQW8GctXbq8QYMGxcXFFRVhny9ACMs2N23b9njcHIDf705R3Hp2IZOHDURtsUBKkec5hwYP0viqHFqbtEOlEm2dFMCdT5OugtT30soQEQAQ4olYIOATRd40TUmUfT4lOzu3oF7B9Gl/ndT/eABw0hokSbRt8PlciqJkZWV17tz5lFNOefjhh6+++upJkyZddtllRx99dOvWrefMnTNr1pxevY4EqDFLOINDELuT746ILA+MEhAEYBXgX3zxxd9//21Zlq7r5RXlLhcXj5uBgFJcHC4szNZ1PS8vb+3atUOGDEkmkyzCLwhCw4YNO3XqtGbNms8++4xl/iUSiVg8duWVoyQJVJXcfvsNAPDFF5Nj8diFF17IyG23bNly5JFHCgIkEpbXK3OcDACqakqSJEncvzK9O6KYPv/VJvaISCnwPOdUwlbWOTMqS8JxnCDwzK/OaKf3eLpz+gHZuoZZE6IAHAeNGhWeeeaZ06dPh0rCXADQNFsQ+Mp0HcvjkRGlvn37Dho0aPLkyVdfffWvv/569NFHjxkzplfPXnPnzu3SpYskSXs2DzqDAxa7s7YXRZEJjqbphKQapMuyfMIJJ3Tq1MmyLJfiCoWSfr/8xx8zWdIez/OhUEjX9ZYtWw4dOlQQBAQEAF3XmzRpMmjQoFtuveXXX381TbO4uDg7K7uiIhyPmx6PUFQU+uOPmdnZ2QAwcODAq6+++uyzzxZFUdd124aioqJffvl98+ZiwyCIyJrY1F03Xl3ma+slVuUrVbU6pJhtbNtOU8hIadV1026MsINKnly2pAJKQRRFRDQMw+12sykGEU499dQ5c+bMn7/CNIFl/cmyyJz/mmYJgmDbwHHg97s5DgYMGLB16+arrrrqxx9/PPXUU2fOmvnOO+/IssRxwDwyGRz62NVVgVPcSwiapo2Iq1auY2v7aCSpJq1bb7kLQNI1ct65F3ft0rNL5yNfevF1NWk1btRi8KBhyYTJ2rxyIP82dXrbNkc89uhTG9ZvLSxozIEMIP380+/1C5vcestdsaimJq1+fQf27TNg+rRZHnewojyGFJMJs0f3Xtdde+P33/18zNF9juzRu1fP44q2lbHMH0pwJ1u5OWRVpmk6NfbVwdb2bOnOKABYC1pK0NBJIq4nE8Z2jgCb0VTZlmWx6iPGkLkbK3zWxM40qK7ZmmppqqVrxNCJbdu6rrImZ8RGQyfRiL5u7dY7bntg+dINTqDEYStgHgfToJFwwinyZ7GSH3/45YpR13g9QQBx1sy5yUStg5DBIYZd1vZO8NmyLFawqeu6z+crKioKBDyCIKxfvx4ASkpKTNP89ddfjznmmDfeeKO0tLRRo0bbtm1zuSQAqKioQMBYLCaKYjAYbNq0wUsvvYSAbpe7Y8eO7du3f/XVVy+88MK2bdtO/W1qz549y8vLEVHXWV8qyeVyhcNhnud79uw5Y8aMefPm/f777wAQDKZaR9SRs4tpFXgM6Wxk1cELwPOpIpb0DQAYoZVj+0DKLtjBcNh5nqNq51lDo0GO42zbVhRFkiTbtnXdlGU+EFCaN2/w2GP3tmvXlH3X5RIYew9zPYRCMUnigkGvaZrRaBIADINwHAwceOLrr7/88MMP5+flq6rq8ciRSGw3TjWDgw67vLZnEkIIYSyuum7m5Gade97Z555zPrMnR4y48NRTT/V6vZ988tHIkSOLioqGDRvWtGmDSy65BBGZfA0fPtztdnfr1u2iiy5q3bq1YdAzzxz69FNPu91ur9f75ZdfPvbYY/PmzevWrdvTTz89ePBgXddfeeWVrKwsQkAQ4JZbbpEk6cQT+wHA4MGDjz/++MGDBwNASUmFYRhNmjaoqAjn5mbXdglYWSCUXtBe287pMsvxlSE6DgBAEIEXhFThcOXOHMdDtRZDuzrI7FCVHsQUkRbPczwPkqCwmcVZmJSWRgOBgChwAJBUdVEUvV4xmTS9XhkRbBtzcgKJhC4IQiDgAYBEQvf5XLGYSinNyvI1b968rLyspKQEAFhZbgaHPnbVPGCE7Q5Yp+REQmWJ98RGNWmyzsoDBwzpdET3d97+kMWZmIlu6NTQKSVYXhZlGSaaaiPFivKYaWBpSZil8bDXUEXc0Gll8+lUVg/r+mzodMH8pdlZ9UZfd9PmTcWaaqlJc87sBd27HTVr1uw6zn9Xg2rp+7LW0TXyT+0NRipm5Bs6MXTCAp9IkVKq65VxSoplpeF33p7w2affxKM2Epz59/yvv/ph3drNn336dUlxBVJMxPUpP/76y8+/RyNJp682S+xHiuFQ/IvPJ+XmFMyaOXfb1tI9fAEZHKjYjSy9mvvDs4feySErKa444fgTA/6cI3v0Gv/hJ07Xd7bg1DXbWWSyVSibMtjjmF6rk56Uxmp1kGJ5WUTX7IcefMznzerYoesZp5+7ZXOxoZOVK9YGA7lnn30ubu/xnjrJKrPVwQJio67ZumZvzx2oFHtN05Di3DkLGzVsmZ/XaNofc9QEXnnFGL8v79tvfgSQNqzfoibNRFwfPOi07t2OYkPNhD8aSTojPOXHXyXR/fdfs+2DcoQy2B3sMcIqZsl6vQohYNskOzv7jjvuYKWybdq0CYWiublBAFBVNRDwGIbBcS7WAdbhembxsFhMDwQ80WiSORG8XgUAEEHTTI9HZkxb7FBDhw7t3r27KEputzs/P1+W+UaNGo0bN+7pZ55csGBR166d2XkBgGmarFfsbkfRDxwwZwQiulwuqKzMicVizzzzzJdfTmjQoEE8Ec/Ozs4KZv3555+nnnpqVpaP5QUSAqFQOD8/W9ftQMCzb1iJMzhAseszRQ2J4gyhUAQRk0kt3YeMlQsBRIzFEs7OtNLvzdSyadqaZqiqjjuivDyEiKZpl5VVsARBSjEeT7LfcjLkkgmD5aURG484ovPw4SNYDSkrDWCqfl9V6e5JVNf27GNN0xDRNOjMv+e0atmxa5eeAV/B559+d/tt9wIoU36cCiBxIHXs0IUDSRRcfU7oz2ylSDhhGlRNmhltfzhjT9JUMCeTx+Ni7DscB6aZaufGdvD7vQCgaUZFRZgV0jI/N8eBJAmKIkuSRAgCQCgUAYBEQtV1/amnnunTp8+tt976ww8/sL9yHJedHbRtalYyQzg9ankerrvuukmTJv3xxx8AwLo7sXrBg6tir244HH6M5mDo0KGnnnrqNddc89tvv3HAqarq8/oGDx7crVu3Sy+9tF69eqZput3Sb79Nu/HGGx9//HGnMjqDwxS7PlMQRKty20HbO66yeDyJmNLhDscD+5NT/uW4xxxomhEKRRwqiFAosnjx0jZt2gHw9es39Hh8APz55w9nuSvby8UoMqcgVnJ4lJaWH3FE5wEDTi4tLcdKH14q0H2wKfwatT2lNiLatk1s/Puv2aLgfe3Vd+fOXpaT1VAUvADKpK+/V2TfksUr2FfOOP2cfn0HrFq5rtMR3a4fc3P7dp3ef29CRtsfzthVbV+rwozH4xzHWRZRVb2SvH07E7Pf71VV3TTtgoJ8VdVVVbcsSxA4RqGrqrqum0w+XS5Z182FCxe/++67//vf/xo3bvzaa6+NGTPGMIyrrrpqxowZXbp0eeyxx9atWwcAqqoDAM/zhIBhEFEESeI9Hs+tt946Y8YMpvA5jtN1/VDq7sbIRQkhPA9er9fn8yWTyW7d2j/44IOSJAm84PF4DNNgLb0sCwsKCiKRCKX0/vvvv+WWW4444ggWrsvg8MUuThOkJm2/Xec7ZeTz5y+cPv0v9t407a+//iYcjiJiNBq/5ZbbTj550Pvvf7hs2Qq2Q4oq27DKyipiscTLL7/atGnzYDD72WefX7duAyKWlVU0adLsiy++2rx569ix9zRs2LiwsMEnn3yKuL3IfHtJHKJhWOecc96QIUNLS0uROb0PTtSo7Q1DQzbUFEuKK+64/b4fvp+KBBMxcuUVY64YNXrN6o333vPQpo3b2Ffef2/Co488gRS/mzylYYOmJ/U/xQkHZrT94YndNvJrcOw5rNiIeN55F4wadaVtU0MnyYThcQdWrlj7w/c/N27UvFHDZq1atgMQLxk5auGCpU726Ib1W37/bfp5510gSUrPnr0XLVrirBE2b946ZMjQIUOGImI0Gv/22+969Phfdnbu2WefO/ufBU6Ej9ipgF88npz59xwA/ptvJjMqPkSMRGJ7btz+dYgQ8b8tKCqvaAexxx1qY9nFhiriTmSU5T6zOGgirrPjlJVVIMU5c+a1bNH2xH4D58xesHHD1prFfjdTD6pGc/f0/hnsYeyGS69G+odUuq4TIauoKNuyZZMgcKLIa5pOKa5Zs/axxx7Py8v/+utJf/zx56Svv5ky5ae33nqbfSMajb355lvnnHPurJmzn3nmmalTp3bq1JF54AEgNzeXEb+xg5900kk//vjj9ddfX1JScu655955572rV28AAERgAT+eE1u3bnPFqKtGXnzpls3bJFE0Der1+Csvge7qFo9H2RvbNqEyCU/XTVXVmZcxEokl4jo7uE1MSm22PyGWpiUBqGUZhGzvHl9RUeG8Z3xE7H08pgGCadBEwgBgNOHEJmaqXz0AUlbxA1B5sS6XQikwN6rHKwEHssIDB16fAgC6YXo8LuCAUvuITh2Kirfe/8C9kWiI48EmFAAkSWLlCakEZdzF1xqGCwBA0wxAYJuhAyBYJvsKLS0rZnuyUUJEx8Vo2zRUEXO+uGscJxnsPPbU/LGdRQsREU899VRRFEeOvPT++x45undfSfR9M2mKwHuefeYVTU3l291376PNm7WLRY1wSO3c6X885x5x4aWhipRONgzLce8ZhvXJJ5/yvPjpp587P2Ga9rZtxdePuRlAcrsCE8Z/immUskhxxvR/JNFz5x33MrWZUomItfBV1bwxfivLMiqJrlJ9qZxzw7QkJdO0LctgKyDTUp2lkGFoiETXdUJIKBRipMPhcJQQjMViztA5yXNpGUoWS3NyKnycPzErAOm/090mk0lmhTG/ZlFRCfvcsghSnPrrnwKvTJ82swpxyE5tiIgWolmDi5diPKZ9NOGzJYtXI8FYxFq1YvPPP/0ej8fZzlu2bGJj8sgjj7zxxhvsKrZuKXn2mRfVpMXWbpX3K4M9jD0WwGMhJUopK5gRBMG27aKiok8//dS2bcu2Nm3aRChp0aJFWVmZYUBZWax58+amaaqq6vO5Tz755CeeeGLcuHHZ2X6WSSLLIgvLEYKEkOOOO87lck2ZMgUANM0wDEuShPr1C5566qm5c+YMGHDSZZddesEFF82ePS+RSCYSOiL06NF9+PALXn75pQ0btuzYl6I2g6WGjbWaF0XZNG1m1FAKPM+7FDlUEbMtAATDMEtKQkVF5ZIoUJo6vmUS9oZRgCaTmqIoPM97vX6fzwcILsXD8+D1+hlBgKGTRCJJCJgmm4/BMEAURVVVw+F4Mplk7CYAoGm2YRBFEWRZAABVVZnFUSOSySSjNoDK9H6fz/cvoUxup7c6YZrmbbfdtmnTBuDA5Rbffffd66+/0efzWRYB4Bs2bAzAh8PRv/+edcUVV303+QfToH/88ccHH3wgioIo8oy8YB/DEYx9/cP7FntsXLGyFx8jtHa73X379n311VdnzJjx8ccfA0BOTg4H3Lffftu4cT1Fgfz8wE8//dS6deucnCxRhIcffvDmm6/LyspKJHTDYA8+EIKqqlNK3W4lKyurRYsWW7ZsYfIjCIJtU00zRBE6duw4fvz4r7/+etOmTcccc8xtt92mqirHgW3bjz76aJcuXSZMmCCKUFxcvhuPkSiKLO8AMY0wB0FVzZycwLZt2wyD5uT4OY4rKMiLxzW5ssuNLMsAfCKh8jzvcrl4Xnz33fefeuqZaX/OIDZomvXXX3+tWb2B2AgAatJctWp1To5fEMA0iG1BMkkXL1p6662333ff/WvWrBV4SZGV33+bPnfuIkURFUUIhWK//vo7AAQCvjpaX3q9XqdvH8ti8Pk8dY3DHspjrKiIBgKBiooKNuNIEqiq2rhxY0BAFOJxDQCIDX5fsLwsJPDSQw89VF5eHovFNm/eLEkcC7zsS7FPl/ZDXuz3mJHPwm9sNR6NRs8666yzzz4bMeVjB5B+mvLbeeeOAJCeGPfslB+nXnnFdYrse+XlN5FiLKpZJiYT5qaNRY5XqUrZPKX49NPPtm3bfvnylem/6xjYsai6ds3Ge+95sEH9Jj5v1pdffLNi+Rqk+NCDjwGIM/+es4Npuiuvur7dT2YalNgYDiWee/blBvWbAkg52fWvu/bmuXOWhENqukuMDQULUqxYvubss85n7e5zcwoHDxpWWhI+fdg5Z515HjOGX3n5zWZNW/8za2FFmaolMRnHD9//EsDdsf2R9fIb52QX/PzTb3NmL2jSuMWw085m3rsnxj3j82atWL7GtinzWdYIQggz8p2qhB2aYVQ38hF3pR0IqS2mw4YaQBIFd4f23eoXNgNQjj3mRF0jTvDFttA0sHmzNsMvGFm/sMnTT73wxeeT6hc2djqm7K6LcXeQ3jfe8UwfqthjYs/AlqmxWOzZZ599+OGHw+GoaVBDp8NOO/unKb+VlUauunK0LHk97qDbFbj8sqtDFXEWTKIkVWMXjSRN065S0MYW0uFwNCsrZ/Lk7xGZFZB6cHXNNg2atqSfdcnIUQDiwAGDv/ry28WLljdp3KJXz2MNnZSVhnd5+VrJRekUEVkmfvbp1znZBacNPefbb366/LJrG9RvftMNYyMhIxrRnSc1Gk11DYqEE6Muv1qRveM//GTb1rIXX3iN55QP3v+4sKBx2zZHsJ94+aU3AJTVK7cgQVPHN16bAOB9/NEXp/0xb8oPf3bv1htA+uD9j9u26XjKyUMZ88ctN98BIG7eVPSvNyV9+ozFYrqeWjHXKfY7v1UR+8pbplrJhJGXW/+k/oPuuvOB2269p0H95t269rJNRIJlJQliIRIsKY507dLzilHXPvvMS1nB/CtGXVtY0MjQSYomZF/BkXm7Evvut/cH9pjYs5EyDIPl6um6zlj0TYOaBjLGW9NATbU3bypev25LaUmY6XlWkEtsrCiPsdR6BkKQreHZfxmTz1FH9Roz5obqJa6OacBIaRDxl1+mtmvXQRCkSy+9/JFHHisoqP/99z86NDi7tLFvsUsgNiYT9qBTTu/apWciRtijfs/YRwG8loFItmcQxGMaU2jLl63JzSk8behZtoXFRWGkOOXH3zdtLDnm6H6NGrac8uPUH77/5aIRowDcC+atTMYxGcczT79Y4ILlpRo75kfjv+LAdded9wFIJxzf//XX3nnj9XdOHXK6xx1g1bJ1aHtEVFU1kUg4zcuw0gbZQ2Jfc0UmUkwmjGAgd9LX37EBvGLUtUf2OCYatpcsWn/3XY/dM/bxkqJEuEI/9uiTXnv13XjM7Nrlf5Loyc9rwKyqvVHLXBvSxZ4xI+2jH95P2GOLJ7ZulGWZrYQVRfF4PIQgx3GSBJIEtg2SBC6X0KhRQUFBQX5+lm2DZVk5Of5IJEkp5OT4KaU2oYZhWRbheXC5ZKdPsyQJ4XC0X79+n3zySXFxKsmM8b1rmsEof3TdtCyb9Xs98cS+kyZNeu655/7888+XXnqppKTkwQcf3A2KSMtKxcZYSj/Pg2VZP/74Y98+J3q9PCGQTNIBA06WBOnTTyexr8TjKgCwJj/JpAoAiOj1egUBCgqyolG9R48efr9fTeqlpaU33HDT9ddfP/GTz2RRdrk8ggAeDyQSCYrUMExKIR6nsiwj4Pz5C1s0b/Hnn3++/PLL77zzznfffadqajQaBQBnlKrDtm1GXsJ8rixSuG+WrpqmKYrCcZwogmFQv98vCILHI1xwwfBkUp0+fcYTTzyRlaUkk8lIOIaI7733gWVboiiqqimKHMelRm/fgMmD836f/e5+wR4rvHW6zTttsFNvKieWtO7Y4HaLiCAIkJ3tpxT8fi8imCZlTawFga+xQJbn+YKCAtu2Z8+ePWjQIFHkCSGiyDst2Z2CHEkSCME2bVq1adNq4MCBL7zwwhtvvDF37ty+fU88/ri+qqqqqspaenEcx7j0asveZV39BEEIBoOhUOjMM88866zTACArK8swwDRtv1/kOM4iVrdu3dhXAgEPY7DRNCsQ8CSTQcuyIpEIpaDrRJbls846a9CgQW63u2XLllOnTkUk777z4dh7xiqKsm7dplWrVufn5yNgdnagrCzi8XhYNm6HDh3mz5/bv3//8ePHU0qeffbZp59+WtO0eDzJapxqhCAI7CFm8QLWgJznGRsnTwnYts16FhsGcbkERHQGn3U3c+5sLeABQFVVQRAczuIUjzhHR48e3atXL0pBUfjjjz+udevWmkavuOKKK6+8+PjjB4TDYdOEiy66qFu3bn6/3KVLu9dfez0cDns8MpM7n2+X25+wImtIJS/ziMjqvVRV9Xg86W3aNU1jowH/gfvsIMUeE/tawdWcdFGFiHZn5tdg0H/yySffe++9s2fPHjBggCjKdfRsEwTOMCxFkVq3bvn888+fcsopX3/99eLFi+fMmW2aFhMkURQFQWBenNp6TkuSxLL6S0pKEHH9+vUVFYlRo0Y98eTj3bt3HzjwxL/+mn/DDdd3bN+xQYMGzrfYs8Wmktzc3OHDh3/00UevvPJ6jx7/+/DDD//+++9BgwYVFW91uVxZWQGXS1BcUsAXuOyyS1atWuPz+TmOcyvu/v0HjBkzhuPw5ptvbtG8xbnnnv3555+aplmvXjYAxGIxQkleXp7f72VX+q8DWAW2TXmO93q9sixHo1GXS4hGk8EsLwDjCAdJUnjeAuArbR3K3qe9gqYlvV6v055I0wwAUBSF4yA3N/uCCy7IysrSddPjkU855RRJ4gChQYP6/fsPDgYDzz//vCzDlVde6fYAAOg6ueKKSwgBVTU9HjkUing8Hmcq30k4kRSe55kwM4JjJvOMEi4ej/v9fkfmD0PsfbGHnYgJcQgc8/wiQM1a17apKPKNGjUKBALTp08nhFAKul5XJwxFkVhpKgD069fn+OOPtSwCyDMqW8ZX8a8lOqZp5ufnEAK6rrMlX06O76abbli4cP61113tcrnYpDDu8SeDQdGyQZLAJlRxicABxyNwIMvc1VdftW3b1tFjriuoV2jb9pgx15122qm//z41NzcXABChfv2CRo0bFBUVPf30k9nZuTfccMNTTz153ejrFi1aJAicP+B9/PFHW7RooarJXr16WRZIErRt23bASQMsyyIELWuXxV7TNK/XbRo0Pz/f5/O1atUqrfswx9ZKksQD8KqqKwpr4FVDh1+v18vuDiFEUSTH8opG48Ggv0XLJgAgyTIASDIHCCWlkRtvvL5Lly7Dhg2rqCjz+eu5KzW6yyV89dXkPn1OyMryA0BOdtZuRBNjsRhbUjlaned51jXMMAx2tn6/37IsFpoVxX0iAgca9odDoSoY97aum5pmMKa6GsEKdceOvadFi1askWMdLp94PF4XZ95OB/CSCcOyiG2lSMFS3iaCM/+ee/VVY045eehNN97529S/1CRJxC1is/NM+YFN00450Skyqr/58xY7RQRrVm9kkQWWQbhu7ebiovAjDz0D4H715Q/iUbp1c2jmXwt/+H7q5k3FzCtWWhKKx3QnvrB2zcZ/DXHRSlT/UyKhUoKRcILRjYcq4k7mP1I0DIu9N3RS1yhVts1kPldEjMeTrM46FkvYNtV1kxBkN1dV9VUr17Vp3bFhg2a9ex3/1pvvM2LFRNxQk1Y0onZo37lf3wEsYqKp1n+sDopEIolEIv2TRCKRSCQYP3odLOmHPA4UsbcsYhgWe0RqlFYnBXXr1iK32zt+/Ec74+ZlBp5pmqwJL2Otr/xRYpq2YRiWxfy3xLKs6q/OoUzTZk92LJagJOXeZ+56pFhaElaTKTlx8nnZb7HHi0XL16xZ5yTVYir91iQEi4vKkeKTTzx31P+Oe+yR58pKErqKSFBNElZdEw7FnW8ZOnXmIKSYSKjJZK0lhrWJ/bZtxYhIbNy6pSQe07ZuKUkdLW5URi4oC6k6XEm1bU4Qnr13wgqJhFr9HrFP1q3bMGvW7O0Z06mf1j//7Ot6+Q1+mzoNHdLUXYRhGOl3jV24c9NZLaaTqqyq/9408ZDEASH2jGDLsghTjzXKM3uyWRVdkybNrr12NKZlnlRHPB5Pb4PNFvC7cW7xeDwUCrH3LKc9NQFRRIpvvfneqpXrWFSSiYptp3pUm6Ze+cZkD19xcek999xXXh4Kh6OJuK6pO+iyom1lHncQQPJ6ci6/7Fom87aFoYpYqCLmRCid9ATWrJIJhhOKr446tP306X953AFZ8rBqyFBFnMmt025c11Kvzo/WuLE5KB7TWFLDmjXrNm/eylItWFDGqX20LAuRbNu2BZE4UzA7ectMHeeyS68UeGXB/CVsKtk9aJrmVFvrus7e//bbbz/88AMbE9M0q1SRHFbYbwubKk0jWXvJOrypbA3PfMXnnHPO7NmzWXvm2vb3+XwAkEgkRFF0uVzMl8NkEnZsL832r41yq9KZzCKFSUnKIsQSRQU42LRpy3fff7tp84YH7r8vGAwQAoLIHJhoE1uUBPYtSRIQKQCnqolnn326Y8f2AwcOZOVxyaRGiOXz+WKxRGH9vMmTvy0pKd28efPpp58eixs+n8LzkJ3ttywURc7xUbPR43lGOgqCCLvhz/vxx5+uv/76I444omvXrh6P54MPPvD7A48//vjmzVs//vhjQF5xSZpquNxyMqG53LJtUeAoIF/l1bbNRCKem5tr27bL5QqFQpO++Wrbtm1dunQ55phj8vLyevXq1a5dG0I8giDwPADQ+vULYvFIwJ8FAMlkEgA4DgVBEgXOtmDMmDFvv/POu+++99xzT+4GNwpz1ymKEg6Ho9Ho/Pnz//rrL03Txo8fX1FR0bBhw4svvvj++++XJIkVjxym2F/zTRW2+Up+69Tn1deQlKRWm4TgF59PAuAXL1pex/HTK+Sc36o0/1h3qu1JpoymqsbkU6a04/EoIalcNOY0YmyfN954s6K4S0tCmmqllfdZqppguWuqmmDfYqY+AHz++eeIGI8nndUGImGGSSKhbt5UhGlNAcpKI8mEqWt2PKaxUUrPHdqu+Wu3Y2rT9hddNNLnzWKrekpw5MWjvJ6srVvKf/h+assWHWTJn5fb0OPODgbquZRgYUHT/LxGNW0NmjVtlZdXr13bI5o0adau7RGdO3flOEGWXccee/wJJ/QVRVkU5ZYtW/fqdfQ777xXXl5uWQarayTEqqJvnQSnl196IxjImzN7YYoyYBehado777zTr1+/5s2bK4ri9/sHDhz4ySefLFmyZPTo0RzHLViwABFZQeQuHnuX0pYPXOx1sWepYE66G0u3NnTirE6dxWGoImZbKQ5ctjN7uNNT5Vju15bNJW3bdHz2mZdqND6JjbVl49Ha7wVbtzt+Kdy+gqglCw1TE5Dfl/3TlKkV5VGkjrFdw403TTsWS8iy64033jJ0Eg7FkaJtU4qEbRaxddPQDcu0CKFoE4wnDEoxHrc2bSqnFA0DbRspwYryWDiUiEU1x8CuZgxvP2cH22WfIlJs3ar9JSOvYMMVixrfTJqiyIGff/rTNCjzYlTZLIvUuDFaZEadxFBUVHL00ccecURnyyLz5y3+8IOPB50y9Ojexzds0FQS3b16Hnv7bWO//+6nZUtXlZaE0hcsrPEJ2445us+J/U5Wk6ZzI9KVRDKpOb6eZFJLJNTy8tBff8187bU3jj32+Fat2uTk5LVt2/6yy0Z99tkXmzZtYUeIRuPFxaVut/eSSy5LJNR0xcCOHI8n2Wye5u2rnom8S68HqPDvfW1Psbws8vdfs7dsLmZ3dOGCpZs3FbH2LJ9O/PLC4SOfefqFObMXMMlnXiX2TDO1xoSfzQ6aaifiRklx6Kj/HXN07xPSZw1HsNnGniS2OZ/UvVakFJNJjeXSa5qRNgXUIPbsSSoprggGci8cPtIysbQkVPdIJJOaIntfefkNYqfy/ClBioSiRZHY1DJty7Qty6bOBcViJqWo67h1a5RSnD9/5c033XXC8QMGDxo25ceppSXhLZtLkGIsWsU1tf0ZrU3s/3fk0eefdxGbMiwDP/loEg/eX3+ZTul2AyEdpBYwfwezVjRNY/pz0qRvc3LyHnzwYWe+XrVy3fx5Sz7/bNK119zQskU7ACknu6BvnwHXj7nlxx9+dewXpMhcDHPnLAKQnn7qeTbUbD61bVpeHnL8l5TimjXr3nnnvXPPPb9VqzaBQJbX6x89+vqXX371n3/mhEIRNluxq3aE/M033/b5AjNn/sMknCmJ9CnAMAx2UTveeqf6YJe2w1jsv/7qux7dey1auBwpxmN6yxbtbrzhNtvCs848PzenMCe7QBTcXk/Wzz/9zqJTjq42dOJwyDGad8dGeOjBxwReWbN6Q7rYs6mkDucTVq4jqm/pep5pkjT6ihpuHtvf0EnXLkce0bHrhvVbmPauYySSSU2WPE+Me4bNQUzsCdpM7CkSmxKbEkKRIqqaTREjEX3r1gpVRcvCVau2FRa2AFAaNmjmdgUApNtvG+uMzI6oru3TtCVFpHjH7fcASC++8AZSDFUkB51yenawwaKFK6ufdt1IkxBkNEGIqGnGZZeNAuAXLVwWi6qVZprpeP6XLF5x0423NW/WWpG9iuyVRPeZZ5w7YfzEJYtXsLbF8Zh2ztkXdGjfef78hVV+MRSKzJo1++677z3uuBMEQQLgO3XqcuONN//yy9R4PJlOOsLojxymRsQU53L//gMGDz6VRYtTT45NnS+yRVz1kayp1nAX6xQOGOx1sSc2fvH5N35fzprVG5FieVkUQDrv3BHnnnNhvfyGD9z/6KaNRb/+8qci+5o0bsmUfDSSZJLPSs2QYkV5lAk8ExjToL/8/HswkPvoI0/EomoyYahJMx7TwqF4JJxQkyZr88aWEoZOWMwstbKoHSzazKzWZFLTNKNSCdRw89iqMBpJvvD8KwF/zjeTvk9JYO2Ix5OS6L7rznudec00qE0tR+wpouPZSEk+xUTCjsdJPE7Gjn0MwD3p6x8TcSNUEb9w+CX18hvMm7soGkmSqgVj/y72q1dt6Nd3YHZW4dG9+zZv1i4YqPfKS+9Wmz7+HU61NYNt27FYwrLIggWLcnPzzzzjXEpSE1P6jMwaeMdj2vJlq99958Mxo2/q0b1ng/pNsoJ5vXsdd+cd93zw/kf/zJonie6zzjpny5ZtlkVmzZr97LPPn3feBcccc5wgSCec0PeMM8567LFxc+fOT5+yEVPBYGdFYNvU4WtnN3ThwsUej++1194gDhcTIiN0RtyhYPFQFXsO93bVAcKMGXOGDBly7LHHtm/fvqKi4pNPPhk+fPjXX3/dvn37CRMmFBTkWxZ5/vnnx44d+/vvU9u2bfP444/PmDEjPz+f47hIJML6STPKZ5YVRynNz8///vvv8/Pz8/LyWBomK5/iOE6WZUVRDMNgXnpErKyi4QVBSCRr7uVcVlY2aNCgsWPHduzY3rK2U33XcV3JpOH1KvG4FggGH3/s8ZEjRxYU5NSRWJZMavXyCy+//PInnnhCUQQAME0qyMBz4CS9pQc4wuFEdpbPskDXbY9HPO+8i9auXfvD95MLC7M1zVq0aFHfvn0vvfTSF196DnZMdk5HZYQiVebAVeZKFxWV1a+f/+qrby1evDgnJ+eEE07o379PPK75A+4as6nrTllHRF3XWboryxQ2Tfu999678sqrp/w4ZcCAfrGYGgh4olE1GPQwaiD2xVhMRcRg0EspFBWVLF++/L333pvw0QQAaNqk6datWxWX1KtXr7Vr15aWlrpcrkaNGo0YMaJXr15t27b1+/0sdRcRLMuuUo9EKSBieqwnkVB9vlR52HXXXffRRx/Nnj27ebOWqqoGgh4A0HWTHTAtaJIe30mNZB3jUBP2OUPQTmBfBPBEUYxEI8uXLy8uLjYMQ9XU8vJyQRB4nm/UKB8RdJ306dOnfv36y5ataNKkscfjEUUxGo0yZi5RFBGxadOmFRUVfr+f5/mtW7dqmjZ48ODS0tJAIMCaVbP1J8dxrLDEScBmnwOAIAiiKIpSoxpPMh6Pf/zxx9OmTbvxxhv79evXuHFjr9fLcVwdsTF2fK/XPey0YVOnTr3llpvqHgdZlllaqCNCosgDt50p0okhsr9nZflMM1XCJAggCMLGjesLC7MBwLIsTdNs2w4GgyyYt6uoVy8fAEaMGOH1KuwIFRUxl8vFenNX37829cDyWzmOEwSBUsrzvCxLACDL4hVXXD752+/vu+++Dh06NGpUCADBoMeykMl8NJrkOI713tZ12+USs7Ky+vfv079/n9dff33dunUffPDBokWLiku2IWKHDh1uvPHGQYMG5ebmZmUFnSmoMjFZlmWREAyHw8FgkE3ZPA8AHMvFQkRRFFkslqmNW2+99eeff3722WdfefmlQMDDJnqXS2Zz1qFflrO3zQli4+KFa3KzG82YNm/Nqq0L5q0EcF9x+fUN67fq3vUYRiwRCRmXXXIdgHv5snWbNxWVlJSFw9F4PKnrpmFYoVBk7dr1xcWl27YVRyIxyyIVFeHi4lJCMBqNh8PRiopweXmotLS8pKSstLS8vDwUCkUikVgslojHk5FIrLw8VF4eikbjyaQWjydr3GbO/KewsEHr1m0B+J49e99xx121XlKap8C2MBJO/v7bjKxgfklxqEoGTnW0bNH2qiuvS6fKdA5mU2JaxLSIVZnCx/z5K1et//zzyatXbx49+tbCwmaz/1lQXhZBik+MewaAnzLl53R3VA3jT7aHRXeI4lEsLQmxNZRpUE21UlmAtV10LaiS6Mbchqqqx+PJ8vLQzL/n5OfVv/++h5FiSXGl357UTPvpXIhlEdbRiBDcurWI3c1kUksP96ZnKFWJTpqmzdZoVcYBdwwBTJz4WevWbSd/+yO7aseZX2X8ajLyD3rsdbFXk2TOP0sbNWg986+FSJBYCOC+eMRVLzz3psD5rr36lr9nLHj7zY8K6zUfeNKwdF4qxxMTjycdv3p6/ywnCZTR7LCN5YezN+yvhKCT9ls3Bg0actZZ50Qisf79B9SrV9iyZeuffvqlhv12jDsixQXzlwb8uXfdeV8dYsPOp0P7zleMukZTLYfh1xF7i9i6YemGZVrIvHqxuL5s+Zr2Hbrk5DQoLo788MNvgWBevfwG7707fthpZwm8ctllo4qKSt566521a9fX9ru1iT3zlRg6YTGFREJNBRRrQd1Dl0wm0/fZPtQUh19wcaOGzdav28x8H+nBFEYHxuQwfX3O3qfPAumfs4NXuZvbMz52BE1z11WZCMLh6MCBpzRv1jocimNlIkbKU1tzAI+J/aGAfeHJX7hgxYXDL1u3ditSTMSt4Rdc+vBDT2oqffut8Ud07AGg5GTXv+rK63//7e94TCf2vuNUqYLXXnujUaMmjMf6u+9+OO+8C9xu77BhZ/z553TqlKZQtEy0zJTQJhNmNKIixZ5HHd+qZUddI4ipQgDm6GLK0Hngevc67tQhpzOZNw3UNZsi2gTtSvWvalY8oRsm3bK1ZOQlowrrNzn+hP5vvPke++s33/548UWXde3afcCAk++8c6xp2uXloU6dujRs2Pi7735g82AslkjPdWdFMg71ECMs2wdI9UEkuGb1hm5d/3ftNdej07+kUmiZjNWRWcyQLuFMvBksi2iaUVv0pMo0V33eLy0tnzt3PoD45hvvsj2dSGGak7JmsWc7sLAFu8WVidupxRdWEswxByH7K3N/HgglQHtd7BlnluPFNQ3cvKmUkSjGY/qmjSWrV23YuKE4HEqwfeqowNvb+PPP6QUF9SdM+Jg9SRUV4cmTv2ds2XfddTcT+2gk6VwIK5JBivGYedaZwwP+/IryGFYauuxOs3tMSKqm4PRhZzPazO0BRYqJpMbs+Vhco4iJpPHr1D8DwdzcvMKxdz+QSJoUMRJVWUiPKSUn3MBsnL59TwTgX375VXYhhk4YsyhLCqqOutcFexDsnj726JOFBY1+/eVP52TC4SgTME0z/lXsnR6qLM7KVHc1axwreZarfqjrZnqpkrMDIRgOR6+5ekzHDl02bNiUnnGUfoBquTqIlaLOUFlqZWNa8aUDXdfZDulxwXSCs/2CfaHt2aKRLWjT4vCW897QaSKusyxUQvBfTcq9hFgs0bFjpyFDhjpteSsqwuFQ/OGHHm/Zom3nTt2fGPfMurWbttfAULQt1FSaTNhTf52hSFmvvvIOIeh0102PbDFVc9GIS/ufeHI4FGcd5mmanmeq/p/Z8y+97EoA8Ywzz/1w/CeqZlHEaEzVdJsimhYahqWqKuMpNAyjoqICEZcvX3nbbXfwvDj8gotZvq2zsfJVy8RkYruA7aj39lbAyTBSvT22bC6uX9h40CmnbdtaqmmpCjmW4cPkpO4kWbYWqK7VVVWvqAjXOGuwOu70rzjv02uEEVFTrRbN29x9971YuYS0LKv2dJ3UeabPm2yuST+NZFJzXAlYqQDY9aa/34/YFzn5kUiMpZSbBtU0wzSobadqKm0LbZvaFhKWRWdTlk+2D86qCtgtHzny0gYNGq1bt4Gdgq6b7MFdtXLdxRddJonuIzp2Hf/hxBSva1oicKgimZPV8LZb7yFkuypwLsR5qi+/7Krjju2bXjar6XZJaYj97513P/R4g/UKGr708uukcpdE0kiqJlsLJNXtOepM8hGRdQctKSmbPPl7UXC1btV+29ZSpFi0rTy9xSXSGhfAeyvOzMTMtlKZ9q++8mbAn/vC868g4saNGxGREOJcQh1MtelWPQOr3bDtHR4Th221Svd0RLQsoutmuliyfdiyHyneftvYnJy89es32jZlZlT671cRe6a62QrCNO0qdlP6rzguiR3Ltw+Iat+9LvbpPAdsUNhd0XVT1/UquXHJZHJ/iT0i2jb99NPPXS7P99//6DDwOuKNFJcsXnnC8f0BpIEDhvzx+8zysjhSrChPxCJWJGRccfn1AwcMda7IuQrH9ahpxs033X7M0SewNCRDp8RGimjZOH/B0guGjwSQhp1+zvoNWyhiUjVVzWLaniLqBklp/mjUtk3bNsPhCvY8OUwemmr9NnVaxw5dmjZpNfnbKezME3E9EddTCUI7nlhNaad7TOxT40CxvCzCpp7Th51zZI9elG4viWciVHcBbLoMM7XP4jtM3ihFFq9hO9TRF6zGZ8q2KSW4bOmqHj3+N3jwqeFwlN2smoaIVNZWqenHZDtWVIS3bSt28vzLy0NYOR0bhsFW+2yy+9fr3TfY62LvEBvUNrWz4mdnRtyPYo+I0Wi8c+euN9xwEwsCsToiVimANNVU+/ffZhzZo3eD+s2Hnnr2vLlLkSK1MRmnP3z3uyz5WTKpbdu6rlcu8lPXaxjWgw882qF953Ao7ij8LVtLX3/j3abNWjdu0nL8hE9jcT0cSRCKpWVhJvAVoVg4kmDvzdRjTSrLAbfz3juNg+fPWzx40LB6+Q2ff+4V5lgxDbaGquL9qi7ze0HyKToOkXlzF7du1f622+7ANAWoqmrd7NSOJDMNX+WvzpNimjaT2HQnH7Pn058mFujZ8RCIFCdO/AyAf+ed9xAxHA7XIfbOyaRf5ptvvn3GGWf9/fcsRFyyZNmoUVeuWrXmzTfffvbZ59k+W7duHTlypLOk3+88/PvAyN/BhiwvL2W1qIahVTaTJIRYuq5qWlLX1f0l9k7M7/HHnzj++D5OCcd2C9nGaERNxA1W2/PKy2/n5TYM+AquvfqWeXOWJ2IkESNH9jhm9Ojr2QFZXadzg9ny75mnX2japCWzexNxY+WKdf1PGsTxytnnDC8pDdPKVHwnbq8bhKQF+ZKamkyy1pEkFouwgzvnmUrOp7h+3ZZLRl6Rm9PgzDPOc7rcI0VdNyvDokY1mTcrO1juMbHXNKPSj2My/8799z3scnl+/fXXyjGhTPWlJ/ZXvy9Voo+EYDyeNE07kVAjkdjKlatfffX1k08e1K5dh+7dj/z662/mzJmX3tTcWcwzjyDzDm4v5ksYSLG0tPzss8894YS+FRXhHT3tNYi9k1vNnoRIODH8gosBxNHX3ZhMGF9/NRlA/GnK1CtGXdO8eUtEJIT89ttvHMetX7/ecenvqUHePewLsTcMLZGIYWXjV0SiaUlEQqltmrpTx26aejwe3Y/anjnJp02bEQxmr127PhSKOH/SNMPJlU/EDaRICS5ZvPKO2+/Lya5/ZI9jnhj3/PJl68468/yc7HrMJ8wmEeascjTMm2+8W7+wcdG2svXrNj/80LiWLdr1OLL3+AkTmWPPMKmqWWZlV1vTIuyNTba/Tx9ArLSTWRYTs/OZ61TX7Oefe6VxoxYn9jv504lfVrpOq68295aRnxrSpOm4P5Fi0bay9u07DhhwMqP0Ypq87vqldPcku661azb+8fuMhx587Oabbj/2mD6K7C2o1/Ck/qf0POoYABGAz87O7d37mJEXX/7oI09M+vo7ljLARDTdzcEsfGcFt2D+krzcwhtvvBlrChM4jg+aNr06aVfDL7hYljy5OQUTP/ni99+muxTf0iUrL7v0ymAg959/5mzevPndd98F4Jmr2GmXtB9xQJBqOY3H9nY3kkp2jRo2lsOLiJs2berbt2+fPn2YZmAfOikrTuqKE5KcO2fhiAsvFQV3dla904edAyBN+vp7rGzSzHy57AINw/j88y+bN2v9xeeT2rXtJArem2+6IxHX0+tG6mL9rDzDGpFuVjCUl4cWLljKc0qD+k1//WU6i544wkPsmlNcnDiWM+sxG8GpYHNOgaXBMD1c41bt/JHYOG/uIlFwsTprpNu5tJyNsZVWqaTUVLp82bqnn3qpc6f/ceDy+/IAlHr5je+84/7p02avX7cNKc6bu7RtmyPqFzZ+8YVX77/v4fqFTThwKXLA58lv1qT9a6+8P3vWklSQ2EZDJ5XLotQntoVXXzVGkX0Ox6kDw7AcTg7nxJzwraHTM04/F0C66srR7O4HA3lffTn59tvuBhBFUfb5ArLsEnhl2dJVDjGhc/nM/8L8i7tF+7Y72PulODuRHZz++q8M1jsJ0zQZZ5YgCDumWNMd6yuAFUsYhiHLLsuyZFkePny43x986aWXWAcOAMqicV4vY6RPcUJrmiEIgiyLxUXl33777fjx42fM+ItQfPihh6+55ipZlrxehSLwPOi6LkmSIAgfffTJ8OHDAYQ+J/S58MKLRowYTqgpijxLa3fGocaccHbD+H/Lv2eJ8Wz/REJVk0b37keWl5c///zzZ511lsfjicUihYW5O3xnx1/TddO2bZ/PU1ERXr58+ezZswsKCjp37ty2bVtW9WSapssls5ZEorgL9QCIAAiDB5+2bt26WbNmuVwuRUl93TRRkjhE1rcDEGHVqnWLFi3atq146dKl0/6csXHT+qxgTqvWLbp26d7xiPb9TxwQCPry8wLAga6Byw2AsGz52iFDTjniiCMef3xchw6tZ89etHjR0rlz569cuXLlypWqmsjNze19dM/evXu2bNmicePG9evX93q9rOrBsmDp0uUjRoxo377t+++/L0miKAKlYFlEVgR2Q0zTDoeic+fOmz17tsvlOvXUUxs0aCCK4rXXXvvJJ5+89dZbt9xySyAQKC0t/fXXX19//fWvv/7q/gfuRcStW4rGjRs3f/4CURTvuutu26IjRow448zTBAGc592sVk20F7GPppdq2L0k0J0HS5Owq8R5EGsLWaV7aDdv3lpaEnJM4nQwizQWS/HAMApd28JYVFu0cPnXX303cMDQJ594QVPtRFyvfoSJEz8TBOmO2+9ZuWIdm/Ity+HAoA4fRo1XVLe2d/5UhRyS9Rq86cY7AZTR191URVOlriJdP1fmWSDFC86/qEnjFsFALs/J9QsbP/zQ40wzO5XRWPvtMgzLMCxnLe2cOLFx4YKlebmF14+5uaw0zEKhDg9KPKb9/dfsW26+o22bjlnBvCaNWwJIpw454+23xs/+Z8HmTaUV5bFoRNc1oiYJG3+mri0T2Sdz5yxs27b9scf0mTd3MTvDcIVObVyzauusvxe9+vJ7Q089OzenUBRcjRo269Xz2FGXX/P1Vz+w3oRI8ZtJPzSo3/T332Y495ddY2lp+UsvvXL88X06duhSL79Bfl794RdcvHzZambqj7jwEgCR2PjWm+8BiABi0bayyy69sk3rDoxVaeGCpQDi0iWr7rn7wRtvuOPddz5q0rh1SXEEKWqqzX5lXy5t9yOXHtl7Mo+INQl86pdrjFFTiqtXr7UswuixQhWxivKooZNNm7Y4+6xfv5EtzBxLLxZVN28qLi0JO2bb4489+9STLzLhSSYMSnfI31q0aEm9eoW//PwHUozHttNj0Mq+i7st9o6os9UEOxTLiQhVJCnBd9/5SOBdjRo2/+XnPxYuWLZo4bKFC5YumL9kwfwlCxYsWrBg0cKFixcuXDx/3uK5cxZu3VLy6y9/FBY0Ov+8EatWrluyeEXzZq3btT1izeoNlrl9TfuvhELVkUwYtoUjL748Oyt//rzFSHHrlpK//5r90ouvnXXmefULG/t92U2btOzb56Tbbxs78ZMvHFImXbOdDtnOFo2orKaAyQ8bzx9+mJKfXzBm9E3JhFlWGqMEK8oTpr7drg6H4jNm/H3jjTe3bNm6aZNWuTkNcnMaDB50xmuvvr1k8comjVt2aN9l6ZKVGzdsnfn3nDtuv7t167ay7CosbNCtW4+LRlz60YRPN6zfwvIgLRO3bS0dfd2NwUCubWEknDh1yOkA4sIFS8eMvqlfv/6IaFnWsmUrvJ5gOJRYuGDZ7H8WPfjAuO7derN5ijGUMzfHPvNq7Tcjn1Ja3ZTdgwWPpmmKrCHmzgDhzz//euyxx0aMGHHBBefEYtp55513+eWX67o2Y8aM+x+4NxjIXr169SOPPHLaaaede+6ZAEAIuwogJDWALEJ78803q6r6/vvvulwKx3GSzOm67nK52Kuq6mecccaG9ZuXLVus68TjEZiBze43pFH61nCOiFi7kY+I1b9l21QUeE2jbjdPCEybNqNfv36CwMuynDoOR50f5XkA4KORuMfjvfDCC1etWhWPx19//fXu3TsBQFlZpGHDhq+99prb7Y5Goxs2bBAEoWnTJpu3bKzxfFjPGadvNJvWAcDj9pWUlGzdunXmzJmFhYXNmjVbvHhxaWmp3+8/7rjj+vTp06pVq+bNm7dq1crjkQkB07RkRSQ2CiIn8BxwoKmWbqjZWcFUnzUOLBNNSxcFWZIF2zZ5nv/++x+vGHVV7969J078VJZrGExNN2RZFARh7pxFK1asisUiv/7665IlS1auWgmAoiC2bNmyvLzcMLXmzZsfe+yxxx13XPv2bXNz8/2+YFaWDwAsCyUpdeSvv54MACeffLLLJa5fv/m7774bMWLEmjVrTEvv3btnPB4XBOnDDyacffY55eXlN954s2maY8aMOfXUAYmE4fMpAKAb5q62/fov2G9iX9vv7inJj8VikiQpiuIsdGs9MgIAjBv39B133lEvv2DlypVZWV6Ol68YdYVhGFOmTJk58++mTRv++usfQ4YMufLKKx999DFJ2t4yz7ZBVQ0OBL9fBICjj+lr2/b3308OBPyyzAO3nbMBEW2bPv/887feekc0Eg0E3LpOXG4BKsWerZxru6K6xZ7BYRZwPglVxHNy/Jpms8Wq35/Tvn27u+66K/VDHK2UeZ7jkOOEgD9LVbUWLVqcccYZDRs2/P77SSUlIdZbqn79+o888sjbb789f/585jGxbNOluNjcUeMJp6sv9qHb5U2qSbfLLQhCMpls167d0KFDhwwZcuyxvdgOlAJriwoAqqYripJOlaHruiQpgsBpmkGpzZpbObAsC4BKkhSPJ1955bVx48ad1H/gxIkTKipiWVkBdliOT+1pmjoi5/MyYnXD41E4Dr77bsry5csmTpyYl5fXu3fv04ad2rVrZwCIRuOyLKba5mHqPOPxpG3bublB9uvJpOFyKezMGcc5x6czdkAirl999TXjJ3w0ZvSYfv36nXbayYSAIIBhpnqZMd1Qx/3dU9hvPPnO8417x6VHa+G9B6i5FWdOTq4oSKVl5WPG3PDkk0/ynBiPJxs0aEAI+e2331u3br1o0WJFcdk28XgkdmzbAl0nrJsa6+FLCLB2zj6fr9JFB84MYdu2IEgdOnQI+AOffPLJJZdc4nIJUCnP6Uq+rkmqzktmw+h49QAgJ8cPAG63CADTp89MJOMXXXTRsGFDamMB0jXb5RIRoX379rNmzVq8eEWnTu0A4I8//iKEtGzZ8tNPP83KyqqoqIhGo02bNqmoqKhR7FmLa57nGamRY8UwJoyKigoAaNGiRXl5eaNGjdjJxmIJSmlWVgAAmH3g8bgopYjUMCxE4nZ7XS7ZsmyeZ22OJV3XCbE4TnC5ZJ4XOQ513TBN0+/33nbbLevXr58zZ868eYu6d+/sKOdEQpUkQVEkSfICQHFReWFhHlR2AR4yZOCQIQNHjx7tcouUssYKwHEQDPrZdVlWqt+J3+8NZm2fdBCB9T5gXUMFkeN4sCzCZL6kpMzr9fp8nmOPPaawsFDX9eLibYZBFYVn7d6Z2O8GXcpuYq8vI3YCeyOAl0gkdqyEqVwz05q35597pVHD5sz19crLb7tdWSOGX3HXnQ9w4MoK5mdn1Suo1whAOvecC1m8Z+XyTbGIhQQNDaNhm/WuQoLHHn3SoFNO11Q7tQBGxDQyVkpx3boNXk/WqMuvITamF+qmK8Ya13h1r+2rf4UQwnINysui7HX4BRd7PcH0E8MdfavO+Fgmzp+3RJa8fU44afGiFa+/9k7jRi3at+scjai2lcpW1DVSE3tnbae3A00lS313TllVd8hXTU/Ic2KuujPESCi1WQ4IpbaT9FXZhshCtOLxqGUZiLh581bWaJCFBp3D6rqq6XFEgmldCZBu52vfMbs+lbFbpWbWCWGmBzVxR/pwREwmU4F6xo/C1vMs+yPVTA0REYuLt+3xvInasB+74jhMUtRpQcvosaoruho/rBtM2ziH/ddFvmmatm2ff/75mzdvfuuttzRdy83NXbRokd/vv/POOwsKCv7555/XXnutYcOGRUWhiy++ePGipZ07d37rrbcKC/MCAUFVARFME3ietyyL53lmmjJdwaZ8wzBkWWnatGleXt6aNWs2bNjaokVDNgxVrq7Gi627B3v1P6UuGYHnOQAoLi6aM2fO2LFjWR/eal9kGjt1zqIIbdq0efXVV5977rlOnTsF/IHOnTtfffXVfr+b48AwiGXxisLvPFEcx7EWRqkf9nrdkMb/5/TJrTxzcPbkKtn/nLgp+5ANafpVO1YVRerxeHieJwQbNmzAAcTjGqU0GPSqmsHaK1FKRUaXyEE8HmOGOqXgdssUAWCHRkOiKAJQ5z46cK7IOQt205nB4sDpAu4sB7ze1HF8vu0mfUFBQe3jt4exP7v8MiF33tf9WO+5X63ZyE8mkzzPu1yup59+eujQoQCQVOMNGjRo1qzJySef3Llz+9atW3/11VdlZWULFiyIx+PPv/Dsueedv379+tzc3JKSUKNGuZGIlZUlcXzNPgvTNBVFYWXFV1555eOPPy5JUjJpen0yGwOsPWL/X0ApZGf7EWHp0qWhUGjkyJGSJLCu4el7Oe+YF01RJI9HOu+883r06B4KhRVFbteuPVsvAIDbLbHTVFXT493bjqjaF2s1QTd0l+IxLZPnRVEUFy5cPPaue1gY5cEHH+zUqVNZWcU333x98skDGjZsqGna22+/n52Ve84550gSl/Jy1nAHaNqbXTXE086/xmePq7bb3sd+pvVkT7nzrO8j6kJuxw0AAAxDVxQZgDZqVK9Ll04coKJIPp9H0zTGCelyKYlE3O129e/f78svP1+7dnX7dm05HnkB8uvlAoAgcIjA3HKIWKnGU8dnzjYAsG37oosuUlV18eLFrLl6OsOvsz7fU2Ct8jgOXnjhhWOO7V2/QT4AqKqatssOD5wggtsjEYIUweORunTt2Lfvsf87qkdOjh84ME1q2QQx9fTufZnfZbgUTzwel2WXKIqrVq3p3u3IGTP+Wrx4yezZc4YOHfr1118vWLDg8suvWLFilaZpbrf30Ucf/fnnn8PhMAAABxSh2vD/d4FMyxA7MLg5979LL82TvE+0fQ2nAoBw4YUXdu/e/Ygj2lIK48aN69at24ABA0zTOPnkgc2aN9E0q2XLlh988EH37t2XLl0yZsz1oijedtst7du3NU3T7VbKymP5+QGneyem5H775bhcLubURcR69eqdcMIJ77///qBBJ7K/8jzvLM53Nui4c0AAQYAffvh5xYoV519wH/vQ7/dV/r3KM53SZpLMEUJsyokijwCIRNUsQeAcS1vXdZ4X90lWGV95Vjv1ahiW3x8kBHXNvPqqa9u37/Dpp5/Wr19/8+atF154wYQJH91991hRkBXFjcgBQFFRUSwWY/MvW6LXZgftFqrwbVe7szs877tHyL1b2DcuhDrACMYsy3KiuzXus6uHZQesKful5nQd5m2KRuMs/4zlijPmj9TXCCYSajQanzjxM58365ijTxh1+dXFReWaahdtK9c1YplIbDyp/5CBA4aqSSvdc8bOgZUea5qha+TJJ54LBupp6g4FmLvdjbtuEILnnz+8SZNmmzdvjceTOw5I1VIcw9AIsSr/VFdTUKcT1oGJv2b8AyDddecDjBYBCX7+2bei4J3y41QAUVHcTZs2B+AB+AsvvKim2huG/1iqlF66V/nddF/yDnvuO4rOA4K7v3rb6X2F7dYXx6WW1qIESVUTReA4jhcAgBqGAQCU2l6v2+PxNGnSZMRFw/v16+d2u03TdLkERVFkmTcMk5Aq2n47CCGBQAAARFFUFL59+/aEkC+++IJltleew56/fNumS5Ys+fPPP4866qhGjRqwWJpt27UNCMvksW2T/ZfFtwHAsgzbtg1DU1XVsgwA4Hn49yYi+wPFxaWAkJubJ/BSIpHIzfGxNYlp2Eg5RXG7FHe7th36nNBv2LBhAGBZVpWm13WMz9455X26sIf969JjcKR9H8p8DaMsCJymaX6/FwA8Hpdp2YIgIHKCIAgCB0AptQF4UeR79TqqV6+jNM1wuxVKgSLIshQOx4LBgCCAY6Kniz0i2rYtCIJp2iwxoXXr1s2bN584ceLpZwxFFBwvNJsv9uBQUEpnzJhRWlp6++23JxIJn89nGAZzTdf2DQSkaFMEnuMrzXgqiBzP8aLIA0gAYBOT4ziBr7V3yJ7Ervg6EKGwoF4sphUWFkqS9NeMmeXlmsvl8vm4jz/+uFWrVuXl5bqhv/zyy7179+R54HiBGVkAQAhhd4fjuH0vivsSB4S2Z9i3qp6vfN0+Am63goisa40si6ZpchwgIsspkGXZtm0AGo1GAcDlUgDAsixCiMul+P1+5oxLL6Tb4fd4HgB0XWV/atOmeb16eYsXL2JHwMpsJUSsJdFoN59CWRanTJnSu3fvI4/s7vP5dJ3lvVXR0s5ogGnaACBLLo7jnM8JJTwnGqahaQbF1BoV6b66X9wuvHIc2Da43a5AwP35558uXrLw/AvO/nD8u+3adfvp5x/Pv+Dcdu3aAIAkSZZFDNMKBAJ+v59l+zEPC+yY5ggANT4tOwc+7TXtctLPeYed95E8HhBiz3K52PvaQta7ekxRFFm/rWrf5evYOI5zFC8LJnMcJwiSKMqMORuADwaDUOmil0SJErBtIgicJHEcB263m6kORRGhsr8VzzOPuhUI+DgOgYOKUPj8888LhctXrVpl26nyBJbQVin2tJatZpgmM8uBzUrMr4GIyWTyl19+uuaaq9hZuVwuliFX2wjIsosDAYBnr2wTeAmAV2S32+3lORGAFwWZjcau3pfdxK5IPkUbOAoc9D76qHfefR3BvObaUbxAnnv+yUsvG9G8RZNrrrlSVkTFJSiKdP/995555unRaBgAmGuZDV3tD8muopbvcjuxz97DvnEhHKogNqsMsx0OmTNOP/+k/kMScSPF3EIqHWDUQLQIsVQ1wZxqS5Ysy83Nf+utdyppGyuPmXJDVqFzsv7V5RMOh9kby7KcOuLbbrutc+fOmzZtcjx5rDZmz4/FgYR0tyUrkWJWFWN2LCoqYn8Kh8PVEu8O8ZFhOCC0/eEApjwJIZIkWZYFAB07tu/Spcsvv/zCTErTtNiePM8j4m7M/S6XCxEBgBDCikY2btz40UcfderUKSsri5kDpmlW4x05pJBIJHRddy6Qrc5cLhcrx2QcIYWFhYZhqKqalZXFQqosMdxpl3rI47C4yP0BvsobjuOYzIuiyBryAsBZZ501a9aseDxe9cu1Pny13i/TNF0uF0v+Z9F1Sum8efO2bNnSt29fp9KWVvb8/i/XdiDD5/M5RWzsYk3TZNTMkJbhy7qhQ1pdI7s1LKGbxW4OKNSmt3f1COz9IXv7DzAwb5kJwFsW4TiO44RYVO3b58RoJL50yXJAYF7x9Hjejl/fKeUvCEJlyVeJZVkzZ86UZfnkk09WFEWSJE3TmEhUiVcdSqCUmqaZTCZVVaWUiqIoy7Isy5IkIaJlWYIgMMI1QkgoFHLKBJ0j8Dyfnv9/aIDJvOMtzoj9ngbyUMvSiaWCRSIRAGClqHl5eQ0aNPj555+h0keIiDs68nf2BsmyrKoqe7hjsVhBQQEiTpo06frrr2/YsGH6CcCOZS2HGBBRlmWv1+vxeJzrZbYVIYQ5TZnSk2U5JyeH9epwuJ52SX/uS3C1YOePkNH2+wU8xwkAoCgKG3y/3y2KYufOnSdPnpxMGpQiIIiC4GTvO1/cyR8QBAkAEgmVBeEmTfo2EondeuuthJDy8nJN0yRJYiv8Q3ht70DX9Xg8zjrSOFQrsVgMKmv1WJYOs4NY0MdZ/CeTyf189v8Z1eevjNjvfTgKP23wmc4JBAKUYjyeBABFUVq0aDFv3rxYLMakneMYW0aVw1X1FNTwg5iKNvv93pycHE0zHnrooeOPPz43NxcA8vLymIHHXjVN2yNXeWCClXLLsuz3+91utyiKlmWFw2FJkrKzs9kswCqy2ZKHUsoIV9ngMGNhf1/EXkFG7HcfjNQZAHTd5HlIJpOapjFuFkrB5XIx8bZtIAQYsTz7ouNq4oDzerwA4HZLw4dfiABTpvzEOG0oBUWWHF1MqUMTxCNWTapl+zM+P4fRGQAIIVOnTl29evWAAQOciBR7lNk57Bvmpv0CprfZq/OhoijZ2dnsPbP8eZ53lgCs4NrhXzs0UJ3Bgbk52H8PnevcS6i+5OM44DiIx5Mul4wIbrfb7XbHYmosluR5aNasWdOmzQFAksAwiCRxPMfB9vwZgMrsHYZWrVo2bNDw22+/ZUfmeUgkdMtC07QJQZ6HKt4mTKsMZfvzPAgCRwgSQmRZ1HVTkoQZM2YEAoF+/fodDvZ8BruK/Z+Tf4CD5eo6/t7K8gHw+72WRTgQ3G4pFIoFAgFRhMWLV+XnF2Rl5SxbtqzHkUeIIgvIE0ItRupimrZt2zwn8rwAwCECIaR9+45btmwpLQ37fD6PR6pkXNl+a5xGFCkZxhrS1AWes5EHhGRC01Tj04mf9+vbnznzMpKfQRVkxP5fgHUWxjA70e/327Y9YcKn9933gKGTioqQRcznn312zPWjEgmD48DrczF+NUKIphrhcKSkpKSkpCwajc6fP/+PP/6wbKNnz56KoiBix44dJEnKz8/Pyclp2Kh+YWFhMBiUZZnjEIBv1LCJMwc5YCacx+NmJ/Pdd9+tXbf2m2++URSJEDy0q0oy2A3s/2ZYBzhs264SL2EDpuuG260AwtatJQ0bFvz++/RLL70sKyvnvnsfys3Ne+utN7/88vOXXn6ha9fOv/02ddq0aZIsJBKJ0pLyoqKicDiCiF6v3+v1HnnkkaIo9urVq7i4mFJ7y5Ytuq5v27ZNEPhoNFpWVhaJRExLFwSB+Zy9Hr8oii6Xy+12szCVoiiiKLIpg8WcFyxY4HK5/v57WjyR9Hq9ADS9xhH3DntXBgcRMtr+X1BjKisiuN2KphmSqHg8nmg0+dVXX0UikV9+mdqoYUNJgoKCsZ988tH8eQsjkdDdd9+TSMa9XnezZs26de1xzjnntGvXvkWLFo0aNfH7ZcsCRJBl0DTKcehyCaaJssyZJmVZJDwPpmVvnwIMO5FIFBcXb9q0af369Rs3btywYUM8HmeeRRaQTyQTX335FQD4fV5G7VV52pkpPgOAjNjvDKrb+ex/uq67s5TsbH9xcfmKFSssy1IURRCA46BVqwaGZSQSiYsuuqhPnz6NGzfiOM7tditKqqKTNYFABEli/RVZog4CQDKZlGUfz/PsUAAgy2J+fm5ubq5lWYpcc4l7KBRnOfkLFy7s37+/JMmlpeH8/GyO3+4CrHvBksHhg4wn/1/g1HI5nzie/OzsoG6Y5RWhrKys5s2bezzujRvXCwIYBixbti4vNycnNysry9u5c3tRFLOyfI7Mp7NrEsJoasDjEbxekVJQlEpeyspKUhYF5PkdWJwhLYBHKeTk+BVFopQeffT/NF2LRCL16mWns3FjWhuSDA5zZMT+X1BL0X6KEV2WRds2XW5x5CUXWbbx4EP3zZ4zf87cWXfcebMk8R07tgMABFBcUjpXL8enAm8cB7wAVf4kK6Jp2RyPiJRJviBwgsCxLJSqxxFSGwAIAvh8LstCWZJUNQlpXVbSvYD7jao0g32I9PndaUXhfJgx8ncTHo+noqIiNzc3Ozs7FAr16nXUfffd89RTTx19TC9JkoLB4LnnnnvSgBOBAzWpsW4QO8CRux0JdgEQgHIcc7/vinByld9OPxbWyPqeweGOjNjvPnw+HwDwPB+LxXJycq6//vpTTjll5crVlmU1aNCgY8eOjJmvBpmvExz3n8IrGTM+g39FRux3E7ZtK4qiqirP882aNdM0jVLapk2bBg0a+XweACAEI5FYIBBgebu7lPfpmOKOE25nvHFOAt+uVmJncLghs7bfTbCcWcbNAACiKHo8nlAo5PV6KnfgsrIClFJV1euWeUdEnYh6+vI7XYZ3Zk2eLvAZ2c+gClLu4f19GgcrHLG3LIvVz3Ecl5OTwwQzHI5WVIQAQBR5h5OzDlSR7d1wuaVLeEbbZ1AbGA10Rux3H6wtjKZpgUDA5XKpqppIJFj+fCAQkCSJiR6llJXZ1o0dY4S7o+2xhv5tGWSwA1g0J7O2300w3kVWranrusvl8ng8hBBB4E3T5jjO7/fbNuF5XlGkKvH2Go8GlQv4PRhdy8wCGVQB6/CXEfvdBMdxjHSVtbhicsuILiRJhEreC47bHkWr9Lexr6denWz56qnyu9QsiOPAtokkCoZBbGLXr18fAEzTcotSLBZjJ2lZFqtF31ODkMEBi/THpjqPQMbIPyBQxau3G7BtyjrSybLcsEHD9evXI4LbLZmm7ff7WX9RJvOxWOwAZIbNYF8io+33M2rLmd09U58QIISMGjXqyCOPdDg5GT8cpZSR5zPNn8HhjEzh7e4jXWJ3rGwFqGbM1/a547GrcpzdEPtNm7bUL2woSZyu2y6XaJqISGVFoJQ4hn1ZWVl+fr6maWwKyODwRMbIP3QQCAR+//33s846b/To0d9//5NhGLIs/PnntClTpjCK+E2bNr333nuEkEOYMDuDnUFG7Pc/qmj43TPvKYUrrrhi6NChq1evXrdu3eAhgy+++GLTJJdccsl7773Hjjlt2rSHHnpo0aJFtTTVzeBwQUbs9zP+e9sDhs8///zHH3+85JJL/v77719/nXL32LunT58+ceLE9evXm6aJiKyUMJlMGoZRjYo/g8MLGZfeAYEaA3i7hOnT/orHk1dffY3HI1MKl1xy6eOPP/nXX3/n5OTMmTPn9NPPTCRitk0ppS6XJ2PkH+bYn2Jfm0vsYEH1GHvl++2vO+7P/q1ZvHf62tPt8+1NOHTdAOC8Xr9hgCJDXm4hJXx5WURTzVAoFAlPlRUxFk0A8F6P37KIJArAAbCq3/TXAxPVz7O21wwqQQhhZh3r9pv+p4yRfzBix5U5AgDk5ORIovLb1D+IjQAwdervHo+3UaNGmq6NuPDirVu3bt1S9OSTT7pd3qKiolTTHoSqrwcmqp9nba8ZpEEQBEmSJElyZD7TFeegRg137dJLL83Ozr7zzju/+OKLiRMn33DDDYGAf9SoUbIkA0c9XpckC16fGzhqmJokc+ksPdu3AxM1nupBdP77D1X8RBl2nUMIHABCmzbNP/nkoyeffPq+++4D4Nu1a3fjjTe2bdvi6KN7t2jRAhElSejateuwYcP8fr9p2rKcufWHMqpUdrE3jtrfn+k6B/vanmFXXXH/maa+5rU9w7ZtFZqmERsVRWnatB5FAIDikmIAKCgo4HkuFArn5mYfbGRbFIDfudcMqqLG8s2M2P9XHBBiD6CpltstOfJMCfA8WDbouub1udksb9tUEPiDbYx3NcUgI/xVUf2Ry4zRQQq+yr1zuyVNs0wzJSQUwbJBksAfcDtOXMbVm0wmdV3fx6ebwT5GMplk+RqQxpiecekdgnC5JFFMtcTl+VR/PkqB1dtpmsbzPCLKsnwIN7rOgCEUCsViMV3Xa7QuD/pSHErpHqSm2CXWuj2FPbzYqXI/DxKTnlLK8zwhRBAE1ndQEARN03geFEWxbdtpRw8AbDeomVk0o8kAAFjEvrakz4N+jNJ7VyBi9Xb0u4SD0blQFenRrIPnapiTmY0/I34CALfbrShuAGD5hbZNdV0H4DmOIwRVVeU4AQA0zSCEGIZ1CDzPewp1J3ofalGc/675WZ7sflH7exjbT3yXvGL7R3JYSpksywDA8zylVNd1SZKYPud5kedFngdRFBGB50VKgck8ISiKsiAIggCWZe0MYenhgOqMOuk4FMSeSel/FPh0czFd8g9isU/h4Ci243neNE2otPY5jmM8hYSgIHCAoGkGB4LLLapJAzjqcbvdbjcgEIKWSQRB4DnIFBbWhipq7FAwiqqb9LtXWLojwzyyJcN/OrP9AFptOzjAcRxTUIlEQtd19l/bpgLPAUIiYbhdCiHUMtHrVbwet67bgBCP67Iker1KcVEpIVBbO+AMYEdP/qGg7dPtGUQ0TdOyLK/XW+POuxRgP9j9nQcjFEURRZEZX+PHj7ctHD58uGnakYj966+/HXfcMdnZ2d99990330zOyclKJNTzzjunT59jcnPzKIUMOWgd2OHJx0MCTjtqQkgikaioqKC1oLYjOC1Bnf+apmkYxl4/9Uo3JFvc1n2SdYJU26xd38gevradhmVZ6aNNCAmHw9269XAp/s8/+xYJvvvOR00bt1u5YsOLz78V8Oc3KGzZpfNRudmNOnbo/u2kX5CirqJt7a/TPzjgPFoHvZHPunw41jhbFuIe0tJ76jj7BHxNr3wtn9fxun8giqIgCJZlsVQinuc9Hs/q1at1w7xk5GVbtlT4vIFoNLpp45bHxz3auXPnpcsWL1gw6/U3Xi0tLZ383TeUMIbyTCleXdienL9/z+O/A1Oe3u2lhYqiBIPBXWWtYXMhqQQi8jyfHivee2AnVmPzeWeedj5xvA2maQOAZZG0P9Yo8zVviFwtH+4fGIYhCAKllKUSxeNxy7JEQW7dsq3PF3j66WdlWRZFcepvvxQVbR058qKsLPe2bWVnnDHkuOOOmTnzL16AzVs2ffbZNxs2bAUEQydq0gQEQCB29V87+HwfexYH/dq+iqgw+dkNLX1geuyrWy6mabpcslNCx7jx/62jbo2KHQ8cVQ8ALPCGiIzV1+v1GoaRTCZP7Nf5yiuvGXDySeFwhSzLS5cuzs3NLSioFwrFGjTIB4DCwoJVq1bFYtrVV189bdq0pk2bfvDBB716dQNILfQFASwTJbn6/T18q3cO+suursN3L5K3q9bBPkN6QjUiKkoqsg0A8+cvLCoqAdi1LtoHJtgVObl3LGPPsq2CgoJevXqdfebZ3333XWlp6YgRI1RV/eSTT3JyAwiwZs2Gr7/++pRTTvF43C6X6++//968eeOKFcvKy6OmiQBgmlTXbUmq8T4e/KO2uzh8r7wKDjSxT1fy3I6lFIhgWZamGQ8++OAHH3wQDkf310nuQTDvjCRJbrebXaZt282aNmPyf9111xFCbGo2a9bslltu/vbbb7t06XbbbbcPHDhwW9G2o446Kh5PvPvuu6+99lpubm6HDh3y8oKIaNsgSbwkiRnG0Co46I18qClKfyBo6f8OTMsgcrS9KPK6brrdCiJMmjRJEIQbb7xx/57nHgHHcU6OHauz8Hg8Z599dof2Xfx+sUePHrfccsvWbZvdbvf9998djYUXLFgwYcKEtm3bjhs37qyzTjNNPOmkgevXr//ggw+6detmWchxqWIkyzZdLnnHXzvctd1BX4pT3em13xX1HgHumCPoBPYkSVJV3eNxAQDHCcOHDx8//oPdO371Iarxw30Gp97GNE3G+rh40fImjVsGgzIAqBrhOM7t5imFpJrUdT0nJyccDnu9XmLjrFn/9D9pQKcjOmZlZT3zzDNHHtlFVU3LsoJBL3CQYROqgoN+LNL1IfwHma9t+ttfYlBdAtnsZhgWx3GGYfE8z1LWASCZ1Lzeg7u5FSKyLB1Iy9jr2LE9z8Fvv/2jqomBJ/cTRYjFVLfb7fd7KbURSXZ2NqXU7RK6du2yYP68uXPntmzZsnnzZgDg8cjAyYZhybJ0EGZb7l0c9GIP1YirD3Y9Xwcclx4hGIlEPB4PAFgWOdhlHgBM01QUhZn6TOdTSoHjDRNGjBh+3nnnnTSgHwC43W5J5gzDCgaD0Wg0GAwmEmow4M/NDfp8/k6dOrDZ2zSpLPOQCvRANSP/cMchsshJj3v/l4Pskj8PKxPs0v+7qz+a/vX0ZjVVToDjOEEQWP0ZIggC53K5LMsyTZPjuN1YqNV4dftxxnQ6dkiSxG0vvwVWV1dWVkYIRQRJ4ghBRZEAIBgMAkAw6GeFxoqS2l8QQVZ4VoDIApwAYFlpbj2EZMJACoBg29tvWTyepBQQgVJWzLt9WG2bGoa1l8dg3+EQEfuDF06iEcsR2r8nc+CCq0yt4eBfcmxqmbgkSdA0AwDKyioMg3i9CptvWVuBZFIDAL/fy3jHWIWvIHAAQClYFuE4js01hwYyYp/C/tV+tm3btu2IfWYt6oDjalu47XKOndutAEJOdq6iCACg6yYAyLJACSiyGxCikWQsqgICUuBAYOYAUrCtVCHgIXNbMmJ/QCB9sQAHWS3A3gXHMVUPO+W0qX2HcDhKCNp2qkpP122vV2bHJwQNwyAEgkFvIOBh7MOiCJZFWZ6/Q91hWYeInZ8R+6qoEg7MYP+iFm1P095Uvt+BTaiqLZCdFRR4ThThxx9/mTt3kcslAsC8eYtXr15vWZbXq/z88y8XXHDRNdeMmTVrjmUhAIgiz5wtLP6PCPumRmMfICP2OyC9SnFf/q7DHsdwCAcjdhWVYo87PSS1GuK6bm/eXDRy5Mibbrpp69bSaFR96aWX+vbtJ4ris8++OHjw4OnTp7/33nu9j+791FNP6brN88DzwKYAQsBipv4hgYzYHxAQRVEURUfa6yZCO9xQyyRYx9q+VskPhyMlpaULFiyYMmVKMOiRZXnrtq0//jjltttuP//8C/78c9qyZcvPOP3Me+65d9q06apq8TyYpgUAPA+2feik+GYer/0MZ0kvCMLhoeSr037tpKMsfXCqlAxDLX+qBAIAuFxiNBpt3qx5LB67+eab163bqqo6AP/777/bhI4f/269eoX16tW75prrFEX57bc/KioqYDvzNFCacekdotilIpzqWXS74YHf3o2Q44Q0UqgqB2eJCYIgAAIlAAgCLwm8hJSjlB48vggKQBLJsGlpAASAUrQBKOJ2RVpeFmH+c12ziQ2TJ0/ZVrTln3/++eWXXzTNBgQ1yZg2eQDeMCzGOwCVnvlYVAXkDZ0kEwYgWCY6xBuGQevXr19UVPTgAw/Wr19/5MiLtm7dKvBCRUVY5GXLAoEXPB6pYYPGsuzatHGLphlHdPzfueee/8H7nxUVhXxe6ZAp6cmI/Z7EvlTXB0ah4C5D05M+r0eShIpQGQDyHK8bOgBYlmVZxNBJXl6WptkcB+XlFeefP/yiiy7q3q17UVHRzTffPG7cuDVrNvr97vKyCIuuKbIkCiJLxXG5ZGJDIODRdaIogterAIAgcJpmmyaaJgoCHw6HA4GA3++/++67Fy5cOGvW34QSr9erKMratesVBUwT/vnnn0g0ctRRR3355Zddu3bt2bPnzTffrGmapsGhQ8a980Rchwl2ns3OYeNx/sti73sXFImNSNHQSTCQe/ZZ51vWfiPA23UQ00oSqiKaiKZla/FEOJ3AjxLUNRspvvP2hIA/v6Bek1tuvhMphirit95yl9eT5VL8H034FCkixVhUZW9KS0KUIFIsLipHiuFQnNgYj2mJuI4U/5k179VX3lSTJlLcsrmY5+S33nzPMvGyS68EkFyKf8XytQF/fuNGLf74febXX33XrGnbgnqNykpjq1auX71q08033REM1Nu0sQgp0oNopOtERuyr4r+IvfN+L4I9fBRNgx6MYo9oGWYC0US0kmqUyXx5eSiZ1BJxPRHXN20sOn3YeS4leOstd//+299MsImNatKaM3vhpZdc2bhR8759Tlq8aDlStEysKI+yMdFUi+3sbOVlkYsvuszrCQ6/4OLyskg8poVD8R7de3715bfhULy4qPzkgUOOO7YvUvxowmdHdOzqUvyi4Dqx38kzps+yTNy0cdtpQ8864/RzysuikXCCjfn+HsA9g4zYV8XOiz1j70wX9YzY/yts20S0ND1uGBoiMU0zHA4jpgT1jdffBVAAlL+mz0/ECCX45Rff5uYUPPbok0iRaewfvv85L7fQpfjGPf50MmEw4WebmjRNg7Lx+f67nyTRDSB+OvFLZyKwLVy/brNpUPbfTRu3IUVV1eMxjVLcsrl427ZipBgOR9Wk2bZt+8KCRtdeO/q9d8dXVISjkeR+Hrs9h4zYV8VOij3T7VXEfne5rncFB7eRj7ZtU7p9KUQpapqBFD//bFK/vgNdSvDSS66mNhZvi/7y04zLL7vW4w5eMnLUmtUbkCITcqS4YP6SwYNOywrmHXds35+mTFWTpqETR7YXLVx21pnnNWvaavgFF8+YPgspRiPJeExDmlpBsDEsKw2zczAMg1K0LAsRE4mEadqIqKr65MmTzz773Ouuu+7TTz+3LMswrHg8vj/GbM8jI/ZVcYCLPSVoW8ie4IA/56wzzzNNex/MNnsc4XA0Hk8ixY0bto648NKsYH7XLj2XLV1LCUbD5mWXXNe+bXe/L++zT79KJFREtCxCbLTMlKWDFKf++merlu0BpJtvukNTbaS4bWvpKy+/0aJFq5ycvDfeeMuySDKpsa/rusl+t7w8xN7EYglEJu0EEU1Tj0QimpZERF1X4/E4IiGEbNu2BRERSTKZ0faHLg4WsddUy+/LPvOMcw3D2gdriz0FStEwLE0zEJES/GjCp8cd2y87q97dYx8qL4tv3lT6wfsTFSmrSaO2V19509o1W5AipWiaNiEpZc4kny3dLRPffusDUXC3btXh7rEPnDb0rOys/HPOOW/z5q2ImExq7EeZzFOaEnVnotQ0DRFVNYFITFO3bZN1FrEsA5GwZQgiYZ8zYo/9NGx7GAeQ2DMpMk1zX/jD9wT2l0uPGflq0vR6gmecfo5hWAeXtnemrVdfeQtA6td34KyZ8ywTv/7qu4EDhmYFCwYOGPrnH7NSRnt1VBrzbBySCfOP32dedeX1AEp2Vr0pP/7KZB4RneXPv62DqjcUqmM7FHDAlRYcTDHoDHYDCKqq+f1uWRbXrFmTm5P7+OOPd+/e9Zprrps4cWIwGHzzzdfPOus0AIjHTVHk3Z5aH1GW6MTz/PHH92zRosUff/wxatRl3bt3z8vPYjtQShF5jgNBqCM/5VDJvNsVHEDpOk7eSUbyD224XC5CgOehrKw0Egm3bt2qrKycEPu5556dPn3aaacN1TQbAPx+2e1mMl+rZG7dWv7II49t3lReUC9fU4369Rs6Mm9ZFgBlebmZB6oKDiBt71Ap7e8T2fPA/cpIe0BBN0yXIieThterNGvWDADC4XCDhoVvvfVaIqkqsluSOUkSk6om8JLLLdYm84QAIkQikYcfebhXz6Pd7p5er7e8vJwQJMSCSnIuZtPWOfh8ZXucnXk9RHAAiT0cinoeUw0tMmKfAmOz5Hg0LZsXQFbEeCKqKI1DoUhWVoDnOQDQdIORgtq2LYp8muTzAAAcALLq9xQDH8dxoijm5xeEw2Ge5zhOdJQHc7gIgiDU1QT7QO8Lusexny/G8TE4nxxkKeZ1ovrVZQAAlILH4+I4rqioiONQFHnbtnNysgDAsixKqSynlPyOMp+GytYXkUgkK5iVTCZ1XY9EIqZpAu5gMCIi66W7T67soMH+1/Z1aMJDQ0lmxD4dmqZxHOdyuSRJ8HrdgUCgsLCwUrwpI7o1DBOBEwXZsg1JrLn8hZXBWpZlGjYipyhujuMaNGhACHBIIK271r+f087fn4P+YUxhf2r7/7N33VFSFFv/dpw8mzMsOScBCSISVBBFFJEgggETooJZMfAMiDmjmPU9xZwzKoiIKJKT5ByWzTupc1fd74+aaYZdluQC4sfv9JnT09PTXV1dt+6tG/dPD454fLSaU8dI5vPH71PUOVwul9vtNk2T8eHS0tLy8lL2E2P1AOBySaIgAtD9cGmeB1GEhg0aq7rq9/s5jlMUJRKJiCIICTg5sEzT3F+buIP+/LfgWJI9k+drS27/D48pZQPUqd9Sk7C5GiXrkbl9JSXGPrzpgP3pH94/tcEwNAAqijzHoWnqosh7PB5d1xHR5XLxPK+qqm1TAN40bQ5qJXtCQNcJy2mpKIosS7C3bih5XMnygcpj/D+j/H+VouIfCJrAkbvF8UX5Ho8HAHietyyL53mPx2NZltvtZvVwAMDr9YqiSClVFGU/jyYI4HYLu4p2sL9Yli2KIisTdAIHxAmyP+Koc57sXMy57HFE+LZNETkAXhAkUZQphdLSckXRNM0QRRmAD4ejsZjK82JaWsZ+rhOLGQDA83xqSpDnQVVjlNJ/pfX3SODYq/T+ZcC9K9Ue6YF4fLF6SJoEKaWxmMpxXNOmzX0+HyS6zu/383xctrdtum9lPoLH4wKA8vLySCSiKAozBJSUlPybRPEjhxNkX8dgkipXFzX59o/j1qmRBwBAEEXRMkkspsqSOxZTt23d4fW5GzVsQClQghyPosBznACA+8yHyZR9ubm5p556qs/n03XTMDQ2fZzAAXFCKKpj2AlYlsXi8+r8FscZme8Nlv/TMAgg+P1+pFxRUZGumUOGDLlu3A2//Taf5wRJ4lhpOp7nahuihICm2Z07t3355ZfPPruPpmlMWXB0n+Z4xYluqmMw0xFjxcyGx6Jx6/xGxyerB0niAMAwzKqqWGFhg9TUtAULFgYCwddee33nzl1Dhlx48cWjly37i2WnT1jU9zFKGbe3bWjduglFmPf7XI/XJcsnpNeDwgmyr2PIsixJkiRJjP6TDXhHCMcX5ds2IEIw6ElL83fs2LEqVHXTTTc99NBDvXqd8scff8yYMWPlypW9e/d+4IEHFMXcj6ikqpbHIyJCcXHFNddcf/nll4uiOHz48KP4KMcx/j1kf4TcYDGReIOZ3J0kHNXoOdkHgSW0Zz6hyct7lgk/uQzG4VEse0pR5EVRxMNKzn8MIYrAcYAIiNC7d4+iXUU33njja6+91r37ab///nuLFi3ee++90aNHT58+vWvXru+9915ZGatRgQDx+rPscd1uyTDIl19+OWTIkFmzfho//vovv/w8N3d/yv8T2IM6jd4/ljj41JfHN2g8TYVtYVpqFsuuc6zbdAhgSe+IjYYez2MZjehLl6wadO6Q1JSs3r3O3LplFyW4aeP2sdfcwIHUu9cZ3303g/23qjLqPP6K5avP6j8QQBp50aV/rVq/J2HuCRwE/j3c/v8PGLc/oGTDXvBRaM8hQRR5AOB5QKSqalIKfr/rpJPafPHFpzfffFM0Ghk48Jyvv/6uXr2Cl1+e+uOPP5qmefHI0d9/9xNTAaqqWVJS+u67H7bv0L60tPSladPeeOP11q2bmSYNh5Vj/XDHD47trFOHOELcnsn2dhKSE2kdAyTYnWVielr2sKEj98ntqyX8+ueAUqQOW6aIiLaFlkVY5Yn5fyy66qprsjLz+vcf8OknXyLFkuKKLz7/ZuWKNU7azHPOPi8YSL/3nvsXL1qOFGNRvbIiwli9kyfzBPaPE2R/ADBTnGVZpmmapsn2j2W2vySyz0jPGT7sYpbguSbYbHWUW3cwME2zJn2y5JaIyNrcrFkzAH7SpPtYbnz2yLfeMhFACvjTli1dxY44Wzyv5gkcHE4YPA6AmpE2x1xzjgiU7pHhEZFpuThuL5P+MW9nbeB5XhA4ALBt2zAMjuNcLlcg4AOAWCzm9/sVRZk/f/7rr7/+xhtvvffuBzfddDMAPPbYY5qmPfP0MzfddL1pUkEAXbd1Xff5fKLIWZaFKEryP/SR/2ng8J+3/Ds84N5esf9aIBgG5XmOEJKXl3fmmWe+M/1/LECV53me36sH8J+XsEBVY7IsOyGxNWFZFguSNwxj+/add9/1n08+/TQzI7NPnz7PPvusIAjZ2Rk8D5pmeTwSABACQuJi4XA0JSVwVJ7j+MYJbn+w+OdMK5RSAI5ZExGRUsrMh86Oc+Y/obXVwILkHFHF8auzbVsURUKIJEmhUCg1NdXlcjVr1uyjj96vX79RYWHhO++8Qyn1eiXLQoro8UpM5BFEDgAsi/A8f4LmDxLHjSZ/n1KJI+U6ZSpqO5+puJjD/OGhptcNJhQKyV8Tvx2ZTwRKYfLkyeeee+4nn3zSoEEDAHj11VcHDx48depUSRJ4njcMAwDY5z8SPADPcQLPizwvJvzteRZ+JwgSAJ+amp7sh9+0afMGDRrwPO/1SoSiJHOJVNnAFgsAIEmCwP/j5rh/LE5w+yOAI0TzAAAQCkV9Pt+vv/66cOHCcCS8ctXK2b/MqqysHDVqFCJwHCRnpPkHCvmHCx4AATgACiDUiMk7brjXPwTHTX/VloHn6LfkwOCO2AaQnh644oorTMuMRCIAIApiZWVlXl5ekyZNKEVK90pEdXw58J3AUcNxQ/awLxcD5/hxmmHqkMGBrts5OZkF+QVM72UTWxCE+vXrN27cmC1k2CK/tlRfJ3ACcHyRPexN+dV+Sib7Yz3c6RH7BLdbpBTuuOMO0zIz0jMAwOVyDRgwIDs7y7k9Ip4IQT2B/eD4GxzVaP5YU3hNHDmaj1M+pThw4EAAqKiskERJVdURI0ZwHDPg8ZCI+YF/aYmhE/j7OM6Gxf65ffJpR7ddRw+IIMuc3+8/tcepAODxeDp27Ni6dUsA4HlOEASH1Z/g+SdQG477YfEvpvB9gk1ubre7T58+Ai9EopExY8YQgpZF2E+OGu9IJPY5gX8HjieyZ7KrKIoslJ1LlMpk8e215UiHeMHjfQgIfwc1hQ6mXGBO+wBg27au61CD/DRNAwBFUSBBoqx4A4ucYX+xLIv9i12KncBiAdhFAgFf69atmevLySefzHEcqycDsMeAl+wJRyl18nwdoWw/1VCbn4VTA8M5knymaZrOM7Ie4Dg455xzWrduLct8OKywflNV9ci2/rDgFOFQFIU9hWEYrMHsazQaZSewdwFJ7hVsVBw1/Hucc/cDx5EGEffjFnqo12RwKmRAwqaASDhOoNTmeRGA2ja1LEMQJEkSOE5gvxJiATDXdJ4dYTVVFSUqirLLJVEKtm3KshuRGIYFQN1uLwDomg3Aud3C2rUbBw0aJEnS9zO+bdCg/v5b67gVcUmok37YT//UvEU1T0fWgckrEWaJYEeYPQIpMGrStFhqqh84CIfDNbzx4mk5j2Ha3HhrEZm7IXtG5mhsWRYispwrzMLKztE0TZZlti6zbfug6nbVEY4nbv934OS9OdI3sm3btikiGIYFAJFITBRF5oVGCGqawVidIEi6bgLwZWUVHCcAgKrqiODzBVwuFxNi2BU4TnC73exfkUjM7RbdbsEwSMuWTT/99NPPPvusXr16pmkfsGH/EANnTRUM+2SzEqMNZz5FBMNAlwtEEVJT/QAQi8VSUlLKysqOUfNrBZNNKKWmaTo0LwhCWVmZJEmyLLMnEgQhEomw+h9OTU5N0xjNx2Kxo9Pa/xfc/kigNm5PCIoiH+c8CBSB5+KfNqECzyOAbVHZteccQtEyCS+AKIi8AEiB44ESiEQjPm8AgSDlwpGq9LRMUQTmiheL6X6/m900pqh+/wGqwSTL1UeH/mvj9rZts0UZJPrQSTcKiUmBcU7btiOR2Ouv/e/dd9/VdT0jI7Vdu3Y33XxDq1at9u2ld0y5PSQemdXV1jSN53lWh5tSWlFRkZUVt7BWVFRkZGSYpinLMsv266zLNE1jVYOONP613P4YTWccBzwgqKoFCJYFgKDrRIlppskSv4NtUUKoqpjAskcDKDHN7RZlSVRVgznhmgbleUhNCQJwsiQKgpCZkWlZNrtBKKT4/W5EUFXTNKksy/txxksmrX+CU5NhGEy/AEkVBFkQkTM3sRbatl1aWnr//fdnZ2f37t27VatW+fn5+fn5zD3xHwinRAIASJLEaJ5JAYzmmUoiIyMjEomwsnzl5eWsB6qqqnRdPzo0D/9in/xjNbgpBZ4Hr1fatat069btlNq2TdPTU3Nz83NyUv/4Y0lGRlrz5o0AoLw8On/+72ec0W/27F/atevQuHGB3+9avXoDpdC2bTPbhrlzf1u6dHlBQV5BQf2ePbtEIrHvvvv1wgvPY+Np9uxfmzZtWliYT5G3LMvlOsDK8J8g4e8fjmexM0+x8Ptbb721Xbt2aWlBwzASq/p/otMx62HDMDweT3FxcUZGhsfjMQzD5XKZpqlpWkpKSnl5eWpqqiAI27Zta9CgQV5eHlv/+3y+utI6HRRqeryewMGAecI6kX+Jg4gUKcFo2B5w1vnZmQ0aFDbPy2kM4Lrskmvn/DK/XZuuN980MVRpRCPmTRPuat6s3exZ82Up0Lpl519m/4EEB54zpEO77ps37bp09NiC/MZNG7fr1PGUgrymV191w+QHnmzUsOWSxSuRYllp1bkDB08Yf0uoKlZZGdpPO5Oz/R5N7POOzKDg/OTUBWVfmeoLEQ3DQERCyJIly9LT8gTe27XLaad0P23ctePD4XB5eTki2XtjlzvSz7Q/OCnMFEUpKyu7/fbbp0yZwir5Tp069eabb6aUbt68eejQoe3bt+/Spcsdd9wxa9Ys9sdIJMIuomna0Wntv5bbHytQCjwHfr+wYf2mM8888+67727UqNEXX3wx6pJRI0aMWPnXyh49eqSkyACwdetWyyThcNi07DVr1/3046zTenYH5Ldt27F82covv/y6W7cuP/zwhWnCgAGDfpjx02mn9d6ydRvT/wWDKZZl//HH/GDQx3GgKqbXKwPse3GL/yS/HWcdiwnzinPEkUds25Zlma2NU1ICbdu2Pv300wsK8lu0bBYMBgHANPWk2tWJRzum0ozTeJfLtW3bjieeeMrtdo8bd72umx999EllZWVlZahr1+62bd91112yLN99991fffXN119/3bRpY1GUASAUiqSmBo9Oa2sle9yvG9z+4ViGMaGnqbmqxCSVD+5t16kT1Gw/w6HepVYNAZeIieOAIgAAIZRSIDZ4PDwh4PK4i4p3r1i1cunyZR9//HG9evVjqgIA8/74ffyNd+q6vmbd2vLKiqiiAvC5uflTHnmkS9dTeFEyTOuXX+dGorHHn3wqFCYpqcLb70zfsXP74kVL3n3/3XHjxmVmpsuyvGjRkt69+nIAxAZJlAFA06jHw1sWSBJYNgGgkiQdK4I/YMSk40GcfISNCuaPEIvFEElp2e4PPny3a9eTCUFB4JjMLMvuI93+QwXHcYqiuVwuURRMwwbgdd0cMXzkhx9+aOgWJTD1+RcrK0Kffvrp4MHnUgoet++66677YcZPDceO9bhdJcUVOTkZR00rWSvZ10wpURsh1Tw/eajhvky11c53rnwYlF9X5H3o92Ubsls5rXC5+FiM+P2CaZq//DL7l19mu90e0zTbt29/+umnu1zuVatWFhUVZWRkbNmyJTc31zAMr8ffsWPHRqFG48aNS01N9fl8GzdsQqCGbqakCKEqu6Aghecb/vjDT16vLxKJEGLFYmpVVRW7oyBAeXkMgObkBAGAEFJZGcrJzaD0n76Yrwn21hjxi6Lo8XgCAV95eWkoFPL5fIIQ15Mx4j/Wja0Ol8slCjwghEIhr8c7ePAF33333dSpL5SWlhmGsWzZckQ45ZQeuk54nr/44lHjxl23a1cRAHzxxbeqqp555plutyuYcgCjTJ3goFiBw7r3T/n7RLXAOIbkhZ+z+DzUK1e7ZjUc3tUOHixfJXs4jgOeh0SJW/B4BAAwDGPs2GuLi0sWLFgwcODAZcuW/fnnn4ahX375mPLyHevWLbvooots2y4sLFS1WOs2rR597JFINLxm7V+GqffqfRoAhsJVkShJTROnPPxsQb283cVFqhp76623FiyYt3r10vbt23s8Hkph5MirOnfu3L9/f1VFVSVut5CTkxGNKpqmHY/+uWxIAIAsy4FA4LHHHjvttNNSU1OZZfsovNnDg2FYzOWOEFBVVdf1IUOGnHzyydOmvWiaRiDgT0tLRaCiKLjdgixzO3ZsR6D5+XnTp0+fOPHOO++848ILhxy1uezAZO8Q6v41Q/v5u7OfLO0n0/+RcJ6tKyS4evUN9lB+/EyeB55n+W2A+VxWVlYGg4G2bZtcfvnlgUAgFAoJgpiSkgIAJSURTdM0TSsvLxUEvkGD+u3bt73qqiu8Xk8w6O/Vq6ckiWPGXDZ16nP33ffoyy9PO/fcgS1aNAPAnJycUEgpK4tkZmampqauXr2prKzslltuCQQC/7nvXkkSTJMaBgkEfD6f73gke0h4GfA8HwwGhw0bFggEHA7BnJf/gaxekiSfz0MICAKkp6dTpCkpKdOmTWvSpEkoFAqHw/379/e4Pc8880xZWVVFRfill16SRKmgoMDlcv3nP/8ZOnSorutbt20+Oq3dH9kfBhd1iNkpKeFMFuwELlH4HZMyz/0dgZyvBbQWHPaNqiGRtTpekg0RCEFCUNXiDvl9+vSqX7/A7QYAaN26ZZMmjQix+vTpFQz6IxHD5ZL69OnVoEH97OzMgoI809RdLumWW25q375t/foF7dq1Wb58aXp66pQpkydPvr9Tp5O++urDnJysTp06RqPh1FSfy+Xq2bNndnZ227ZNPvjgvRYtmu3cuVNVVUkCWeYty9I0w7KsJL3XcYDk1R/bd7lcbrebEMJc3xzz3rFt5z7BZthwOGLbEIvFAv7A5s2bmzVrOHHixGAwmJmZ2bdv3z59+kx5eEqXLl1atmz57rvvXnDBBf369Rs5cpiiKF988cXZZ5/dtGnTo9PaWr30HMEe9hbvq6lh9lwo8baS2TgkvGJrqvRM03R+ct53HeqfamN0tbW/1uvUMlEkPyN7BDareL1yOKR7vW5RhFBIFUUxFArVr589Z878U0/tvmtXscfjyc5OMQwghGzatKlJ00abNm1q1aolExN27SolhBQU5FVUVIXD4QULFnTo0KFevXo8z8dzwvOC2y0AQElJiBKQJOmJJ5747LPPLrjggsefeGD37vJgMODzu0zTRMRjqNI7DDD/NgCwLMtxa695DtZdYEXdAwEAtmzZMXv27NNO69WsWcOSkoqpU6eedNJJQ4cO3rhx648//rhy5UpKaatWrcaNG8dx3PPPP//www+ff/75TzzxRGpakBULO9I4gHPuYcys1eYLJ/FDNb29YRgsnM4R+Kuddki3O/jjh0oGtZE9QPUaFcxy63K5JZGLxUzmdOl2cwCgKLbPJwKAplGXi6+sjAKAz+fzeHimuY3FdBaSIcuyKEIkogaDXgCwbRBFsG3mBOKKxdSUgLekpCIYTOE4zu0WVq/edEr3Uy3LatO21c033zx06BBZ5krLyrOzMwkhLNTnkJ73GIIFqAAAIYSxBERk7qtMUnO7/3EKfAeaZiCix+3mODAMwnGcLPOGQV0u3jAtl0vSNEMURUkSYjHV7/fquul2y6ZpP/nkk/fdd5/f7+/Xr99TTz1Vv37BUWjtAWbNQzLaQRLd7pOAa1svJM8IdUX2R1qTz1bylHKIzI08/kyUUo4TvF6ZSRWhkJaa6gEASsE0URR5jgNKaXZ2immCYVLTNAIBDxvxHo9kWQjAeTweRIhEFI/HY1mcJHGWxVMKwaAXEHJy4uWcCQFRFEePHr19+/bcvOyUlIAsc6ZlJ1y+/6ks8UBwpmbmt+eIAOygoigej+efJsW43S6OA0rANInLJQCArhOXSygvD2VmpVoWYScAAFPEMg2lLIujRo06//zzFUXJyso6OjQP/6ZQnGQpA+ounxS73JYtO7Ozs9n07HaLO3bsLizM0zS7qqrq119/TUlJ6dOnD/Oy5HleEHhBANOktm37fDIA2DZwHNg2ZT8pirFu3bqtW7empKS0bdsmNzfTcdUwDMu2bZ/PY9t7plH2KISgrut+ryca1dxu94YNG3Nz89PSfMx8uGeWS8ozwHqiTvrhX4NkDULdgnlqMZgmlWV+4sR7Q6HQtJde4Pm41/bfgWmajjTEZg1d191uN/tERObV7whN+0MtivnjD0wOJAnU2WURV65a16hxi2eefZEimhYOGz6qXfvOlVWx776fCSC53IFAMANA+vyLb0NhlSIaJppWvCgjoRiNGeGIFgqry1eseWf6h8OGjwKQ/IF0XnADSMNHjFq9Zh1FVFQ9GlMpomVTtmOYdkzRdMPSdDMSVSybUsRoREOK27cVdet66g8zfmZVHw0daxR4J4gW4j6K4f4/x5FzVaZJpThVxbRMPHvAoGHDRoTDUdumtv23bqqqqrPPLBrMk5cQoigK22G/MrXO/nG8yoHVgEmWAqxT+UVVTU3TtmzeXFpaCgCCAFu3brUs65dffrnwwgu7duv2wAMPUErvuOOOCwYP/nXu3LZt26am+mwbSkoqeZ7fvXv3zz//vGDBghUrVlRWVpaWlnbr1u3mW25p2rTpW2+9tXr16o8+/PDnn3+eMGHChAkTeJ5XVZPneZ/PY9sgCIIoCowtuVySZWFlZVV2VhoAiKL454I/WbYWVTWCwX+cQev/GygFx2uL48DjkWwbysvLEdJMU/f7vcmeSIdxfTaqNU3jOE6WZZfLZRgGi95lTo2GYbjd7oO8+HFP9jWJvG7lN69XFkVRlKRFixa9997HkUhE1/VIJDJz5kykdNq0aW3atCGETJs2rXevXn/++WfPnt0sC957773nn3/+r7/+Mk0TEL0+31133TVkyJBAIBAMBoNBD6VACLn33ns//+KLlStXPvjgg/fff/8jjzxy++03A0Akovp8Xp4HRLAsBABJ4iSJy8pKA4BQKJKXl9Wta7d169bBgY3Y9IScfxTABHhKwbLia3tRjOc1E0UxWVtRLePbQYLZYllkLlNzyrLMcZyiKC6Xi+M4SZKcEEBK6QFGxd8RPP4JqM0+X1fXJxSXLFntdqcKgq+goInPl8Hz3nr1mvbq1R/AVVRUqarUMLCoqFKSAldcea1h4nvvf3xar9Nbt+lw/Q03vfHm27/MmVdZFY0phk3QspEiGialiKpmudz+Rx97uiqkzPjh5zFXjE1Ny27VusMHH35mmOw0VDXbkRxVzTYtRERV1RHxgsHDmjdrQ0lSdfd9C/l1tt75d+DIxiNSVBWTvRRiY6eOXc8+e6ATYEcpdaIMDwPl5eUspA8Rq6qqMMnPjS1vD/5Sxz0fYI+RfKRuM0kwpauua1ddddWMGTO+//77Ll26RCKRgoICACgpKZEkTpIgEolYlpmdnc3zMHDgwHfffXfOnDlTpz4zevToLl26pKb6vV6ZUrBtAgCCwJWVVbnd4qBBg37++eeUFG+vXr1eeuml2bNn5+XlXX311SeffPIXX3y7fft2ZqJXVcswqNstiCLouunxuFRVb9S4wZYtm6NRjZAkXVF1fd4JHCVYVtxPRJYlJu1TCixtHnMhYU7of2dksirAAICIqampkCTYOvmImBcjy9u5Hxz3ZM+ASWv7ur2ybcflpdzc3KZNm3bq1IlVnho2bFgwmHLzzTevXr1+/fptEyZMyMzMGjRoEMdBIOCpVy/X4/GYJpUkzuORolGtrKxKFMHlEnbtKuF5YOL6qFGj5s2bt2N7qdslIOWaNW3x1ZffTH/nPVGQhw0d8eQTT69Yvo7Y4HFLksgjBcsCt1sGAFmWe/funZqa+tdfq/6+ivgE/j5wjz8bAADHgShCIBBwfEMxkUsPDqs2YSQSEQShqKiIEMKc/7du3cpy9YbD4R07dpSVlTFPTQA4YDbOE+PlABBF3u125+Tk1q9f3+UCj0coLCwEgN69e99xxx2rV68+44wz+vTps3z58htvvPmU7idzXHw17vXKksSz9xsIeLKy0hhnLijIYVcuK6tq3ryFJLo2bdpk2+BygdsteH3CWQP6ffjR+89PfXbBwvmn9Og29tpxK1etISTuugMIpmmLAl+/XoNQKLR48RJJAtOsqcU88WaPEOjeWxzMSwIRTJMCgG0DIvA8z3OiIEgAIAh7VvjMOntICAaDX3759fnnX/DddzPcbreq6s8++/ybb/43GlXefnv6sGEjWrdu27lzl0mT7isvrzywU/ZhrzSqITlHiqIokUhEURSmbDQMg9kbVFVVVVVLgq7rLDU6E4EO476WZem6bhgGuwILBNhn81hy8kO9vmnQ8rLw9m27dxeVa6ptWxgOGzt2lOk6ahquXL3lg4+/+erbn3fuDukmFpVEkow4qBskEtUU1aSINkFVsyJRTdPjy3VNtysqo5069Rw8+GLTRErZAt5iv5oWicbUJ558lhdcHm/w5Vfe1A2qqBZSLC8LI8XdReWpKVnDhl6sawQp2hYSG2nS+i5h0bRs27QswzR1liff6WrLIoSgadpMIxAJq6zdlRURpEgI2hZaFjnqiXn+ySCIFkXTMBVNjxJqsPQ+rD/ZwDNNGxEJQUrw5M6n9Ondr6pSRYqaalsmaqrNOtnQ46/KMewRQmiSmsY0KNtRYgbbuW7cBACxU8euSHHnjuJgIP2yS6988IGHJdFz5hkD3n/v4wnjb/H7UocNHWnohP3Ftva6mq7FSaPOeAImOe2LoiglIOwNliQ4GU4q68OTz7m9AbXI+c57O9TrSxLn9/vT0tJSUlJcLkEQwOORU1NTBQF4HurXr9+nT5+uXbt6PX6LQDAloGl2KBQLhWKWhbLMs/y2FRVh5skLcWf+eKw+x3E5OTmLFy8OhRTDpJYFoigahmUYlijyhqldfvmly5YtueKKK8aPv6FZs2aPPvpoSUkIkQuHdVGUETlKweXiS0ur9jx04hETXSIkd47TA5FITBR5ngNREMJhBSkQQmbNmnP77XffeefE5557cfu2nYIAmmoYhnnIb+VfDQ5AliS3y8VzfHJ5QkEQdN2UJMEwLEqpouiVlZW2TcOhKABIkiCK4HYLimICgCzzlokAIAhxkzPP86ZpiSJs374bACSJq6yMWhaIosRkh6qqkN8XWL58xfDhoyKRaFZWdjQa+/HHn3Jyct99972LLhr62GOPn3lmv8WLlyxdugwRDIPyPIRCiqpagsCFQgozMQAcNLd3PGFqOyGZx9bUKyY70tStyp1pRx027rCy5FuwcEDLsg7Gk6H69QkSO75RgpQgoWgT1HQSi9m6hTaijRhVsTxkVMXMatw+GtN1g1BEy0bdIJpu6wax7PjXmGI+/vgLAJ5Fi1YrqsX09rph2QRN26oKh0rLKjTdtGxcuGjZFVdeK7v8jRu1+vijryrKY5TgeYMubNa09eZNO5jeOM7ta+lRSikhSCnGu5yiaVDTQEOnxEZNtZ968vmM9FwAyedNBRA7tO+8ZPEKdrW/6WryLwKxiW7Zmk10m+imqZumzsabomiIqKmWrtlIcfOm7YPOHRLwp4uCr3vXvj/M+AUpairVVIoUVcVy3pRp2kxAjjvkUESKkbDK2D7j25pqaao1etTljRo2G3P51QDijO9nNmrY7LSefdu2OWnQuReUlVZZJlZWRDZv2p6RnvPRh5/t3FF88023P/H4M5UVEdOg8dslXuMBuD0mUSzbqXUK3DtfUjXfWCfetlpA3t/XwCXcV/nkrwc87eBBESERVE9pPNiW48Dl4j1eAQBYl3g8EEyReZ5XVSsa1RTFoBRkmff5XBzHaZolCCBJvCwLzIjL8yCKvMslnXvuuQDw559/ejzxmDNRFHkeCCEpwZTMzHTDMDRN79y5w9NPPz1jxozmzZtfc801l1xyyccff9m+fftwOKzruq7H60btpzvZ+2ZkTwkYBlEURZJAljmeh8WLF7/++uv5+flr16wtLy9//733V65c+dJLL2mapaq6IBx/iXqODHiBl0RBBuQFnomzLvbWvF43xN1mhaeeeq5Vq1YrV64cN27cO++8EwqFrr766ltuuYup4igFj0d03pQkCSyPELPJa5oVjWqBgIf510Yika1bd7rdIqVUluXU1NTbb7+9ZYuWt9122/bt2xs3bsxxXHl5eXp6qihCamrgt99+Y+XGunbtumbNmrvvvvuWW25hLdR1OxyJV+OqldszUneYpGEYbIle2/nJfJtNENWO7Ie3/03mnyyG7PMidWvPd7xuLRtVkyg60Uy0KJqImo2mhbpBHefcfW6EJjaChoEtW3Y677yLmKFe023mhEsRNUMn8fUdWjbGFNMwMRoxn33mpVO69/J5Uzu0P9nnTX37f++VlVYpMUNVTE0zdN1MbEyfoiuKFonEwuFoVWW0qjIaqoqFQ6ploqpYho5bt+y2Lfzs028D/szZP//utLJRw2bdup4ai+rhcPTvd9q/BjWHkGURxuHLSqvWrN7Y78xzUoKZE8bfOvfX+YzDb9ta/OQTU5s2adO/38BPP/mqsiLKeriiPMxkBMOIy6qlpeXERsbet23dNe7a8Wecftaa1RvY+SOGj2rdqn2oKrbgzyVZmXkcSJeMHnPxyEtdsm/q8y9ZJv465/cWzdu0btV+29Zdjzz8xMYNWy8YPOyCwcOYQ7dp7Gl5rWTPdGOM5g+G7BkIIVYCjvaomoTvdF81HLYv/f7Jvk6ofa+WI9okLrEzCd9GDMeMiGZZcW0cGiYyirXsuIu+TZKonSJz3TFNNAycMGFio0ZtKiqjFDEa022Cdlwjg8wbPxrTnXnEcb//33/fK8hvCCBlZeYBiBxIHEg8LwqClNiYMkUWBInjBAAeQAQQASQOZAAJQAJwSaL/kYeffvmltyTRv3DBCqS4ZfNOpHhaz74d2ne2TETEqqrw3+zAfw1isbhvvGnajuaMKd4euH8KgNSwQbMff5itKlYkrC1csGzTxp2M+H+Z/Ud2VoEs+a4YM3Z3UXlcUYcYjTKP+rgXFtPDzf55boPCJgDiKy+/wZSslonXjZvQulX7dWs3IcWHJj9ar6Dh5ZddVVJc0blTN1nyAoj1Chp63IFfZv/GiLxtm5Py8wpn/zzXWSY4T1GrB3uyPJ98zn6CexDRKXjiVKHFWnxpat73sAV+547V9mHvjJ2H6wtNcC+nAB45QESe4wHARrBtm+dFUQCCYJq2gExQF5x+YgGjTnYPZ51BCNgW8DzMm/fnpZde+r+33+jbt6eu2263aNsUOCoKySVrwbIox3HUJh6PqOvE7RbWrNnw559/rly5UpZlijbsUeOh02ZJciHlaDwjyJ61Fc+LkiSxObHnqb04jhsxYsTZ55z1v/+9znGwYsVfw4cPz8vLe+uttxo1PkBdzf9fSAxblj8LAHbuLFm2bNkLL7ywdevWc84555577snICC5duvrBBx/84ssv3nrzjeHDh3s8EsdBSUnla6+99sEH71uWdcMNN5x//vmFhfnOhWMx3et1L1m65JFHHpkzZ86ll1563XXX5efnu91uNmaKiooXLlx4/vmDyssrEfHbb78dPHhwSkqwpKT0888/tywrFAqNGDGiRYtmmzZtGT58OKX05ptvHjRoEMdxLL6TZR8GOJCQn4wDsk0WGMTyBybr2KpdhB2vQ6k7mds7BrxkTR6rG31496LUTq7EQMgeA5umm2s2bJwxc9aiZSs1i4YU/Y9FSxcvWRlTTJvgd9/PHDZ8VJ++/ae99Drj1YzPO6K+TVDTkFKMRkmLFh2ffuYF3aDM2mdahCISpJpuxhSNOfNSRD1h1NE1QglqqhWL6swwY1nEtpnSbi8BilIkNtoWWmaSkY8isVFVCNMwIcHKcu3UU86URP+woRe/8vKbzZq2AhC//OJbxpEcFncCzCRmW/GdbVuLJoy/FUBq3qwNq1yiKtbll40FcLVqedIfvy9SlbictruonP2qKuYN198k8K6C/AbfffsjUiwprmBv5O67/uN2e5s2bf7jjzMxqdvZ2g0Rk6Vh07STRzRbi7HTIpFYx46d09Iy/P7gI488xk5Ifol1abdnEj5bDvwdSqsT1Jy2GCKRSCgUUhSFtY1NDfu9jmUYmmFojP4pjROXZVPTIn8sXJSWlX3/Q4/YiFHdOu/C4VnZBYaBV189XhT9ffoM6N37LADXlVdeX1YWtW00DNR1pBSZoV7XMRKxKcULL7ykUeMWznQQn1lsS9NN3bAsO0kvYCNSpAQNnWiqZRqU5fCr2fB9eOMnKRiYhYLJn6pCkOLyZWuvuvL6Vi3bN23SatjQkY88/ERcqxyJ0YQ+3zTNI/ROnVXhERo2lFLmxx4KhRiTcN6785Vp1HHvKNdqSCL44vfe/bhhg2YNCpu++cY7ukbCIfX11/7XvFmb/LwGkx98dOeOEtbDyR3O5l/ToF9/9f2As87Nyy28YszYFcvXfPD+pyOGj87JLrj66rHr12/EhPWEkPgq4FARicSiUUVRNF03azpf1GUoDqXUtm2mC0iueXRMUBvZh8PhUCgUi8XYyz6gQsGyDF1XdV1NsP09tGOY9jczfsirX3j3fx6wEUsqw5deOVYU/W+++Z7Xm3711eO3bNm9Y0fZ2LE3ArimTXuTUrRtLC4OMbIvLY1QitEohkLmU0+9lJaes2nzjuSFvU2JYdqGadskiWATlhjToLpm2xYiYo2erlEoykENBaOh04ryGNtft3ZrSXHlb3P/rKyIVDP5ICIhyLTEWEcak2QwMe2IsgpGzKzSFiIyRVV5eTkLXHfYACKGw7XrMihSgmWlkV6n9XO7Aldfdd2G9VtNA1euWNu715kA0nXjJmzdskuJGUyRVhvZMxXgvfc8kJWZn5mRV79e45Yt2v08a65T2sxhzox0D/VhHWNt8uagjiPwSCJh7uEp5+q2JbVx+0gkoqoqa+EBhy8rWqjrerJKjyIyaXzh0hWFjZtlZBeMuPiykZde0ah5a7c7deLE+wHcGzfuZH29aNEqjyfthhtuq6hQFIWoKq2oUNhPpaURTUNdx8WL17g9wVtvu4siqprBhHyKaNnUsmny0sDZs0w0DKt2Pl8L2SfBcQirKI84smioShl50aVffP4NUoxF9YryMCaM0oSgM1eymf0w382+UHMZWLcwDIMVDnCOVLsRkwUY39rfhSjaFn715fcu2f/Q5MeQ4uq/1t9/30MA4rkDB3/z9QzDsJCiYVhMRZd8E0qRELTMeM/HogZS3LG9mOc8g84dypYA7EzmvVpXz+48r/P4dRxvX7fRb38HtTWDRSkzD4L9nJZ8HabJc6LbmN3e45EAwLKsUFVY07Tt27ebtrVlwyZALhKJAGB2drauo2VZfr8/GAyuXr3a5XKVlpbatu3xeJhxpLAwBwAIgdatW7Zo0WL+/Pm2HQ+2YRAEbv+OhYjV6ifVdPZOPrKX24JNTF6QeR5kWbJtyzA4Qigi/vDDD7IsDRgwwOdz+XwuAPB63eypOY6HpAoWh5qGeP/Yj5Pl30dy0DsichzHPMfdbjf7ZAFXgiCQ/RYXYJER4XCYUjp06NBoVLvllls2bNgw7cVpp5/Rp0WLZrquR6JqMBgEEDH+8vZ6Iuf5du/e7ff769XLOeuss9q3b8/ublmEEIslC6WUqqoqiuJh5A7FpHHjdKzTt3UcsFGHfjhHCLIsy7JczR5Ba4+IEgSR50WeEwEBEJDGnXYsC3SdUIJut/eWW2778ceZc+bMnXDzbQBcq1ZtXC7vTz/Ncru5QECeNWt2JBI7/fQzvV7hpZdeadas+bBhI3TdLCzMKSmJWBaEwxrHQZ8+faLR6NKlSwEgmdS5uObVaSoAxwrv7VU6du9W04PYwO2WKbVN05RdYiDocbkFSRJTU33XXXfdunXrQqGQZaGu2wCgaUZd9P3+cKSHjUPzTMULAG63OxgMyrLsdruZwww7gaUwru06hBDLgtTUFFEUyspKvV7Pgw8++Mf8eeOuu7pZsyYA4HbLwaCfUpstDPd+xj3bmjUbO3bs+N13MwgBv9/v8/lKS6KyzEmSIMsyTTj5+3w+t9tt23YtzakV1XTw1X497rPr1IZDGkD7ec0cAM8JmER+7FxN0/w+j98f1DSNUioIvGXj9u3bPR7vOeecM23atGuvvXbdupuzs7Ofeuqp/Pz8iy66CACuuOKK3NzcZ599tl+/fpdddtmECROiUSM93WOacN555z337LO7du3q0qWjpuluj8xxHJckYkASo3Dau693Wv3hkh7FmR14VjRWFHnEPRxbkjlAGD9+/PPPP1daWpqTk2GaBED0eFwQTxAeTw7DgikOsnsPBkeaTzCVoSRJ77zzzqpVqyilqampBQUFAwcOzM+PW9FisZggCA797xMul6CqJiKKoijLsiBCp84nMasYz4Np6oap8TzvdrvdbhkBASninngTp2BqVlZWTIkZhmHboKpqOBzOzg5AvOwKZX3rFAs4jLoA+/9LXYbiVBuA+5xmjjmcJiU3bz9jrloBLIjzWqAEKisVUZTPOefcbt1OkSUwDKtt2/Zt27Zt1Cj3ueeea9Wq1ZQpU6666kpCyLRp09LT0xGhadP6EyaM/eOPPy655JJHH300Nzf3s88+q6zUKIVTTz3V5/dv3rwZAFgpGIeH12T+ifJ7yHGYYJJ0XxI+A/sJkzZqE5OiDUDZRQixdF1lbDArKy09Pf3jjz8GAFEUkyUJxj14nk+WmY8LSJLk8Xh0XX/00UefeeaZr7766q233rrmmmtGjRq1a9cuFrju9/udrFW1XccwiCzLtm1zPObmZQMAC3F37hLwB3xen8DzAMjtq34te4Nbt271uD2Korhc4PV62cqiuLjKsmzWt+y1apqmKIqmaX+/B/aix7pSGFQTKhy7cV1dv67AMo1hwmLEDu5HjWRbaOjE0Imj2WYKtmjUqqxUKcUNm3fZNtqIio6VYb2yUlUUwpQ3f/21aeHClUVFlUyBxzR5VVVaKKRTirNmzTv//BFud3rXrn2WLFkbCumXXHrlyV16MN8+pthLdulj942r1ilaFqlFpYd7q/QsRDOxWdU2RQ2blsoMk5ZlIKJpUGLjPXffl5GeE6qKIYvAtZnMeQQNeEcazJEkFoulpqYOHTrUsqyysrJx48YB8Mw3lqktD/xwFJHil198y/PisqWrEmG2DBaldqJvTUSTUINS27EBJV9k3dpNouCZ8tCTSHHE8EtvuvFOU4+/XEKIruuOyvnwiChZRVrzldWZkF8z9gaOvOR2GHAyECRLQftpJy8ALyRUQexkAEBwu3m320UpNmqQzwFQgpLASV5JFHjEeLWMpk0LWY/rusHzfDDophR9PonjOEqxR4+TO3d647ff/njs0Sd69TytS5cuHU5qt2PbzqWL/+rUqQ0vyYhAbeB54NlingDFeKYNAEDKcSBwsEeKRwTbRkniAHhEME1CqOVySSwEiWVZNQwjuUKWJEmSKAFQjgNB5ACoJPGEQP369S3L2rx5c8eO7XgebBsBOEHgWMaI4xGiKFZUVLCl8tKlS8eOHRsOhxcsWDR82EWqosuS3+1yf/jBp5988okgCJTSgoKCCRMmNGoU91AkBChlfcuUOyiJrrS0dEoAxPjgtywCgJIkAIBp6YIgCLyQeD2OwMYDAHDA87xNbJfLZVmgxDS/L+hkxOF53kmAedj6jv3LYv/atX3dobaqO8znN34CzwHGZew9sjTHIct+C0n1cCGh2hEEThC5AQPObNKkyXffznhx2tTZc2YD0MWLlkqS5HH7EAhSjuOR50TgKCVA0ZYkgeM4SikTRNnyj/EE5oTPvkK8KCjn9XoRSHZ2piBIqqp7vV7TNE1TRcRAICCJLgBqE1sQBA44Sqmu2V6v3KVLF0rpzJkzO3ZsBwBHpzDbkYbf73e5XKZpFhcXsxKMO3bsGHhOemqqnxDYtWv3n38uWLXqLyZXd+vWrby8olGj+pYFogg8D2wBb1lsXzBMMxwOp6WluVwCJcALyamsqCy5AahpmXL8IJdIYRxPZKyqqkuWEYkkQWpqqmmae9U4OcI4QfaHCWcadkIMuBrF/DCpUI9jMnQSiggC4ytQv37BTTePG3Te2f/73zvTp799zbVXpQQDsZiKSNhVeV5k1gaKtiiIPM8hItPuOrnZKFJJlHieZzIhABBKACArM2vw4MGXX355j1O7ulweQpDZMgDAtk1FUfx+vyjITHrleZFSHQDatWvXvHnzGTNm3HLLzQj030H2oigWFxdXVlZecsklzz//fCwWu/768e+9997UqVNFEfLz81JSggUF+SwLvd/v9/t9AMCEHUGIM11GxW63W5ZkURQCgbhpzbYpx3GEWIQQUeQlSQLgZUmujW1YluXxeNhFCbVsYh5NyfgE2R8A+xGxkn9y9h2yr3YC7iv0iOd5SQJBkDkOmjZteNddd1533di//lqdmZkRiUQRKeMAPC8AMEcrwhIWQaL2K7M2EUIyMzM5jmPaClYibteuXZs3b77yyitfe/21//3vf88999zll18OHBUEWVV1wzDS0lJSUmQ2oTAVkq7rfr+bUpAkbsSIEVOnTt21q6igXl7ddecxQzQaDQQCubm56enpHMdJkpSfn5+TkxWJRkpKSgoKciKRCKW0vLxclmWm/ysrK2vSpIks84zPI4Ki6H6/27JYomSL6eFsGyzL8nhZwjwZABCJbdtcPGcU7JPyfT6fruuiKFoWhEKhRo0aAYBlgXRUSpOfIPvDxD6ng2oH90n2e88LqKiaz+cBhKpQOC01xefPzs/PBg4AAQEAgeMBmEsO7q+OGqvKwnSUsswDQH5+fk5Ojsvl7tOnT2Fh4UMPTZk+/d0LLxxy9dVX+/1ur8cNALZNEQnPi4RQZnYCBMuiiHTIkCEPPfTQb7/9dvGo4UdT/jxCCAQCLOfimDFj+vfv7/P5AGDgwIGqYgqCoOt2WlrwvvsmXXbZZSxFKgAw5Y9tA6XUNE2/381SpNm2jUglSYybWjjq8UrMc1kQWJkKQRQFy7I4Dtl7rmky8/v9uqFTStldPB4PcHCghLd1hn+D8HZMUJN7Vzu4z3nBUaVCYiFgmjoAAAdpaSnAQVlZWUxRDcNAAKZXppQyMxBFoEidG9g2WBYyy6JtxxUHksTJMs/czLxeuWnTph06dAiFQk8++eRLL72Um5s7adJ/evXqPXfuH7pu2xYIPM+qqfB8XIo1Tepy8TzPN23aMCsra8aMGQDHPc0z8DyfkpJyyy23nHnmmUwzcs455zw/9dnc3EyXS1RVgyVHFEUQBFBV1TRpJKKKIsgy73a7WfJiAHC5xGAw6FjdIpEIC2h1uWQWisZuJ0kSz4s1SCz+VRAEl+zyeDwcF+f85lFMWXiC7A8f1Sg/mZiddX4ynTtIct7gUlNTmb09EgkBQFZWht/vdbkkZl1nRnUA2GufA4pAqEXRpiznF48U4x4FhKKmq+FIVNMNnodnnnlu48bNv/32+6BBA9577/3XXnsNEQcNOu+ii0b+/PPPHAeAoGsmE0XLSqsoRUjo8AYOHLhw4cLS0vIj2o1HB7quM91Kfn4+z7O1N3Acl5KSYlo2AogSDxyIEmcTyvEQTPHKLt7n9zg+kYIIggimSS2LWJYVi8ViSkQ3zFmzZj355JPFxaUcB16v1+VymabN5ICE/d+hsj3k5vV6b7rppo4dTwIAQeBUNXY03SBOkP1hIlldV/Nr8mkMNf2iIa7eYxGgJBgMMvpPuM3sScma9EnZv3k+2Q8amMKJ6fIEgfP7vcFgQJZljoMOHTpkZeasWLGC/WvkyKEzZ8689957//rrr3HjrrvyyrErV67xemVCIBrVsrLSWB0eQtCycPDgwaWlpdu3bz9ivXj04HK5RFFkrJhxaUQURVEQOEopz4PLJem6yXFxWmX+yGxVT6mjuAVZ5l2ueP4Yds0FCxY8/fTTI0eOnD79PV03IV6jht2Wr43EUlJ8999/f7dunTXNIoTwPC+K8QoLRwOH4Qnwz0Sdh4LuHyzQsOYda6b0OlBIPznEbd+o1hCaSHRPCd56870tW3RgofWO01FlRXTC+FsBRJ835cknnmUx5LuLypBiJByPGN2+rahF8zbjxl3PnFJYjlemSnRC0/+/IRKJIeKsWbMzM7Pbtm2/det2RFy4cHGDBo0A+K5du69du57lPmG565zQfUqpZcVfHwuqNQxr186S8TfcLEveSfc+wFJfHZ2nOEH2h4l9BofXbMMxJ3uk+NSTL3jcqcuWrkGK4ZCqa8TQKQv8nvPLvAsGD3PJvvbtOr3z9vtsOkjMCxGkeM7Z5wWDqSx/QrW02f9AF8yjA8simma8+urrHTt27tix8z33TNq5s0hRtP/+9+0ePXr6/cEH7p+yedN2pBiqiiEipdTJ7eGgtLT8yy+/bt+uk8+b8tijT5WVVjm1K44C/iVkn5xJ6ujcsSbZ77MBR5Hs93lfihRXLF+Tlpo98c5JLHOT81laUqkqJiLOnj2nR4+esuxu0aLVn/MXY1JtltdefcvvD/7550JNMxjPx6S8NHUeE/7Ph6qqFRUVbL+0tHTixIk+XyA3N/+bb76zbarEjKnPvyTwrqzMvMcfewb3HoxOEP6GDZvOOutsAH7o0OGVlSHbpkyIOGr1CP49ZH9EkzTURM3b0RppwvGgyB4TxHwwn7WiNrK3TIxFjdN6nt6qZftwSGX8n9jIUuISguFw2LZpOBx+5ZVXOnbsnJtT76Ybb/9t7nx22ob1WwRBuuOOiZZFdN1k4YZOjh0nU83/K7DC1bZta5pmWdZXX30zePAQAH7MmCuXLV1VUR4u2lV67sDBqSlZp3Tv9d23P4ZC8ULXqqqXlJS98cZb+fn1mjRp9sEHH7GJwKH2o5az8N9A9jQpIfdRo/x90vzhkn0dYD9kjxSfevK5lGDGmtUbFEVjK0zDsBJiZ/xT19WKiooH7p/idgW6nHzKFWOuCVXFohGtXbsOV111DSJSik6pdpaR6v8hty8rK2FiVywW74poVKmqCs/+eW7zZq3z8wofmvwoy5Pzy+x5V1057oWpL7OlvqGTOb/M69C+czCYeu+9/6msZLnVbBYIFInEQqHQUXuK457snVC//YccHaH7Jn9l5P0PI/t4qY3Nm7b7fIHHH39y76xsBJFomqIoUdPU4/RPsXh3xeDzhzYobJKRnjNr5pw777wrL6+gpKQME9SOiEyfdxilRI9/kHC4yrIMRMLKtyKiphmWiZs3bR8xfJTb5e/WtefSJassEyNhjWXU27F99+233eX3pXbu1O2nn2aZps1KmCS/tKM5h/4byJ5Ru5PD7+gw/NrJ7NDJvkZay1q3Q2+PphmISAiec845l19+OaNbXVdt20wEhO6Jw7Usg7EmpDhr5pxLRo8BENu0aQfAf/75l+zKTEZg1/l/qNUjxEK0WFbVvX6gcbvJRx9+3r/fQA7km2680zRw186Sr778ruNJXRoUNnnl5TdKSyoNw6LxAFukFA3DcmSoo7Zo+heQPUvtiEzVzNI87k0DB5tS8u81g+7TpHew3J4e9GftDdj76544eVbTZsWKFW+88RYmGHWCtxCW7pjFijMyNnTClgbExvl/LBJ4V0pK2sQ772XqKMbfnGIEB3iufxuIYWiIFsaLJsSHUzgcVVXdMX9oqv3iC6+6XQFJ9Hbq2BWAP/OMAdu27UAaz2ZfU3XHspIetceotSpOXYESoBREEebPXzR79mwWf1ZYWNi5c+dmzRp98MEnHTp0aNWqGSLs3l26du3avn17vfLKGz169GjVqpUowrZtu3777bfRo0dUVkY/+eSTHTt2EEIaNmw4YsQIURS//PLLgQMHejweUeTeffeDwsL6vXqdGgqH09JS2M0BgFArHpTK8wnv6ENzUqJJlXaYp8dhJJY5CqkHLIuwYG8lZni9LsuiiChJAs+DZSHHoyjwEPfqQUKIyyUxr1JNMzweF9unlPI8j8y/CAEAKisj11xzjWlaX331qWEQl9tJwsWciP5feXw5flPJTx1PK+q8ZNOgpmlu2bLlzDPPVNToDz9836ZNu2DQz4YNIlJK6zb76CHjiE8slNmKqgafPwxACgYyfN5UAKlb154//jC712ln3HrLRHbOw1OeSEvN/mHGL61anpQSzN61s9w08I7bJ53e9+xI2Lhu3M0ArpzswoL8xpkZBS9Ne/Pd6Z/4fRmsxtiO7aWS6J/y0JPMHaW0tFxV1WQh1rJVm2iI5mEwfLZwYPsOS3eUCPs03ddE3XTmfsFSNZuJyjksBzaxsXh3OTsSr7uWtIWqYsklHBIr/3h1Y3ZQU+2rrhw36NwhTC+V3DGUHj1T8z8DTsKifciPcU1KwodCVcx+/c7q0aNncXGxc45TBeRoN3xvHPGpOhrVACArK3Xr1i2n9ey5deuWWKzqiccf/3PBfEQaiYS3b9/G0rPKsmSaZmVl5Zq1awzDePjhhymFYDC4bdu29evXT3tp2gtTX9i6devOnZvGjBkze/bs9PT0mBIjNpYUR+oVZFFKN2zYEArFACArK0OW3ZTu8ZYVBFHgRdhXbrPDBh5hQemQgAiyLKqqKUncBx988sYb/3O5xKqqWCymff31N4ZB33jj7T/+mG/bQCksWbLyzTff2bp11xNPPHnddeMvv/zqK6+89tVX3yovq2RZ5ZKdiCVJ8Hg8mBQ4mJyR7dg87T8SPM+zUoOEUADweKRAIBAIBJx014wBOJkXjiGOeOCtKIqWhYQQj8ezdu3a//znPzk5OfPmzQMAQkg0Gp01a9bo0aMppaWlpYoaS00N5mTnFBYWfvbZZ4MGDaqqqiKE/P777w0KG7AifppGb7nlllgsVl5e7pJdl1xyidfrDQQChGLzZi3T0vylpVXZ2WkCzwEn2LZNiMVcrxOCWd30uJNdA/ZOTnis3qhl2bIssvwZkydP3rhxIyIMGzbs119/feSRR1q2bDl+/PjJkyf37duL5+H999+fM2dOx44dH3300fr167dr1y4ajb751pvDhg6d9tLzqalBUZQdId+2KdPYw1FZqhzXYClUKKUAfCymRyIRRVFisZjf72czqeDk6zimOOJk7/FIhkHcbjErK+uP+X/897//FQQhHAm3aN6iffv2+fn5mzZvmjFjhqIqfp8fANxut22bV1xx+XfffXf55ZeOHDly164dpqnruur1ul0uAOA9nrRo1FNcXGSYxqZNmzhOiEQiXre3rKysuLgqEAgQArt3F6dnpHq9blEU2SzLsk3V1ZIqOXkOTdSHAgAnC9pRhiyLFRVVGelppkmLiopMy7z++uvPOeecqqrwtm070tIyKAXLIlVVMZ/PV1UV3rx5q66bhOLo0ZdOnnyvptHevXtv3LgpeQpjoIkqUbB3BO4JVp8M1ktsxc7SNLpcLpbiXpZlZyXPBqFz5rHCEWdNMUV1uQRKYevWrY0bNf7tt9+WLFkyYfyEdevXzZs3b926df379S8rK0Nq3XHHHQCwc+fOtLS03Nzchx56qLik+M033+zevXtOTk44HK6srCQEKioiL730+l133bVq1SpZkj/44IO1a9euW7dOklyapuXmpD399NOdOnV95JFH5/wylxIAAI7jCUE219bho9XMonFsKYGxekHg3W53p46dsrOzJ02aFA6H3W63pmmCIEydOvXqq68ePXr0559/HggEDMOQJfmnn376z3+mXHXVVRs3bnS73V6vlwWlUkoJAURgCeEJIdUe7ohWszjuwER31kVsipQkzufzeb1e9l6c+ZTVgD+mjT3yZO/3e4EDjoe09BRR4lPTgjm5WZ06nyRJgqYrBfXycvOyFTVqmJYgcsFAMDMzc+vWrbIst27datK9k8KRcElJSe/evU899dQWLVtMn/7eDz/8cN3113Ec165dO0JIgwYN0tNdgUAgHA3n5+cvXLjqow8/eeWVV2bM+HHduvWqagACsUEQpFqSmh0mnLfIcicJgiCK4mGUMagrUAqBgE9RDEEASmnz5s0ff/zxjz76aPny5RnpWSzNbnlZJVKO2GgadjgUrawImZb954KFL7/06scffaoqeocOHRxtMyRVcYF4lRWoSfnH4FH/qXCmQUb2hABTADNf5oS49I/osaMxTGMx1e/3nn322Rs2bMjOzna7XZ06dercubOu6y1btuzXr196ejrPQ5cuXVq1bpGXl3vttdc2atRI140HH5y0bt0627br18+95557BEG4//77RVEcMXzEhAkTLMs69dRTysrKmjYt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" alt="Q097原題圖，CH20 PDF p.40" width="470" />

(A) 衍生物具UV 吸收

(B) 降低極性,增加衍生物與分析管柱的作用

(C) 較易進行分析

(D) 過量之試劑可以在衍生物前沖提出,減少干擾

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**neomycin原反應；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**原反應導入二硝基芳香UV基團且降低題定silica的強作用 → B說增加管柱作用錯。

**其他選項／關鍵錯選：**A UV吸收改善；C較易分析；D過量试劑在該方法可先冲出而減干扰。

**條件／易錯與來源边界：**试劑先後次序依此反應與方法，不能變成所有衍生化试劑永遠先出。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18|L18]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l18|R18]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f13|F13]]。

</details>

### Q098｜102-2 #33｜弱鹼與負電試劑

^hplc-c-q098

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.40–41。

**原題：**C6H5CH2NH2 適合以離子對-逆相液相層析進行分析定量,在酸性移動相中加入下列 何者其滯留時間最長?

(A) (C4H9)4NCl

(B) (C3H7)4NCl

(C) C8H17SO3Na

(D) C6H13SO3Na

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**弱鹼與負電試劑；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**酸性苄胺為BH⁺ → 配负電alkylsulfonate → C8比C6同族疏水尾長 → C。

**其他選項／關鍵錯選：**A/B季銨為正電，不合；D反號正確但尾較短。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|L14]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14|R14]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f09|F09]]。

</details>

### Q099｜102-2 #34｜paracetamol緩衝液

^hplc-c-q099

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.41。

**原題：**以ODS 管柱之液相層析法,分析paracetamol(pKa 9.5)錠劑中主成分之含量,其移 動相之組成,下列何者最適宜?(paracetamol 結構如圖)

<img src="data:image/png;base64,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" alt="Q099原題圖，CH20 PDF p.41" width="760" />

(A) 0.05 M NaOH/acetonitrile (15: 85)

(B) 0.05 M borate buffer (pH 10)/acetonitrile (15: 85)

(C) 0.05 M acetic acid/acetonitrile (15: 85)

(D) 0.1 N HCl/acetonitrile (15:85)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**paracetamol緩衝液；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**paracetamol為弱酸pKa9.5 → 弱酸環境以中性態為主並兼顾一般silica穩定 → 題本C acetic acid。

**其他選項／關鍵錯選：**A NaOH與B pH10促解離且威胁部分silica；D強HCl雖抑酸解離，也要看過低pH與材料穩定，不是題本最佳。

**條件／易錯與來源边界：**這是給定配方最佳選擇，不等于實用最適法已经驗證；acid/ACN是15:85別讀反。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|L09]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09|R09]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f22|F22]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c03|C03]]。

</details>

### Q100｜102-2 #37｜cyclodextrin手性

^hplc-c-q100

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.41。

**原題：**下列層析管柱之固定相,何者適用於分離鏡像異構物?

(A) Cyclodextrin

(B) Polyethylene glycol

(C) Polyamide

(D) Octadecyl silane

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**cyclodextrin手性；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**A。

**最短完整解題鏈：**cyclodextrin具手性包接環境 → 可供對映選擇 → A。

**其他選項／關鍵錯選：**B PEG、C polyamide、D普通ODS不因名字自动具有該手性識別。

**條件／易錯與來源边界：**實际要匹配分析物、孔腔與條件，非任何cyclodextrin柱都分任何镜像體。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|L17]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17|R17]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f12|F12]]。

</details>

### Q101｜102-1 #30｜UPLC縱向擴散

^hplc-c-q101

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.41–42。

**原題：**依Van Deemter equation,下列何者非UPLC(ultra-HPLC)減少帶加寬效應 (band broadening)之項目?

(A) 漩渦擴散(Eddy diffusion)

(B) 縱向擴散(Longitudinal diffusion)

(C) 分析物於靜相之質量轉移抗力(Resistance to mass transfer)

(D) 分析物於靜相孔隙中移動相之擴散抗力(Resistance to diffusion)

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**UPLC縱向擴散；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**B。

**最短完整解題鏈：**細粒可減少A與質傳距離／阻力 → 不直接改溶液縱向扩散B → 選B。

**其他選項／關鍵錯選：**A多路徑、C固定相質傳、D孔内相關質传／扩散距離均可受細粒影響。

**條件／易錯與來源边界：**B係數未直接變不等于B/u项不變；改變速度u會改變此项贡献。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|L24]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l24|R24]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f19|F19]]。 紙筆：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c09|C09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-c12|C12]]。

</details>

### Q102｜102-1 #35｜aminopropyl與封端

^hplc-c-q102

**來源：**CH20儀器分析-高效能液相層析法(HPLC).pdf，PDF p.42。

**原題：**下列有關常用HPLC 固定相的敘述,何者錯誤?

(A) ODS 上的殘餘矽醇基(residual silanol group)為造成層析峰拖尾的因素之一

(B) Endcapped ODS 上的殘餘矽醇基之覆蓋程度以含碳率(carbon rate)表示

(C) 胺丙烷基矽膠(aminopropyl silica gel)固定相常用於蛋白質分析

(D) Bonded phase 其液相以共價鍵鍵結於矽膠上,其使用壽命較包覆液相(coated phase)長

<details>
<summary>作答後展開解析</summary>

**真正問什麼：**aminopropyl與封端；按原題的正確／錯誤／最長／最短／無法问法回答。

**題本答案：**C。

**最短完整解題鏈：**題本aminopropyl主要常考醣／界面活性劑 → C蛋白質配對錯。

**其他選項／關鍵錯選：**A殘餘silanol可能拖尾；D鍵結相比简單塗覆常較少流失；B題本以碳率描述覆盖需加科學限制。

**條件／易錯與來源边界：**carbon load不是封端百分率；不能由B推「含碳率每多1%即多封端1%」。

**答案身分：**題本答案；未取得官方答案表。

回查：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|L08]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08|R08]]。 必背：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f04|F04]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-f21|F21]]。

</details>

## 全章必背總表與各固定點

^hplc-c-fixed

HPLC01–19與F01–19一對一保留；F20–27補上原圖次序與科學边界。可由定義推的量仍教算法，不全部變口訣。

| ID／舊代碼 | 必背或必要固定輸入 | 條件／來源限制 | 觸發與回查 |
|---|---|---|---|
|F01／HPLC01|流路：儲液→去氣泡→幫浦→進樣→保護柱→分析柱→所選偵測器；幫浦主要連到流量與tR。|手動進樣平頭針、短保護柱是舊教材操作配對。舊列內徑1–10 mm、長5–100 cm與恆溫槽100–150°C是來源數值，不能作所有儀器規格或通用操作上限；保護柱粒徑查產品。|pump、degasser、guard column；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q058\|Q058｜108-2 #38]]|
|F02／HPLC02|題本NP沖提序：MeOH>ethyl acetate>DCM>hexane；RP常考：THF>ACN>MeOH>water。正逆相切換題選ethanol。|均為指定相上的教材常用序，實際強度、選擇性及相容性仍查方法；ethyl acetate不是一般水相RP慣用溶劑。|溶劑強度、正逆切換；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q026\|Q026｜111-1 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q035\|Q035｜110-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q067\|Q067｜107-1 #34]]|
|F03／HPLC03|官能基表先看酸鹼／電荷，再看氫鍵與完整疏水骨架。題定silica：丁酸>丁醛>丁烷；benzyl alcohol比benzoic acid早。|舊便記序COOH>ArOH>ROH>NH₂>CHO>ketone>ester>ether>ArX>Ar>alkene>RX>alkane不是完整分子普遍保留定律；羰基及異構物次序特別不能硬推。|官能基、同骨架；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q054\|Q054｜108-2 #11]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q056\|Q056｜108-2 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q071\|Q071｜106-2 #31]]|
|F04／HPLC04|aminopropyl：醣與介面活性劑常考；cyano、diol是極性鍵結相；KOH處理silica的題本對象是鹼性化合物。|NH₂、CN、diol的模式由移動相及條件決定，並非名稱一出就全是NP。醣也可用anion-exchange+PAD，不宣稱只有一種柱能分析。|NH₂、CN、KOH-silica；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q064\|Q064｜107-2 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q088\|Q088｜104-2 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q102\|Q102｜102-1 #35]]|
|F05／HPLC05|ODS=C18=n-octadecyl；C8=octyl；phenyl可給芳香相關選擇性。endcapping遮蔽殘餘Si–OH，減少部分次級作用。|題本常列trimethylchlorosilane試劑；高pH與溶劑穩定性以產品為準。C18能測鹼性物；C8與C18不能單憑碳鏈替高極性物普遍排序。|ODS、封端、phenyl；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q004\|Q004｜113-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q027\|Q027｜111-1 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q032\|Q032｜110-2 #31]]|
|F06／HPLC06|Q025的chlorophenol位置異構物最適原理配對為adsorption。舊教材吸附相經驗序silica<alumina<magnesium silicate<charcoal保留作來源配對。|表面活性、含水與分析物會改吸附；ortho>meta>para不是普遍極性或tR定律，RP分配也可分位置異構物。|adsorption、異構物；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q025\|Q025｜111-1 #36]]|
|F07／HPLC07|常見樹脂styrene+DVB交聯；DVB含量關係交聯程度。強陽SO₃⁻、弱陽COO⁻；強陰季銨正電、弱陰可質子化胺。|命名依被交換離子。舊清洗配對：陽交換HCl/HNO₃、陰交換NaOH/NaHCO₃；是否可再生及濃度按樹脂與分析方法，非所有管柱一律適用。|羧酸根、磺酸根、DVB；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q019\|Q019｜112-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q072\|Q072｜106-2 #32]]|
|F08／HPLC08|離子強度I=½Σcᵢzᵢ²；IEC相反電荷保留，競爭鹽常促進沖提。電導與PAD是兩種不同偵測機制。|I不含原子序；樹脂選擇性另受電荷、溶劑化等影響。不要把I增加寫成分析物一定保留更強；PAD讀電流，不是電導。|鹽、電荷、ion strength；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q016\|Q016｜112-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060\|Q060｜107-2 #12]]|
|F09／HPLC09|陽電分析物配alkylsulfonate；陰電分析物配alkylammonium。常考heptanesulfonate、decanesulfonate、TBACl、cetrimide；ammonium acetate不是該族經典長尾試劑。|相同家族、其餘條件相當時較長烷鏈常保留較強。正／負電試劑名稱是它自己的電荷。sodium octanesulfonate簡寫SOSA須看實際全名。|離子對、反號、烷鏈；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q009\|Q009｜113-1 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q014\|Q014｜112-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q022\|Q022｜111-2 #31]]|
|F10／HPLC10|SEC：可進孔少者先出，孔徑範圍內的小者常較晚。親水gel例agarose、dextran、polyacrylamide；硬質材料例交聯polystyrene、controlled-porosity glass。|以水動力尺寸分離，非單一分子量定律。材料依表面化學選水相GFC或有機GPC；玻璃珠不必親脂、固定相不保證全不帶電。|玻尿酸、SEC、gel filtration；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q031\|Q031｜110-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q091\|Q091｜104-1 #36]]|
|F11／HPLC11|Q008圖定HILIC短→長：phenylalanine<tyrosine<threonine<serine<arginine；峰D=serine。水增加常增強HILIC沖提。|舊例Ascorbic acid<GSH<GSSG只作該例次序；VitaminC不是硫醇、GSSG是二硫化物。ZIC-HILIC只是其中一類。|高有機、親水相、峰D；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q008\|Q008｜113-1 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q011\|Q011｜112-2 #28]]|
|F12／HPLC12|Pirkle、cyclodextrin、手性移動相與手性衍生化可供對掌選擇；三點模型是題本最少3點配對。α/β/γ-cyclodextrin常由6/7/8葡萄糖組成，包接疏水部分。|手性crown ether確有商品柱。未具手性的普通冠醚不自動分鏡像；Q017的D必加此條件。Labetalol四組態為兩對對映體。|Pirkle、cyclodextrin、chiral；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q003\|Q003｜113-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q017\|Q017｜112-1 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q030\|Q030｜111-1 #40]]|
|F13／HPLC13|neomycin+fluorodinitrobenzene→可UV偵測的衍生物；Q097在silica題定下降低極性、減少過強相互作用。|以Q097原反應為準；反應產率、空白、過量試劑和產物穩定性均要核對。衍生化目的不等於每種反應都必定降極性。|胺基醣苷、無發色基；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q002\|Q002｜114-1 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q097\|Q097｜103-1 #36]]|
|F14／HPLC14|題本靈敏度序ECD>FL>UV/Vis>ELSD>RI；選擇性FL>ECD>UV/Vis>ELSD>RI；耐變性UV/Vis>ELSD>ECD>RI。|題本簡表，不是不同儀器／所有化合物的共同定律。靈敏、選擇、耐變三個問題先分開，實際方法仍須實測。|sensitivity、selectivity、robustness；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q001\|Q001｜114-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q033\|Q033｜110-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q046\|Q046｜109-2 #40]]|
|F15／HPLC15|不依發色基的常考三台：RI、ELSD、CAD。RI一般不配梯度；ELSD/CAD可配適當梯度且用揮發相／添加物。|非揮發分析物才留粒子；非揮發緩衝鹽可能成背景；響應不保證線性或跨組成不變。|通用、梯度、蒸發；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q001\|Q001｜114-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q013\|Q013｜112-2 #36]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q028\|Q028｜111-1 #31]]|
|F16／HPLC16|題本配對：醣/PEG/UDCA/非離子界面活性劑→ELSD；B2/aflatoxins→FL；adrenaline→電化學；不同吸收波長混合物→DAD；氯離子→IC。|氯離子IC通常讀電導，不指定PAD；糖可PAD。mannitol排常規直接UV；electron capture為GC，不是液相electrochemical。|分析物與偵測器；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q036\|Q036｜110-1 #26]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060\|Q060｜107-2 #12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q063\|Q063｜107-2 #34]]|
|F17／HPLC17|舊教材列質量量級：RI約1µg、ELSD約10ng、UV/Vis約0.01–100µg、FL約ng、ECD及PAD可<1ng。|來源沒有統一分析物、S/N與進樣條件；這些不全可直接比較，也不是任何藥物的法定LOD或LOQ。只保留量級提示，不拿來算驗證限量。|ng/µg、檢出量級；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q073\|Q073｜106-2 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q075\|Q075｜106-1 #37]]|
|F18／HPLC18|內標穩定、結構與行為相近、不反應、峰可分辨、濃度與tR宜可比；用面積比校正。|先於想補償的步驟加入；只補償共同且經驗證的變動。舊R²>0.995保留作來源示例，不是所有方法的充分驗證標準。|IS、面積比、萃取回收；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q006\|Q006｜113-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q015\|Q015｜112-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q066\|Q066｜107-1 #13]]|
|F19／HPLC19|細粒減少多路徑與質傳展寬；題本以1.7µm示例。H下降，同L時N=L/H增加；更高壓需求。|粒徑≠內徑；短柱N不必增。粒徑不直接改B，但u變會改B/u；H=A+B/u+Cu是簡化模型。|UPLC、UHPLC、Van Deemter；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q012\|Q012｜112-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q020\|Q020｜111-2 #27]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q101\|Q101｜102-1 #30]]|
|F20／新增配對|Q039原圖給定短→長：prednisolone<betamethasone<betamethasone17-valerate<betamethasone21-valerate<betamethasone17,21-dipropionate。|C18、MeOH/water75:25題定序；位置酯基差異不能只數OH或碳數。|第3個流出、類固醇；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q039\|Q039｜110-1 #33]]|
|F21／新增邊界|C8常比可比C18疏水保留弱；碳負載不直接等於封端比例。|Q043題本D與其説明是來源爭議；Q102題本B的碳率說法保留但科學上需分開。|C8/C18、carbon load；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q043\|Q043｜109-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q102\|Q102｜102-1 #35]]|
|F22／新增公式|酸：pH=pKa+log([A⁻]/[HA])；鹼：pH=pKa+log([B]/[BH⁺])。|pKa對應酸或BH⁺的共軛酸；同溶劑與活度近似。RP中性態較強保留是假設，不是定義。|H–H、pH-pKa；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q007\|Q007｜113-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q024\|Q024｜111-1 #30]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q034\|Q034｜110-2 #38]]|
|F23／新增條件|混合溶劑pH受活度、pKa、組成與量測尺度影響；Q053題本選加入ACN後pH增加。|保留答案並教實測與尺度；不用「ACN中性所以稀釋酸」當普遍證明。|乙酸緩衝液＋ACN；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q053\|Q053｜108-2 #10]]|
|F24／新增策略|同梯度端點，時間增加1.5倍，斜率變原來2/3；題本Q084選較慢梯度。|不保證所有選擇性或Rs都改善；先核對近鄰峰、時間與重平衡。|梯度時間與斜率；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q042\|Q042｜109-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q084\|Q084｜105-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q086\|Q086｜105-1 #38]]|
|F25／新增結構|VitaminC是烯二醇內酯；ascorbate的負電不來自COO⁻。|依ChEBI結構修正來源說明；Q080正電離子對選項仍成立。|Ascorbic acid；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q080\|Q080｜105-2 #12]]|
|F26／新增偵測|PAD用脈衝電位量安培電流；電導量離子導電。|無機陰離子如氯通常用IC＋抑制型電導；醣可anion-exchange＋PAD。|PAD≠conductivity；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060\|Q060｜107-2 #12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q064\|Q064｜107-2 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q078\|Q078｜106-1 #38]]|
|F27／新增定量|檢量範圍須涵蓋題目的關鍵低高區，並在該基質驗證。|Q015只是題設MIC10及疑慮50µg/mL，題本選1–100；不作臨床建議。|range、accuracy、precision；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q015\|Q015｜112-2 #39]]|

### F01｜HPLC01｜pump、degasser、guard column

^hplc-c-f01

**固定輸入：**流路：儲液→去氣泡→幫浦→進樣→保護柱→分析柱→所選偵測器；幫浦主要連到流量與tR。

**適用條件：**手動進樣平頭針、短保護柱是舊教材操作配對。舊列內徑1–10 mm、長5–100 cm與恆溫槽100–150°C是來源數值，不能作所有儀器規格或通用操作上限；保護柱粒徑查產品。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q058|Q058｜108-2 #38]]。

### F02｜HPLC02｜溶劑強度、正逆切換

^hplc-c-f02

**固定輸入：**題本NP沖提序：MeOH>ethyl acetate>DCM>hexane；RP常考：THF>ACN>MeOH>water。正逆相切換題選ethanol。

**適用條件：**均為指定相上的教材常用序，實際強度、選擇性及相容性仍查方法；ethyl acetate不是一般水相RP慣用溶劑。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q026|Q026｜111-1 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q035|Q035｜110-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q067|Q067｜107-1 #34]]。

### F03｜HPLC03｜官能基、同骨架

^hplc-c-f03

**固定輸入：**官能基表先看酸鹼／電荷，再看氫鍵與完整疏水骨架。題定silica：丁酸>丁醛>丁烷；benzyl alcohol比benzoic acid早。

**適用條件：**舊便記序COOH>ArOH>ROH>NH₂>CHO>ketone>ester>ether>ArX>Ar>alkene>RX>alkane不是完整分子普遍保留定律；羰基及異構物次序特別不能硬推。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q054|Q054｜108-2 #11]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q056|Q056｜108-2 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q071|Q071｜106-2 #31]]。

### F04｜HPLC04｜NH₂、CN、KOH-silica

^hplc-c-f04

**固定輸入：**aminopropyl：醣與介面活性劑常考；cyano、diol是極性鍵結相；KOH處理silica的題本對象是鹼性化合物。

**適用條件：**NH₂、CN、diol的模式由移動相及條件決定，並非名稱一出就全是NP。醣也可用anion-exchange+PAD，不宣稱只有一種柱能分析。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q064|Q064｜107-2 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q088|Q088｜104-2 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q102|Q102｜102-1 #35]]。

### F05｜HPLC05｜ODS、封端、phenyl

^hplc-c-f05

**固定輸入：**ODS=C18=n-octadecyl；C8=octyl；phenyl可給芳香相關選擇性。endcapping遮蔽殘餘Si–OH，減少部分次級作用。

**適用條件：**題本常列trimethylchlorosilane試劑；高pH與溶劑穩定性以產品為準。C18能測鹼性物；C8與C18不能單憑碳鏈替高極性物普遍排序。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q004|Q004｜113-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q027|Q027｜111-1 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q032|Q032｜110-2 #31]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q055|Q055｜108-2 #12]]。

### F06｜HPLC06｜adsorption、異構物

^hplc-c-f06

**固定輸入：**Q025的chlorophenol位置異構物最適原理配對為adsorption。舊教材吸附相經驗序silica<alumina<magnesium silicate<charcoal保留作來源配對。

**適用條件：**表面活性、含水與分析物會改吸附；ortho>meta>para不是普遍極性或tR定律，RP分配也可分位置異構物。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q025|Q025｜111-1 #36]]。

### F07｜HPLC07｜羧酸根、磺酸根、DVB

^hplc-c-f07

**固定輸入：**常見樹脂styrene+DVB交聯；DVB含量關係交聯程度。強陽SO₃⁻、弱陽COO⁻；強陰季銨正電、弱陰可質子化胺。

**適用條件：**命名依被交換離子。舊清洗配對：陽交換HCl/HNO₃、陰交換NaOH/NaHCO₃；是否可再生及濃度按樹脂與分析方法，非所有管柱一律適用。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q019|Q019｜112-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q072|Q072｜106-2 #32]]。

### F08｜HPLC08｜鹽、電荷、ion strength

^hplc-c-f08

**固定輸入：**離子強度I=½Σcᵢzᵢ²；IEC相反電荷保留，競爭鹽常促進沖提。電導與PAD是兩種不同偵測機制。

**適用條件：**I不含原子序；樹脂選擇性另受電荷、溶劑化等影響。不要把I增加寫成分析物一定保留更強；PAD讀電流，不是電導。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q016|Q016｜112-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060|Q060｜107-2 #12]]。

### F09｜HPLC09｜離子對、反號、烷鏈

^hplc-c-f09

**固定輸入：**陽電分析物配alkylsulfonate；陰電分析物配alkylammonium。常考heptanesulfonate、decanesulfonate、TBACl、cetrimide；ammonium acetate不是該族經典長尾試劑。

**適用條件：**相同家族、其餘條件相當時較長烷鏈常保留較強。正／負電試劑名稱是它自己的電荷。sodium octanesulfonate簡寫SOSA須看實際全名。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q009|Q009｜113-1 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q014|Q014｜112-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q022|Q022｜111-2 #31]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q044|Q044｜109-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q057|Q057｜108-2 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q062|Q062｜107-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q098|Q098｜102-2 #33]]。

### F10｜HPLC10｜玻尿酸、SEC、gel filtration

^hplc-c-f10

**固定輸入：**SEC：可進孔少者先出，孔徑範圍內的小者常較晚。親水gel例agarose、dextran、polyacrylamide；硬質材料例交聯polystyrene、controlled-porosity glass。

**適用條件：**以水動力尺寸分離，非單一分子量定律。材料依表面化學選水相GFC或有機GPC；玻璃珠不必親脂、固定相不保證全不帶電。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q031|Q031｜110-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q091|Q091｜104-1 #36]]。

### F11｜HPLC11｜高有機、親水相、峰D

^hplc-c-f11

**固定輸入：**Q008圖定HILIC短→長：phenylalanine<tyrosine<threonine<serine<arginine；峰D=serine。水增加常增強HILIC沖提。

**適用條件：**舊例Ascorbic acid<GSH<GSSG只作該例次序；VitaminC不是硫醇、GSSG是二硫化物。ZIC-HILIC只是其中一類。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q008|Q008｜113-1 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q011|Q011｜112-2 #28]]。

### F12｜HPLC12｜Pirkle、cyclodextrin、chiral

^hplc-c-f12

**固定輸入：**Pirkle、cyclodextrin、手性移動相與手性衍生化可供對掌選擇；三點模型是題本最少3點配對。α/β/γ-cyclodextrin常由6/7/8葡萄糖組成，包接疏水部分。

**適用條件：**手性crown ether確有商品柱。未具手性的普通冠醚不自動分鏡像；Q017的D必加此條件。Labetalol四組態為兩對對映體。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q003|Q003｜113-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q017|Q017｜112-1 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q030|Q030｜111-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q079|Q079｜106-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q100|Q100｜102-2 #37]]。

### F13｜HPLC13｜胺基醣苷、無發色基

^hplc-c-f13

**固定輸入：**neomycin+fluorodinitrobenzene→可UV偵測的衍生物；Q097在silica題定下降低極性、減少過強相互作用。

**適用條件：**以Q097原反應為準；反應產率、空白、過量試劑和產物穩定性均要核對。衍生化目的不等於每種反應都必定降極性。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q002|Q002｜114-1 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q097|Q097｜103-1 #36]]。

### F14｜HPLC14｜sensitivity、selectivity、robustness

^hplc-c-f14

**固定輸入：**題本靈敏度序ECD>FL>UV/Vis>ELSD>RI；選擇性FL>ECD>UV/Vis>ELSD>RI；耐變性UV/Vis>ELSD>ECD>RI。

**適用條件：**題本簡表，不是不同儀器／所有化合物的共同定律。靈敏、選擇、耐變三個問題先分開，實際方法仍須實測。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q001|Q001｜114-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q033|Q033｜110-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q046|Q046｜109-2 #40]]。

### F15｜HPLC15｜通用、梯度、蒸發

^hplc-c-f15

**固定輸入：**不依發色基的常考三台：RI、ELSD、CAD。RI一般不配梯度；ELSD/CAD可配適當梯度且用揮發相／添加物。

**適用條件：**非揮發分析物才留粒子；非揮發緩衝鹽可能成背景；響應不保證線性或跨組成不變。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q001|Q001｜114-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q013|Q013｜112-2 #36]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q028|Q028｜111-1 #31]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q051|Q051｜109-1 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q075|Q075｜106-1 #37]]。

### F16｜HPLC16｜分析物與偵測器

^hplc-c-f16

**固定輸入：**題本配對：醣/PEG/UDCA/非離子界面活性劑→ELSD；B2/aflatoxins→FL；adrenaline→電化學；不同吸收波長混合物→DAD；氯離子→IC。

**適用條件：**氯離子IC通常讀電導，不指定PAD；糖可PAD。mannitol排常規直接UV；electron capture為GC，不是液相electrochemical。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q036|Q036｜110-1 #26]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060|Q060｜107-2 #12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q063|Q063｜107-2 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q073|Q073｜106-2 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q078|Q078｜106-1 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q082|Q082｜105-2 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q092|Q092｜103-2 #30]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q093|Q093｜103-2 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q095|Q095｜103-1 #11]]。

### F17｜HPLC17｜ng/µg、檢出量級

^hplc-c-f17

**固定輸入：**舊教材列質量量級：RI約1µg、ELSD約10ng、UV/Vis約0.01–100µg、FL約ng、ECD及PAD可<1ng。

**適用條件：**來源沒有統一分析物、S/N與進樣條件；這些不全可直接比較，也不是任何藥物的法定LOD或LOQ。只保留量級提示，不拿來算驗證限量。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q073|Q073｜106-2 #35]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q075|Q075｜106-1 #37]]。

### F18｜HPLC18｜IS、面積比、萃取回收

^hplc-c-f18

**固定輸入：**內標穩定、結構與行為相近、不反應、峰可分辨、濃度與tR宜可比；用面積比校正。

**適用條件：**先於想補償的步驟加入；只補償共同且經驗證的變動。舊R²>0.995保留作來源示例，不是所有方法的充分驗證標準。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q006|Q006｜113-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q015|Q015｜112-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q066|Q066｜107-1 #13]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q068|Q068｜107-1 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q076|Q076｜106-1 #32]]。

### F19｜HPLC19｜UPLC、UHPLC、Van Deemter

^hplc-c-f19

**固定輸入：**細粒減少多路徑與質傳展寬；題本以1.7µm示例。H下降，同L時N=L/H增加；更高壓需求。

**適用條件：**粒徑≠內徑；短柱N不必增。粒徑不直接改B，但u變會改B/u；H=A+B/u+Cu是簡化模型。

**來源：**舊建構／複習稿同碼；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q012|Q012｜112-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q020|Q020｜111-2 #27]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q101|Q101｜102-1 #30]]。

### F20｜新增配對｜第3個流出、類固醇

^hplc-c-f20

**固定輸入：**Q039原圖給定短→長：prednisolone<betamethasone<betamethasone17-valerate<betamethasone21-valerate<betamethasone17,21-dipropionate。

**適用條件：**C18、MeOH/water75:25題定序；位置酯基差異不能只數OH或碳數。

**來源：**本次校正／教學補充；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q039|Q039｜110-1 #33]]。

### F21｜新增邊界｜C8/C18、carbon load

^hplc-c-f21

**固定輸入：**C8常比可比C18疏水保留弱；碳負載不直接等於封端比例。

**適用條件：**Q043題本D與其説明是來源爭議；Q102題本B的碳率說法保留但科學上需分開。

**來源：**本次校正／教學補充；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q043|Q043｜109-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q102|Q102｜102-1 #35]]。

### F22｜新增公式｜H–H、pH-pKa

^hplc-c-f22

**固定輸入：**酸：pH=pKa+log([A⁻]/[HA])；鹼：pH=pKa+log([B]/[BH⁺])。

**適用條件：**pKa對應酸或BH⁺的共軛酸；同溶劑與活度近似。RP中性態較強保留是假設，不是定義。

**來源：**本次校正／教學補充；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q007|Q007｜113-1 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q024|Q024｜111-1 #30]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q034|Q034｜110-2 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q041|Q041｜109-2 #28]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q045|Q045｜109-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q049|Q049｜109-1 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q074|Q074｜106-1 #36]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q099|Q099｜102-2 #34]]。

### F23｜新增條件｜乙酸緩衝液＋ACN

^hplc-c-f23

**固定輸入：**混合溶劑pH受活度、pKa、組成與量測尺度影響；Q053題本選加入ACN後pH增加。

**適用條件：**保留答案並教實測與尺度；不用「ACN中性所以稀釋酸」當普遍證明。

**來源：**本次校正／教學補充；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q053|Q053｜108-2 #10]]。

### F24｜新增策略｜梯度時間與斜率

^hplc-c-f24

**固定輸入：**同梯度端點，時間增加1.5倍，斜率變原來2/3；題本Q084選較慢梯度。

**適用條件：**不保證所有選擇性或Rs都改善；先核對近鄰峰、時間與重平衡。

**來源：**本次校正／教學補充；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q042|Q042｜109-2 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q084|Q084｜105-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q086|Q086｜105-1 #38]]。

### F25｜新增結構｜Ascorbic acid

^hplc-c-f25

**固定輸入：**VitaminC是烯二醇內酯；ascorbate的負電不來自COO⁻。

**適用條件：**依ChEBI結構修正來源說明；Q080正電離子對選項仍成立。

**來源：**本次校正／教學補充；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q080|Q080｜105-2 #12]]。

### F26｜新增偵測｜PAD≠conductivity

^hplc-c-f26

**固定輸入：**PAD用脈衝電位量安培電流；電導量離子導電。

**適用條件：**無機陰離子如氯通常用IC＋抑制型電導；醣可anion-exchange＋PAD。

**來源：**本次校正／教學補充；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060|Q060｜107-2 #12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q064|Q064｜107-2 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q078|Q078｜106-1 #38]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q095|Q095｜103-1 #11]]。

### F27｜新增定量｜range、accuracy、precision

^hplc-c-f27

**固定輸入：**檢量範圍須涵蓋題目的關鍵低高區，並在該基質驗證。

**適用條件：**Q015只是題設MIC10及疑慮50µg/mL，題本選1–100；不作臨床建議。

**來源：**本次校正／教學補充；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q015|Q015｜112-2 #39]]。

## 全題路由：辨識任務比年份更好用

^hplc-c-routes

| Q ID／原題身分 | 本題辨識任務 | 要保留的條件 | 精準回查 |
|---|---|---|---|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q001\|Q001｜114-1 #28]]|ELSD與梯度|分析物揮發性、移動相與是否梯度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22\|R22]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q002\|Q002｜114-1 #29]]|衍生化的目的|原分析物的偵測／分離弱點及反應產率|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18\|L18]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l18\|R18]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q003\|Q003｜113-2 #29]]|手性與離子對|對映異構物與可作用的對掌環境|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17\|L17]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17\|R17]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q004\|Q004｜113-2 #32]]|固定相的適用性|鍵結基團、殘餘矽醇基、pH 與峰形|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08\|R08]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q005\|Q005｜113-2 #33]]|RP水醇比例|模式、溶劑種類及明確的比例順序|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11\|R11]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q006\|Q006｜113-2 #40]]|內標的適用範圍|校正、稀釋、樣品面積與內標加入時點|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23\|L23]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23\|R23]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q007\|Q007｜113-1 #28]]|pKa區間與變動|pH 區間、pKa 及中性／離子態保留假設|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10\|L10]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l10\|R10]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q008\|Q008｜113-1 #35]]|HILIC原圖峰D|親水表面、高有機／少量水相及電荷條件；保留原題圖|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16\|L16]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l16\|R16]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q009\|Q009｜113-1 #38]]|離子對與解離|分析物在 pH 下的電荷及試劑疏水端|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14\|R14]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q010\|Q010｜112-2 #27]]|C18同族次序|疏水固定相、移動相與分析物在該 pH 的性質|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06\|L06]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06\|R06]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q011\|Q011｜112-2 #28]]|HILIC多重作用|親水表面、高有機／少量水相及電荷條件|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16\|L16]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l16\|R16]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q012\|Q012｜112-2 #32]]|粒徑與內徑|粒徑、柱長、內徑、F／u與板高|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24\|L24]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l24\|R24]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q013\|Q013｜112-2 #36]]|無發色基偵測|分析物揮發性、移動相與是否梯度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22\|R22]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q014\|Q014｜112-2 #38]]|離子對保留方向|分析物在 pH 下的電荷及試劑疏水端|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14\|R14]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q015\|Q015｜112-2 #39]]|檢量範圍|校正、稀釋、樣品面積與內標加入時點|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23\|L23]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23\|R23]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q016\|Q016｜112-2 #40]]|陽交換與pH|固定基團電荷、分析物電荷、pH 與競爭離子|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13\|L13]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l13\|R13]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q017\|Q017｜112-1 #34]]|冠醚條件|對映異構物與可作用的對掌環境|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17\|L17]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17\|R17]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q018\|Q018｜112-1 #39]]|常用RP基團|鍵結基團、殘餘矽醇基、pH 與峰形|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08\|R08]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q019\|Q019｜112-1 #40]]|IEC基團與命名|固定基團電荷、分析物電荷、pH 與競爭離子|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13\|L13]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l13\|R13]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q020\|Q020｜111-2 #27]]|UPLC粒徑|粒徑、柱長、內徑、F／u與板高|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24\|L24]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l24\|R24]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q021\|Q021｜111-2 #30]]|NP混合比例|模式、溶劑種類及明確的比例順序|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11\|R11]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q022\|Q022｜111-2 #31]]|弱酸與正電試劑|分析物在 pH 下的電荷及試劑疏水端|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14\|R14]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q023\|Q023｜111-2 #36]]|RP保留最長|模式、溶劑種類及明確的比例順序|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11\|R11]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q024\|Q024｜111-1 #30]]|aspirin酸鹼方向|分析物為酸或鹼、pKa、移動相 pH 與 RP 模式|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09\|R09]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q025\|Q025｜111-1 #36]]|位置異構物原理|完整結構、骨架、解離與選定模式|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07\|L07]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l07\|R07]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q026\|Q026｜111-1 #39]]|正逆相切換溶劑|樣品基質、互溶性、目的與溶解度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04\|L04]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04\|R04]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q027\|Q027｜111-1 #29]]|聚合物相容性|鍵結基團、殘餘矽醇基、pH 與峰形|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08\|R08]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q028\|Q028｜111-1 #31]]|未衍生化醣|分析物揮發性、移動相與是否梯度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22\|R22]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q029\|Q029｜111-1 #32]]|UV的通用性|分析物吸收、選定波長及校正|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l19\|L19]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l19\|R19]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q030\|Q030｜111-1 #40]]|三點模型|對映異構物與可作用的對掌環境|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17\|L17]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17\|R17]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q031\|Q031｜110-2 #29]]|玻尿酸分離|水動力尺寸、孔隙大小及有效分離範圍|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15\|L15]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l15\|R15]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q032\|Q032｜110-2 #31]]|低極性與C18|疏水固定相、移動相與分析物在該 pH 的性質|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06\|L06]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06\|R06]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q033\|Q033｜110-2 #32]]|偵測器選擇性排序|激發波長、發射波長及分析物螢光特性|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20\|L20]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l20\|R20]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q034\|Q034｜110-2 #38]]|弱酸適用pH|分析物為酸或鹼、pKa、移動相 pH 與 RP 模式|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09\|R09]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q035\|Q035｜110-2 #39]]|NP沖提序|模式、溶劑種類及明確的比例順序|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11\|R11]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q036\|Q036｜110-1 #26]]|B2螢光配對|激發波長、發射波長及分析物螢光特性|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20\|L20]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l20\|R20]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q037\|Q037｜110-1 #28]]|多模式辨識|極性固定相、適當低極性移動相及分析物|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05\|L05]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05\|R05]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q038\|Q038｜110-1 #32]]|強RP移動相|模式、溶劑種類及明確的比例順序|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11\|R11]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q039\|Q039｜110-1 #33]]|五類固醇原圖|完整結構、骨架、解離與選定模式；保留原題圖|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07\|L07]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l07\|R07]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q040\|Q040｜109-2 #27]]|RP常用溶劑|樣品基質、互溶性、目的與溶解度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04\|L04]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04\|R04]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q041\|Q041｜109-2 #28]]|ibuprofen影響最大|pH 區間、pKa 及中性／離子態保留假設|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10\|L10]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l10\|R10]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q042\|Q042｜109-2 #29]]|時間調整反向題|等度／梯度、流量、柱長、溫度與 Rs|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12\|L12]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l12\|R12]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q043\|Q043｜109-2 #32]]|C8/C18題本爭議|鍵結基團、殘餘矽醇基、pH 與峰形|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08\|R08]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q044\|Q044｜109-2 #38]]|經典離子對試劑|分析物在 pH 下的電荷及試劑疏水端|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14\|R14]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q045\|Q045｜109-2 #39]]|pH8.4與缺字動相|pH 區間、pKa 及中性／離子態保留假設；來源標記見本題|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10\|L10]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l10\|R10]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q046\|Q046｜109-2 #40]]|UV耐變性|激發波長、發射波長及分析物螢光特性|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20\|L20]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l20\|R20]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q047\|Q047｜109-1 #8]]|非慣用RP溶劑|樣品基質、互溶性、目的與溶解度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04\|L04]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04\|R04]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q048\|Q048｜109-1 #10]]|一律給分註記|檢品的溶解性、穩定性及分析目的；來源標記見本題|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01\|L01]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l01\|R01]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q049\|Q049｜109-1 #34]]|弱鹼升pH方向|分析物為酸或鹼、pKa、移動相 pH 與 RP 模式|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09\|R09]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q050\|Q050｜109-1 #37]]|四種保留機制|極性固定相、適當低極性移動相及分析物|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05\|L05]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05\|R05]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q051\|Q051｜109-1 #38]]|梯度非離子物偵測|分析物揮發性、移動相與是否梯度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22\|R22]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q052\|Q052｜108-2 #9]]|中性物與pH|分析物為酸或鹼、pKa、移動相 pH 與 RP 模式|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09\|R09]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q053\|Q053｜108-2 #10]]|混合溶劑pH|pH 區間、pKa 及中性／離子態保留假設|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10\|L10]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l10\|R10]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q054\|Q054｜108-2 #11]]|silica結構比較|極性固定相、適當低極性移動相及分析物|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05\|L05]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05\|R05]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q055\|Q055｜108-2 #12]]|C18全名|鍵結基團、殘餘矽醇基、pH 與峰形|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08\|R08]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q056\|Q056｜108-2 #33]]|丁烷丁醛丁酸|極性固定相、適當低極性移動相及分析物|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05\|L05]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05\|R05]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q057\|Q057｜108-2 #34]]|四丁基銨對象|分析物在 pH 下的電荷及試劑疏水端|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14\|R14]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q058\|Q058｜108-2 #38]]|幫浦角色|流路、流量及固定的進樣量|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02\|L02]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l02\|R02]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q059\|Q059｜108-1 #11]]|軟膏基質萃取|樣品基質、互溶性、目的與溶解度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04\|L04]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04\|R04]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060\|Q060｜107-2 #12]]|氯離子與IC|可氧化還原基團、電位控制或離子導電|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21\|L21]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l21\|R21]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q061\|Q061｜107-2 #13]]|嗎啡類最短|完整結構、骨架、解離與選定模式|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07\|L07]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l07\|R07]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q062\|Q062｜107-2 #32]]|苯乙酸離子對|分析物在 pH 下的電荷及試劑疏水端|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14\|R14]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q063\|Q063｜107-2 #34]]|PEG配對|分析物揮發性、移動相與是否梯度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22\|R22]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q064\|Q064｜107-2 #37]]|醣類固定相|鍵結基團、殘餘矽醇基、pH 與峰形|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08\|R08]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q065\|Q065｜107-1 #10]]|已知蛋白親脂序|疏水固定相、移動相與分析物在該 pH 的性質|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06\|L06]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06\|R06]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q066\|Q066｜107-1 #13]]|內標相近tR|校正、稀釋、樣品面積與內標加入時點|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23\|L23]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23\|R23]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q067\|Q067｜107-1 #34]]|RP溶劑強度|模式、溶劑種類及明確的比例順序|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11\|R11]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q068\|Q068｜107-1 #39]]|乳酸內標|校正、稀釋、樣品面積與內標加入時點|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23\|L23]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23\|R23]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q069\|Q069｜107-1 #40]]|THF互溶|樣品基質、互溶性、目的與溶解度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04\|L04]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04\|R04]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q070\|Q070｜106-2 #2]]|室溫兩相|樣品基質、互溶性、目的與溶解度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04\|L04]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04\|R04]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q071\|Q071｜106-2 #31]]|silica官能基|極性固定相、適當低極性移動相及分析物|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05\|L05]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05\|R05]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q072\|Q072｜106-2 #32]]|磺酸強陽交換|固定基團電荷、分析物電荷、pH 與競爭離子|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13\|L13]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l13\|R13]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q073\|Q073｜106-2 #35]]|mannitol偵測|分析物揮發性、移動相與是否梯度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22\|R22]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q074\|Q074｜106-1 #36]]|bupivacaine延長題|分析物為酸或鹼、pKa、移動相 pH 與 RP 模式|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09\|R09]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q075\|Q075｜106-1 #37]]|較廣偵測範圍|分析物揮發性、移動相與是否梯度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22\|R22]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q076\|Q076｜106-1 #32]]|內標tR距離|校正、稀釋、樣品面積與內標加入時點|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23\|L23]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l23\|R23]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q077\|Q077｜106-1 #37′]]|RP模式辨識|疏水固定相、移動相與分析物在該 pH 的性質；來源標記見本題|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06\|L06]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06\|R06]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q078\|Q078｜106-1 #38]]|ECD縮寫|可氧化還原基團、電位控制或離子導電|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21\|L21]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l21\|R21]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q079\|Q079｜106-1 #40]]|alanine題缺字|對映異構物與可作用的對掌環境；來源標記見本題|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17\|L17]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17\|R17]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q080\|Q080｜105-2 #12]]|VitaminC陰離子|分析物在 pH 下的電荷及試劑疏水端|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14\|R14]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q081\|Q081｜105-2 #32]]|RP保留方向|疏水固定相、移動相與分析物在該 pH 的性質|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06\|L06]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l06\|R06]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q082\|Q082｜105-2 #33]]|aflatoxins配對|激發波長、發射波長及分析物螢光特性|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20\|L20]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l20\|R20]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q083\|Q083｜105-2 #35]]|等比例RP強度|模式、溶劑種類及明確的比例順序|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11\|R11]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q084\|Q084｜105-2 #39]]|梯度1.5倍|等度／梯度、流量、柱長、溫度與 Rs|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12\|L12]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l12\|R12]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q085\|Q085｜105-2 #40]]|NP低極性溶劑|模式、溶劑種類及明確的比例順序|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11\|R11]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q086\|Q086｜105-1 #38]]|梯度沖提方向|等度／梯度、流量、柱長、溫度與 Rs|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12\|L12]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l12\|R12]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q087\|Q087｜104-2 #32]]|hexanol苯己烷|極性固定相、適當低極性移動相及分析物|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05\|L05]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l05\|R05]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q088\|Q088｜104-2 #37]]|KOH處理silica|鍵結基團、殘餘矽醇基、pH 與峰形|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08\|R08]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q089\|Q089｜104-2 #38]]|三配方強度|模式、溶劑種類及明確的比例順序|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l11\|R11]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q090\|Q090｜104-1 #33]]|silanol與siloxane|鍵結基團、殘餘矽醇基、pH 與峰形|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08\|R08]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q091\|Q091｜104-1 #36]]|玻尿酸方法|水動力尺寸、孔隙大小及有效分離範圍|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15\|L15]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l15\|R15]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q092\|Q092｜103-2 #30]]|UDCA偵測|分析物揮發性、移動相與是否梯度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l22\|R22]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q093\|Q093｜103-2 #35]]|DAD多波長|分析物吸收、選定波長及校正|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l19\|L19]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l19\|R19]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q094\|Q094｜103-1 #8]]|DMF互溶|樣品基質、互溶性、目的與溶解度|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04\|L04]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l04\|R04]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q095\|Q095｜103-1 #11]]|adrenaline電化學|可氧化還原基團、電位控制或離子導電|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21\|L21]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l21\|R21]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q096\|Q096｜103-1 #35]]|benzylmorphine|完整結構、骨架、解離與選定模式|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07\|L07]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l07\|R07]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q097\|Q097｜103-1 #36]]|neomycin原反應|原分析物的偵測／分離弱點及反應產率；保留原題圖|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18\|L18]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l18\|R18]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q098\|Q098｜102-2 #33]]|弱鹼與負電試劑|分析物在 pH 下的電荷及試劑疏水端|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l14\|R14]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q099\|Q099｜102-2 #34]]|paracetamol緩衝液|分析物為酸或鹼、pKa、移動相 pH 與 RP 模式；保留原題圖|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l09\|R09]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q100\|Q100｜102-2 #37]]|cyclodextrin手性|對映異構物與可作用的對掌環境|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17\|L17]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l17\|R17]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q101\|Q101｜102-1 #30]]|UPLC縱向擴散|粒徑、柱長、內徑、F／u與板高|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24\|L24]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l24\|R24]]|
|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q102\|Q102｜102-1 #35]]|aminopropyl與封端|鍵結基團、殘餘矽醇基、pH 與峰形|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]／[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-l08\|R08]]|

## 易錯救援：斷在哪裡，就回那一段

^hplc-c-rescue

| 題幹触發 | 先做的判讀 | 入口 |
|---|---|---|
|看见silica|先按NP表面作用；別先套C18|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05\|L05]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07\|L07]]|
|看見C18/ODS|先RP，再看離子化及配方|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l06\|L06]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08\|L08]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11\|L11]]|
|見pH與pKa|先酸或鹼，再判兩態比例；大小題看區間|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09\|L09]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l10\|L10]]|
|見ionic／ion-pair|先固定基團交換還是加試劑，再判反號|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13\|L13]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14\|L14]]|
|見高分子／分子篩|问孔隙與水動力尺寸，不先排極性|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15\|L15]]|
|見HILIC|親水相＋富有機水相，水常是強沖提|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16\|L16]]|
|見鏡像|找真正手性環境，不是只看碳鏈|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17\|L17]]|
|見無發色基|查揮發性／梯度，選RI/ELSD/CAD或適合電化學|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l21\|L21]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22\|L22]]|
|見波長混合物|DAD給多波長，不独證未知身分|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l19\|L19]]|
|見內標|相近但分開、早加、共變，校正面積比|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23\|L23]]|
|見UPLC／粒徑|dp與dc分開、N=L/H、B係數和B/u分開|[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24\|L24]]|

## 來源、科學边界與版本校正

^hplc-c-source

| 真正讀到的附件 | 本次用途 |
|---|---|
|高效能液相層析法HPLC 建構式教學版 v1.0|第0–24層、HPLC01–19與102題索引；保留有效分類與旧入口|
|高效能液相層析法HPLC 複習卡 v1.0|14題診斷、固定點、快掃路由；改為答案收起與雙向跳轉|
|CH20儀器分析-高效能液相層析法(HPLC).pdf|42頁、102題；完整題幹與408個A–D選項，另列E給分註記；全部頁面原圖檢視|
|雙檔章節編譯器v3.0|四站、全部L/R接點、來源身份、紙筆與五圖同源規格|

### 邊界｜題目與答案身分

CH20共42頁、102題；年份與題號依題本，尚無官方答案表。Q045答案欄空白；Q048另列E一律給分；Q075/Q077重複106-1#37，後者加′只為辨識；Q079-alanine前缺字。

回原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q045|Q045｜109-2 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q048|Q048｜109-1 #10]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q075|Q075｜106-1 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q077|Q077｜106-1 #37′]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q079|Q079｜106-1 #40]]。

### 邊界｜內徑與粒徑

Q012題本選C，但「流速」可能指F或u；縮內徑不能獨自保證或否定效率。Q020同L時細粒可增N，短柱時須再算L/H。

回原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q012|Q012｜112-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q020|Q020｜111-2 #27]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q101|Q101｜102-1 #30]]。

### 邊界｜冠醚、C8/C18與相命名

Q017不可外推所有crown ether不分鏡像；Q043不可用C8/C18碳鏈替高極性物作普遍排序；NH₂/CN/diol模式看移動相。

回原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q017|Q017｜112-1 #34]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q026|Q026｜111-1 #39]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q043|Q043｜109-2 #32]]。

### 邊界｜碳負載與silica穩定性

Q102題本B以carbon rate表示覆盖需限制：含碳率不直接量封端比例；Q027聚合物溶劑穩定性看產品。旧100–150°C、保護柱粒徑只作來源記录。

回原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q027|Q027｜111-1 #29]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q102|Q102｜102-1 #35]]。

### 邊界｜離子強度與偵測

I只含各離子濃度與電荷平方。競爭鹽常促沖提；樹脂選擇性另論。PAD量電流，不是電導；氯離子IC常配抑制型電導。

回原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q016|Q016｜112-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q019|Q019｜112-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q060|Q060｜107-2 #12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q064|Q064｜107-2 #37]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q072|Q072｜106-2 #32]]。

### 邊界｜分子結構與氫鍵

VitaminC是烯二醇內酯而非羧酸；DMF是醯胺；ACN可接受氫鍵；benzyl是苄基，不是tolyl。aflatoxins原題寫多環芳香烴，正文改為真菌毒素。

回原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q069|Q069｜107-1 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q080|Q080｜105-2 #12]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q082|Q082｜105-2 #33]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q094|Q094｜103-1 #8]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q096|Q096｜103-1 #35]]。

### 邊界｜pH、光源與排序界線

Q053混合溶劑pH不可用「中性ACN稀釋酸」證明；常見UV氘燈與FL氙燈配對要看型號；偵測器三張排序為教材情境，不是所有分析物定律。

回原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q024|Q024｜111-1 #30]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q029|Q029｜111-1 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q033|Q033｜110-2 #32]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q046|Q046｜109-2 #40]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q053|Q053｜108-2 #10]]。

### 邊界｜沒有實讀的外部來源

旧文提IMG3460–3467原始照片、gpt2.md與外部精編筆記，本次未提供，不宣稱已核對。舊文的UDCA精確ε、吸附相及全官能基序只保留有條件教材配對；不當作新實測資料。

回原題：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q025|Q025｜111-1 #36]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q071|Q071｜106-2 #31]]、[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-q092|Q092｜103-2 #30]]。

### 原始資料核對｜本次真正查閱的補充

以下是一次性補充核對，不替代來源題或冒稱現行藥典全文。查閱日期2026-10-02；ChEBI的結構結论是依結構式作編輯判讀。

| 原始來源 | 支持的修正／條件 | 接點 |
|---|---|---|
|[Merck / Sigma-Aldrich](https://www.sigmaaldrich.com/TW/en/technical-documents/technical-article/analytical-chemistry/small-molecule-hplc/hilic)|HILIC：親水固定相、富有機水相；富水層分配及多重作用。|L16／F11|
|[Daicel](https://www.daicelchiral.com/en/chiral-columns/crownpak/)|CROWNPAK含手性冠醚，可作胺基酸對映分離，修正「冠醚全部不行」。|L17／F12／Q017|
|[Agilent](https://www.agilent.com/store/en_US/Prod-972700-906/972700-906)|可比相的C8常較C18少疏水保留；產品將carbon load、endcapped分列。|L08／F21／Q043、Q102|
|[PalmSens](https://www.palmsens.com/knowledgebase-article/pulsed-amperometric-detection-pad/)|PAD以脈衝電位量安培反應，糖與polyol可用；與電導分開。|L21／F26|
|[Thermo Fisher / Dionex](https://appslab.thermofisher.com/App/1448/an175-determination-sulfate-chloride-ethanol-by-ion-chromatography)|AN175以離子層析與抑制型電導測chloride/sulfate。|Q060／F16|
|[IUPAC Gold Book](https://goldbook.iupac.org/terms/view/I03180)|濃度式離子強度I=½Σcᵢzᵢ²定義。|L13／C05|
|[ChEBI](https://www.ebi.ac.uk/chebi/CHEBI:29073)|L-ascorbic acid結構與SMILES；由此判讀為內酯烯二醇，不含COOH。|F25／Q080（結構判讀）|
|[Waters](https://help.waters.com/content/dam/waters/pt_br/support/usermanuals/2018/715002900/715002900.pdf)|Auto•Blend Plus Quick Reference p.2：量測pH會随有機相／離子強度變，應同條件校正。|L10／F23／Q053|

**外部筆記：**本次沒有字根檔；英文名詞在正文先以白話解釋，不製造未核對的字根連結。旧文照片與外部精編筆記未提供，已在边界登記。

**實際驗收：**核對102題原文／選項集合與答案身分、24組L/R、12類紙筆數值、所有內部與雙檔連結、旧唯一標題、五SVG XML及真正渲染；兩MD內嵌圖源與獨立檔一致。没有在使用者Obsidian裝置點擊實測。

## 五張 SVG 入口索引

| 圖 | 已嵌入的正文位置 | 獨立檔案 |
|---|---|---|
|1|[[#圖1｜分析全流程母圖\|回圖1]]|[[藥物分析_高效能液相層析法HPLC_分析全流程母圖_v3_0.svg]]|
|2|[[#圖2｜小循環掛載點圖\|回圖2]]|[[藥物分析_高效能液相層析法HPLC_小循環掛載點圖_v3_0.svg]]|
|3|[[#圖3｜全章方法分類與大小循環對照圖\|回圖3]]|[[藥物分析_高效能液相層析法HPLC_全章方法分類與大小循環對照圖_v3_0.svg]]|
|4|[[#圖4｜儀器與操作考點圖\|回圖4]]|[[藥物分析_高效能液相層析法HPLC_儀器與操作考點圖_v3_0.svg]]|
|5|[[#圖5｜公式與誤差判讀總表\|回圖5]]|[[藥物分析_高效能液相層析法HPLC_公式與誤差判讀總表_v3_0.svg]]|

## 舊版入口相容：以新內容為準

舊版**唯一標題**保留作回查入口；原稿多次重複的「①帶上來」等不能各自作唯一定位，只保留一個入口。舊標題中的「唯一條件」「唯一大分子先出」等原文字樣只為連結相容，下列新版已補足科學條件。

### 使用方法

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### 最小入口檢查

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### 第 0 層｜先看見整座樓梯

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### 第 1 層｜為什麼是「液相」：HPLC 挑客人的唯一條件

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### ① 帶上來

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### ② 動手看

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### ③ 找規律

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### ④ 命名與定位

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### ⑤ 邊界

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### ⑥ 出口檢查

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l01|建構模組]]。

### 第 2 層｜走一次儀器：五個部件各自只負責一件事

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02|建構模組]]。

### ② 動手看：訊號從左走到右

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02|建構模組]]。

### ③ 找規律：每個部件回答一個問題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02|建構模組]]。

### ④ 管柱內部再拆一次

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02|建構模組]]。

### ⑤ 出口檢查

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l02|建構模組]]。

### 第 3 層｜同一條規則的兩個方向：正相與逆相

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|建構模組]]。

### ② 動手看：把兩種管柱擺在一起

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|建構模組]]。

### ④ 命名幾個一定會考的名字

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|建構模組]]。

### ⑤ 邊界：這句話**不能**寫成「極性越大越慢」

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l05|建構模組]]。

### 第 4 層｜四步解題法：本章的主判讀器

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### ② 寫成四步

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### ③ 立刻試跑一題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### ④ 再試一題方向相反的

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### 第 5 層｜移動相沖提強度：一條規則生出兩張方向相反的表

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### ③ 找規律：沖提強度的生成式

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### ④ 兩張順序表

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### ⑤ 兩個常考的補丁

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### ⑥ 比例題怎麼算：不用計算機

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### ⑦ 出口檢查

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### 第 6 層｜官能基極性排序：把「分析物是誰」變成可比較的量

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### ② 動手看：什麼讓一個分子「極性」

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### ③ 命名並排序

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### ④ 拿去掃四題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### ⑤ 分子越大越非極性的逆相版本

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### 第 7 層｜pH 是分析物極性的遙控器

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|建構模組]]。

### ③ 找規律：只有兩句

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|建構模組]]。

### ④ 紙筆技巧一：pH 落在 p$K_a$ 哪一側

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|建構模組]]。

### ⑤ 紙筆技巧二：畫一條數線判「影響大小」

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|建構模組]]。

### ⑥ 掃掉一整批同型題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|建構模組]]。

### ⑦ 邊界

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|建構模組]]。

### ⑧ 出口檢查

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|建構模組]]。

### 第 8 層｜矽膠上面接什麼，它就變成誰

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|建構模組]]。

### ③ 兩張修飾表

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|建構模組]]。

### ④ 三個由此長出的判讀

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l08|建構模組]]。

### 第 9 層｜吸附層析：極性以外的第二種抓法

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### ② 命名兩種機制

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### ③ 為什麼異構物題要選 adsorption

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### ④ 一個常見混淆

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### 第 10 層｜換第二把量尺：離子交換

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13|建構模組]]。

### ④ 兩張必背

新版固定輸入：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-fixed|F01–27／保留HPLC01–19]]。

### ⑤ pH 在離子交換裡做什麼

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13|建構模組]]。

### ⑥ 陰陽離子誰先出

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13|建構模組]]。

### 第 11 層｜離子對層析：把離子「偽裝」成非極性

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|建構模組]]。

### ③ 一刀切開兩者

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|建構模組]]。

### ④ 兩組配對

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|建構模組]]。

### ⑤ 掃掉整族「選哪個試劑」的題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|建構模組]]。

### ⑥ 一個方向陷阱

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|建構模組]]。

### 第 12 層｜換第三把量尺：分子排斥（*唯一大分子先出的模式*）

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15|建構模組]]。

### ③ 命名

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15|建構模組]]。

### ④ 掃題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l15|建構模組]]。

### 第 13 層｜HILIC：用逆相的硬體，做出正相的行為

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16|建構模組]]。

### ③ 命名與四個判讀

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16|建構模組]]。

### ④ 出口檢查

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l16|建構模組]]。

### 第 14 層｜換第四把量尺：對掌性

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|建構模組]]。

### ② 動手看：為什麼需要「三個點」

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|建構模組]]。

### ③ 四種可行做法與一個不行的

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|建構模組]]。

### 第 15 層｜衍生化：當分析物本身不會被看見

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18|建構模組]]。

### ③ 找規律：衍生化的三個目的

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18|建構模組]]。

### ④ 三個高頻陷阱

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18|建構模組]]。

### ⑤ 一個順帶的正相判斷

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18|建構模組]]。

### 第 16 層｜沖提方式：一支曲子與一段漸強

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|建構模組]]。

### ② 兩種方式

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|建構模組]]。

### ③ 方向不能背反

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|建構模組]]。

### ④ 兩個時間調整

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l12|建構模組]]。

### 第 17 層｜檢測器：先問「分析物讓什麼東西改變」

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|建構模組]]。

### ② 動手看：偵測器不認得藥名

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|建構模組]]。

### ③ 八台偵測器，八種「被探測的特徵」

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|建構模組]]。

### ④ 三張排序表：先建立「為什麼是這個順序」

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|建構模組]]。

### ⑤ 三個一定要拆開的混淆

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l22|建構模組]]。

### 第 18 層｜定量：外標與內標各修正什麼誤差

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|建構模組]]。

### ② 兩條路

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|建構模組]]。

### ③ 內標的四個條件

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|建構模組]]。

### ④ 一個容易被忽略的品質題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|建構模組]]。

### 第 19 層｜UPLC：把 Van Deemter 的三項各自處理

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|建構模組]]。

### ② 動手看：UPLC 動了哪些硬體

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|建構模組]]。

### ③ 找規律：哪些項被壓小

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|建構模組]]。

### ④ 一個必須分開的概念

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|建構模組]]。

### 第 20 層｜把全章壓成一棵判讀樹

新版方法判讀：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-methods|全章分類]]；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-decide|四步判讀器]]。

### 全章符號與角色總表

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|建構模組]]。

### 第 21 層｜代表題型：每一種生成動作只示範一次

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### 題型 1｜移動相比例題：只問「整體極性往哪走」

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### 題型 2｜極性排序題：正相與逆相共用同一張表

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l07|建構模組]]。

### 題型 3｜pH 方向題與 pH 距離題（兩種不同問法）

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|建構模組]]。

### 題型 4｜離子對試劑選擇題：兩步刪去

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l14|建構模組]]。

### 題型 5｜離子交換沖提順序題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l13|建構模組]]。

### 題型 6｜方法選擇題：問「哪把尺還有差別」

新版方法判讀：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-methods|全章分類]]；[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-decide|四步判讀器]]。

### 題型 7｜偵測器選擇題：先問分析物有什麼特徵

新版偵測器入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-detectors|物理量與配對總表]]。

### 題型 8｜偵測器排序題：只有兩張表要分清

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l20|建構模組]]。

### 題型 9｜溶媒沖提強度排序題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l11|建構模組]]。

### 題型 10｜對掌性分離題：四可一不可

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l17|建構模組]]。

### 題型 11｜「何者無法減少／延長滯留時間」的雙重否定題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l09|建構模組]]。

### 題型 12｜衍生化題：分辨「目的」與「手段」

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l18|建構模組]]。

### 題型 13｜內標題：四個特性輪流被考

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l23|建構模組]]。

### 題型 14｜UPLC 與 Van Deemter 題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l24|建構模組]]。

### 題型 15｜溶劑互溶題

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l04|建構模組]]。

### 題型 16｜「錯相反」的解題技巧

新版判讀：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-decide|四步判讀器]]；不憑兩個選項措辭相反就猜答案必在其他選項。

### 第 22 層｜102 題完整打靶表

新版102題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-bank|完整來源題]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-routes|閉卷路由]]。

### 22.1｜114-1～111-1

新版102題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-bank|完整來源題]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-routes|閉卷路由]]。

### 22.2｜110-2～108-1

新版102題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-bank|完整來源題]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-routes|閉卷路由]]。

### 22.3｜107-2～105-1

新版102題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-bank|完整來源題]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-routes|閉卷路由]]。

### 22.4｜104-2～102-1

新版102題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-bank|完整來源題]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-routes|閉卷路由]]。

### 22.5｜這 102 題真正反覆測什麼

新版102題入口：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-bank|完整來源題]]；[[藥物分析_高效能液相層析法HPLC_複習導航_v3_0#^hplc-r-routes|閉卷路由]]。

### 第 23 層｜來源衝突、科學邊界與考場用法

新版來源與边界：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-source|來源登記]]。

### 23.1｜管柱恆溫槽的溫度數值

新版來源與边界：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-source|來源登記]]。

### 23.2｜管柱「內徑」減小到底能不能提高 LC 分離效果

新版來源與边界：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-source|來源登記]]。

### 23.3｜UV 檢測器的光源

新版來源與边界：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-source|來源登記]]。

### 23.4｜ortho ＞ meta ＞ para 的極性順序

新版來源與边界：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-source|來源登記]]。

### 23.5｜題號與答案身分的來源限制

新版來源與边界：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-source|來源登記]]。

### 23.6｜三個不可外推的句型

新版來源與边界：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-source|來源登記]]。

### 第 24 層｜考場 30 秒流程、60 秒總整理與掌握檢查

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|建構模組]]。

### 24.1｜考場 30 秒流程

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|建構模組]]。

### 24.2｜題幹翻譯器

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|建構模組]]。

### 24.3｜考前最後 60 秒

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|建構模組]]。

### 24.4｜離開樓梯前的掌握檢查

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|建構模組]]。

### 24.5｜三種熟練程度

對應新版：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-l03|建構模組]]。

### 來源與使用說明

新版來源與边界：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-source|來源登記]]。

### 全章必背總表

新版固定輸入：[[藥物分析_高效能液相層析法HPLC_建構講義_v3_0#^hplc-c-fixed|F01–27／保留HPLC01–19]]。

