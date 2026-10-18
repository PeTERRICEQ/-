"""藥分精華圖產生器：每章一份 spec（essence/specs/<章>.py 的 SPEC）→ HTML → PDF（1–3 頁，A4 橫式）。

格式仿藥理藥化精華圖（pharmacy-handbook 全景網頁/build/essence_lib.py），五軸改成藥分的峰方程式：
  ① 適配　② 位置　③ 寬度　④ 換量　⑤ 條件
  精華① 翻譯座標（①②）　精華② 驗證座標（③④⑤）　精華③ 考點補完（熱門章）

字型：Noto Sans TC／Noto Serif TC／IBM Plex Mono（npm 的 @fontsource 套件），放在 $YF_FONTS（預設 /home/user/fonts）：
  cd $YF_FONTS && for p in @fontsource/noto-sans-tc @fontsource/noto-serif-tc @fontsource/ibm-plex-mono; do npm pack $p; done
  再把每個 .tgz 解到同名資料夾。

用法：python3 essence/lib.py [章 key …]（不給就全部）
"""
import html, importlib, json, os, re, subprocess, sys


def load_spec(key):
    """用檔案路徑載入 specs/<key>.py（避免 gc 這類名字撞到內建模組）。"""
    import importlib.util
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "specs", f"{key}.py")
    sp = importlib.util.spec_from_file_location(f"yf_spec_{key}", path)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m.SPEC

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "../../.."))
OUT = os.path.join(REPO, "藥物分析_精華圖")
FONTS = os.environ.get("YF_FONTS", "/home/user/fonts")
VER = "v1_1"  # v1.1：依 100–115 年 1280 題的生成規則改版
sys.path.insert(0, os.path.join(HERE, "specs"))

# 四本帳的顏色（和全科圖、網頁一致）
LEDGER = {"nrg": ("#326991", "#dceaf7", "能量帳"), "time": ("#356844", "#dcecdc", "時間帳"),
          "mz": ("#685185", "#e8e1f2", "質荷帳"), "cnt": ("#9e771c", "#fff1c8", "點數帳")}
TONE = {  # 方塊色：框線、底色
    "key": ("#5b6b78", "#eef1f4"), "red": ("#b72d4a", "#f8e5e8"), "grn": ("#356844", "#e3f0e3"),
    "blu": ("#326991", "#e2edf8"), "pur": ("#685185", "#ece6f4"), "org": ("#b0621a", "#fbeadb"),
    "yel": ("#9e771c", "#fdf3d6"), "line": ("#61717a", "#ffffff"),
}
AXES = ["① 適配", "② 位置", "③ 寬度", "④ 換量", "⑤ 條件"]


def esc(s):
    return html.escape(str(s), quote=False)


def rich(s):
    """**粗體**、{紅字}、[[藍字]]；其餘照字面。"""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\{\{(.+?)\}\}", r'<span class="r">\1</span>', s)
    s = re.sub(r"\[\[(.+?)\]\]", r'<span class="g">\1</span>', s)
    return s


def cell(c):
    if isinstance(c, (list, tuple)):
        t, tone = c[0], c[1]
        w = c[2] if len(c) > 2 else 400
        col = {"red": "#b72d4a", "grn": "#356844", "blu": "#326991", "ink": "#1f2a31", "pur": "#685185", "org": "#b0621a"}.get(tone, tone)
        return f'<span style="color:{col};font-weight:{w}">{rich(t)}</span>'
    return rich(c)


