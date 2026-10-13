# 藥分精華圖產生器

每章一份 spec（`specs/<章>.py` 的 `SPEC`）→ `lib.py` 排成 HTML → `print.js`（Playwright／Chromium）印成 PDF，輸出到 repo 根目錄的 `藥物分析_精華圖/`。

- **精華① 翻譯座標**：① 適配（探針 × 把柄、零件）＋② 位置（誰晚出、讀數在軸上的哪裡）
- **精華② 驗證座標**：③ 寬度＋④ 換量（斜率、背景、外標內標）＋⑤ 條件
- **精華③ 考點補完**：只在前兩頁漏掉很多考古題考點時才做

```
python3 essence/lib.py hplc        # 產生 PDF（每頁太滿會自動縮字，回報字級）
python3 essence/cover.py hplc      # 正解選項關鍵詞有沒有出現在頁面上（字面比對；未命中的要人工看）
```

字型（Noto Sans TC、Noto Serif TC、IBM Plex Mono）用 npm 的 @fontsource 套件，位置見 `lib.py` 檔頭。

spec 的格式看 `specs/hplc.py`：每頁 `left`／`right`／`full`／`bottom` 是方塊清單，方塊型別有 `flow`、`table`、`box`、`eqs`、`pairs`、`groups`。文字裡 `**粗體**`、`{{紅字}}`、`[[藍字]]`。
