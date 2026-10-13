---
title: 藥物分析_拉曼光譜_建構講義_v3_0
version: '3.0'
document_role: construction
chapter_abbr: rm
computation: 紙筆；不使用計算機步驟
paired_review: 藥物分析_拉曼光譜_複習導航_v3_0
figure_set: 拉曼光譜五圖_v3_0
source_questions: 8
learning_loops: 10
fixed_inputs: 15
paper_calculation_families: 5
same_number_review_cards: 10
extended_recall_cards: 28
completion_date: '2026-10-01'
figures:
- 藥物分析_拉曼光譜_分析全流程母圖_v3_0.svg
- 藥物分析_拉曼光譜_小循環掛載與能階圖_v3_0.svg
- 藥物分析_拉曼光譜_全章方法分類與大小循環對照圖_v3_0.svg
- 藥物分析_拉曼光譜_儀器與操作考點圖_v3_0.svg
- 藥物分析_拉曼光譜_公式與誤差判讀總表_v3_0.svg
---


# Raman spectroscopy（拉曼光譜）｜用光的能量差讀振動

^rm-c-home

**先抓全章：Raman 用光的能量差讀振動；峰的位置幫助鑑別，峰的強度要帶著取樣與校正讀。**

本章用來回答藥物／製劑是什麼、固態晶型有何差異，以及在已驗證條件下含量多少。第一次依「四站 → 完整基本例 → 最小工具 → 六組小循環 → 方法與操作 → 紙筆 → 全部原題」閱讀。你只需逐項寫出誰得能、誰失能，無須先想像電子雲動畫。

本版有 10 條 L、15 組 F、3 張核心方法 P1–P4 卡、5 組自編紙筆計算、8 題完整來源題，以及 5 張共用 SVG。閉卷重建由 [[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-start|複習導航]] 進入。

## Part 0｜全章大循環

^rm-c-macro

| 站 | 白話問題 | 實際交出的資訊 |
|---|---|---|
| M01 先定問題 | 要辨身分、比晶型，還是報含量？ | 目的、代表性檢品、方法與參考／校正基準。 |
| M02 準備與測量 | 怎樣照到可用檢品並取得訊號？ | 取樣／空白、合適雷射、作用條件與收光配置。 |
| M03 讀訊號 | 圖在量什麼，單位與處理正確嗎？ | 散射強度、波數位移、實際譜窗與可比光譜。 |
| M04 核對結論 | 證據足夠回答原問題嗎？ | 附條件的鑑別、晶型或含量結論；不符才指定回查。 |

**M01 → M02 → M03 → M04。** 條件合格便交出結論。這是分析者流程；分子散射過程不會自己檢查含量或重新校正。

### M01｜先定問題

^rm-c-m01

先寫目的，再選固體、溶液、製劑或包裝內的代表性檢品。晶型需保留原固態；定量需參考含量與有效校正，不能把鑑別的單峰證據拿來直接報含量。L7 從本站取條件，交取樣方案給 M02。

### M02｜準備與測量

^rm-c-m02

選空白、焦點、功率與照射時間，確認不改樣。雷射與分子作用後收集散射，再用濾片及色散／FT 配置取得訊號。L1、L2、L3、L5、L6、L10 從這裡取得作用或量測條件，交訊號資訊給 M03。

### M03｜讀訊號

^rm-c-m03

先辨軸：雷射波長、散射光波長與 Raman 位移是不同量。保存資料處理、背景及可見譜窗；L4、L8、L9 將可比的峰位置、固態譜或校正訊號交 M04。

### M04｜核對結論

^rm-c-m04

指紋須比參考與可用峰群；晶型須有固態與製樣證據；含量須有校正、範圍與驗證。若不符：目的／代表性回 M01，製樣／光學回 M02，座標／處理回 M03，判準／過度推論在 M04 修正。紅虛線表示這些有原因的回查。

### 圖1｜分析全流程母圖

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="2730" viewBox="0 0 1900 2730" role="img" aria-labelledby="rm3_g1_title rm3_g1_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="rm3_g1_title">拉曼光譜｜分析全流程母圖</title><desc id="rm3_g1_desc">拉曼光譜教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊，藍線表示光路；能階子圖另標藍線為能量帳。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="2730" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH30 / RAMAN / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">拉曼光譜｜分析全流程母圖</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">先走中間四站；身分、晶型、含量各用自己的證據。合格便交出，不符才按原因回查。</text>
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
<rect x="50" y="385" width="350" height="560" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="426" font-size="27" font-weight="600" fill="#9e771c">先帶進來的條件</text>
<text x="72" y="473" font-size="24" font-weight="400" fill="#24343f">分析目的與代表性檢品</text>
<text x="72" y="507.08" font-size="24" font-weight="400" fill="#24343f">固態／溶液／製劑／包裝</text>
<text x="72" y="541.16" font-size="24" font-weight="400" fill="#24343f">參考品或參考含量</text>
<text x="72" y="575.24" font-size="24" font-weight="400" fill="#24343f">樣品穩定與量測條件</text>
<text x="72" y="609.32" font-size="24" font-weight="400" fill="#24343f">接受標準及適用範圍</text>
<rect x="460" y="385" width="970" height="235" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="482" y="426" font-size="27" font-weight="600" fill="#9e771c">M01｜先定問題</text>
<text x="482" y="473" font-size="24" font-weight="400" fill="#24343f">要辨身分、比晶型，還是報含量？</text>
<text x="482" y="507.08" font-size="24" font-weight="400" fill="#24343f">先選代表性檢品、方法、空白與基準。</text>
<text x="482" y="541.16" font-size="24" font-weight="400" fill="#24343f">L7：目的／包裝／不均勻 → 代表性取樣方案 → M02。</text>
<polyline points="945,620 945,660 695,660 695,700" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="695.0,700.0 688.8,688.6 701.2,688.6" fill="#61717a"/>
<polyline points="945,660 1195,660 1195,700" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1195.0,700.0 1188.8,688.6 1201.2,688.6" fill="#61717a"/>
<rect x="460" y="700" width="470" height="285" rx="18" fill="#e8e1f2" stroke="#685185" stroke-width="2"/>
<text x="482" y="741" font-size="27" font-weight="600" fill="#685185">身分／晶型</text>
<text x="482" y="788" font-size="24" font-weight="400" fill="#24343f">比可用峰群與參考譜</text>
<text x="482" y="822.08" font-size="24" font-weight="400" fill="#24343f">晶型須保留原固態</text>
<text x="482" y="856.16" font-size="24" font-weight="400" fill="#24343f">單峰不證明完整身分</text>
<text x="482" y="890.24" font-size="24" font-weight="400" fill="#24343f">L3、L7、L8</text>
<rect x="960" y="700" width="470" height="285" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="982" y="741" font-size="27" font-weight="600" fill="#b72d4a">含量</text>
<text x="982" y="788" font-size="24" font-weight="400" fill="#24343f">先有參考含量與校正</text>
<text x="982" y="822.08" font-size="24" font-weight="400" fill="#24343f">固定基質、聚焦與功率</text>
<text x="982" y="856.16" font-size="24" font-weight="400" fill="#24343f">範圍與獨立驗證適用</text>
<text x="982" y="890.24" font-size="24" font-weight="400" fill="#24343f">L7、L9</text>
<polyline points="695,985 695,1035 945,1035 945,1090" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="945.0,1090.0 938.8,1078.6 951.2,1078.6" fill="#61717a"/>
<polyline points="1195,985 1195,1035 945,1035" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="460" y="1090" width="970" height="275" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="482" y="1131" font-size="27" font-weight="600" fill="#286c68">M02｜準備與測量</text>
<text x="482" y="1178" font-size="24" font-weight="400" fill="#24343f">取樣、空白、雷射、功率與時間，確認未改樣。</text>
<text x="482" y="1212.08" font-size="24" font-weight="400" fill="#24343f">作用：能量守恆、虛擬態、極化率選擇律、振動人口。</text>
<text x="482" y="1246.16" font-size="24" font-weight="400" fill="#24343f">收光／濾片／色散或 FT 配置：先得到可用訊號。</text>
<text x="482" y="1280.24" font-size="24" font-weight="400" fill="#24343f">L1、L2、L3、L5、L6、L10 → M03。</text>
<polyline points="945,1365 945,1450" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="945.0,1450.0 938.8,1438.6 951.2,1438.6" fill="#61717a"/>
<rect x="460" y="1450" width="970" height="275" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="482" y="1491" font-size="27" font-weight="600" fill="#326991">M03｜讀訊號</text>
<text x="482" y="1538" font-size="24" font-weight="400" fill="#24343f">先辨入射 λ₀、散射 λₛ 與有號位移 Δν̃。</text>
<text x="482" y="1572.08" font-size="24" font-weight="400" fill="#24343f">波數差 cm⁻¹；縱軸強度另帶單位與處理條件。</text>
<text x="482" y="1606.16" font-size="24" font-weight="400" fill="#24343f">記錄譜窗、背景、座標校正；保存固態和校正資料。</text>
<text x="482" y="1640.24" font-size="24" font-weight="400" fill="#24343f">L4、L8、L9：整理可比資料 → M04。</text>
<polyline points="945,1725 945,1820" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="945.0,1820.0 938.8,1808.6 951.2,1808.6" fill="#61717a"/>
<rect x="460" y="1820" width="970" height="350" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="482" y="1861" font-size="27" font-weight="600" fill="#b72d4a">M04｜核對結論</text>
<text x="482" y="1908" font-size="24" font-weight="400" fill="#24343f">身分：全譜／峰群＋參考，確認背景與代表性。</text>
<text x="482" y="1942.08" font-size="24" font-weight="400" fill="#24343f">晶型：原固態＋製樣紀錄＋參考，避免化學組成誤判。</text>
<text x="482" y="1976.16" font-size="24" font-weight="400" fill="#24343f">含量：校正、適用區間、取樣與驗證都合格。</text>
<text x="482" y="2010.24" font-size="24" font-weight="400" fill="#24343f">位移不變不保證峰高相同；峰高不直接等於含量。</text>
<text x="482" y="2044.32" font-size="24" font-weight="400" fill="#24343f">證據不夠時，指明缺哪一項，回實際需要修正的站。</text>
<polyline points="945,2170 945,2330" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="945.0,2330.0 938.8,2318.6 951.2,2318.6" fill="#61717a"/>
<text x="970" y="2260" font-size="24" font-weight="400" fill="#356844">條件合格</text>
<rect x="460" y="2330" width="970" height="155" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="482" y="2371" font-size="27" font-weight="600" fill="#356844">正常出口｜交出附條件的結論</text>
<text x="482" y="2418" font-size="24" font-weight="400" fill="#24343f">留下方法、取樣、量測、參考／校正與接受標準。</text>
<rect x="1500" y="400" width="350" height="205" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="1522" y="441" font-size="27" font-weight="600" fill="#b72d4a">目的／代表性不合</text>
<text x="1522" y="488" font-size="23" font-weight="400" fill="#24343f">重選檢品或目的 → M01</text>
<polyline points="1500,502.5 1470,502.5 1470,505 1430,505" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1430.0,505.0 1441.4,498.8 1441.4,511.2" fill="#b72d4a"/>
<rect x="1500" y="1110" width="350" height="230" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="1522" y="1151" font-size="27" font-weight="600" fill="#b72d4a">取樣／背景／樣品被改</text>
<text x="1522" y="1198" font-size="23" font-weight="400" fill="#24343f">修正取樣、波長或功率</text>
<text x="1522" y="1230.66" font-size="23" font-weight="400" fill="#24343f">→ M02</text>
<polyline points="1500,1225.0 1470,1225.0 1470,1225 1430,1225" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1430.0,1225.0 1441.4,1218.8 1441.4,1231.2" fill="#b72d4a"/>
<rect x="1500" y="1460" width="350" height="230" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="1522" y="1501" font-size="27" font-weight="600" fill="#b72d4a">座標／處理不合</text>
<text x="1522" y="1548" font-size="23" font-weight="400" fill="#24343f">改單位、FT、背景讀法</text>
<text x="1522" y="1580.66" font-size="23" font-weight="400" fill="#24343f">→ M03</text>
<polyline points="1500,1575.0 1470,1575.0 1470,1550 1430,1550" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1430.0,1550.0 1441.4,1543.8 1441.4,1556.2" fill="#b72d4a"/>
<rect x="1500" y="1840" width="350" height="305" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="1522" y="1881" font-size="27" font-weight="600" fill="#b72d4a">判準／校正／推論不合</text>
<text x="1522" y="1928" font-size="23" font-weight="400" fill="#24343f">查參考、校正與驗證 → M04</text>
<text x="1522" y="1960.66" font-size="23" font-weight="400" fill="#24343f">需新資料才回相應上游</text>
<polyline points="1500,1992.5 1470,1992.5 1470,2035 1430,2035" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1430.0,2035.0 1441.4,2028.8 1441.4,2041.2" fill="#b72d4a"/>
<polyline points="1430,2135 1450,2135 1450,2200 1880,2200 1880,375 1675,375 1675,400" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1675.0,400.0 1668.8,388.6 1681.2,388.6" fill="#b72d4a"/>
<polyline points="1880,1225.0 1850,1225.0" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1850.0,1225.0 1861.4,1218.8 1861.4,1231.2" fill="#b72d4a"/>
<polyline points="1880,1575.0 1850,1575.0" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1850.0,1575.0 1861.4,1568.8 1861.4,1581.2" fill="#b72d4a"/>
<polyline points="1880,1992.5 1850,1992.5" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1850.0,1992.5 1861.4,1986.3 1861.4,1998.7" fill="#b72d4a"/>
<text x="1500" y="2260" font-size="22" font-weight="400" fill="#b72d4a">紅虛線＝分析者回查；</text>
<text x="1500" y="2291.24" font-size="22" font-weight="400" fill="#b72d4a">不是分子自發的控制迴路。</text>
<rect x="50" y="2510" width="1800" height="105" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="72" y="2551" font-size="27" font-weight="600" fill="#61717a">第一輪完整例｜自編</text>
<text x="72" y="2598" font-size="23" font-weight="400" fill="#24343f">500 nm → 20000 cm⁻¹ → 減 Stokes 位移 1000 → 19000 cm⁻¹ → 約 526.3 nm；圖峰仍標 +1000。</text>
<text x="50" y="2662" font-size="20" font-weight="400" fill="#61717a">灰線＝分析資訊；藍線＝光路；紅虛線＝條件不符才回查。FT＝傅立葉轉換；L 的編號沿用舊章。</text>
<text x="50" y="2698" font-size="20" font-weight="400" fill="#61717a">原題：ch30 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

[[藥物分析_拉曼光譜_分析全流程母圖_v3_0.svg|開啟獨立 SVG]]

圖源：`藥物分析_拉曼光譜_分析全流程母圖_v3_0.svg`。文字等價：先定目的 → 相容取樣與作用 → 正確讀位移／強度 → 比參考或有效校正；合格便交出。

## 先成功一次：1000 cm⁻¹ 到底是什麼？

^rm-c-basic

**自編完整基本例：**用波長 500 nm 的雷射照樣品，某振動的 Stokes 位移是 +1000 cm⁻¹。要問的是「散射光在哪裡，圖上的 1000 又代表什麼？」已知真空波長換算：波數 cm⁻¹＝10⁷／波長 nm。

| 步驟 | 實際動筆 |
|---|---|
| M01 問題 | 求散射光的絕對位置，並辨 Raman 圖上的位移；未問含量。 |
| M02 留條件 | 同模式、同物態；Stokes 是分子得能、光子失能。 |
| M03 整理輸入 | 入射波數＝10⁷／500＝20000 cm⁻¹。 |
| 用 L1／L4 | 散射波數＝20000−1000＝19000 cm⁻¹。 |
| 算絕對波長 | λₛ＝10⁷／19000＝10000／19 nm；19×526＝9994，所以約 526.3 nm。 |
| M04 核對 | 散射光比 500 nm 長波，符合 Stokes；Raman 圖的峰仍標 +1000 cm⁻¹。 |

**這裡 1000 是差值，19000 才是散射光的絕對波數。** 不能把位移單獨取倒數就當成散射光波長。紙筆完整推導見 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc2|C2]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc4|C4]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-basic|閉卷重做基本例]]。

## Part I｜先分開五種量

^rm-c-symbols


|符號／專名|意思|單位與防錯|
|---|---|---|
|λ₀、λₛ|激發光、散射光的絕對波長|nm；兩者皆不是位移。|
|ν̃₀、ν̃ₛ|兩束光的波數，為波長倒數|cm⁻¹；和頻率ν(Hz)不同。|
|Δν̃|Raman位移＝入射波數−散射波數|cm⁻¹；先定正負慣例。|
|ΔE|指定振動能量間距，取正的大小|J等能量單位；能量帳的末減初可正可負。|
|Q、μ、α|正常振動座標／偶極矩／極化率|選擇律問沿Q改變時μ或α有無變化。|
|S、C|分析訊號、濃度或含量|不可把峰高直接視為mg；C要寫清濃度基準。|
|T、kB|熱力學溫度／波茲曼常數|人口比公式T用K；本章只判方向。|


### 最小工具與正式縮寫

^rm-c-definitions

位移（Raman shift）是兩束光的波數差；頻率 frequency 用 Hz，波數 wavenumber 用 cm⁻¹，波長 wavelength 用 nm 等長度單位。橫軸位置和縱軸強度要分開。

IR（infrared spectroscopy，紅外光譜）量振動吸收；NIR（near-infrared，近紅外）是波段；FT（Fourier transform，傅立葉轉換）是將干涉圖還原成頻譜的處理方式。FT-Raman 和色散式是取得同一類 Raman 訊號的不同配置。

本章比較／操作縮寫：UV-Vis（ultraviolet-visible spectroscopy，紫外／可見光譜）；AAS（atomic absorption spectroscopy，原子吸收光譜）；AES（atomic emission spectroscopy，原子放射光譜）；MS（mass spectrometry，質譜）；LC-MS/MS（liquid chromatography–tandem mass spectrometry，液相層析串聯質譜）；NMR（nuclear magnetic resonance，核磁共振）；XRD（X-ray diffraction，X 射線繞射）。CCD（charge-coupled device，電荷耦合元件）是偵測器；API（active pharmaceutical ingredient，藥物有效成分）是樣品成分。