# ───────── 方塊 ─────────
def b_flow(b, acc):
    out = [f'<div class="blk flow"><div class="bt" style="color:{acc}">{rich(b["title"])}</div>']
    for i, st in enumerate(b["steps"]):
        parts = "".join(f'<span class="chip"><b>{esc(k)}</b>{rich(v)}</span>' for k, v in st.get("parts", []))
        lines = "".join(f"<li>{rich(x)}</li>" for x in st.get("lines", []))
        tags = "".join(f'<div class="tag" style="--tb:{TONE[t][0]};--tf:{TONE[t][1]}"><b>{rich(k)}</b> {rich(v)}</div>'
                       for k, v, t in st.get("tags", []))
        out.append(f'<div class="st"><div class="sh"><span class="code" style="background:{acc}">{esc(st["code"])}</span>'
                   f'<b>{rich(st["name"])}</b></div>{("<div class=parts>" + parts + "</div>") if parts else ""}'
                   f'{("<ul>" + lines + "</ul>") if lines else ""}{tags}</div>')
        if i < len(b["steps"]) - 1:
            out.append('<div class="arr">▼</div>')
    out.append("</div>")
    return "".join(out)


def b_table(b, acc):
    cols = b["cols"]
    tw = sum(w for _, w in cols)
    head = "".join(f'<th style="width:{w / tw * 100:.1f}%">{rich(n)}</th>' for n, w in cols)
    rows = "".join("<tr>" + "".join(f"<td>{cell(c)}</td>" for c in r) + "</tr>" for r in b["rows"])
    note = f'<span class="note">{rich(b["note"])}</span>' if b.get("note") else ""
    return (f'<div class="blk tbl"><div class="bt" style="color:{acc}">{rich(b["title"])}{note}</div>'
            f'<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>')


def b_box(b, acc):
    bd, bg = TONE[b.get("tone", "line")]
    items = b["lines"]
    body = "".join(f"<li>{rich(x)}</li>" for x in items) if b.get("list", True) else "".join(f"<p>{rich(x)}</p>" for x in items)
    tag = "ul" if b.get("list", True) else "div"
    return (f'<div class="blk box" style="--bd:{bd};--bg:{bg}"><div class="bt" style="color:{bd}">{rich(b["title"])}</div>'
            f"<{tag}>{body}</{tag}></div>")


def b_eqs(b, acc):
    rows = []
    for t, f, ex in b["items"]:
        rows.append(f'<div class="eq"><div class="et">{rich(t)}</div><div class="ef">{rich(f)}</div>'
                    f'{("<div class=ex>" + rich(ex) + "</div>") if ex else ""}</div>')
    return f'<div class="blk eqs"><div class="bt" style="color:{acc}">{rich(b["title"])}</div>{"".join(rows)}</div>'


def b_pairs(b, acc):
    rows = "".join(f'<tr><td class="pa">{rich(a)}</td><td class="vs">↔</td><td class="pa">{rich(c)}</td><td>{rich(d)}</td></tr>'
                   for a, c, d in b["items"])
    return (f'<div class="blk pairs"><div class="bt" style="color:{acc}">{rich(b["title"])}</div>'
            f"<table><tbody>{rows}</tbody></table></div>")


def b_groups(b, acc):
    gs = []
    for t, lines, *tone in b["items"]:
        bd, bg = TONE[tone[0] if tone else "line"]
        gs.append(f'<div class="grp" style="--bd:{bd};--bg:{bg}"><div class="gt" style="color:{bd}">{rich(t)}</div>'
                  f'<ul>{"".join(f"<li>{rich(x)}</li>" for x in lines)}</ul></div>')
    return f'<div class="blk groups" style="--gc:{b.get("cols", 3)}">{"".join(gs)}</div>'


BLK = {"flow": b_flow, "table": b_table, "box": b_box, "eqs": b_eqs, "pairs": b_pairs, "groups": b_groups}


