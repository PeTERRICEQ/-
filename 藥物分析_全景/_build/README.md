# 重新產生《藥物分析｜理化性質全景》

1. `python3 parse_q.py <講義資料夾> questions.json`：從 20 章建構講義抽出歷屆題（題幹＋選項、題本答案、回查 L）。
2. `python3 stats.py`：依 `tags.py` 的字典逐題標記（考點物件、藥物性質、五站、九條線），輸出 `questions_tagged.json`、`stats.json`。
3. `python3 build.py questions_tagged.json <輸出.html> [--font-css 本機字型 css]`：產生講義 HTML。文字在 `content.py`，樣式在 `style.css`，數字全部由題庫現算。
4. `node print.js <輸入.html> <輸出.pdf>`：用 Playwright 印成 A4 PDF。

補章節或改字：改 `content.py`（文字）或 `tags.py`（字典），重跑 2–4。

## 互動網頁《藥分全景》

5. `python3 parse_l.py <講義資料夾> lcards.json`：抽出每個 L 小節的精華（先問、短鏈、立即用一次、易錯、閉卷自問）；非水滴定改用 NAT 必背卡。
6. `python3 export_app.py questions_tagged.json lcards.json app_data.json`：把全景、L 卡、歷屆題整理成網頁資料。
7. `python3 build_app.py app_template.html app_data.json ../app/藥分全景.html`：產生可發布的單一網頁；`node test_app.js ../app/藥分全景.html <截圖資料夾>` 跑一次互動測試。