晶型比較會遇到：NIRA（near-infrared analysis，近紅外分析）；ATR（attenuated total reflection，衰減全反射）；DRIFT（diffuse reflectance infrared Fourier transform，漫反射紅外）；Mull（糊漿製樣）；KBr pellet（溴化鉀壓錠）。前三種與製樣層次不同，不能全部當成互斥的整套方法。

**先知道：**吸收量入射光被移除的程度；散射觀察光被重新導向。Raman屬非彈性散射，典型螢光來自真實激發態放射；不能單靠偵測器擺在哪邊替機制定義。
[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-loops|返回複習]]

## Part II｜十條小循環

^rm-c-loops

### 六個存檔點｜先叫回一句話

^rm-c-groups

| 組 | 先叫回一句話 | 所有 L |
|---|---|---|
| A 先讀對位移 | 位移是波數差；要算散射波長，還需雷射位置。 | [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4\|L4]] |
| B 光與分子的能量帳 | 先分誰得能；虛擬態不存真實激發人口。 | [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l1\|L1]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l2\|L2]] |
| C 哪個振動會有峰 | Raman 看極化率變化；IR 看偶極矩變化。 | [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3\|L3]] |
| D 取樣與固態 | 先確認照到誰；晶型比較要保留原固態。 | [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7\|L7]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l8\|L8]] |
| E 背景與光路 | 壓 Rayleigh、處理螢光，最後比較實際訊噪。 | [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l5\|L5]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6\|L6]] |
| F 峰強、人口與結論 | 峰高會受條件影響；含量要校正、溫度要校正。 | [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9\|L9]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l10\|L10]] |

第一輪先 A → B → C，再讀 D／E，最後 F 核對結論。這是建議閱讀順序；各 L 是依問題取用的模組，並未把平行作用硬排成物理串流。


### L1｜光子與分子互相交換能量

^rm-c-l1

**先問：**Stokes 光子失去能量時，分子如何改變？散射波長朝哪邊走？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02\|M02 入口]] | 入射光能量＋分子初末振動態 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03\|M03 出口]] | 散射光的能量、方向與有號位移 |

**短鏈：**分子得能 → 光子失能 → Stokes 長波；分子失能 → 光子得能 → anti-Stokes 短波。

**白話理由：**總能量守恆。光子少掉的能量交給分子；分子交出的能量加到光子。光子能量越低，波長越長。

**立即用一次：**雷射波數 20000 cm⁻¹、模式間距 1000 cm⁻¹：Stokes 散射波數 19000，anti-Stokes 為 21000 cm⁻¹。

**條件／易錯：**同一雷射、同一模式；anti-Stokes 需初始高振動態。

<details>
<summary>閉卷自問｜Stokes 光子失去能量時，分子如何改變？散射波長朝哪邊走？</summary>

分子得到振動能，光子能量下降；散射波長比雷射長。

短鏈：分子得能 → 光子失能 → Stokes 長波；分子失能 → 光子得能 → anti-Stokes 短波。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

能量守恆寫成 E₀+E分子初=Eₛ+E分子末。Rayleigh scattering（瑞利散射）前後分子能量相同，Eₛ=E₀。Stokes scattering（斯托克斯散射）留下較高振動能，Eₛ=E₀−ΔE；anti-Stokes scattering（反斯托克斯散射）釋出原有振動能，Eₛ=E₀+ΔE。因E=hc₀/λ，光子能量與波長方向相反。

Raman包括Stokes及anti-Stokes，不只「光少了能量」。散射光可由不同方向收集，不能一律稱彈回來。這裡先教振動Raman，不展開轉動Raman。

</details>

原題入口：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q1|Q01]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q7|Q07]]。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f1|F01]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f3|F03]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc2|C2]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l1|同號 R-L1 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03|交回結果的站]]。

### L2｜虛擬態不等於螢光的真實激發態

^rm-c-l2

**先問：**有誘導偶極，是否每個振動都一定 Raman 活性？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02\|M02 入口]] | 光的電場＋分子對外場的響應 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03\|M03 出口]] | 散射機制與螢光的分界 |

**短鏈：**外加電場 → 誘導偶極 → 散射響應 → 交換振動能時出現 Raman。

**白話理由：**光的電場可暫時改變分子的電荷分布。能階圖的虛擬態只是描述散射過程，不是先存人口再等待放光。

**立即用一次：**樣品沒有在雷射波長出現明顯電子吸收，仍可能有 Raman；但某振動能否有峰還要檢查 L3。

**條件／易錯：**一般非共振自發 Raman；共振時另看電子躍遷。

<details>
<summary>閉卷自問｜有誘導偶極，是否每個振動都一定 Raman 活性？</summary>

不一定；還需該正常振動使極化率改變。虛擬態也不能當成螢光的真實電子激發態。

短鏈：外加電場 → 誘導偶極 → 散射響應 → 交換振動能時出現 Raman。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

Polarizability（極化率）α描述電子雲對外場的可變形程度；簡式 $p_{ind}=\alpha\mathcal E$ 描述 Induced dipole（誘導偶極）；此處 $\mathcal E$ 是電場，不是光子能量 E。Virtual state（虛擬態）是散射計算及能階示意的中間標記，不是先儲存人口、等一會才放光的真實定態。一般Raman不要求分析物先在該激發波長產生真實電子吸收。

不需特定電子吸收發色團，不代表任一振動都活性，也不代表訊號都強。Resonance Raman（共振拉曼）在接近電子躍遷時可增強，因此「Raman強度永遠與吸收帶無關」不正確。

</details>

原題入口：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q1|Q01]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q7|Q07]]。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f1|F01]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f4|F04]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l2|同號 R-L2 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03|交回結果的站]]。

### L3｜用極化率與偶極矩分開Raman及IR

^rm-c-l3

**先問：**某模式 Raman 有峰，IR 是否必定沒有峰？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02\|M02 入口]] | 同一正常振動沿 Q 的 α／μ 變化 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03\|M03 出口]] | 哪些模式可產生 Raman 或 IR 訊號 |

**短鏈：**沿振動檢查 α／μ → 判 Raman／IR 活性 → 得到可比較的模式資訊。

**白話理由：**IR 問振動是否改變電荷分離；Raman 問振動是否改變外場使電子雲變形的程度。兩個問題不同，所以兩張譜可互補。

**立即用一次：**N₂ 的伸縮不產生偶極矩變化，卻可改變極化率：基本振動可 Raman 活性而 IR 不活性。

**條件／易錯：**基本振動近似；嚴格互斥須反演中心。

<details>
<summary>閉卷自問｜某模式 Raman 有峰，IR 是否必定沒有峰？</summary>

不一定。具有反演中心時，基本振動才適用 IR／Raman 互斥；互補不是無條件全峰相反。

短鏈：沿振動檢查 α／μ → 判 Raman／IR 活性 → 得到可比較的模式資訊。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

Dipole moment（偶極矩）μ回答電荷分離狀態；α回答外場多容易扭動電子雲。IR條件為(∂μ/∂Q)₀≠0；Raman條件為極化率張量至少一項(∂α/∂Q)₀≠0。不要怕偏微分：只是在問「沿這個振動方向，這個量有沒有變」。同核雙原子分子的伸縮可改α而不改μ，是Raman活性／IR不活性的清楚例子。

「對稱找Raman、不對稱找IR」是考題入口，不是所有模式的強弱定律。具有反演中心時，基本振動的IR與Raman活性遵守Mutual exclusion rule（互斥規則）；沒有此前提，同一模式可以兩者皆活性，也可能兩者都不活性。IR也不需UV-Vis發色團，這不是兩者差別。

</details>

原題入口：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q1|Q01]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q2|Q02]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q6|Q06]]。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f5|F05]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f10|F10]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l3|同號 R-L3 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03|交回結果的站]]。

### L4｜換雷射改變絕對波長，位移仍對準振動

^rm-c-l4

**先問：**位移 1000 cm⁻¹ 能否單獨換成散射光 10000 nm？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03\|M03 入口]] | 雷射／散射位置、軸名與單位 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m04\|M04 出口]] | 有號位移與可比的峰位置 |

**短鏈：**先辨量 → 各波長取倒數 → 入射減散射 → 核對振動位移。

**白話理由：**同一振動要求固定能量差。改雷射會搬動入射與散射的絕對位置，但兩束光的波數差仍可對準同一模式。

**立即用一次：**500 nm 雷射產生約 526.3 nm Stokes；換成 800 nm 時約 869.6 nm。兩次位移均為 +1000 cm⁻¹。

**條件／易錯：**物態、模式、溫度不變；峰位校正正確。

<details>
<summary>閉卷自問｜位移 1000 cm⁻¹ 能否單獨換成散射光 10000 nm？</summary>

不能；1000 是兩束光的波數差，還缺雷射的絕對位置。10000 nm 只是把 1000 cm⁻¹ 當絕對波數取倒數的結果。

短鏈：先辨量 → 各波長取倒數 → 入射減散射 → 核對振動位移。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

Raman shift（拉曼位移）定義為Δν̃=ν̃₀−ν̃ₛ，常用cm⁻¹。Stokes為正，anti-Stokes為負。橫軸是相對雷射的波數差；IR的波數軸通常是吸收光本身的波數。兩者同單位，所標的量不同。

近似不變的是同一模式的位移位置，不是整張圖。雷射改變會改強度、螢光背景、穿透及共振條件；加熱或樣品狀態改變也可改峰位。原始散射資料可用nm表示，只是本題標準Raman圖譜橫軸用cm⁻¹位移。

</details>

原題入口：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q1|Q01]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q6|Q06]]。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f6|F06]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f7|F07]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc1|C1]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc2|C2]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc3|C3]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc4|C4]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l4|同號 R-L4 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m04|交回結果的站]]。

### L5｜先壓低彈性散射，再分辨微弱Raman

^rm-c-l5

**先問：**濾片把雷射附近切得更乾淨，可能同時失去什麼？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02\|M02 入口]] | 收集光＋Rayleigh 濾片截止範圍 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03\|M03 出口]] | 背景較可控的訊號與實際可見位移區間 |

**短鏈：**強彈性光壓住弱峰 → 匹配抑制濾片 → 取得可用 Raman 譜窗。

**白話理由：**很強的雷射同波長散射會占用量測範圍，弱 Raman 容易被遮住。濾掉它有助讀峰，但雷射附近的低頻 Raman 也可能一起被切掉。

**立即用一次：**想比較低頻晶格峰，卻使用截止太遠的濾片：沒看到峰，不能直接判樣品沒有該模式。

**條件／易錯：**確認濾片截止與 Stokes／anti-Stokes 可見側。

<details>
<summary>閉卷自問｜濾片把雷射附近切得更乾淨，可能同時失去什麼？</summary>

近零位移的低頻 Raman；依濾片配置也可能只留下其中一側。Rayleigh 濾片不保證去掉螢光。

短鏈：強彈性光壓住弱峰 → 匹配抑制濾片 → 取得可用 Raman 譜窗。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

Rayleigh是同頻率的彈性散射；Raman是有頻移的非彈性散射。Tyndall effect（廷得耳效應）常指膠體／較大粒子造成可見散射，屬粒徑及散射表現的描述，與前兩者不完全是同一分類軸。Edge filter（邊緣濾光片）常保留一側；Notch filter（陷波濾光片）可抑制雷射附近而保留兩側，依型號而定。

Rayleigh不限溶劑分子，Raman也可來自分析物、溶劑與固體。113-1題本用「Raman較弱」判A錯，但不能為所有樣品硬排Rayleigh、Tyndall、Raman的固定強度全序。濾光片也可能截去靠近零位移的低頻訊號；無法把螢光一律全濾掉。

</details>

原題入口：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q2|Q02]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q3|Q03]]。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f2|F02]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f9|F09]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l5|同號 R-L5 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03|交回結果的站]]。

### L6｜調雷射波長，是背景與訊號的取捨

^rm-c-l6

**先問：**近紅外下峰變弱、背景降更多，量測一定變差嗎？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02\|M02 入口]] | 激發波長、匹配光學與樣品背景 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03\|M03 出口]] | 可用量測條件與其代價 |

**短鏈：**改激發 → 背景與 Raman 效率皆改 → 匹配光學／偵測 → 比實際訊噪。

**白話理由：**較長波激發可避開許多螢光激發，但非共振 Raman 散射通常也會變弱。訊號弱不等於結果更差，要看背景、雜訊與可用峰一起變多少。

**立即用一次：**換近紅外後峰降低，背景降得更多，峰反而可辨。題本接受 450–800 nm，但實際還有 1064 nm 配置。

**條件／易錯：**固定目的與樣品；避免加熱改樣；重新匹配元件。

<details>
<summary>閉卷自問｜近紅外下峰變弱、背景降更多，量測一定變差嗎？</summary>

不一定；應比較實際訊噪、光譜品質與樣品穩定性，不只比較峰高。

短鏈：改激發 → 背景與 Raman 效率皆改 → 匹配光學／偵測 → 比實際訊噪。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

Near-infrared（近紅外）激發常能減少許多有機樣品的螢光。背景降低有利看峰，但近似非共振模型中散射強度帶有散射頻率四次方因子，波長拉長一般使Raman變弱。波長也影響焦斑、偵測效率與熱負荷；不能只比較雷射亮度。

NIR不是「保證所有螢光都消失」，也不是所有螢光物質保證測得好。450–800 nm是112-2題本接受的範圍敘述，不是Raman全部光源範圍；常見另有1064 nm、也有UV配置。

</details>

原題入口：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q3|Q03]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q6|Q06]]。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f7|F07]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f8|F08]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f9|F09]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l6|同號 R-L6 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03|交回結果的站]]。

### L7｜取樣與包裝決定你到底量到誰

^rm-c-l7

**先問：**一點有有效成分峰，能推出整錠含量均勻嗎？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m01\|M01 入口]] | 分析目的、包裝與樣品不均勻性 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02\|M02 出口]] | 背景對照與代表性取樣方案 |

**短鏈：**辨背景材料／取樣深度 → 選空白與多點計畫 → 取得代表性檢品。

**白話理由：**光會先遇包裝，也可能只聚焦在一顆賦形劑粒子。量到某點的訊號只代表那個量測體積，必須先決定如何代表整錠或整批。

**立即用一次：**錠劑某點只有賦形劑峰，換點才見有效成分；這不直接證明整錠沒有藥，也不直接證明含量均勻。

**條件／易錯：**包裝須適用；照射功率／時間不改樣。

<details>
<summary>閉卷自問｜一點有有效成分峰，能推出整錠含量均勻嗎？</summary>

不能；需要代表性多點或映射與適當驗證。包裝及溶劑也須有背景對照。

短鏈：辨背景材料／取樣深度 → 選空白與多點計畫 → 取得代表性檢品。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

固體常可少前處理直測；合適包裝可透光，但包裝本身也會貢獻訊號。溶液可以量Raman；溶劑的峰及螢光可能重疊，需溶劑空白與合適濃度。小焦斑能看局部，也可能只照到一粒賦形劑，不能直接代表整錠。

「可穿透包裝」不代表任何材質、厚度與顏色都可；「非破壞」也需功率與照射時間不改樣。IR可用ATR直接測固體，不能為凸顯Raman而寫所有IR都必須壓片。

</details>

原題入口：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q3|Q03]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q4|Q04]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q5|Q05]]。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f11|F11]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f15|F15]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l7|同號 R-L7 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m01|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02|交回結果的站]]。

### L8｜保留固態，才能比較晶型環境

^rm-c-l8

**先問：**雷射把樣品改成另一晶型，量到的譜還能代表原樣嗎？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03\|M03 入口]] | 可比固態譜＋製樣／照射紀錄 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m04\|M04 出口]] | 附製樣條件的晶型判讀及限制 |

**短鏈：**先查原固態是否保留 → 比峰群與參考 → 區分環境與化學組成 → 支持晶型結論。

**白話理由：**晶型是同分子不同晶格排列。溶解會失去原晶格；雷射加熱或製樣也可能改掉要鑑別的固態，所以先確認測到原樣。

**立即用一次：**同化合物兩個粉末譜不同，溶解後相同：可支持固態環境差異，但晶型指認還需參考與其他證據。

**條件／易錯：**同化合物、可比條件；防研磨／壓力／濕氣／加熱改樣。

<details>
<summary>閉卷自問｜雷射把樣品改成另一晶型，量到的譜還能代表原樣嗎？</summary>

不能。要修正量測條件並重新確認原固態；不是先把變化當原晶型證據。

短鏈：先查原固態是否保留 → 比峰群與參考 → 區分環境與化學組成 → 支持晶型結論。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

Polymorph（多晶型）是同化合物的不同結晶排列；多晶型性不等於只要很多晶粒的「多晶」。低頻晶格振動亦可提供資訊，Raman位移不只侷限中紅外常見官能基區。XRD（X射線繞射）、適當IR、solid-state NMR（固態核磁共振）等也能提供固態資訊。

溶解常丟失原晶格；加壓、研磨、濕氣或雷射加熱可能改樣。KBr壓錠法在題本解析被排除，是前處理可能改樣的提醒，不是每次加壓都必然轉晶、也不是KBr物理上永不可能研究晶型。Raman、XRD、IR沒有跨所有樣品的固定靈敏度排名。

</details>

原題入口：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q2|Q02]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q4|Q04]]。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f12|F12]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f13|F13]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l8|同號 R-L8 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m04|交回結果的站]]。

### L9｜峰能辨識身分，定量還需要校正與取樣

^rm-c-l9

**先問：**同含量樣品換焦點後峰變高，能說含量增加嗎？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03\|M03 入口]] | 處理後訊號 S＋參考含量 C＋校正條件 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m04\|M04 出口]] | 有校正基準與適用範圍的含量 |

**短鏈：**固定條件 → 對照標準響應 → 查適用範圍／驗證 → 才報含量。

**白話理由：**峰高不只隨含量改變，光路、焦點、背景與樣品不均勻都會影響。只有把這些條件固定並建立可靠校正，才可把訊號換成含量。