# ───────── pick up 版（v2）：本體 → 投影 ─────────
# 封閉動詞（全書 16 個）：每個本體開頭標一個
VERBS = [
    ("分配", "grn", "在兩相間按相似度分到兩邊"), ("解離", "org", "得失質子而帶電或不帶電"),
    ("吸收", "blu", "能量對上能階差就被吃掉"), ("放光", "yel", "激發態回基態時放出光子"),
    ("散射", "key", "光撞到分子或顆粒改方向"), ("遮蔽", "pur", "電子雲擋住外場或改變能階"),
    ("耦合", "pur", "鄰近自旋或振動互相傳話"), ("游離", "red", "中性分子被弄成離子"),
    ("遷移", "blu", "帶電粒子在電場或磁場中移動"), ("擴散", "key", "分子群自己散開"),
    ("計量", "grn", "照反應式定比例反應"), ("沉澱", "yel", "溶度積夠小就析出，軟配軟最牢"),
    ("轉電子", "red", "電子從低 E° 流向高 E°"), ("燒失", "org", "加熱讓東西揮發或分解"), ("折射", "blu", "光在物質裡變慢而轉彎；左右圓偏光慢得不同就旋光"), ("錯合", "grn", "配位基佔住金屬的空位，K 最大者得手"),
]
VTONE = {v: t for v, t, _ in VERBS}
PILL = {"治": ("#356844", "#e3f0e3", "治"), "價": ("#b72d4a", "#f8e5e8", "價"), "性": ("#5b6b78", "#eef1f4", "性")}


def verb_chip(v):
    bd, bg = TONE[VTONE.get(v, "line")]
    return f'<span class="vb" style="--bd:{bd};--bg:{bg}">{esc(v)}</span>'


def proj_rows(proj):
    out = []
    for pr in proj:
        k, txt = pr[0], pr[1]
        ref = pr[2] if len(pr) > 2 else ""
        bd, bg, lab = PILL[k]
        out.append(f'<div class="pj"><span class="pill" style="--bd:{bd};--bg:{bg}">{lab}</span>'
                   f'<span class="pt">{rich(txt)}</span>{("<span class=pref>" + rich(ref) + "</span>") if ref else ""}</div>')
    return "".join(out)


def b_engine(b, acc):
    """一個本體：引擎號＋動詞＋名稱 → 綠底推導鏈（本體）→ 投影（治價性同組，用顏色分）→ 手寫類比線。"""
    verbs = "".join(verb_chip(v) for v in b.get("verbs", []))
    n = f'<span class="en">16 年 {b["n"]} 題</span>' if b.get("n") is not None else ""
    head = (f'<div class="eh"><span class="el">{esc(b["L"])}</span>{verbs}<b class="enm">{rich(b["name"])}</b>{n}</div>')
    vec = f'<div class="vec">{rich(b["vec"])}</div>'
    hooks = "".join(f'<div class="hook"><b>{"機轉橋" if h[0] == "橋" else "記憶鉤"}</b>{rich(h[1])}</div>' for h in b.get("hooks", []))
    lines = '<div class="hw"></div>' * b.get("lines", 0)
    return f'<div class="blk eng">{head}{vec}<div class="pjs">{proj_rows(b.get("proj", []))}</div>{hooks}{lines}</div>'


def b_vcard(b, acc):
    """零件向量卡：本體一句 → 投影 → 孤點。"""
    verbs = "".join(verb_chip(v) for v in b.get("verbs", []))
    sub = f'<span class="vsub">{rich(b["sub"])}</span>' if b.get("sub") else ""
    ex = f'<span class="en">{rich(b["exam"])}</span>' if b.get("exam") else ""
    iso = ("<div class=iso><b>孤點</b>" + "；".join(rich(x) for x in b["iso"]) + "</div>") if b.get("iso") else ""
    return (f'<div class="blk vcard"><div class="eh">{verbs}<b class="enm">{rich(b["name"])}</b>{sub}{ex}</div>'
            f'<div class="vec">{rich(b["vec"])}</div><div class="pjs">{proj_rows(b.get("proj", []))}</div>{iso}</div>')


def b_legend(b, acc):
    vs = "".join(f'<span class="lg">{verb_chip(v)}<span class="lgm">{esc(m)}</span></span>' for v, _, m in VERBS)
    pills = "".join(f'<span class="pill" style="--bd:{bd};--bg:{bg}">{lab}</span>{esc(t)}　'
                    for (bd, bg, lab), t in [(PILL["治"], "能做什麼"), (PILL["價"], "做不到、會被騙"), (PILL["性"], "條件與性質")])
    return (f'<div class="blk legend"><div class="bt" style="color:{acc}">{rich(b.get("title", "讀法"))}</div>'
            f'<div class="lgp">{rich(b.get("text", ""))}</div><div class="lgv">{vs}</div><div class="lgp">{pills}</div></div>')


