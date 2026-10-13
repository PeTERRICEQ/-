# 重新產生《藥物分析｜理化性質全景》

1. `python3 parse_q.py ../../藥物分析_講義 questions.json`：從 20 章建構講義抽出歷屆題（題幹＋選項、題本答案、回查 L）。
2. `python3 stats.py`：依 `tags.py` 的字典逐題標記（考點物件、藥物性質、五站、九條線），輸出 `questions_tagged.json`、`stats.json`。
3. `python3 build.py questions_tagged.json <輸出.html> [--font-css 本機字型 css]`：產生講義 HTML。文字在 `content.py`，樣式在 `style.css`，數字全部由題庫現算。
4. `node print.js <輸入.html> <輸出.pdf>`：用 Playwright 印成 A4 PDF。

補章節或改字：改 `content.py`（文字）或 `tags.py`（字典），重跑 2–4。

## 互動網頁《藥分全景》

5. `python3 parse_l.py ../../藥物分析_講義 lcards.json`：抽出每個 L 小節的精華（先問、短鏈、立即用一次、易錯、閉卷自問）；非水滴定改用 NAT 必背卡。
6. `python3 export_app.py questions_tagged.json lcards.json app_data.json`：把全景、L 卡、歷屆題整理成網頁資料。
7. `python3 build_app.py app_template.html app_data.json ../app/藥分全景.html`：產生可發布的單一網頁；`node test_app.js ../app/藥分全景.html <截圖資料夾>` 跑一次互動測試。

## 互動網頁《藥分全景》新版（藥理藥化全景架構）

網頁連結（私人，更新沿用同一個）：https://claude.ai/artifact/TMy42ZiTsYyiCHkCkkYEse

單一頁面、四層放大：四本帳（能量帳、時間帳、質荷帳、點數帳）→ 帳 → 章（M 站主幹，L 掛下，源樣選測算掛在站上）→ 卡與題（右側焦點欄）。
視角：全景地圖、性質矩陣、五格矩陣（圖6）、Te 作戰表、我的筆記；`#r.<章>.<序>` 讀書模式、`#print` A4 版。
每章 5 張圖（大循環母圖、小循環掛載點、方法分類、儀器與操作、公式與誤差）＋全科圖0–6，圖上的 L、M 站、章名、帳名都能點。

8. `python3 pan/figs_src.py <上傳資料夾>`：85 張章節圖存進 `藥物分析_全科大中小循環/各章圖組/`（修正簡體字、補 width／height）。
9. `python3 pan/mount.py`：從每章圖2 讀出每張 L 掛在哪一個 M 站（NMR 用講義母圖的站別）。
10. `python3 pan/export.py`：輸出 `../app/data/index.json`、`q.json`、`ch/<章>.json` 與 `../app/fig/*.svg`。五格內容直接取自 `_generator/common.py`。

測試（先 `sh ../tests/serve.sh /tmp/yf-wt &`）：

```
node ../tests/smoke.js      # 30 個代表路由
node ../tests/interact.js   # 跳轉與返回、選取保留、題目、複習、舊版進度遷移、搜尋、手機抽屜、主題
node ../tests/crawl.js      # 1,547 個路由、每個內部連結、抽 40 個跳轉＋返回
node ../tests/figs.js       # 92 張圖、圖上可點的 L／M／章名
node ../tests/ipad.js       # iPad mini／Pro 11／Pro 12.9 直橫放
node ../tests/sync.js       # 兩台裝置共用模擬雲端：筆記與進度同步、舊版雲端進度帶入
node ../tests/backup.js     # 備份下載、手動加載
```

發布：`藥分全景.html` 為頁面，`data/`、`fig/` 以 Artifact 的 `files` 一起上傳；能力 `db`、`user`、`downloads`。

雲端資料只用每人私人空間 `data/users/<id>/`：`progress`（J／K 與日期）、`meta/notes/<格子代號>`（我的筆記）。
舊版的每章進度（`c01`…`c20`、本機 `yfqj:prog`）在第一次開新版時自動換成 J／K，只搬一次。