**立即用一次：**10% 標準得 20 a.u.、20% 得 40 a.u.；在已驗證線性區間，未知 30 a.u. 內插得 15% w/w。

**條件／易錯：**功率、聚焦、基質、取樣與處理相符；驗證有效。

<details>
<summary>閉卷自問｜同含量樣品換焦點後峰變高，能說含量增加嗎？</summary>

不能；焦點是改變的條件，先查取樣與量測。FT 和色散式都不會自動提供有效校正。

短鏈：固定條件 → 對照標準響應 → 查適用範圍／驗證 → 才報含量。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

峰位與峰群常用於指紋；峰面積或多變量模型可用於定量。樣品粗糙度、粒徑、聚焦、螢光背景、功率漂移都會改訊號，所以不能只把峰高直接當毫克數。色散式與FT-Raman皆可在合適方法下定量。傅立葉轉換只是取得頻譜的運算，不會自動修好上述偏差。

110-1選C、104-1選B是題本比較；109-1選B、113-1接受FT-Raman定量。不能把它們串成「只有FT-Raman測制酸錠才可定量」。制酸錠的Glycine（甘胺酸）與Calcium carbonate（碳酸鈣）是要記的指定例，不是唯一可能。

</details>

原題入口：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q4|Q04]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q5|Q05]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q8|Q08]]。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f14|F14]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc5|C5]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l9|同號 R-L9 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m04|交回結果的站]]。

### L10｜anti-Stokes較弱，先看振動態人口

^rm-c-l10

**先問：**兩側位移絕對值相同，是否代表峰高相同？

| 入口／出口 | 帶進或交出什麼？ |
|---|---|
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02\|M02 入口]] | 振動間距 ΔE、溫度 T 與熱平衡人口 |
| [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03\|M03 出口]] | 兩側訊號的相對趨勢與需校正的項目 |

**短鏈：**T 升高 → 高振動態人口增加 → anti-Stokes 可出發者變多 → 相對訊號可增加。

**白話理由：**anti-Stokes 要從較高振動態出發。一般溫度下這種分子較少，所以訊號常弱；升溫提高人口比例，但峰高還受頻率與儀器響應影響。

**立即用一次：**只提高溫度而樣品未變性、激發與響應可比：anti-Stokes 相對 Stokes 通常增加；不能用未校正峰高直接報溫度。

**條件／易錯：**熱平衡、同模式與可比響應；T 用 K。

<details>
<summary>閉卷自問｜兩側位移絕對值相同，是否代表峰高相同？</summary>

不代表；初始人口、散射頻率與儀器響應不同。

短鏈：T 升高 → 高振動態人口增加 → anti-Stokes 可出發者變多 → 相對訊號可增加。

</details>

<details>
<summary>正式名詞與成立邊界</summary>

Stokes可由低振動態出發；anti-Stokes需要先有振動能可交還光子。人口比可由Boltzmann（波茲曼）關係N₁/N₀=exp[−ΔE/(kBT)]理解，這裡只讀方向，不要求無計算機算指數。兩邊強度比還受頻率因子、收集光學及偵測響應影響。

不能只靠未校正的兩峰高度精確讀溫度；同一模式的兩側位移絕對值相同，也不代表兩峰等高。本節為能量圖的補鏈，非附件獨立考題。

</details>

來源身分：L10 是自編補鏈；附件沒有獨立人口比題。

相關固定輸入／紙筆：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f3|F03]]。

回跳：[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l10|同號 R-L10 閉卷卡]]；[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m02|大循環入口]] → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-m03|交回結果的站]]。

### 圖2｜小循環掛載與能階圖

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="4240" viewBox="0 0 1900 4240" role="img" aria-labelledby="rm3_g2_title rm3_g2_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="rm3_g2_title">拉曼光譜｜小循環掛載與能階圖</title><desc id="rm3_g2_desc">拉曼光譜教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊，藍線表示光路；能階子圖另標藍線為能量帳。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="4240" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH30 / RAMAN / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">拉曼光譜｜小循環掛載與能階圖</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">全部 10 條 L 各有一個主要位置：入口／實際輸入 → 短鏈 → 出口／交回結果。</text>
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
<rect x="50" y="370" width="570" height="1170" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="412" font-size="27" font-weight="600" fill="#9e771c">A｜先讀對位移</text>
<text x="72" y="455" font-size="23" font-weight="400" fill="#24343f">位移是波數差；要算散射波長，還需雷射位置。</text>
<rect x="68" y="530" width="534" height="440" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="85" y="565" font-size="25" font-weight="600" fill="#9e771c">L4｜位移不是絕對波長</text>
<text x="85" y="608" font-size="22" font-weight="400" fill="#24343f">入口 M03｜雷射／散射位置、軸名與單位</text>
<text x="85" y="694" font-size="23" font-weight="400" fill="#24343f">先辨量 → 各波長取倒數 → 入射減散射 → 核對振</text>
<text x="85" y="726.66" font-size="23" font-weight="400" fill="#24343f">動位移</text>
<text x="85" y="832" font-size="22" font-weight="400" fill="#9e771c">出口 M04｜有號位移與可比的峰位置</text>
<text x="85" y="916" font-size="21" font-weight="400" fill="#61717a">條件：物態、模式、溫度不變；峰位校正正確。</text>
<rect x="68" y="1050" width="534" height="420" rx="18" fill="#fff" stroke="#9e771c" stroke-width="2"/>
<text x="90" y="1091" font-size="27" font-weight="600" fill="#9e771c">把這組立即用一次</text>
<text x="90" y="1138" font-size="24" font-weight="400" fill="#24343f">500 nm 入射、+1000 cm⁻¹ 位移：</text>
<text x="90" y="1172.08" font-size="24" font-weight="400" fill="#24343f">20000−1000=19000 cm⁻¹</text>
<text x="90" y="1206.16" font-size="24" font-weight="400" fill="#24343f">λₛ=10000/19≈526.3 nm。</text>
<text x="90" y="1240.24" font-size="24" font-weight="400" fill="#24343f">1000 是差值，不能直接當散射波數。</text>
<rect x="670" y="370" width="570" height="1170" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="692" y="412" font-size="27" font-weight="600" fill="#286c68">B｜光與分子的能量帳</text>
<text x="692" y="455" font-size="23" font-weight="400" fill="#24343f">先分誰得能；虛擬態不存真實激發人口。</text>
<rect x="688" y="530" width="534" height="440" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="705" y="565" font-size="25" font-weight="600" fill="#286c68">L1｜誰得能、誰失能</text>
<text x="705" y="608" font-size="22" font-weight="400" fill="#24343f">入口 M02｜入射光能量＋分子初末振動態</text>
<text x="705" y="694" font-size="23" font-weight="400" fill="#24343f">分子得能 → 光子失能 → Stokes 長波；分子失能 </text>
<text x="705" y="726.66" font-size="23" font-weight="400" fill="#24343f">→ 光子得能 → anti-Stokes 短波</text>
<text x="705" y="832" font-size="22" font-weight="400" fill="#286c68">出口 M03｜散射光的能量、方向與有號位移</text>
<text x="705" y="916" font-size="21" font-weight="400" fill="#61717a">條件：同一雷射、同一模式；anti-Stokes 需初始高振</text>
<text x="705" y="945.82" font-size="21" font-weight="400" fill="#61717a">動態。</text>
<rect x="688" y="1000" width="534" height="440" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="705" y="1035" font-size="25" font-weight="600" fill="#286c68">L2｜虛擬態與真實激發</text>
<text x="705" y="1078" font-size="22" font-weight="400" fill="#24343f">入口 M02｜光的電場＋分子對外場的響應</text>
<text x="705" y="1164" font-size="23" font-weight="400" fill="#24343f">外加電場 → 誘導偶極 → 散射響應 → 交換振動能</text>
<text x="705" y="1196.66" font-size="23" font-weight="400" fill="#24343f">時出現 Raman</text>
<text x="705" y="1302" font-size="22" font-weight="400" fill="#286c68">出口 M03｜散射機制與螢光的分界</text>
<text x="705" y="1386" font-size="21" font-weight="400" fill="#61717a">條件：一般非共振自發 Raman；共振時另看電</text>
<text x="705" y="1415.82" font-size="21" font-weight="400" fill="#61717a">子躍遷。</text>
<rect x="1290" y="370" width="570" height="1170" rx="18" fill="#dcecdc" stroke="#356844" stroke-width="2"/>
<text x="1312" y="412" font-size="27" font-weight="600" fill="#356844">C｜哪個振動會有峰</text>
<text x="1312" y="455" font-size="23" font-weight="400" fill="#24343f">Raman 看極化率變化；IR 看偶極矩變化。</text>
<rect x="1308" y="530" width="534" height="440" rx="18" fill="#fff" stroke="#356844" stroke-width="2"/>
<text x="1325" y="565" font-size="25" font-weight="600" fill="#356844">L3｜極化率與偶極矩</text>
<text x="1325" y="608" font-size="22" font-weight="400" fill="#24343f">入口 M02｜同一正常振動沿 Q 的 α／μ 變化</text>
<text x="1325" y="694" font-size="23" font-weight="400" fill="#24343f">沿振動檢查 α／μ → 判 Raman／IR 活性 → 得到</text>
<text x="1325" y="726.66" font-size="23" font-weight="400" fill="#24343f">可比較的模式資訊</text>
<text x="1325" y="832" font-size="22" font-weight="400" fill="#356844">出口 M03｜哪些模式可產生 Raman 或 IR 訊號</text>
<text x="1325" y="916" font-size="21" font-weight="400" fill="#61717a">條件：基本振動近似；嚴格互斥須反演中心。</text>
<rect x="1308" y="1050" width="534" height="420" rx="18" fill="#fff" stroke="#356844" stroke-width="2"/>
<text x="1330" y="1091" font-size="27" font-weight="600" fill="#356844">把這組立即用一次</text>
<text x="1330" y="1138" font-size="24" font-weight="400" fill="#24343f">N₂ 伸縮可改 α 而不改 μ：</text>
<text x="1330" y="1172.08" font-size="24" font-weight="400" fill="#24343f">Raman 可活性，基本 IR 不活性。</text>
<text x="1330" y="1206.16" font-size="24" font-weight="400" fill="#24343f">只有具反演中心等前提，基本振動才嚴</text>
<text x="1330" y="1240.24" font-size="24" font-weight="400" fill="#24343f">格互斥。</text>
<text x="1330" y="1274.32" font-size="24" font-weight="400" fill="#24343f">互補不等於全峰強弱相反。</text>
<rect x="50" y="1580" width="570" height="1170" rx="18" fill="#e8e1f2" stroke="#685185" stroke-width="2"/>
<text x="72" y="1622" font-size="27" font-weight="600" fill="#685185">D｜取樣與固態</text>
<text x="72" y="1665" font-size="23" font-weight="400" fill="#24343f">先確認照到誰；晶型比較要保留原固態。</text>
<rect x="68" y="1740" width="534" height="440" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="85" y="1775" font-size="25" font-weight="600" fill="#685185">L7｜實際照到誰</text>
<text x="85" y="1818" font-size="22" font-weight="400" fill="#24343f">入口 M01｜分析目的、包裝與樣品不均勻性</text>
<text x="85" y="1904" font-size="23" font-weight="400" fill="#24343f">辨背景材料／取樣深度 → 選空白與多點計畫 → </text>
<text x="85" y="1936.66" font-size="23" font-weight="400" fill="#24343f">取得代表性檢品</text>
<text x="85" y="2042" font-size="22" font-weight="400" fill="#685185">出口 M02｜背景對照與代表性取樣方案</text>
<text x="85" y="2126" font-size="21" font-weight="400" fill="#61717a">條件：包裝須適用；照射功率／時間不改樣。</text>
<rect x="68" y="2210" width="534" height="440" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="85" y="2245" font-size="25" font-weight="600" fill="#685185">L8｜固態不能先被改掉</text>
<text x="85" y="2288" font-size="22" font-weight="400" fill="#24343f">入口 M03｜可比固態譜＋製樣／照射紀錄</text>
<text x="85" y="2374" font-size="23" font-weight="400" fill="#24343f">先查原固態是否保留 → 比峰群與參考 → 區分環</text>
<text x="85" y="2406.66" font-size="23" font-weight="400" fill="#24343f">境與化學組成 → 支持晶型結論</text>
<text x="85" y="2512" font-size="22" font-weight="400" fill="#685185">出口 M04｜附製樣條件的晶型判讀及限制</text>
<text x="85" y="2596" font-size="21" font-weight="400" fill="#61717a">條件：同化合物、可比條件；防研磨／壓力／濕氣／</text>
<text x="85" y="2625.82" font-size="21" font-weight="400" fill="#61717a">加熱改樣。</text>
<rect x="670" y="1580" width="570" height="1170" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="692" y="1622" font-size="27" font-weight="600" fill="#326991">E｜背景與光路</text>
<text x="692" y="1665" font-size="23" font-weight="400" fill="#24343f">壓 Rayleigh、處理螢光，最後比較實際訊噪。</text>
<rect x="688" y="1740" width="534" height="440" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="705" y="1775" font-size="25" font-weight="600" fill="#326991">L5｜壓彈性光、留可用峰</text>
<text x="705" y="1818" font-size="22" font-weight="400" fill="#24343f">入口 M02｜收集光＋Rayleigh 濾片截止範圍</text>
<text x="705" y="1904" font-size="23" font-weight="400" fill="#24343f">強彈性光壓住弱峰 → 匹配抑制濾片 → 取得可用 </text>
<text x="705" y="1936.66" font-size="23" font-weight="400" fill="#24343f">Raman 譜窗</text>
<text x="705" y="2042" font-size="22" font-weight="400" fill="#326991">出口 M03｜背景較可控的訊號與實際可見位移區間</text>
<text x="705" y="2126" font-size="21" font-weight="400" fill="#61717a">條件：確認濾片截止與 Stokes／anti-Stokes 可見側。</text>
<rect x="688" y="2210" width="534" height="440" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="705" y="2245" font-size="25" font-weight="600" fill="#326991">L6｜波長與訊噪的取捨</text>
<text x="705" y="2288" font-size="22" font-weight="400" fill="#24343f">入口 M02｜激發波長、匹配光學與樣品背景</text>
<text x="705" y="2374" font-size="23" font-weight="400" fill="#24343f">改激發 → 背景與 Raman 效率皆改 → 匹配光學／</text>
<text x="705" y="2406.66" font-size="23" font-weight="400" fill="#24343f">偵測 → 比實際訊噪</text>
<text x="705" y="2512" font-size="22" font-weight="400" fill="#326991">出口 M03｜可用量測條件與其代價</text>
<text x="705" y="2596" font-size="21" font-weight="400" fill="#61717a">條件：固定目的與樣品；避免加熱改樣；重新匹配元</text>
<text x="705" y="2625.82" font-size="21" font-weight="400" fill="#61717a">件。</text>
<rect x="1290" y="1580" width="570" height="1170" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="1312" y="1622" font-size="27" font-weight="600" fill="#b72d4a">F｜峰強、人口與結論</text>
<text x="1312" y="1665" font-size="23" font-weight="400" fill="#24343f">峰高會受條件影響；含量要校正、溫度要校正。</text>
<rect x="1308" y="1740" width="534" height="440" rx="18" fill="#fff" stroke="#b72d4a" stroke-width="2"/>
<text x="1325" y="1775" font-size="25" font-weight="600" fill="#b72d4a">L9｜含量要校正與驗證</text>
<text x="1325" y="1818" font-size="22" font-weight="400" fill="#24343f">入口 M03｜處理後訊號 S＋參考含量 C＋校正條件</text>
<text x="1325" y="1904" font-size="23" font-weight="400" fill="#24343f">固定條件 → 對照標準響應 → 查適用範圍／驗證 </text>
<text x="1325" y="1936.66" font-size="23" font-weight="400" fill="#24343f">→ 才報含量</text>
<text x="1325" y="2042" font-size="22" font-weight="400" fill="#b72d4a">出口 M04｜有校正基準與適用範圍的含量</text>
<text x="1325" y="2126" font-size="21" font-weight="400" fill="#61717a">條件：功率、聚焦、基質、取樣與處理相符；驗證有</text>
<text x="1325" y="2155.82" font-size="21" font-weight="400" fill="#61717a">效。</text>
<rect x="1308" y="2210" width="534" height="440" rx="18" fill="#fff" stroke="#b72d4a" stroke-width="2"/>
<text x="1325" y="2245" font-size="25" font-weight="600" fill="#b72d4a">L10｜人口不等於峰高</text>
<text x="1325" y="2288" font-size="22" font-weight="400" fill="#24343f">入口 M02｜振動間距 ΔE、溫度 T 與熱平衡人口</text>
<text x="1325" y="2374" font-size="23" font-weight="400" fill="#24343f">T 升高 → 高振動態人口增加 → anti-Stokes 可出</text>
<text x="1325" y="2406.66" font-size="23" font-weight="400" fill="#24343f">發者變多 → 相對訊號可增加</text>
<text x="1325" y="2512" font-size="22" font-weight="400" fill="#b72d4a">出口 M03｜兩側訊號的相對趨勢與需校正的項目</text>
<text x="1325" y="2596" font-size="21" font-weight="400" fill="#61717a">條件：熱平衡、同模式與可比響應；T 用 K。</text>
<text x="50" y="2820" font-size="29" font-weight="600" fill="#24343f">L1＋L10｜三種能量帳：同一雷射的入射箭頭長度相同</text>
<text x="50" y="2867" font-size="23" font-weight="400" fill="#61717a">虛擬態用點線；不是可儲存人口的真實激發態。anti-Stokes 起點較高，中間標記也相應較高。</text>
<rect x="50" y="2910" width="570" height="660" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="72" y="2953" font-size="28" font-weight="600" fill="#326991">Rayleigh</text>
<polyline points="95,3375 570,3375" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="515" y="3362" font-size="21" font-weight="400" fill="#24343f">v=0</text>
<polyline points="95,3275 570,3275" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="515" y="3262" font-size="21" font-weight="400" fill="#24343f">v=1</text>
<polyline points="95,3135 570,3135" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<text x="92" y="3118" font-size="20" font-weight="400" fill="#61717a">虛擬態標記</text>
<polyline points="240,3375 240,3135" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="240.0,3135.0 246.2,3146.4 233.8,3146.4" fill="#326991"/>
<polyline points="365,3135 365,3375" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="365.0,3375.0 358.8,3363.6 371.2,3363.6" fill="#326991"/>
<text x="255" y="3260" font-size="21" font-weight="400" fill="#326991">入射</text>
<text x="380" y="3280" font-size="21" font-weight="400" fill="#326991">散射</text>
<text x="73" y="3430" font-size="23" font-weight="400" fill="#24343f">分子 v=0 → v=0；Δν̃=0</text>
<text x="73" y="3475" font-size="24" font-weight="400" fill="#326991">Eₛ=E₀；原波長</text>
<rect x="670" y="2910" width="570" height="660" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="692" y="2953" font-size="28" font-weight="600" fill="#326991">Stokes Raman</text>
<polyline points="715,3375 1190,3375" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="1135" y="3362" font-size="21" font-weight="400" fill="#24343f">v=0</text>
<polyline points="715,3275 1190,3275" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="1135" y="3262" font-size="21" font-weight="400" fill="#24343f">v=1</text>
<polyline points="715,3135 1190,3135" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<text x="712" y="3118" font-size="20" font-weight="400" fill="#61717a">虛擬態標記</text>
<polyline points="860,3375 860,3135" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="860.0,3135.0 866.2,3146.4 853.8,3146.4" fill="#326991"/>
<polyline points="985,3135 985,3275" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="985.0,3275.0 978.8,3263.6 991.2,3263.6" fill="#326991"/>
<text x="875" y="3260" font-size="21" font-weight="400" fill="#326991">入射</text>
<text x="1000" y="3180" font-size="21" font-weight="400" fill="#326991">散射</text>
<text x="693" y="3430" font-size="23" font-weight="400" fill="#24343f">分子 v=0 → v=1；Δν̃&gt;0</text>
<text x="693" y="3475" font-size="24" font-weight="400" fill="#326991">Eₛ=E₀−ΔE；長波</text>
<rect x="1290" y="2910" width="570" height="660" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="1312" y="2953" font-size="28" font-weight="600" fill="#326991">anti-Stokes Raman</text>
<polyline points="1335,3375 1810,3375" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="1755" y="3362" font-size="21" font-weight="400" fill="#24343f">v=0</text>
<polyline points="1335,3275 1810,3275" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<text x="1755" y="3262" font-size="21" font-weight="400" fill="#24343f">v=1</text>
<polyline points="1335,3035 1810,3035" fill="none" stroke="#61717a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<text x="1332" y="3018" font-size="20" font-weight="400" fill="#61717a">虛擬態標記</text>
<polyline points="1480,3275 1480,3035" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1480.0,3035.0 1486.2,3046.4 1473.8,3046.4" fill="#326991"/>
<polyline points="1605,3035 1605,3375" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1605.0,3375.0 1598.8,3363.6 1611.2,3363.6" fill="#326991"/>
<text x="1495" y="3160" font-size="21" font-weight="400" fill="#326991">入射</text>
<text x="1620" y="3280" font-size="21" font-weight="400" fill="#326991">散射</text>
<text x="1313" y="3430" font-size="23" font-weight="400" fill="#24343f">分子 v=1 → v=0；Δν̃&lt;0</text>
<text x="1313" y="3475" font-size="24" font-weight="400" fill="#326991">Eₛ=E₀+ΔE；短波</text>
<text x="1313" y="3523" font-size="22" font-weight="400" fill="#b72d4a">需要初始高振動態人口。</text>
<rect x="50" y="3610" width="1800" height="200" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="3651" font-size="27" font-weight="600" fill="#9e771c">文字能量守恆｜光與分子兩邊一起算</text>
<text x="72" y="3698" font-size="24" font-weight="400" fill="#24343f">E₀＋E_i＝Eₛ＋E_f；hc(ν̃₀−ν̃ₛ)＝E_f−E_i。i＝分子初態，f＝分子末態。</text>
<text x="72" y="3732.08" font-size="24" font-weight="400" fill="#24343f">同模式兩側 |Δν̃| 可相同，峰高未必相同：人口、頻率與響應都會影響。</text>
<rect x="50" y="3850" width="1800" height="265" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="72" y="3891" font-size="27" font-weight="600" fill="#61717a">完整示範路線｜自編基本例走完四站</text>
<text x="72" y="3938" font-size="24" font-weight="400" fill="#24343f">M01：問散射位置 → M02：500 nm 雷射、同模式 Stokes 間距 1000 cm⁻¹</text>
<text x="72" y="3972.08" font-size="24" font-weight="400" fill="#24343f">→ M03：20000−1000＝19000 cm⁻¹ → L4：倒數得 λₛ≈526.3 nm</text>
<text x="72" y="4006.16" font-size="24" font-weight="400" fill="#24343f">→ M04：比入射長波，方向符合；圖上的位移仍是＋1000 cm⁻¹。</text>
<text x="50" y="4172" font-size="20" font-weight="400" fill="#61717a">α＝極化率；μ＝偶極矩；Q＝正常振動座標；v＝振動能階標號。藍箭頭表示入射／散射的能量帳，非空間光路。</text>
<text x="50" y="4208" font-size="20" font-weight="400" fill="#61717a">原題：ch30 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