BLK.update({"engine": b_engine, "vcard": b_vcard, "legend": b_legend})


# ───────── 題型練習（STJ 式：一個題型一張卡；題目頁留手寫空白，詳解另頁）─────────
def b_drill(b, acc):
    """題目卡：題型編號＋名稱＋本體＋考次 → 母題題幹與選項 → 手寫區（先寫本體，再推一次）。"""
    eng = f'<span class="dq-e">{rich(b["E"])}</span>' if b.get("E") else ""
    n = f'<span class="en">16 年 {b["n"]} 題</span>' if b.get("n") is not None else ""
    opts = "".join(f'<div class="dq-o"><b>{esc(k)}</b> {rich(v)}</div>' for k, v in b.get("opts", {}).items())
    src = f'<div class="dq-src">母題 {esc(b["src"])}</div>' if b.get("src") else ""
    lines = b.get("lines", 5)
    hw = ('<div class="dq-hw"><div class="dq-p">① 這題考哪個本體？</div><div class="hw"></div>'
          '<div class="dq-p">② 從本體推一次：</div>' + '<div class="hw"></div>' * max(lines - 1, 1) + "</div>")
    return (f'<div class="blk drill"><div class="eh"><span class="el">{esc(b["no"])}</span><b class="enm">{rich(b["name"])}</b>{eng}{n}</div>'
            f'<div class="dq-s">{rich(b["stem"])}</div><div class="dq-os">{opts}</div>{src}{hw}</div>')


def b_sol(b, acc):
    """詳解卡：答案 → 推導鏈（從本體出發）→ 其餘選項錯在哪 → 歷年變形 → 陷阱。"""
    chain = "".join(f"<li>{rich(x)}</li>" for x in b.get("chain", []))
    wn = "".join(f"<li>{rich(x)}</li>" for x in b.get("why_not", []))
    var = "".join(f'<li><b class="mono">{esc(i)}</b> {rich(t)}</li>' for i, t in b.get("var", []))
    trap = f'<div class="ds-trap"><b>陷阱</b>{rich(b["trap"])}</div>' if b.get("trap") else ""
    return (f'<div class="blk sol"><div class="eh"><span class="el">{esc(b["no"])}</span><b class="enm">{rich(b["name"])}</b>'
            f'<span class="ds-a">答 {esc(b["ans"])}</span></div>'
            f'<div class="vec"><ol class="ds-c">{chain}</ol></div>'
            f'{("<ul class=ds-w>" + wn + "</ul>") if wn else ""}'
            f'{("<div class=ds-vt>歷年變形</div><ul class=ds-v>" + var + "</ul>") if var else ""}{trap}</div>')


BLK.update({"drill": b_drill, "sol": b_sol})


def render_blocks(bs, acc):
    return "".join(BLK[b["type"]](b, acc) for b in bs)


def page(ch, n, p, acc, tint, ledger):
    label = p.get("label") or {1: "精華① 翻譯座標", 2: "精華② 驗證座標", 3: "精華③ 考點補完"}[n]
    cols = p.get("cols", [0.46, 0.54])
    body = ""
    if p.get("full"):
        body += f'<div class="full">{render_blocks(p["full"], acc)}</div>'
    if p.get("left") or p.get("right"):
        body += (f'<div class="cols" style="grid-template-columns:{cols[0]}fr {cols[1]}fr">'
                 f'<div class="col">{render_blocks(p.get("left", []), acc)}</div>'
                 f'<div class="col">{render_blocks(p.get("right", []), acc)}</div></div>')
    if p.get("bottom"):
        body += f'<div class="full">{render_blocks(p["bottom"], acc)}</div>'
    foot = ""
    if p.get("one") or p.get("axes"):
        foot = (f'<div class="foot"><div class="one">{rich(p.get("one", ""))}</div>'
                f'<div class="axes">{rich(p.get("axes", ""))}</div></div>')
    return (f'<section class="page" style="--acc:{acc};--tint:{tint}"><header>'
            f'<div class="kick">{esc(ledger)}｜{esc(ch["name"])}｜{label}</div>'
            f'<h1><span class="cn">{esc(ch["name"])}</span>｜{label}：{rich(p["sub"])}</h1>'
            f'<div class="read">{rich(p.get("read", ""))}</div></header>'
            f'<main>{body}</main>{foot}'
            f'<div class="pno">藥物分析全景｜精華圖 {ch.get("ver", VER).replace("_", ".")}　{n}／{ch["npages"]}</div></section>')