[[藥物分析_拉曼光譜_小循環掛載與能階圖_v3_0.svg|開啟獨立 SVG]]

圖源：`藥物分析_拉曼光譜_小循環掛載與能階圖_v3_0.svg`。若閱讀器限制原碼SVG，可用同資料夾嵌入 `![[藥物分析_拉曼光譜_小循環掛載與能階圖_v3_0.svg]]`。

## Part III｜保留正式分類，分清題本語言

^rm-c-classification


|類別／模式|物理量或機制|L／F與位置|作答界線|
|---|---|---|---|
|Rayleigh scattering（瑞利散射）|彈性散射；Δν̃=0|L1、L5 → M02／M03|是需抑制的強背景之一。|
|Stokes Raman（斯托克斯拉曼）|非彈性；光子失能；位移正|L1、L4 → M02／M03|一般常用側；非吸收。|
|Anti-Stokes Raman（反斯托克斯拉曼）|非彈性；光子得能；位移負|L1、L10 → M02|需有初始振動激發人口。|
|Tyndall effect（廷得耳效應）|膠體／粒子散射表現|F02、L5 → M03|不與前兩者硬排普遍強度次序。|
|Dispersive Raman（色散式）|光柵分光取得Raman譜|F09 → M03|不是「只能定性」的模式。|
|FT-Raman（傅立葉轉換式）|干涉圖經FT取得Raman譜|F09、F14 → M03|不是不同散射機制。|
|IR／UV-Vis／AAS|此處為吸收方法|F01；IR另接L3 → M02|IR振動吸收；UV-Vis電子吸收；AAS原子吸收。|
|Fluorescence／AES|螢光／原子放射|F01；螢光背景接L6 → M03|典型由真實激發態放射，與Raman分開。|
|MS／LC-MS/MS（質譜／液相串聯質譜）|離子m/z；可搭配色層分離|來源選項辨識 → M03／M04|不是Raman散射；109-1直接錠劑題不選它。|
|NMR（核磁共振）|核自旋相關訊號；有定量方法|104-1選項辨識 → M03／M04|晶型另看固態NMR，不把溶液與固態混同。|


[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-methods|返回複習]]

### 題本「放射」與學理「散射」如何同時存檔？

107-1-2的選項是可見、紫外、IR、Raman，題本選D。114-1-16以C的單位敘述為錯誤答案。兩題答案保留；機制表仍把Raman寫成非彈性散射。這樣解題不會因修正分類而遺失原題，也不必把螢光、Raman硬當同一電子過程。

## 三張核心方法P1–P4卡

^rm-c-methods

色散式與FT-Raman是取得Raman譜的兩種配置；IR是需要完整對照的相鄰方法。其他家族保留辨識，不在本章擴寫整套儀器學。
[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-methods|返回複習]]

### Dispersive Raman（色散式拉曼）

^rm-c-method-dispersive

位置：L1–L9；M01→M04。

|層次|完整說明|
|---|---|
|P1 對象與目的|散射中的振動資訊；可做身分、固態比較及經校正定量。|
|P2 作用與條件|雷射激發，振動改α時可Raman活性；選合適波長及功率。|
|P3 部件與讀數|收光、Rayleigh抑制、繞射光柵與適合偵測器；常見CCD；讀散射強度對位移。|
|P4 結論與限制|指紋／峰群須比較參考；螢光、取樣、雜散光與響應校正影響結果。|


[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-methods|返回複習]]

### FT-Raman（傅立葉轉換拉曼）

^rm-c-method-ft

位置：L1–L9；M01→M04。

|層次|完整說明|
|---|---|
|P1 對象與目的|同樣量Raman；常見1064 nm配置可協助處理許多有機樣品背景。|
|P2 作用與條件|散射選擇律不變；NIR激發、光學和偵測器需互相匹配。|
|P3 部件與讀數|干涉儀編碼光訊號→偵測干涉圖→傅立葉轉換→Raman頻譜。|
|P4 結論與限制|FT是頻譜取得方式；不等於消螢光保證或定量資格。題本制酸錠為指定應用。|


[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-methods|返回複習]]

### IR spectroscopy（紅外光譜；主要比較中紅外）

^rm-c-method-ir

位置：L3、L8；M02、M04。

|層次|完整說明|
|---|---|
|P1 對象與目的|振動吸收；官能基、指紋及合適固態／含量分析。|
|P2 作用與條件|振動使μ改變時可IR活性；與Raman不同選擇律。|
|P3 部件與讀數|適合IR光源／光學／偵測器；吸收光波數cm⁻¹；可採ATR、透射等配置。|
|P4 結論與限制|可與Raman互補；樣品處理、接觸與參考譜影響比較，不能說所有IR都須壓片。|


[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-methods|返回複習]]

## 晶型題：方法與前處理必須一起看

^rm-c-solid


|方法|固態資訊|條件|
|---|---|---|
|Raman|固態振動／晶格環境|防雷射加熱，檢查低頻量測範圍。|
|NIR／NIRA（近紅外分析）|光譜差異配合參考／模型|解析度與模型需足以區分目標晶型。|
|Mull（糊漿法）／DRIFT（漫反射IR）|保留固態作IR比較|研磨、介質與顆粒效應仍會影響譜。|
|ATR（衰減全反射IR）|固體表面附近的IR資訊|常需接觸壓力，不能寫完全不施壓。|
|KBr pellet（溴化鉀壓錠）|IR透射樣品製備|題本排除；關鍵是壓力、研磨、濕氣可能改樣。|
|Solid-state NMR（固態核磁共振）|固態局部化學環境|與溶解後的溶液NMR區分。|
|XRD（X射線繞射）|晶格排列的繞射資訊|與Raman互補，無跨所有樣品的固定靈敏度高低。|


舊稿寫「Raman靈敏度大於X-ray與中紅外」但未提供同分析物、訊噪定義與條件的比較。本版不將此排序納入必背。舊稿所稱多晶性在本題應以polymorphism（多晶型性）理解，避免與polycrystalline（多晶粒）混同。
[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-methods|返回複習]]

### 圖3｜全章方法分類與大小循環對照圖

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="3120" viewBox="0 0 1900 3120" role="img" aria-labelledby="rm3_g3_title rm3_g3_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="rm3_g3_title">拉曼光譜｜全章方法分類與大小循環對照</title><desc id="rm3_g3_desc">拉曼光譜教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊，藍線表示光路；能階子圖另標藍線為能量帳。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="3120" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH30 / RAMAN / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">拉曼光譜｜全章方法分類與大小循環對照</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">先分分類身分，再用同一四站核對目的、條件、讀數與結論；不同層的名稱不硬排成同列。</text>
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
<rect x="50" y="375" width="1800" height="340" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="72" y="416" font-size="27" font-weight="600" fill="#61717a">分類分層｜這些名稱在回答不同問題</text>
<text x="72" y="463" font-size="24" font-weight="400" fill="#24343f">光子能量：Rayleigh 彈性；Stokes／anti-Stokes Raman 非彈性。</text>
<text x="72" y="497.08" font-size="24" font-weight="400" fill="#24343f">粒子現象：Tyndall 為膠體／粒子散射，不是普遍固定強度排序的一欄。</text>
<text x="72" y="531.16" font-size="24" font-weight="400" fill="#24343f">取得光譜：色散式／FT-Raman；波段：UV、可見、NIR；角度：90°或 180°等。</text>
<text x="72" y="565.24" font-size="24" font-weight="400" fill="#24343f">相鄰方法：IR／UV-Vis／AAS 吸收；螢光／AES 真實激發態放射。MS／LC-MS/MS、NMR 另看各自訊號。</text>
<rect x="50" y="770" width="570" height="1230" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="72" y="815" font-size="29" font-weight="600" fill="#326991">色散式 Raman</text>
<text x="72" y="862" font-size="22" font-weight="400" fill="#61717a">配置／取得光譜；L1–L9</text>
<rect x="68" y="920" width="534" height="220" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="90" y="961" font-size="27" font-weight="600" fill="#326991">P1／M01｜目的</text>
<text x="90" y="1008" font-size="24" font-weight="400" fill="#24343f">鑑別、固態比較；經驗證定量。</text>
<polyline points="335,1140 335,1170" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="335.0,1170.0 328.8,1158.6 341.2,1158.6" fill="#61717a"/>
<rect x="68" y="1175" width="534" height="220" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="90" y="1216" font-size="27" font-weight="600" fill="#326991">P2／M02｜作用與條件</text>
<text x="90" y="1263" font-size="24" font-weight="400" fill="#24343f">雷射激發；模式改 α；匹配濾片與光學。</text>
<polyline points="335,1395 335,1425" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="335.0,1425.0 328.8,1413.6 341.2,1413.6" fill="#61717a"/>
<rect x="68" y="1430" width="534" height="220" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="90" y="1471" font-size="27" font-weight="600" fill="#326991">P3／M03｜取得與讀數</text>
<text x="90" y="1518" font-size="24" font-weight="400" fill="#24343f">光柵分光 → CCD 等適配偵測 → 強度對位移。</text>
<polyline points="335,1650 335,1680" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="335.0,1680.0 328.8,1668.6 341.2,1668.6" fill="#61717a"/>
<rect x="68" y="1685" width="534" height="220" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="90" y="1726" font-size="27" font-weight="600" fill="#326991">P4／M04｜判斷與限制</text>
<text x="90" y="1773" font-size="24" font-weight="400" fill="#24343f">比參考或用有效校正；查背景、代表性。</text>
<rect x="670" y="770" width="570" height="1230" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="692" y="815" font-size="29" font-weight="600" fill="#286c68">FT-Raman</text>
<text x="692" y="862" font-size="22" font-weight="400" fill="#61717a">配置／取得光譜；L1–L9</text>
<rect x="688" y="920" width="534" height="220" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="710" y="961" font-size="27" font-weight="600" fill="#286c68">P1／M01｜目的</text>
<text x="710" y="1008" font-size="24" font-weight="400" fill="#24343f">相同 Raman 分析；常見 1064 nm 配置。</text>
<polyline points="955,1140 955,1170" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="955.0,1170.0 948.8,1158.6 961.2,1158.6" fill="#61717a"/>
<rect x="688" y="1175" width="534" height="220" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="710" y="1216" font-size="27" font-weight="600" fill="#286c68">P2／M02｜作用與條件</text>
<text x="710" y="1263" font-size="24" font-weight="400" fill="#24343f">NIR 激發；同選擇律；光學與偵測匹配。</text>
<polyline points="955,1395 955,1425" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="955.0,1425.0 948.8,1413.6 961.2,1413.6" fill="#61717a"/>
<rect x="688" y="1430" width="534" height="220" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="710" y="1471" font-size="27" font-weight="600" fill="#286c68">P3／M03｜取得與讀數</text>
<text x="710" y="1518" font-size="24" font-weight="400" fill="#24343f">干涉儀 → 偵測干涉圖 → FT → Raman 譜。</text>
<polyline points="955,1650 955,1680" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="955.0,1680.0 948.8,1668.6 961.2,1668.6" fill="#61717a"/>
<rect x="688" y="1685" width="534" height="220" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="710" y="1726" font-size="27" font-weight="600" fill="#286c68">P4／M04｜判斷與限制</text>
<text x="710" y="1773" font-size="24" font-weight="400" fill="#24343f">FT 非消螢光／定量保證；需校正與驗證。</text>
<rect x="1290" y="770" width="570" height="1230" rx="18" fill="#e8e1f2" stroke="#685185" stroke-width="2"/>
<text x="1312" y="815" font-size="29" font-weight="600" fill="#685185">IR spectroscopy</text>
<text x="1312" y="862" font-size="22" font-weight="400" fill="#61717a">相鄰方法／振動吸收；L3、L8</text>
<rect x="1308" y="920" width="534" height="220" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="1330" y="961" font-size="27" font-weight="600" fill="#685185">P1／M01｜目的</text>
<text x="1330" y="1008" font-size="24" font-weight="400" fill="#24343f">官能基、指紋、固態與適合含量分析。</text>
<polyline points="1575,1140 1575,1170" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1575.0,1170.0 1568.8,1158.6 1581.2,1158.6" fill="#61717a"/>
<rect x="1308" y="1175" width="534" height="220" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="1330" y="1216" font-size="27" font-weight="600" fill="#685185">P2／M02｜作用與條件</text>
<text x="1330" y="1263" font-size="24" font-weight="400" fill="#24343f">振動改 μ；相容製樣，可用 ATR 等。</text>
<polyline points="1575,1395 1575,1425" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1575.0,1425.0 1568.8,1413.6 1581.2,1413.6" fill="#61717a"/>
<rect x="1308" y="1430" width="534" height="220" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="1330" y="1471" font-size="27" font-weight="600" fill="#685185">P3／M03｜取得與讀數</text>
<text x="1330" y="1518" font-size="24" font-weight="400" fill="#24343f">吸收光波數 cm⁻¹；T／A 或相應讀數。</text>
<polyline points="1575,1650 1575,1680" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1575.0,1680.0 1568.8,1668.6 1581.2,1668.6" fill="#61717a"/>
<rect x="1308" y="1685" width="534" height="220" rx="18" fill="#fff" stroke="#685185" stroke-width="2"/>
<text x="1330" y="1726" font-size="27" font-weight="600" fill="#685185">P4／M04｜判斷與限制</text>
<text x="1330" y="1773" font-size="24" font-weight="400" fill="#24343f">與 Raman 互補；查製樣、接觸與參考。</text>
<rect x="50" y="2050" width="1800" height="340" rx="18" fill="#e8e1f2" stroke="#685185" stroke-width="2"/>
<text x="72" y="2091" font-size="27" font-weight="600" fill="#685185">晶型題的完整方法家族｜方法與前處理一起看</text>
<text x="72" y="2138" font-size="24" font-weight="400" fill="#24343f">Raman：固態振動／晶格資訊；防激光加熱，低頻範圍須可用。</text>
<text x="72" y="2172.08" font-size="24" font-weight="400" fill="#24343f">NIR／NIRA：譜差配合參考與模型；IR：Mull、DRIFT、ATR 等相容固態配置。</text>
<text x="72" y="2206.16" font-size="24" font-weight="400" fill="#24343f">KBr 壓錠：題本解析排除；研磨、壓力、濕氣或相容性可能改譜，不是每次必轉晶。</text>
<text x="72" y="2240.24" font-size="24" font-weight="400" fill="#24343f">固態 NMR：局部化學環境；XRD：晶格繞射。溶解後資料不能代表原晶格。</text>
<rect x="50" y="2435" width="875" height="450" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="72" y="2476" font-size="27" font-weight="600" fill="#9e771c">題本「放射」｜答案保留</text>
<text x="72" y="2523" font-size="24" font-weight="400" fill="#24343f">Q07（107-1）四選項依題本選 D Raman。</text>
<text x="72" y="2557.08" font-size="24" font-weight="400" fill="#24343f">Q01（114-1）單位錯誤選 C。</text>
<text x="72" y="2591.16" font-size="24" font-weight="400" fill="#24343f">物理機制：Raman 是非彈性散射，不能與螢光的真實激發態過程混為一談。</text>
<rect x="975" y="2435" width="875" height="450" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="997" y="2476" font-size="27" font-weight="600" fill="#b72d4a">題本「定量」｜條件說清楚</text>
<text x="997" y="2523" font-size="24" font-weight="400" fill="#24343f">Q04（110-1）選 C；Q08（104-1）選 B。</text>
<text x="997" y="2557.08" font-size="24" font-weight="400" fill="#24343f">Q05（109-1）制酸錠中甘胺酸＋碳酸鈣選 B Raman；解析提 FT-Raman。</text>
<text x="997" y="2591.16" font-size="24" font-weight="400" fill="#24343f">一般 Raman 可經校正與驗證定量，配置名稱不代替標準、取樣與適用範圍。</text>
<text x="50" y="3052" font-size="20" font-weight="400" fill="#61717a">IR＝紅外；UV＝紫外；NIR＝近紅外；AAS／AES＝原子吸收／放射；MS＝質譜；NMR＝核磁共振；XRD＝X 射線繞射。</text>
<text x="50" y="3088" font-size="20" font-weight="400" fill="#61717a">原題：ch30 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