CSS = r"""
@page{size:1600px 1131px;margin:0}
*{box-sizing:border-box}
html,body{margin:0;background:#fff}
body{font-family:"Noto Sans TC",sans-serif;color:#1f2a31;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:1600px;height:1131px;padding:26px 34px 22px;display:flex;flex-direction:column;gap:10px;overflow:hidden;page-break-after:always;
  font-size:var(--fs,15px);line-height:1.5;position:relative}
header{border-bottom:3px solid var(--acc);padding-bottom:6px}
.kick{font-size:.8em;letter-spacing:.08em;color:#61717a}
h1{font-family:"Noto Serif TC",serif;font-weight:700;font-size:1.75em;margin:2px 0 2px;line-height:1.3}
h1 .cn{color:var(--acc)}
.read{font-size:.86em;color:#46525a}
main{flex:1;display:flex;flex-direction:column;gap:10px;min-height:0}
.cols{display:grid;gap:14px;align-items:start}
.col,.full{display:flex;flex-direction:column;gap:10px;min-width:0}
.blk{min-width:0}
.bt{font-weight:700;font-size:1.02em;margin-bottom:4px;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.bt .note{font-weight:400;font-size:.8em;color:#61717a}
b{font-weight:700}
.r{color:#b72d4a;font-weight:700}
.g{color:#326991;font-weight:700}
.mono{font-family:"IBM Plex Mono","Noto Sans TC",monospace}
.ef{font-variant-numeric:tabular-nums}
/* 流程 */
.flow .st{border:1.5px solid var(--acc);border-radius:10px;padding:6px 10px 7px;background:#fff}
.flow .sh{display:flex;gap:8px;align-items:center;font-size:1.02em}
.flow .code{color:#fff;font:600 .82em "IBM Plex Mono",monospace;padding:1px 7px;border-radius:5px}
.flow ul{margin:3px 0 0;padding-left:1.15em}
.flow li{margin:1px 0}
.flow .parts{display:flex;flex-wrap:wrap;gap:4px;margin-top:4px}
.chip{font-size:.86em;border:1px solid #c9d2d6;border-radius:6px;padding:0 6px;background:var(--tint)}
.chip b{color:var(--acc);margin-right:4px}
.tag{margin-top:4px;border:1.2px solid var(--tb);background:var(--tf);border-radius:7px;padding:2px 8px;font-size:.92em}
.tag b{color:var(--tb)}
.arr{text-align:center;color:var(--acc);font-size:.8em;line-height:1;margin:2px 0}
/* 表 */
table{width:100%;border-collapse:collapse;table-layout:fixed;font-size:.9em}
th{background:var(--tint);color:#1f2a31;text-align:left;font-weight:700;padding:3px 6px;border:1px solid #b9c3c8}
td{padding:3px 6px;border:1px solid #c9d2d6;vertical-align:top;overflow-wrap:anywhere}
tbody tr:nth-child(even) td{background:#fafbf8}
/* 方塊 */
.box{border:1.5px solid var(--bd);background:var(--bg);border-radius:10px;padding:6px 10px 7px}
.box ul{margin:0;padding-left:1.15em}.box li{margin:1px 0}.box p{margin:2px 0}
.eqs{border:1.5px solid var(--acc);border-radius:10px;padding:6px 10px 8px;background:var(--tint)}
.eq{display:grid;grid-template-columns:10.5em 1fr;column-gap:10px;padding:3px 0;border-top:1px dotted #9aa6ab}
.eq:first-of-type{border-top:0}
.et{font-weight:700}
.ef{font-weight:600}
.ex{grid-column:2;font-size:.9em;color:#46525a}
.pairs table{font-size:.9em}.pairs td{border:0;border-bottom:1px dotted #b9c3c8;padding:2px 4px}
.pairs td.pa{font-weight:700;width:17%}.pairs td.vs{width:3%;color:var(--acc);text-align:center}
.groups{display:grid;grid-template-columns:repeat(var(--gc),minmax(0,1fr));gap:10px;align-items:start}
.grp{border:1.5px solid var(--bd);background:var(--bg);border-radius:10px;padding:6px 10px 7px}
.gt{font-weight:700;margin-bottom:2px}
.grp ul{margin:0;padding-left:1.15em}.grp li{margin:1px 0}
/* pick up 版 */
.eng,.vcard{border:1.5px solid #9aa6ab;border-radius:10px;padding:6px 10px 7px;background:#fff}
.eh{display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin-bottom:4px}
.el{background:#1f2a31;color:#fff;font:600 .85em "IBM Plex Mono",monospace;padding:1px 8px;border-radius:5px}
.enm{font-size:1.04em}
.en{margin-left:auto;font-size:.8em;color:#61717a}
.vsub{font-size:.82em;color:#61717a}
.vb{border:1.5px solid var(--bd);background:var(--bg);color:var(--bd);font-weight:700;font-size:.82em;padding:0 6px;border-radius:12px;white-space:nowrap}
.vec{background:#e3f0e3;border:1.5px solid #356844;border-radius:8px;padding:4px 9px;margin-bottom:4px}
.pjs{display:flex;flex-direction:column;gap:2px}
.pj{display:grid;grid-template-columns:2em 1fr auto;gap:6px;align-items:baseline;padding:1px 0;border-bottom:1px dotted #d3d9dc}
.pill{display:inline-block;border:1.3px solid var(--bd);background:var(--bg);color:var(--bd);font-weight:700;font-size:.8em;
  border-radius:10px;padding:0 6px;text-align:center;line-height:1.5}
.pref{font-size:.76em;color:#8a969c;white-space:nowrap}
.iso{margin-top:4px;border-left:4px solid #685185;background:#ece6f4;padding:2px 8px;font-size:.92em}
.iso b{color:#685185;margin-right:6px}
.hook{font-size:.88em;color:#46525a;margin-top:3px}
.hook b{border:1px solid #9aa6ab;border-radius:4px;padding:0 4px;margin-right:6px;font-size:.85em}
.hw{height:1.7em;border-bottom:1.6px dashed #c4c8be}
.legend{border:1.5px solid #9aa6ab;border-radius:10px;padding:6px 10px;background:#fafbf8}
.lgv{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:3px 8px;margin:4px 0;font-size:.86em}
.lg{display:flex;gap:4px;align-items:baseline}.lgm{color:#46525a;font-size:.88em}
.lgp{font-size:.88em}
/* 題型練習 */
.drill,.sol{border:1.5px solid #9aa6ab;border-radius:10px;padding:6px 10px 7px;background:#fff}
.dq-e{border:1.3px solid #356844;background:#e3f0e3;color:#356844;font-weight:700;font-size:.8em;border-radius:10px;padding:0 6px}
.dq-s{font-weight:500;margin:2px 0 3px}
.dq-os{display:grid;grid-template-columns:1fr 1fr;gap:1px 14px;font-size:.94em}
.dq-o b{color:#326991;margin-right:3px}
.dq-src{font-size:.76em;color:#8a969c;text-align:right}
.dq-hw{margin-top:2px}
.dq-p{font-size:.82em;color:#61717a;margin-top:3px}
.ds-a{margin-left:auto;background:#b72d4a;color:#fff;font-weight:700;border-radius:6px;padding:0 9px}
.ds-c{margin:0;padding-left:1.3em}.ds-c li{margin:1px 0}
.ds-w{margin:4px 0 0;padding-left:1.15em;font-size:.92em}.ds-w li{margin:1px 0}
.ds-vt{font-weight:700;font-size:.84em;color:#326991;margin-top:4px}
.ds-v{margin:0;padding-left:1.15em;font-size:.88em}.ds-v li{margin:0}
.ds-trap{margin-top:4px;border-left:4px solid #b72d4a;background:#f8e5e8;padding:2px 8px;font-size:.9em}
.ds-trap b{color:#b72d4a;margin-right:6px}
/* 頁尾 */
.foot{border:2px solid #9e771c;background:#fdf3d6;border-radius:10px;padding:7px 14px}
.one{font-weight:700;font-size:1.08em}
.axes{font-size:.86em;color:#46525a;margin-top:2px}
.pno{position:absolute;right:34px;bottom:6px;font-size:.7em;color:#8a969c}
"""


def font_css():
    pk = {"sans": "fontsource-noto-sans-tc-5.3.1", "serif": "fontsource-noto-serif-tc-5.3.1", "mono": "fontsource-ibm-plex-mono-5.3.0"}
    links = []
    for k, w in [("sans", 400), ("sans", 500), ("sans", 700), ("serif", 700), ("mono", 400), ("mono", 600)]:
        p = os.path.join(FONTS, pk[k], "package", f"{w}.css")
        if not os.path.exists(p):
            sys.exit(f"缺字型：{p}（見檔頭說明）")
        links.append(f'<link rel="stylesheet" href="file://{p}">')
    return "".join(links)


def build(key):
    S = load_spec(key)
    idx = json.load(open(os.path.join(REPO, "藥物分析_全景/app/data/index.json"), encoding="utf-8"))
    chs = {c["key"]: c for c in idx["chapters"]}
    keys = S.get("keys", [key])
    c0 = chs.get(keys[0], {})  # 傳統分析多數章不在 index.json：spec 自己給 field、name
    acc, tint, ledger = LEDGER[S.get("field") or c0["field"]]
    pages = [S[k] for k in ("p1", "p2", "p3", "p4", "p5") if k in S]
    for qk in S.get("drills", []):  # 題型練習頁：specs/q_<章>.py 的 PAGES，接在 pick up 頁後面
        pages += load_spec(qk)["PAGES"]  # q_<章>.py 裡寫 SPEC = dict(PAGES=[...])
    ch = dict(name=S.get("name") or c0["name"], npages=len(pages), ver=S.get("ver", VER))
    body = "".join(page(ch, i + 1, p, acc, tint, ledger) for i, p in enumerate(pages))
    doc = (f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">{font_css()}<style>{CSS}</style></head>'
           f"<body>{body}</body></html>")
    os.makedirs(OUT, exist_ok=True)
    hp = os.path.join(HERE, "out", f"{key}.html")
    os.makedirs(os.path.dirname(hp), exist_ok=True)
    open(hp, "w", encoding="utf-8").write(doc)
    ver = S.get("ver", VER)
    pdf = os.path.join(OUT, f'{S["file"]}_精華圖_{ver}.pdf')
    r = subprocess.run(["node", os.path.join(HERE, "print.js"), hp, pdf], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip())
    if S.get("append"):  # pick up 版後面接上 v1.1 精華頁（對答案用）
        old = os.path.join(OUT, f'{S["append"]}_精華圖_{VER}.pdf')
        tmp = pdf + ".tmp.pdf"
        subprocess.run(["pdfunite", pdf, old, tmp], check=True)
        os.replace(tmp, pdf)
        print("  接上", os.path.basename(old))
    # 純文字（覆蓋檢核用）
    txt = re.sub(r"<[^>]+>", " ", body)
    open(os.path.join(HERE, "out", f"{key}.txt"), "w", encoding="utf-8").write(html.unescape(txt))
    return pdf


if __name__ == "__main__":
    ks = sys.argv[1:] or sorted(f[:-3] for f in os.listdir(os.path.join(HERE, "specs")) if f.endswith(".py") and not f.startswith("_"))
    for k in ks:
        build(k)