[[藥物分析_拉曼光譜_全章方法分類與大小循環對照圖_v3_0.svg|開啟獨立 SVG]]

圖源：`藥物分析_拉曼光譜_全章方法分類與大小循環對照圖_v3_0.svg`。若閱讀器限制原碼SVG，可用同資料夾嵌入 `![[藥物分析_拉曼光譜_全章方法分類與大小循環對照圖_v3_0.svg]]`。

## 儀器與操作：每個部件解決哪個問題

^rm-c-operations


|部件／條件|作用|對應|
|---|---|---|
|Laser（雷射）|強而窄頻的激發；λ₀是波長，不是圖譜位移。|F07／L4、L6|
|功率、照射時間、聚焦|提高收集量也可能加熱、損傷或改變取樣；先確認樣品穩定。|L7、L8|
|90°側向／180°背向收集|收光幾何；90°並非所有Raman必備，也不能單靠角度濾掉螢光。|F09|
|Edge／Notch filter（邊緣／陷波濾片）|抑制Rayleigh；截止會影響低頻與哪一側可見。|L5|
|Grating（繞射光柵）|色散式把不同波長分到不同位置。|色散式／M03|
|CCD（電荷耦合元件）|常見可見／部分近紅外色散式偵測器；不是所有波長皆適用。|色散式／M03|
|Interferometer（干涉儀）|FT配置將光譜資訊編碼成干涉圖。|FT-Raman／M03|
|FT與近紅外偵測器|先偵測干涉圖，再FT還原；依波段選Ge或InGaAs等合適配置。|FT-Raman／M03|
|波數／強度參考|峰位校正與相對強度校正解決不同偏差；依方法執行。|L4、L9|
|包裝／溶劑空白|識別額外峰與螢光背景；不能把空白訊號當API。|L7|
|多點／映射／代表性取樣|處理錠劑與粉體不均勻，局部點不自動代表整批。|L7、L9|
|校正集與獨立驗證|濃度或含量模型須適用基質與區間，不能只看擬合漂亮。|L9|


**可口述的操作鏈：**定目的 → 選取樣及空白 → 選雷射與功率 → 確認樣品未改變 → 匹配收光／濾光／光譜配置 → 依方法作波數及訊號校正 → 取得足夠訊噪的譜 → 比參考或用驗證模型定量。

**收益與代價：**小焦斑便於局部辨識，但要補代表性取樣；提高功率可增訊號，但可能加熱；拉長激發波長可能減螢光，但也可能減Raman效率。FT轉換本身不保證訊噪一定改善，更不會自動消除所有背景。

### 圖4｜儀器與操作考點圖

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="3500" viewBox="0 0 1900 3500" role="img" aria-labelledby="rm3_g4_title rm3_g4_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="rm3_g4_title">拉曼光譜｜儀器與操作考點</title><desc id="rm3_g4_desc">拉曼光譜教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊，藍線表示光路；能階子圖另標藍線為能量帳。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="3500" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH30 / RAMAN / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">拉曼光譜｜儀器與操作考點</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">藍線畫光；灰線畫資料。色散式與 FT 式擇一配置；FT 偵測器在干涉儀之後。</text>
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
<rect x="50" y="385" width="420" height="245" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="72" y="426" font-size="27" font-weight="600" fill="#326991">雷射</text>
<text x="72" y="473" font-size="24" font-weight="400" fill="#24343f">λ₀、功率與時間</text>
<text x="72" y="507.08" font-size="24" font-weight="400" fill="#24343f">不是 Raman 位移</text>
<polyline points="470,505 506,505" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="506.0,505.0 494.6,511.2 494.6,498.8" fill="#326991"/>
<rect x="510" y="385" width="420" height="245" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="532" y="426" font-size="27" font-weight="600" fill="#326991">樣品／聚焦</text>
<text x="532" y="473" font-size="24" font-weight="400" fill="#24343f">空白、背景與代表性</text>
<text x="532" y="507.08" font-size="24" font-weight="400" fill="#24343f">確認照射未改樣</text>
<polyline points="930,505 966,505" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="966.0,505.0 954.6,511.2 954.6,498.8" fill="#326991"/>
<rect x="970" y="385" width="420" height="245" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="992" y="426" font-size="27" font-weight="600" fill="#326991">收集散射</text>
<text x="992" y="473" font-size="24" font-weight="400" fill="#24343f">90°側向／180°背向等</text>
<text x="992" y="507.08" font-size="24" font-weight="400" fill="#24343f">不是所有配置都 90°</text>
<polyline points="1390,505 1426,505" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1426.0,505.0 1414.6,511.2 1414.6,498.8" fill="#326991"/>
<rect x="1430" y="385" width="420" height="245" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="1452" y="426" font-size="27" font-weight="600" fill="#326991">Rayleigh 抑制</text>
<text x="1452" y="473" font-size="24" font-weight="400" fill="#24343f">匹配激發的濾片</text>
<text x="1452" y="507.08" font-size="24" font-weight="400" fill="#24343f">確認兩側與低頻譜窗</text>
<text x="50" y="700" font-size="27" font-weight="600" fill="#24343f">以下依儀器擇一取得頻譜；不是同一束光串過兩種完整儀器。</text>
<rect x="50" y="745" width="1800" height="420" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="75" y="792" font-size="29" font-weight="600" fill="#326991">色散式 Raman｜用光柵分波長</text>
<rect x="75" y="835" width="390" height="250" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="97" y="876" font-size="27" font-weight="600" fill="#326991">濾後散射光</text>
<text x="97" y="923" font-size="23" font-weight="400" fill="#24343f">含不同散射波長</text>
<polyline points="465,950 510,950" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="510.0,950.0 498.6,956.2 498.6,943.8" fill="#326991"/>
<rect x="515" y="835" width="390" height="250" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="537" y="876" font-size="27" font-weight="600" fill="#326991">繞射光柵</text>
<text x="537" y="923" font-size="23" font-weight="400" fill="#24343f">把波長分到不同位置</text>
<polyline points="905,950 950,950" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="950.0,950.0 938.6,956.2 938.6,943.8" fill="#326991"/>
<rect x="955" y="835" width="390" height="250" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="977" y="876" font-size="27" font-weight="600" fill="#326991">適配偵測器</text>
<text x="977" y="923" font-size="23" font-weight="400" fill="#24343f">可見／部分 NIR 常見 CCD</text>
<polyline points="1345,950 1390,950" fill="none" stroke="#61717a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1390.0,950.0 1378.6,956.2 1378.6,943.8" fill="#61717a"/>
<rect x="1395" y="835" width="390" height="250" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="1417" y="876" font-size="27" font-weight="600" fill="#326991">Raman 譜</text>
<text x="1417" y="923" font-size="23" font-weight="400" fill="#24343f">換算位移、校正與讀軸</text>
<rect x="50" y="1220" width="1800" height="1390" rx="18" fill="#d9eeea" stroke="#286c68" stroke-width="2"/>
<text x="75" y="1270" font-size="29" font-weight="600" fill="#286c68">FT-Raman｜先干涉編碼，再偵測干涉圖，最後 FT</text>
<text x="75" y="1315" font-size="23" font-weight="400" fill="#24343f">常見 1064 nm；近紅外光學與 Ge／InGaAs 等偵測器須適配。FT 是處理，不是偵測器。</text>
<rect x="100" y="1370" width="1700" height="845" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="125" y="1420" font-size="27" font-weight="600" fill="#286c68">干涉儀的兩臂｜Raman 散射光進入；固定鏡／移動鏡不是樣品／參考品</text>
<rect x="130" y="1740" width="420" height="195" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="152" y="1781" font-size="27" font-weight="600" fill="#326991">濾後 Raman 散射光</text>
<text x="152" y="1828" font-size="24" font-weight="400" fill="#24343f">來自已受雷射激發的樣品</text>
<rect x="740" y="1730" width="245" height="210" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="775" y="1818" font-size="28" font-weight="600" fill="#326991">分光器</text>
<rect x="740" y="1470" width="340" height="130" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="762" y="1511" font-size="27" font-weight="600" fill="#326991">固定鏡</text>
<text x="762" y="1558" font-size="22" font-weight="400" fill="#24343f">一臂光程固定</text>
<rect x="1270" y="1730" width="340" height="160" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="1292" y="1771" font-size="27" font-weight="600" fill="#326991">移動鏡</text>
<text x="1292" y="1818" font-size="22" font-weight="400" fill="#24343f">改變另一臂光程</text>
<polyline points="550,1840 740,1840" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="740.0,1840.0 728.6,1846.2 728.6,1833.8" fill="#326991"/>
<polyline points="835,1730 835,1600" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="835.0,1600.0 841.2,1611.4 828.8,1611.4" fill="#326991"/>
<polyline points="870,1600 870,1730" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="870.0,1730.0 863.8,1718.6 876.2,1718.6" fill="#326991"/>
<polyline points="985,1780 1270,1780" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1270.0,1780.0 1258.6,1786.2 1258.6,1773.8" fill="#326991"/>
<polyline points="1270,1860 985,1860" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="985.0,1860.0 996.4,1853.8 996.4,1866.2" fill="#326991"/>
<text x="1030" y="1745" font-size="22" font-weight="400" fill="#326991">去程</text>
<text x="1030" y="1902" font-size="22" font-weight="400" fill="#326991">回程</text>
<polyline points="865,1940 865,2000" fill="none" stroke="#326991" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="865.0,2000.0 858.8,1988.6 871.2,1988.6" fill="#326991"/>
<rect x="650" y="2000" width="720" height="150" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="672" y="2041" font-size="27" font-weight="600" fill="#326991">合束 → NIR 偵測器</text>
<text x="672" y="2088" font-size="23" font-weight="400" fill="#24343f">光程差改變時，偵測輸出隨之改變。</text>
<rect x="100" y="2280" width="380" height="245" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="122" y="2321" font-size="27" font-weight="600" fill="#286c68">干涉圖</text>
<text x="122" y="2368" font-size="23" font-weight="400" fill="#24343f">訊號對光程差</text>
<polyline points="480,2400 520,2400" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="520.0,2400.0 508.6,2406.2 508.6,2393.8" fill="#61717a"/>
<rect x="525" y="2280" width="380" height="245" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="547" y="2321" font-size="27" font-weight="600" fill="#286c68">傅立葉轉換</text>
<text x="547" y="2368" font-size="23" font-weight="400" fill="#24343f">還原散射光譜</text>
<polyline points="905,2400 945,2400" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="945.0,2400.0 933.6,2406.2 933.6,2393.8" fill="#61717a"/>
<rect x="950" y="2280" width="380" height="245" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="972" y="2321" font-size="27" font-weight="600" fill="#286c68">位移與校正</text>
<text x="972" y="2368" font-size="23" font-weight="400" fill="#24343f">ν̃₀−ν̃ₛ；背景與響應</text>
<polyline points="1330,2400 1370,2400" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1370.0,2400.0 1358.6,2406.2 1358.6,2393.8" fill="#61717a"/>
<rect x="1375" y="2280" width="380" height="245" rx="18" fill="#fff" stroke="#286c68" stroke-width="2"/>
<text x="1397" y="2321" font-size="27" font-weight="600" fill="#286c68">交 M04</text>
<text x="1397" y="2368" font-size="23" font-weight="400" fill="#24343f">比參考／有效定量校正</text>
<polyline points="1010,2150 1010,2240 290,2240 290,2280" fill="none" stroke="#61717a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="290.0,2280.0 283.8,2268.6 296.2,2268.6" fill="#61717a"/>
<rect x="50" y="2670" width="570" height="590" rx="18" fill="#dceaf7" stroke="#326991" stroke-width="2"/>
<text x="72" y="2711" font-size="27" font-weight="600" fill="#326991">濾片</text>
<text x="72" y="2758" font-size="24" font-weight="400" fill="#24343f">Edge 常取一側；Notch 可看兩側，仍有截止。</text>
<text x="72" y="2792.08" font-size="24" font-weight="400" fill="#24343f">強濾光可能丟低頻晶格峰，不等於去掉所</text>
<text x="72" y="2826.16" font-size="24" font-weight="400" fill="#24343f">有螢光。</text>
<polyline points="335,2930 335,2970" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="335.0,2970.0 328.8,2958.6 341.2,2958.6" fill="#b72d4a"/>
<rect x="68" y="2970" width="534" height="245" rx="18" fill="#fff" stroke="#b72d4a" stroke-width="2"/>
<text x="90" y="3011" font-size="27" font-weight="600" fill="#b72d4a">若低頻峰被切／可見側不合</text>
<text x="90" y="3058" font-size="23" font-weight="400" fill="#24343f">換適合濾片 → M02／L5。</text>
<text x="90" y="3090.66" font-size="23" font-weight="400" fill="#24343f">修正後重測並確認譜窗。</text>
<rect x="670" y="2670" width="570" height="590" rx="18" fill="#fff1c8" stroke="#9e771c" stroke-width="2"/>
<text x="692" y="2711" font-size="27" font-weight="600" fill="#9e771c">激發與功率</text>
<text x="692" y="2758" font-size="24" font-weight="400" fill="#24343f">較長波可能減螢光，也可能減 Raman 效率。</text>
<text x="692" y="2792.08" font-size="24" font-weight="400" fill="#24343f">加功率可能加熱改樣；以實際品質與穩定</text>
<text x="692" y="2826.16" font-size="24" font-weight="400" fill="#24343f">性比較。</text>
<polyline points="955,2930 955,2970" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="955.0,2970.0 948.8,2958.6 961.2,2958.6" fill="#b72d4a"/>
<rect x="688" y="2970" width="534" height="245" rx="18" fill="#fff" stroke="#b72d4a" stroke-width="2"/>
<text x="710" y="3011" font-size="27" font-weight="600" fill="#b72d4a">若背景遮峰／照射改樣</text>
<text x="710" y="3058" font-size="23" font-weight="400" fill="#24343f">重選波長、功率與時間</text>
<text x="710" y="3090.66" font-size="23" font-weight="400" fill="#24343f">→ M02／L6、L8；確認穩定再測。</text>
<rect x="1290" y="2670" width="570" height="590" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="1312" y="2711" font-size="27" font-weight="600" fill="#b72d4a">取樣與校正</text>
<text x="1312" y="2758" font-size="24" font-weight="400" fill="#24343f">包裝／溶劑空白，多點或映射。</text>
<text x="1312" y="2792.08" font-size="24" font-weight="400" fill="#24343f">波數校正查峰位；響應校正查強度；含量另需標</text>
<text x="1312" y="2826.16" font-size="24" font-weight="400" fill="#24343f">準與驗證。</text>
<polyline points="1575,2930 1575,2970" fill="none" stroke="#b72d4a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 7"/>
<polygon points="1575.0,2970.0 1568.8,2958.6 1581.2,2958.6" fill="#b72d4a"/>
<rect x="1308" y="2970" width="534" height="245" rx="18" fill="#fff" stroke="#b72d4a" stroke-width="2"/>
<text x="1330" y="3011" font-size="27" font-weight="600" fill="#b72d4a">若代表性／校正條件不合</text>
<text x="1330" y="3058" font-size="23" font-weight="400" fill="#24343f">取樣回 M01／M02（L7）；</text>
<text x="1330" y="3090.66" font-size="23" font-weight="400" fill="#24343f">校正、範圍與驗證回 M04（L9）。</text>
<text x="50" y="3432" font-size="20" font-weight="400" fill="#61717a">CCD＝電荷耦合元件；Ge＝鍺；InGaAs＝銦鎵砷；FT＝傅立葉轉換；NIR＝近紅外。干涉儀兩臂藍線是去／回光。</text>
<text x="50" y="3468" font-size="20" font-weight="400" fill="#61717a">原題：ch30 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

[[藥物分析_拉曼光譜_儀器與操作考點圖_v3_0.svg|開啟獨立 SVG]]

圖源：`藥物分析_拉曼光譜_儀器與操作考點圖_v3_0.svg`。若閱讀器限制原碼SVG，可用同資料夾嵌入 `![[藥物分析_拉曼光譜_儀器與操作考點圖_v3_0.svg]]`。

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-operations|返回複習]]

## 應用：由問題選證據

^rm-c-applications


|分析問題|需要的資訊|不能省略|
|---|---|---|
|藥物／製劑身分|峰群、位移、相對模式與參考譜|混合物背景、基質及代表性取樣。|
|包裝內裸錠|合適包裝透過的光與樣品散射|包裝材質、厚度、色澤及其本身光譜。|
|原料藥晶型|保留固態的振動／晶格特徵|溫度、加熱、處理及參考晶型。|
|製劑成分含量|適合峰面積或多變量模型|標準校正、適用區間、獨立驗證。|
|舊稿延伸例|Heroin（海洛因）／Morphine（嗎啡）／Codeine（可待因）指紋；胜肽構形變化|僅作應用方向，不新增精確特徵峰；不宣稱FT-IR必定無法辨別。|


[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-methods|返回複習]]

## Part IV｜五個紙筆公式護照

^rm-c-math

附件沒有數值計算題；下列皆為自編，步驟可紙筆重現，不提供計算機按鍵。每次先分「絕對位置」與「差值」，再做倒數或減法。
[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-math|返回複習]]

### C1｜nm換波數：把單位先變一致

^rm-c-calc1

**要解什麼：**由光的波長取得其波數，不是自動取得Raman位移。

**母式：**$\tilde\nu=1/\lambda$，本章光譜換算採真空波長慣例。$\lambda$若用cm，倒數就是cm⁻¹；若用nm，需先換長度單位。

$$1\ \mathrm{nm}=10^{-7}\ \mathrm{cm}$$
$$\lambda(\mathrm{cm})=\lambda(\mathrm{nm})\times10^{-7}$$
$$\tilde\nu(\mathrm{cm}^{-1})=\frac{1}{\lambda(\mathrm{nm})\times10^{-7}}=\frac{10^7}{\lambda(\mathrm{nm})}$$

**紙筆例（自編）：**500 nm → $10^7/(5\times10^2)=2\times10^4=20000$ cm⁻¹；800 nm → $10^7/(8\times10^2)=1.25\times10^4=12500$ cm⁻¹。

**方向與界線：**波長拉長，波數降低。$10^7$是nm與cm指定單位後的數值換算因子，不能在λ已經用cm時再乘一次。450 nm可估：450×22000=9.9×10⁶，所以波數略大於22000 cm⁻¹。雷射波數在這個量級，不代表所有Raman位移也在此量級。

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-math|返回複習]]

**C1-P｜換數字先動筆（自編）：**一束光波長 1000 nm，求波數並說明它是否已是 Raman 位移。

<details>
<summary>展開紙筆步驟與方向驗算</summary>

1000=10³ nm，10⁷/10³=10⁴=10000 cm⁻¹。這是此光的絕對波數；沒有另一束光位置，就沒有 Raman 位移。

</details>

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-calc1|回同組閉卷紙筆]]。

### C2｜由能量守恆算Stokes與anti-Stokes

^rm-c-calc2

**要解什麼：**指定雷射及振動間距時，求散射光的位置。

**母式：**$E_0+E_i=E_s+E_f$；移項得$E_0-E_s=E_f-E_i$。光子$E=hc_0\tilde\nu$，因此

$$hc_0(\tilde\nu_0-\tilde\nu_s)=E_f-E_i$$
$$\Delta\tilde\nu=\tilde\nu_0-\tilde\nu_s=\frac{E_f-E_i}{hc_0}$$

**符號／單位：**ν̃₀是入射、ν̃ₛ是散射波數；Δν̃為有正負的位移，均用cm⁻¹。若計算焦耳，要把cm⁻¹轉m⁻¹再配c₀的m/s，或統一採cm/s；不混長度單位。本章以下只算波數及波長，不需代h。

**紙筆例（自編）：**λ₀=500 nm，故ν̃₀=20000 cm⁻¹；某模式振動間距對應1000 cm⁻¹。

| 散射 | 分子末態−初態 | 有號位移 | 散射波數 |
|---|---|---|---|
| Rayleigh | 0 | 0 | 20000 |
| Stokes | +ΔE | +1000 | 20000−1000=19000 |
| anti-Stokes | −ΔE | −1000 | 20000−(−1000)=21000 |

Stokes：$\lambda_s=10^7/19000=10000/19$ nm。因19×526=9994，答案約526.3 nm，大於500。

anti-Stokes：$\lambda_s=10^7/21000=10000/21$ nm。因21×476=9996，答案約476.2 nm，小於500。

**驗算：**anti-Stokes短、Rayleigh原長、Stokes長。Stokes需ν̃₀大於振動位移，才有正的散射光頻率；anti-Stokes還需初始高振動態人口。

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-math|返回複習]]

**C2-P｜換數字先動筆（自編）：**雷射 500 nm、模式間距 2000 cm⁻¹，先求兩側散射波數，再判波長長短。

<details>
<summary>展開紙筆步驟與方向驗算</summary>

入射 20000 cm⁻¹。Stokes：20000−2000=18000，長波；anti-Stokes：20000+2000=22000，短波。若續算：10⁷/18000=5000/9≈555.6 nm；10⁷/22000=5000/11≈454.5 nm。

</details>

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-calc2|回同組閉卷紙筆]]。

### C3｜換雷射：同位移，不同散射光

^rm-c-calc3

**問題：**雷射由500換成800 nm，同一模式仍為1000 cm⁻¹的Stokes位移。

**成立條件：**模式、樣品狀態與溫度不變；忽略激發改變造成的改樣及峰位校正誤差。

母式先整理：$\tilde\nu_s=\tilde\nu_0-\Delta\tilde\nu$，再$\lambda_s=10^7/\tilde\nu_s$。

| 雷射 | 入射波數 | Stokes散射波數 | 散射波長 |
|---|---|---|---|
| 500 nm | 20000 cm⁻¹ | 19000 cm⁻¹ | 約526.3 nm |
| 800 nm | 12500 cm⁻¹ | 11500 cm⁻¹ | $10^7/11500=20000/23$，約869.6 nm |

**手算驗證：**23×869=19987，餘13；13/23約0.6。兩次波數差同為1000，但波長差約26.3與69.6 nm，**不相同**。所以固定波數差不能換成固定波長差。

**判讀界線：**只能說同模式位移位置近似一致；峰高、背景和可見模式可能改變。典型同一發光物種、同環境的螢光發射峰常相對穩定，但也不能教成所有螢光永遠不受激發條件影響。

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-math|返回複習]]

**C3-P｜換數字先動筆（自編）：**自編換雷射例：同模式仍為 +1000 cm⁻¹，若入射 1000 nm，求 Stokes 散射波長。

<details>
<summary>展開紙筆步驟與方向驗算</summary>

先算 10⁷/1000=10000 cm⁻¹；散射為 10000−1000=9000 cm⁻¹；λₛ=10⁷/9000=10000/9≈1111.1 nm。因 9×1111=9999，餘 1，故約 1111.1。位移仍是 +1000，峰高不必相同。1000 nm 僅為整除練習設定。

</details>

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-calc3|回同組閉卷紙筆]]。

### C4｜由兩個波長反算位移：先倒數，再相減

^rm-c-calc4

**要解什麼：**已知λ₀和λₛ，判斷Stokes／anti-Stokes並算位移。

$$\Delta\tilde\nu=10^7\left(\frac1{\lambda_0}-\frac1{\lambda_s}\right)$$

λ₀、λₛ都必須以nm代入，結果才是cm⁻¹。不要把$1/(\lambda_s-\lambda_0)$當成位移。

**自編已知：**λ₀=500 nm，λₛ=625 nm。

$$\Delta\tilde\nu=\frac{10^7}{500}-\frac{10^7}{625}=20000-16000=4000\ \mathrm{cm}^{-1}$$

**紙筆：**625×16=10000，所以625×16000=10⁷。散射光較長波，位移正，屬Stokes。這個自編4000只為整除練習，不是任何藥物的指定峰位。

**常見錯法：**625−500=125 nm是波長差；$10^7/125=80000$不能拿來冒充本題波數差。

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-math|返回複習]]

**C4-P｜換數字先動筆（自編）：**λ₀=800 nm、λₛ=1000 nm，求有號位移並判散射種類。

<details>
<summary>展開紙筆步驟與方向驗算</summary>

10⁷/800=12500；10⁷/1000=10000；Δν̃=12500−10000=+2500 cm⁻¹，Stokes。散射波長較長、波數較低，方向符合。

</details>

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-calc4|回同組閉卷紙筆]]。

### C5｜定量內插：把校正條件一起帶入

^rm-c-calc5

**模型而非普遍定律：**在已驗證的局部線性區間，處理後訊號S與濃度C可寫$S=aC+b$。S是固定程序的峰面積或模型響應，單位由量測定義；C需固定濃度基準。a.u.（arbitrary units，任意單位）由程序定義；w/w 為質量／質量基準。若 C 寫成 10、20 代表百分數，斜率單位是 a.u.／百分點；若 C 寫成 0.10、0.20，斜率數值也須跟著換。兩標準點本身不能證明線性，例題已另給驗證條件。

已知低標準$C_1=10\%$ w/w、$S_1=20$ a.u.；高標準$C_2=20\%$ w/w、$S_2=40$ a.u.；未知$S=30$ a.u.。樣品與標準基質、取樣、雷射及背景處理相符，題設已驗證此區間線性。

$$\frac{C-C_1}{C_2-C_1}=\frac{S-S_1}{S_2-S_1}$$
$$C=10\%+\frac{30-20}{40-20}(20\%-10\%)=15\%\;w/w$$

**紙筆與驗算：**訊號在兩標準正中間，濃度也在中間。不任意外插；未知若與標準粒徑／基質不同，這個數字不因此自動可靠。FT或色散式之名不能替代校正與驗證。

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-math|返回複習]]

**C5-P｜換數字先動筆（自編）：**沿用已驗證線性區間：10% w/w→20 a.u.、20%→40 a.u.，未知 35 a.u.；求含量並列一個失效條件。

<details>
<summary>展開紙筆步驟與方向驗算</summary>

35−20=15，40−20=20，比值 15/20=3/4。C=10%+(3/4)×10 個百分點=17.5% w/w。若基質、功率、聚焦、代表性取樣或資料處理不符合校正，這個內插數字不能直接當可靠含量。

</details>

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-calc5|回同組閉卷紙筆]]。

## 補充公式：只判人口方向，不硬算指數

^rm-c-population

熱平衡近似下$N_1/N_0=\exp[-\Delta E/(k_BT)]$（忽略或另計簡併因素）。固定ΔE，T升高使負指數的絕對值變小，故N₁/N₀上升。這支持L10的anti-Stokes人口推理；它不是完整的兩側強度比公式。真要由強度測溫，還需頻率及儀器響應校正。
[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-l10|返回複習]]

### 圖5｜公式與誤差判讀總表

<svg xmlns="http://www.w3.org/2000/svg" width="1900" height="3550" viewBox="0 0 1900 3550" role="img" aria-labelledby="rm3_g5_title rm3_g5_desc" font-family="Noto Sans CJK TC, Microsoft JhengHei, Droid Sans Fallback, sans-serif" fill="#24343f">
<title id="rm3_g5_title">拉曼光譜｜公式與誤差判讀總表</title><desc id="rm3_g5_desc">拉曼光譜教學向量圖，v3.0。四站角色固定：先定問題、準備與測量、讀訊號、核對結論。灰線表示分析資訊，藍線表示光路；能階子圖另標藍線為能量帳。紅虛線表示條件不符的分析者回查。示意不按比例。</desc>
<rect x="0" y="0" width="1900" height="3550" rx="0" fill="#f8f6ee" stroke="#f8f6ee" stroke-width="2"/>
<text x="50" y="64" font-size="20" font-weight="400" fill="#61717a">PHARMACEUTICAL ANALYSIS / CH30 / RAMAN / v3.0</text>
<text x="50" y="120" font-size="38" font-weight="400" fill="#24343f">拉曼光譜｜公式與誤差判讀總表</text>
<text x="50" y="164" font-size="24" font-weight="400" fill="#24343f">先辨絕對位置或差值，再列式、代指定單位、紙筆計算，最後用方向與條件驗算。</text>
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
<rect x="50" y="375" width="1800" height="255" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="72" y="416" font-size="27" font-weight="600" fill="#326991">同一例的三種位置｜λ₀＝500 nm；模式間距＝1000 cm⁻¹</text>
<text x="72" y="463" font-size="24" font-weight="400" fill="#24343f">anti-Stokes：Δν̃＝−1000；ν̃ₛ＝21000 cm⁻¹；λₛ≈476.2 nm。</text>
<text x="72" y="497.08" font-size="24" font-weight="400" fill="#24343f">Rayleigh：Δν̃＝0；ν̃ₛ＝20000 cm⁻¹；λₛ＝500 nm。</text>
<text x="72" y="531.16" font-size="24" font-weight="400" fill="#24343f">Stokes：Δν̃＝＋1000；ν̃ₛ＝19000 cm⁻¹；λₛ≈526.3 nm。峰高不在這張位置表內。</text>
<rect x="50" y="675" width="1800" height="290" rx="18" fill="#fff" stroke="#326991" stroke-width="2"/>
<text x="75" y="720" font-size="27" font-weight="600" fill="#326991">有號位移軸｜本圖只對應三個位置，不是實驗峰高</text>
<polyline points="170,810 1710,810" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<polygon points="1710.0,810.0 1698.6,816.2 1698.6,803.8" fill="#326991"/>
<polyline points="340,790 340,830" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<text x="180" y="773" font-size="24" font-weight="400" fill="#326991">−1000｜anti-Stokes</text>
<text x="190" y="879" font-size="24" font-weight="400" fill="#24343f">476.2 nm；短波</text>
<polyline points="920,790 920,830" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<text x="760" y="773" font-size="24" font-weight="400" fill="#326991">0｜Rayleigh</text>
<text x="770" y="879" font-size="24" font-weight="400" fill="#24343f">500 nm</text>
<polyline points="1500,790 1500,830" fill="none" stroke="#326991" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<text x="1340" y="773" font-size="24" font-weight="400" fill="#326991">＋1000｜Stokes</text>
<text x="1350" y="879" font-size="24" font-weight="400" fill="#24343f">526.3 nm；長波</text>
<text x="75" y="929" font-size="23" font-weight="400" fill="#61717a">λₛ 從左至右增加；ν̃ₛ 從左至右降低。若閱讀器把位移軸反畫，先看刻度再判方向。</text>
<rect x="50" y="1010" width="1800" height="350" rx="18" fill="#fff1c8" stroke="#61717a" stroke-width="2"/>
<text x="75" y="1054" font-size="28" font-weight="600" fill="#24343f">C1｜nm → 波數｜L4；F06</text>
<rect x="75" y="1090" width="570" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="93" y="1126" font-size="25" font-weight="600" fill="#24343f">母式／量與單位</text>
<text x="93" y="1177" font-size="23" font-weight="400" fill="#24343f">ν̃＝1/λ；λcm＝λnm×10⁻⁷</text>
<text x="93" y="1209.66" font-size="23" font-weight="400" fill="#24343f">ν̃(cm⁻¹)＝10⁷／λ(nm)</text>
<rect x="670" y="1090" width="610" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="688" y="1126" font-size="25" font-weight="600" fill="#326991">紙筆例（均為自編）</text>
<text x="688" y="1177" font-size="23" font-weight="400" fill="#326991">500 nm → 20000 cm⁻¹</text>
<text x="688" y="1209.66" font-size="23" font-weight="400" fill="#326991">800 nm → 12500 cm⁻¹</text>
<rect x="1305" y="1090" width="520" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1323" y="1126" font-size="25" font-weight="600" fill="#b72d4a">驗算／常見斷點</text>
<text x="1323" y="1177" font-size="23" font-weight="400" fill="#b72d4a">長波 → 低波數。</text>
<text x="1323" y="1209.66" font-size="23" font-weight="400" fill="#b72d4a">10⁷ 只適用指定 nm／cm⁻¹ 單位。</text>
<text x="1323" y="1242.32" font-size="23" font-weight="400" fill="#b72d4a">單位錯 → M03 重換算。</text>
<rect x="50" y="1395" width="1800" height="350" rx="18" fill="#d9eeea" stroke="#61717a" stroke-width="2"/>
<text x="75" y="1439" font-size="28" font-weight="600" fill="#24343f">C2｜能量守恆｜L1、L4；F03</text>
<rect x="75" y="1475" width="570" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="93" y="1511" font-size="25" font-weight="600" fill="#24343f">母式／量與單位</text>
<text x="93" y="1562" font-size="23" font-weight="400" fill="#24343f">E₀＋E_i＝Eₛ＋E_f</text>
<text x="93" y="1594.66" font-size="23" font-weight="400" fill="#24343f">Δν̃＝ν̃₀−ν̃ₛ＝(E_f−E_i)/(hc)</text>
<text x="93" y="1627.32" font-size="23" font-weight="400" fill="#24343f">i／f：分子初／末態</text>
<rect x="670" y="1475" width="610" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="688" y="1511" font-size="25" font-weight="600" fill="#326991">紙筆例（均為自編）</text>
<text x="688" y="1562" font-size="23" font-weight="400" fill="#326991">20000−1000＝19000 → 長波</text>
<text x="688" y="1594.66" font-size="23" font-weight="400" fill="#326991">20000＋1000＝21000 → 短波</text>
<rect x="1305" y="1475" width="520" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1323" y="1511" font-size="25" font-weight="600" fill="#b72d4a">驗算／常見斷點</text>
<text x="1323" y="1562" font-size="23" font-weight="400" fill="#b72d4a">Stokes 正；anti-Stokes 負。</text>
<text x="1323" y="1594.66" font-size="23" font-weight="400" fill="#b72d4a">算 J 時 c 與波數長度單位須一致。</text>
<text x="1323" y="1627.32" font-size="23" font-weight="400" fill="#b72d4a">方向錯 → M03 重列能量帳。</text>
<rect x="50" y="1780" width="1800" height="350" rx="18" fill="#dceaf7" stroke="#61717a" stroke-width="2"/>
<text x="75" y="1824" font-size="28" font-weight="600" fill="#24343f">C3｜換雷射｜L4；F06、F07</text>
<rect x="75" y="1860" width="570" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="93" y="1896" font-size="25" font-weight="600" fill="#24343f">母式／量與單位</text>
<text x="93" y="1947" font-size="23" font-weight="400" fill="#24343f">ν̃ₛ＝ν̃₀−Δν̃</text>
<text x="93" y="1979.66" font-size="23" font-weight="400" fill="#24343f">λₛ＝10⁷／ν̃ₛ</text>
<rect x="670" y="1860" width="610" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="688" y="1896" font-size="25" font-weight="600" fill="#326991">紙筆例（均為自編）</text>
<text x="688" y="1947" font-size="23" font-weight="400" fill="#326991">800 nm：12500−1000＝11500</text>
<text x="688" y="1979.66" font-size="23" font-weight="400" fill="#326991">10⁷／11500＝20000／23≈869.6 nm</text>
<rect x="1305" y="1860" width="520" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1323" y="1896" font-size="25" font-weight="600" fill="#b72d4a">驗算／常見斷點</text>
<text x="1323" y="1947" font-size="23" font-weight="400" fill="#b72d4a">同模式與物態下位移近似同。</text>
<text x="1323" y="1979.66" font-size="23" font-weight="400" fill="#b72d4a">峰高、背景與波長差不一定同。</text>
<text x="1323" y="2012.32" font-size="23" font-weight="400" fill="#b72d4a">混量 → M03 分列位移／波長。</text>
<rect x="50" y="2165" width="1800" height="350" rx="18" fill="#dceaf7" stroke="#61717a" stroke-width="2"/>
<text x="75" y="2209" font-size="28" font-weight="600" fill="#24343f">C4｜兩波長反算｜L4；F06</text>
<rect x="75" y="2245" width="570" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="93" y="2281" font-size="25" font-weight="600" fill="#24343f">母式／量與單位</text>
<text x="93" y="2332" font-size="23" font-weight="400" fill="#24343f">Δν̃＝10⁷(1/λ₀−1/λₛ)</text>
<text x="93" y="2364.66" font-size="23" font-weight="400" fill="#24343f">兩個 λ 均以 nm 代入</text>
<rect x="670" y="2245" width="610" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="688" y="2281" font-size="25" font-weight="600" fill="#326991">紙筆例（均為自編）</text>
<text x="688" y="2332" font-size="23" font-weight="400" fill="#326991">500、625 nm：20000−16000</text>
<text x="688" y="2364.66" font-size="23" font-weight="400" fill="#326991">＝＋4000 cm⁻¹；Stokes</text>
<rect x="1305" y="2245" width="520" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1323" y="2281" font-size="25" font-weight="600" fill="#b72d4a">驗算／常見斷點</text>
<text x="1323" y="2332" font-size="23" font-weight="400" fill="#b72d4a">先各自倒數，再相減。</text>
<text x="1323" y="2364.66" font-size="23" font-weight="400" fill="#b72d4a">10⁷／(625−500)＝80000 是錯法。</text>
<text x="1323" y="2397.32" font-size="23" font-weight="400" fill="#b72d4a">錯倒數 → M03 各取倒數再減。</text>
<rect x="50" y="2550" width="1800" height="350" rx="18" fill="#f5dfe2" stroke="#61717a" stroke-width="2"/>
<text x="75" y="2594" font-size="28" font-weight="600" fill="#24343f">C5｜已驗證線性內插｜L9；F14</text>
<rect x="75" y="2630" width="570" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="93" y="2666" font-size="25" font-weight="600" fill="#24343f">母式／量與單位</text>
<text x="93" y="2717" font-size="23" font-weight="400" fill="#24343f">S＝aC＋b</text>
<text x="93" y="2749.66" font-size="23" font-weight="400" fill="#24343f">(C−C₁)/(C₂−C₁)＝(S−S₁)/(S₂−S₁)</text>
<rect x="670" y="2630" width="610" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="688" y="2666" font-size="25" font-weight="600" fill="#326991">紙筆例（均為自編）</text>
<text x="688" y="2717" font-size="23" font-weight="400" fill="#326991">10%→20 a.u.；20%→40 a.u.</text>
<text x="688" y="2749.66" font-size="23" font-weight="400" fill="#326991">未知 30：C＝10%＋(10/20)×10%</text>
<text x="688" y="2782.32" font-size="23" font-weight="400" fill="#326991">＝15% w/w</text>
<rect x="1305" y="2630" width="520" height="245" rx="18" fill="#fff" stroke="#61717a" stroke-width="2"/>
<text x="1323" y="2666" font-size="25" font-weight="600" fill="#b72d4a">驗算／常見斷點</text>
<text x="1323" y="2717" font-size="23" font-weight="400" fill="#b72d4a">固定功率、聚焦、基質與處理。</text>
<text x="1323" y="2749.66" font-size="23" font-weight="400" fill="#b72d4a">不外插；兩點本身不證明線性。</text>
<text x="1323" y="2782.32" font-size="23" font-weight="400" fill="#b72d4a">取樣不合 → M02；校正不合 → M04。</text>
<rect x="50" y="2970" width="1800" height="340" rx="18" fill="#f5dfe2" stroke="#b72d4a" stroke-width="2"/>
<text x="72" y="3011" font-size="27" font-weight="600" fill="#b72d4a">L10 補充｜人口比只讀方向；不是第六組來源計算</text>
<text x="72" y="3058" font-size="24" font-weight="400" fill="#24343f">熱平衡近似：N₁／N₀＝exp[−ΔE／(kBT)]；T 用 K，簡併另計或忽略。</text>
<text x="72" y="3092.08" font-size="24" font-weight="400" fill="#24343f">固定 ΔE，T 升高 → 負指數絕對值變小 → 高振動態人口比例增加 → anti-Stokes 相對訊號通常增加。</text>
<text x="72" y="3126.16" font-size="24" font-weight="400" fill="#24343f">這不是完整強度比公式；精確測溫還需頻率因子、相對響應校正與適用模型。</text>
<text x="50" y="3482" font-size="20" font-weight="400" fill="#61717a">a.u.＝任意單位；w/w＝質量／質量；a＝斜率；b＝截距。λ＝真空波長慣例；ν̃＝波數；Δν̃＝有號 Raman 位移。</text>
<text x="50" y="3518" font-size="20" font-weight="400" fill="#61717a">原題：ch30 PDF；正文：建構講義 v3.0。M＝大循環站；L＝理解模組；P＝方法條目。示意不按比例。</text>
</svg>

[[藥物分析_拉曼光譜_公式與誤差判讀總表_v3_0.svg|開啟獨立 SVG]]

圖源：`藥物分析_拉曼光譜_公式與誤差判讀總表_v3_0.svg`。若閱讀器限制原碼SVG，可用同資料夾嵌入 `![[藥物分析_拉曼光譜_公式與誤差判讀總表_v3_0.svg]]`。

## Part V｜看到題幹，選對補鏈入口

^rm-c-route


|觸發字|最短問題|回查|
|---|---|---|
|放射／吸收|在問題本分類，還是實際物理機制？|[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-classification\|補完整推導]]|
|對稱鍵／互補|這個模式改的是α還是μ？|[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3\|補完整推導]]|
|nm／cm⁻¹／換雷射|是在講λ₀、λₛ還是Δν̃？|[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4\|補完整推導]]|
|Rayleigh／Tyndall／弱|能量分類、粒子分類是否混用？|[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l5\|補完整推導]]|
|螢光物質不能測|是否把可處理的干擾寫成絕對不可能？|[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6\|補完整推導]]|
|包裝／裸錠／溶液|實際有哪些成分被照到？|[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7\|補完整推導]]|
|晶型／多形體|原固態有沒有被處理或雷射改掉？|[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l8\|補完整推導]]|
|FT／制酸錠／定量|是指定題本例，還是一般方法能力？|[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9\|補完整推導]]|


[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]

## 全題目打靶表｜8題

^rm-c-targets


|題號／PDF頁|題本答案|觸發|最短理由／回查|
|---|---|---|---|
|114-1-16／p.1|C|Raman與IR比較|標準Raman橫軸為cm⁻¹位移，不是把它一概寫成nm。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q1\|逐項解析]]|
|113-1-18／p.1–2|A|散射強弱／FT定量／晶型|題本以Raman較弱否定此排序；不外推任意樣品的固定強度次序。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q2\|逐項解析]]|
|112-2-12／p.2–3|C|光路／波長／螢光／包裝|「無法檢測具螢光物質」過度絕對；適合激發與背景處理可能取得可用訊號。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q3\|逐項解析]]|
|110-1-20／p.3|C|一般應用與定量|題本將「常用於定量」列錯；保留本題答案，不改寫成Raman物理上不能定量。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q4\|逐項解析]]|
|109-1-24／p.3|B|制酸錠成分含量|Raman為印刷答案；解析列FT-Raman測Glycine（甘胺酸）及Calcium carbonate（碳酸鈣）。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q5\|逐項解析]]|
|108-1-27／p.3|C|位移單位與光譜範圍|不能把Raman光譜一概等同遠紅外；光源、散射光及振動位移須分開。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q6\|逐項解析]]|
|107-1-2／p.4|D|題本放射分類|按題本選Raman；學理分類是非彈性散射，不以偵測器放旁邊定義放射。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q7\|逐項解析]]|
|104-1-14／p.4|B|四種方法定量比較|題本最不適用選Raman；這是本題慣例，不是否認一般Raman定量技術。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q8\|逐項解析]]|


PDF頁碼依實際4頁計；113-1題幹在第1頁、解析在第2頁；112-2題幹在第2頁、解析在第3頁。
[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]

### Q01｜114-1-16：Raman與IR比較

^rm-c-q1

**來源：**附件 PDF p.1；114-1 第 16 題。以下保留原題文字、四選項與順序；僅合併斷行並將 cm-1 排成 cm⁻¹。

**原題：**下列關於拉曼光譜法(Raman spectroscopy)與紅外光光譜法(Infrared spectrophotometry)之比較，何者錯誤？

- **(A)** 紅外光光譜為吸收光光譜，拉曼光譜為放射光光譜
- **(B)** 紅外光光譜法較適用於不對稱分子鍵，拉曼光譜法較適用於對稱分子鍵
- **(C)** 紅外光光譜以cm⁻¹ 表示，拉曼光譜以nm 表示
- **(D)** 兩者皆可應用於測定待測物之官能基

**題本印刷答案：C。**

**它問什麼／最短推理：**問錯誤比較。IR 與 Raman 常都用 cm⁻¹；前者是吸收波數，後者是位移，故 C 的 nm 一概說法錯。

|選項|逐項判讀|
|---|---|
|A|題本接受IR吸收、Raman放射；物理上Raman應單列非彈性散射。|
|B|題本接受對稱／不對稱偏好；精確標準是模式中的α／μ變化。|
|C|標準Raman橫軸為cm⁻¹位移，不是把它一概寫成nm。|
|D|兩者的振動特徵皆可支持官能基與指紋分析。|


[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4|補核心理由]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]。

精準路由：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4|L4]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3|L3]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l1|L1]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f6|F06]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f5|F05]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f1|F01]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc1|C1]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc4|C4]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-q1|回此題反查]]。

**VQ1｜換條件再驗證（自編，非來源題）：**若改問：500 nm 雷射、位移 +1000 cm⁻¹，散射光是否 10000 nm？

<details>
<summary>展開最小變化題答案</summary>

否。先求入射 20000，再減 1000 得 19000 cm⁻¹，取倒數約 526.3 nm。

</details>

### Q02｜113-1-18：散射強弱／FT定量／晶型

^rm-c-q2

**來源：**附件 PDF p.1–2；113-1 第 18 題。以下保留原題文字、四選項與順序；僅合併斷行並將 cm-1 排成 cm⁻¹。

**原題：**有關拉曼光譜的敘述，下列何者錯誤？

- **(A)** 各種散射效應的強弱順序為：Rayleigh＞Raman＞Tyndall
- **(B)** 一般在中紅外光區吸收較弱的官能基，會有較強的拉曼吸收
- **(C)** FT-Raman 技術可應用於藥品之定量分析
- **(D)** Raman 技術可應用於固體藥品中多形體的檢測

**題本印刷答案：A。**

**它問什麼／最短推理：**問錯誤。按題本以 Raman 弱於 Rayleigh／Tyndall 的比較，A 的排序不合；一般學理也不能將不同樣品、粒子與收集條件混成固定全序。

|選項|逐項判讀|
|---|---|
|A|題本以Raman較弱否定此排序；不外推任意樣品的固定強度次序。|
|B|IR弱的模式可能Raman較強；題中「拉曼吸收」應理解為散射訊號。|
|C|FT-Raman可在合適校正下定量；不是FT才具有定量可能。|
|D|固體保留晶格環境，Raman可用於多晶型比較。|


[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l5|補核心理由]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]。

精準路由：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l5|L5]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3|L3]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9|L9]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f2|F02]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f10|F10]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f14|F14]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-q2|回此題反查]]。

**VQ2｜換條件再驗證（自編，非來源題）：**若某模式 IR 弱，是否必定 Raman 強？

<details>
<summary>展開最小變化題答案</summary>

不一定；需分別看偶極矩與極化率沿模式的變化，也要看量測條件。

</details>

### Q03｜112-2-12：光路／波長／螢光／包裝

^rm-c-q3

**來源：**附件 PDF p.2–3；112-2 第 12 題。以下保留原題文字、四選項與順序；僅合併斷行並將 cm-1 排成 cm⁻¹。

**原題：**關於拉曼光譜儀的敘述，下列何者錯誤？

- **(A)** 檢測光路之垂直設計與螢光光譜儀類似
- **(B)** 光源之波長為450～800 nm
- **(C)** 無法檢測具螢光之物質
- **(D)** 可以穿透包裝進行裸錠檢測

**題本印刷答案：C。**

**它問什麼／最短推理：**問錯誤。螢光可能遮住 Raman；改激發與處理背景可能取得可用譜，所以 C 的「無法」過度絕對。

|選項|逐項判讀|
|---|---|
|A|90°是題本接受的配置，實際也常見背向收集。|
|B|450–800 nm是題本接受的範圍敘述；不是排除1064 nm的硬規則。|
|C|「無法檢測具螢光物質」過度絕對；適合激發與背景處理可能取得可用訊號。|
|D|合適包裝可透光量測；不是任何包裝皆成立。|


[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6|補核心理由]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]。

精準路由：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6|L6]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7|L7]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l5|L5]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f7|F07]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f8|F08]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f9|F09]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f11|F11]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-q3|回此題反查]]。

**VQ3｜換條件再驗證（自編，非來源題）：**換成 1064 nm 後完全沒有峰，可以直接說樣品 Raman 不活性嗎？

<details>
<summary>展開最小變化題答案</summary>

不可以；先查光學／偵測匹配、濾片、訊噪與取樣。背景減少不保證訊號足夠。

</details>

### Q04｜110-1-20：一般應用與定量

^rm-c-q4

**來源：**附件 PDF p.3；110-1 第 20 題。以下保留原題文字、四選項與順序；僅合併斷行並將 cm-1 排成 cm⁻¹。

**原題：**關於拉曼光譜分析應用的敘述，下列何者錯誤？

- **(A)** 常用於建立藥物的指紋區
- **(B)** 可直接檢測製劑中的有效成分
- **(C)** 常用於定量分析
- **(D)** 可鑑定原料藥晶形

**題本印刷答案：C。**

**它問什麼／最短推理：**問錯誤應用。題本將「常用於定量」列 C；同時 Raman 在有校正、取樣與驗證的條件下可定量，兩層分開存。

|選項|逐項判讀|
|---|---|
|A|可用特徵峰群建立藥物指紋。|
|B|合適配置可直接檢測製劑API；取樣與背景仍需處理。|
|C|題本將「常用於定量」列錯；保留本題答案，不改寫成Raman物理上不能定量。|
|D|固態振動與晶格環境差異可支持晶型鑑別。|


[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9|補核心理由]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]。

精準路由：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9|L9]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7|L7]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l8|L8]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f11|F11]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f12|F12]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f14|F14]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc5|C5]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-q4|回此題反查]]。

**VQ4｜換條件再驗證（自編，非來源題）：**同含量錠劑換焦點後訊號加倍，可以直接報含量加倍嗎？

<details>
<summary>展開最小變化題答案</summary>

不可以；焦點與代表性取樣改變，先回 M02／L7、L9 查條件。

</details>

### Q05｜109-1-24：制酸錠成分含量

^rm-c-q5

**來源：**附件 PDF p.3；109-1 第 24 題。以下保留原題文字、四選項與順序；僅合併斷行並將 cm-1 排成 cm⁻¹。

**原題：**下列方法何者可用於直接分析制酸錠中甘胺酸（glycine）和碳酸鈣的含量？

- **(A)** 紫外光光譜
- **(B)** Raman 光譜
- **(C)** 串聯式液相層析質譜儀
- **(D)** 原子吸收光譜

**題本印刷答案：B。**

**它問什麼／最短推理：**問指定制酸錠中兩成分的直接含量分析。題本印刷答案 B Raman，解析另提 FT-Raman；不是證明只有 FT 能定量。

|選項|逐項判讀|
|---|---|
|A|本題不選UV，未提供能直接分辨兩成分的UV方法。|
|B|Raman為印刷答案；解析列FT-Raman測Glycine（甘胺酸）及Calcium carbonate（碳酸鈣）。|
|C|本題不選LC-MS/MS，與所問直接錠劑應用不同。|
|D|AAS可提供元素資訊，但不是本題同時直接分析兩成分的答案。|


[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9|補核心理由]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]。

精準路由：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9|L9]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7|L7]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f14|F14]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f11|F11]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc5|C5]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-q5|回此題反查]]。

**VQ5｜換條件再驗證（自編，非來源題）：**若題幹只給「FT-Raman」名稱、沒有標準與驗證，可否直接換峰高成含量？

<details>
<summary>展開最小變化題答案</summary>

不可以。取得光譜的配置不會補出校正、基質條件與代表性取樣。

</details>

### Q06｜108-1-27：位移單位與光譜範圍

^rm-c-q6

**來源：**附件 PDF p.3；108-1 第 27 題。以下保留原題文字、四選項與順序；僅合併斷行並將 cm-1 排成 cm⁻¹。

**原題：**下列有關拉曼光譜分析（Raman spectroscopy）之敘述，何者錯誤？

- **(A)** 可用於具對稱性鍵結之結構分析
- **(B)** 單位為cm⁻¹
- **(C)** 其光譜範圍相當於遠紅外光譜
- **(D)** 提供額外的指紋鑑別資訊，可互補紅外光譜

**題本印刷答案：C。**

**它問什麼／最短推理：**問錯誤。激發光波長、散射光波長與兩者能量差是不同量；不能把 Raman 全部等同遠紅外光譜，故 C。

|選項|逐項判讀|
|---|---|
|A|對稱相關振動是Raman常見應用入口。|
|B|cm⁻¹為位移常用單位。|
|C|不能把Raman光譜一概等同遠紅外；光源、散射光及振動位移須分開。|
|D|選擇律不同，提供互補IR的指紋資訊。|


[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4|補核心理由]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]。

精準路由：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4|L4]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3|L3]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6|L6]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f6|F06]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f7|F07]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f10|F10]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-q6|回此題反查]]。

**VQ6｜換條件再驗證（自編，非來源題）：**雷射波長是可見光，是否代表 Raman 只能量可見光能量的振動？

<details>
<summary>展開最小變化題答案</summary>

不是；振動由入射與散射的能量差讀出。適當低頻配置也可讀低能晶格模式。

</details>

### Q07｜107-1-2：題本放射分類

^rm-c-q7

**來源：**附件 PDF p.4；107-1 第 2 題。以下保留原題文字、四選項與順序；僅合併斷行並將 cm-1 排成 cm⁻¹。

**原題：**下列何者屬於放射（emission）光譜？

- **(A)** 可見光譜
- **(B)** 紫外光光譜
- **(C)** 紅外光光譜
- **(D)** 拉曼光譜

**題本印刷答案：D。**

**它問什麼／最短推理：**按本題四選項的放射／吸收分類慣例選 D Raman；實際物理機制記為非彈性散射，與螢光的真實激發態放射分開。

|選項|逐項判讀|
|---|---|
|A|此題可見光指常規UV-Vis吸收。|
|B|此題紫外光指常規UV-Vis吸收。|
|C|此題IR為振動吸收。|
|D|按題本選Raman；學理分類是非彈性散射，不以偵測器放旁邊定義放射。|


[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-classification|補核心理由]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]。

精準路由：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l1|L1]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l2|L2]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f1|F01]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-q7|回此題反查]]。

**VQ7｜換條件再驗證（自編，非來源題）：**把偵測器放在 90°，是否已能判定光一定是 Raman？

<details>
<summary>展開最小變化題答案</summary>

不能；角度不是物理機制。需分清散射能量差、選擇律與螢光等背景。

</details>

### Q08｜104-1-14：四種方法定量比較

^rm-c-q8

**來源：**附件 PDF p.4；104-1 第 14 題。以下保留原題文字、四選項與順序；僅合併斷行並將 cm-1 排成 cm⁻¹。

**原題：**下列光譜法中，何者最不適用於定量分析？

- **(A)** 質譜法
- **(B)** 拉曼光譜法
- **(C)** 核磁共振光譜法
- **(D)** 原子吸收光譜法

**題本印刷答案：B。**

**它問什麼／最短推理：**問「最不適用」。題本比較答案 B Raman；保留此題答案，不據此禁止所有已驗證 Raman 定量方法。

|選項|逐項判讀|
|---|---|
|A|MS可在合適校正與條件下定量。|
|B|題本最不適用選Raman；這是本題慣例，不是否認一般Raman定量技術。|
|C|NMR也有經設計與驗證的定量方法。|
|D|AAS常用於元素定量；需校正及干擾處理。|


[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9|補核心理由]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-targets|返回複習]]。

精準路由：[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9|L9]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-f14|F14]]、[[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc5|C5]]；[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-q8|回此題反查]]。

**VQ8｜換條件再驗證（自編，非來源題）：**色散式已校正並獨立驗證，FT-Raman 卻沒有校正；誰已有可評估的含量依據？

<details>
<summary>展開最小變化題答案</summary>

前者。配置名稱不是定量門票；仍須查校正範圍、取樣與未知樣品是否適用。

</details>

## Part VI｜全章固定輸入F01–F15

^rm-c-fixed


|代碼|固定輸入|條件與補鏈|
|---|---|---|
|F01|Raman物理分類：非彈性散射；IR是吸收。|107-1選D、114-1接受「放射」題本用語，另保留物理分類。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l1\|補鏈]]|
|F02|Rayleigh彈性、Raman非彈性；Tyndall常見於膠體粒子散射。|113-1 A錯；不背無條件三者固定全序或「只來自溶劑」。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l5\|補鏈]]|
|F03|Stokes失去光子能量、λₛ較長；anti-Stokes相反。|同一模式兩側位移絕對值相同；峰高不必相同。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l1\|補鏈]]|
|F04|一般Raman不需先在激發波長有真實電子吸收。|可Raman活性仍須振動改極化率；IR也不需UV-Vis發色團。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l2\|補鏈]]|
|F05|Raman看振動造成的α改變；IR看μ改變。|對稱／不對稱是入口；嚴格互斥需反演中心。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3\|補鏈]]|
|F06|標準Raman圖：位移cm⁻¹；IR常用吸收波數cm⁻¹。|同單位不同量；雷射波長nm、散射絕對波長另列。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4\|補鏈]]|
|F07|112-2題本接受450–800 nm；常見實際配置另有785、1064 nm與UV。|不是整個Raman的硬範圍，也不能把108-1推成沒有低頻Raman。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6\|補鏈]]|
|F08|較長波NIR可減少許多樣品的螢光背景。|不保證完全消除；Raman效率與偵測條件同時改變。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6\|補鏈]]|
|F09|有90°側向收集，也有180°背向散射；兩種主配置為色散式及FT式。|112-2接受90°敘述不代表全都90°；FT不是偵測器名稱。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-operations\|補鏈]]|
|F10|Raman與IR可提供互補振動／指紋資訊。|不能直接推IR弱的每一峰都Raman強。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3\|補鏈]]|
|F11|可直接測合適固體／製劑、做指紋；可透過合適包裝。|要排包裝／溶劑背景，並確認取樣代表性。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7\|補鏈]]|
|F12|可分析原料藥與固體製劑的多晶型。|峰群及參考物一起看；不背Raman永遠比XRD／IR靈敏。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l8\|補鏈]]|
|F13|題本晶型方法家族：Raman、NIR、適當IR、固態NMR、XRD。|KBr壓錠被解析排除；關鍵是前處理改樣風險。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-solid\|補鏈]]|
|F14|109-1制酸錠Glycine（甘胺酸）＋Calcium carbonate（碳酸鈣）→B Raman；解析指定FT-Raman。|110-1 C／104-1 B保留；Raman定量不只這一例。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9\|補鏈]]|
|F15|溶劑本身可有Raman峰或螢光背景。|用空白、選峰及方法設計處理；不是Raman不能測溶液。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7\|補鏈]]|


### F 逐條定位｜數字、題本慣例與條件

**F01｜**Raman物理分類：非彈性散射；IR是吸收。

^rm-c-f1

107-1選D、114-1接受「放射」題本用語，另保留物理分類。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l1|補鏈]]

**F02｜**Rayleigh彈性、Raman非彈性；Tyndall常見於膠體粒子散射。

^rm-c-f2

113-1 A錯；不背無條件三者固定全序或「只來自溶劑」。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l5|補鏈]]

**F03｜**Stokes失去光子能量、λₛ較長；anti-Stokes相反。

^rm-c-f3

同一模式兩側位移絕對值相同；峰高不必相同。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l1|補鏈]]

**F04｜**一般Raman不需先在激發波長有真實電子吸收。

^rm-c-f4

可Raman活性仍須振動改極化率；IR也不需UV-Vis發色團。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l2|補鏈]]

**F05｜**Raman看振動造成的α改變；IR看μ改變。

^rm-c-f5

對稱／不對稱是入口；嚴格互斥需反演中心。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3|補鏈]]

**F06｜**標準Raman圖：位移cm⁻¹；IR常用吸收波數cm⁻¹。

^rm-c-f6

同單位不同量；雷射波長nm、散射絕對波長另列。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4|補鏈]]

**F07｜**112-2題本接受450–800 nm；常見實際配置另有785、1064 nm與UV。

^rm-c-f7

不是整個Raman的硬範圍，也不能把108-1推成沒有低頻Raman。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6|補鏈]]

**F08｜**較長波NIR可減少許多樣品的螢光背景。

^rm-c-f8

不保證完全消除；Raman效率與偵測條件同時改變。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6|補鏈]]

**F09｜**有90°側向收集，也有180°背向散射；兩種主配置為色散式及FT式。

^rm-c-f9

112-2接受90°敘述不代表全都90°；FT不是偵測器名稱。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-operations|補鏈]]

**F10｜**Raman與IR可提供互補振動／指紋資訊。

^rm-c-f10

不能直接推IR弱的每一峰都Raman強。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3|補鏈]]

**F11｜**可直接測合適固體／製劑、做指紋；可透過合適包裝。

^rm-c-f11

要排包裝／溶劑背景，並確認取樣代表性。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7|補鏈]]

**F12｜**可分析原料藥與固體製劑的多晶型。

^rm-c-f12

峰群及參考物一起看；不背Raman永遠比XRD／IR靈敏。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l8|補鏈]]

**F13｜**題本晶型方法家族：Raman、NIR、適當IR、固態NMR、XRD。

^rm-c-f13

KBr壓錠被解析排除；關鍵是前處理改樣風險。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-solid|補鏈]]

**F14｜**109-1制酸錠Glycine（甘胺酸）＋Calcium carbonate（碳酸鈣）→B Raman；解析指定FT-Raman。

^rm-c-f14

110-1 C／104-1 B保留；Raman定量不只這一例。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9|補鏈]]

**F15｜**溶劑本身可有Raman峰或螢光背景。

^rm-c-f15

用空白、選峰及方法設計處理；不是Raman不能測溶液。 [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7|補鏈]]

F是數字、專名、題本答案及適用條件的存檔點；能推得的因果回L，不把全部教材句子都當成不可推導的死背。
[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-fixed|返回複習]]

## 來源與本版校正

^rm-c-evidence

**附件來源：**《ch30 光譜分析-拉曼光譜.pdf》4 頁／8 題、建構講義與複習導航 v2.0、四個獨立 SVG 及講義內嵌的第五張母圖；另依《藥物分析_大循環小循環_雙檔章節編譯器_v3_0.md》編排。8 題按原順序完整保留，所有答案稱「題本印刷答案」，本次未逐題比對考選部公告。題幹為文字題；p.2 能階圖是解析用圖，新版以同原理重繪，不把它冒充題幹。

**本版對照：**10 條舊 L、28 個深入抽問與舊定位保留；四站改為統一角色；新增完整基本例、六個存檔點、同號閉卷卡、每組紙筆練習與 8 個最小變化題。5 張 SVG 為可編輯向量，兩份 Markdown 內嵌皆與獨立檔完全相同。附件沒有獨立數值題；C1–C5、C-P 練習與 VQ 均為自編，人口比為補鏈。

**補充核對（2026-10-01；一手來源）：**

- S3 [Renishaw：Multiple lasers and gratings](https://www.renishaw.com/cs/multiple-lasers-and-gratings-for-raman-and-pl-spectroscopy--25938)：核對激發波長、螢光干擾、Rayleigh 濾片與低頻譜窗；元件要匹配激發。
- S4 [Bruker：RAM II](https://www.bruker.com/en/products-and-solutions/raman-spectroscopy/raman-spectrometers/ram-ii-ft-raman-module.html)：核對 FT-Raman 的 1064 nm、Ge／InGaAs 偵測及可選 90°配置；不能排除近紅外。
- S5 [Bruker：Raman FAQ](https://www.bruker.com/en/products-and-solutions/raman-spectroscopy/raman-basics/raman-faq.html)：核對非彈性散射、波數軸與參考樣品校正下的定量可能。
- S7 [Shimadzu：KBr pellet method](https://www.shimadzu.com/an/service-support/technical-support/ftir/essential_knowledge/kbr.html)：核對壓錠、水分與部分樣品離子交換可能造成譜差；不能說每次壓片必定轉晶。
- S8 [NIST：Development and Certification of Standard Reference Materials for Relative Raman Intensity Calibration](https://www.nist.gov/publications/development-and-certification-nist-standard-reference-materials-relative-raman)：核對相對強度需要儀器響應校正，峰位校正與強度校正分開。

**保留的舊版術語入口：**S1 [IUPAC Raman scattering](https://goldbook.iupac.org/terms/view/08667)、[Raman wavenumber shift](https://goldbook.iupac.org/terms/view/08671)、[anti-Stokes](https://goldbook.iupac.org/terms/view/08570)；S2 [HORIBA 群論與選擇律](https://www.horiba.com/fileadmin/uploads/Scientific/Documents/Raman/Specy_Workbench-DT-Practical_Group_Theory__Raman_Spectroscopy-part_1.pdf)。本次這些入口回傳 403，未聲稱重新全文核讀；選擇律與虛擬態說明沿用已提供 v2.0，物理分類另以 S5 核對。

**題本語言與學理各有位置：**107-1「放射」選 D；110-1「常用定量」與 104-1「最不適用」分別保留 C、B；113-1「拉曼吸收」只留在原題，不拿來定義機制。一般機制為非彈性散射，定量需適當校正與驗證，並不只限於制酸錠一例。450–800 nm 是指定題接受的敘述，不是全體儀器硬範圍。

**保留科學界線：**一般互補不等於全峰互斥；互斥須反演中心與基本振動前提。FT 不是偵測器，也不保證消除螢光。任何包裝、任一焦點與任一功率都不保證可用；Raman／IR／XRD 沒有跨全部樣品的固定靈敏度排序。原稿遠紅外 10⁴～10⁶ 未標單位，未補造後當標準。本章主教自發振動 Raman；共振僅用來界定強度與電子吸收的關係，SERS、CARS 等留進階章節。

[[藥物分析_拉曼光譜_複習導航_v3_0#^rm-r-evidence|回複習來源]]。

## 舊定位轉接

保留舊ID供轉接；若既有外部連結包含舊檔名，仍需同步改成這份實際新檔名。

舊定位 `pa-home` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-home|本版對應段落]]

^pa-home

舊定位 `pa-01` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-classification|本版對應段落]]

^pa-01

舊定位 `pa-02` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l5|本版對應段落]]

^pa-02

舊定位 `pa-03` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l1|本版對應段落]]

^pa-03

舊定位 `pa-04` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l2|本版對應段落]]

^pa-04

舊定位 `pa-05` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3|本版對應段落]]

^pa-05

舊定位 `pa-06` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4|本版對應段落]]

^pa-06

舊定位 `pa-f01` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc2|本版對應段落]]

^pa-f01

舊定位 `pa-07` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6|本版對應段落]]

^pa-07

舊定位 `pa-08` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l6|本版對應段落]]

^pa-08

舊定位 `pa-09` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-operations|本版對應段落]]

^pa-09

舊定位 `pa-10` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l3|本版對應段落]]

^pa-10

舊定位 `pa-11` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-applications|本版對應段落]]

^pa-11

舊定位 `pa-12` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l8|本版對應段落]]

^pa-12

舊定位 `pa-m13` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-solid|本版對應段落]]

^pa-m13

舊定位 `pa-13` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l9|本版對應段落]]

^pa-13

舊定位 `pa-m15` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l7|本版對應段落]]

^pa-m15

舊定位 `pa-tree` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-route|本版對應段落]]

^pa-tree

舊定位 `pa-f02` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc1|本版對應段落]]

^pa-f02

舊定位 `pa-c01` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc1|本版對應段落]]

^pa-c01

舊定位 `pa-c02` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-calc3|本版對應段落]]

^pa-c02

舊定位 `pa-c03` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-l4|本版對應段落]]

^pa-c03

舊定位 `pa-q01` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q7|本版對應段落]]

^pa-q01

舊定位 `pa-q02` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q2|本版對應段落]]

^pa-q02

舊定位 `pa-q03` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q3|本版對應段落]]

^pa-q03

舊定位 `pa-q04` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q1|本版對應段落]]

^pa-q04

舊定位 `pa-q05` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q6|本版對應段落]]

^pa-q05

舊定位 `pa-q06` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-q4|本版對應段落]]

^pa-q06

舊定位 `pa-traps` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-route|本版對應段落]]

^pa-traps

舊定位 `pa-60s` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-macro|本版對應段落]]

^pa-60s

舊定位 `pa-memo` → [[藥物分析_拉曼光譜_建構講義_v3_0#^rm-c-fixed|本版對應段落]]

^pa-memo

本版包含10條L、15項F、3張P1–P4方法卡、8題逐項解析及5個自編紙筆例；複習版有28題可摺疊答案。章內連結作靜態檢查，未宣稱已在你的Obsidian裝置實測。
