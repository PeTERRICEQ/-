"""藥物分析精華 v2.0（essence-handout 方法）：理解（① 大循環）和記憶（⓪ 門派擴散）拆開，全部超連結。
一份講義＝specs/hb_<key>.py 的 SPEC；後面接題型練習（specs/q_<key>.py）與 v1.1 精華頁（specs/<key>.py），同一份 HTML 印成 PDF，
所以目錄、L、零件卡、字根、標籤之間的連結全部是 PDF 內部連結。
用法（在 _build 下）：python3 essence/hb.py hplc  → 藥物分析_精華圖/<file>_精華_v2_0.pdf，並回報 links／missing。"""
import html, json, os, re, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lib  # noqa: E402
from lib import esc, TONE, PILL, VERBS, verb_chip, load_spec, LEDGER  # noqa: E402

REPO = os.path.abspath(os.path.join(HERE, "../../.."))
OUT = os.path.join(REPO, "藥物分析_精華圖")
BANK = json.load(open(os.path.join(REPO, "藥物分析_全景/_build/k16/藥分_100-115_1280題.json"), encoding="utf-8"))
SHARED = json.load(open(os.path.join(REPO, "藥物分析_全景/_build/k16/pickup/shared_tally.json"), encoding="utf-8"))
ENGINE_TAGS = {  # 6 個共用本體＝#標籤
    "分配": "分子在兩相之間來回分配 → 待在哪一相的比例由像不像決定 → 越像固定相（或萃取相）待越久",
    "解離": "質子只往更想要它的地方走 → pH 對 pKa 決定帶不帶電 → 帶電型像水、中性型像油",
    "把柄": "探針只量一種物理量 → 分子在這個量上要和背景不同才看得到 → 把柄越少見，選擇性越高、通用性越低",
    "能隙": "光子能量要剛好對上某個能階差才被吸收 → 能階差由結構決定 → 不同波段讀不同的能階",
    "擴散": "同一種分子走的路徑不同、進出固定相有延遲、自己往前後散開 → 峰變寬",
    "計量": "讀數和量成正比 → 比例係數要用同條件的標準品或反應式定 → 讀數比＝量比，再乘回稀釋",
}
GATE_TONE = {"源": "blu", "樣": "org", "選": "grn", "測": "pur", "算": "yel"}


def gtone(gid):
    """閘門顏色：只看第一個字（選1、選2 同色）。"""
    return TONE[GATE_TONE.get(gid[0], "key")]


def slug(s):
    return re.sub(r"[^0-9A-Za-z一-鿿]+", "_", s).strip("_")


class Ctx:
    """一份講義的連結表：卡片名（含別名）→ 錨點；L → 錨點。"""

    def __init__(self, S):
        self.S = S
        self.cards = {}
        for c in S.get("cards", []):
            for nm in [c["name"]] + c.get("alias", []):
                self.cards[nm] = "card-" + slug(c["name"])
        self.Ls = {}
        for g in S["gates"]:
            for ln in g["L"]:
                self.Ls[ln["L"]] = "L-" + ln["L"]

    def rich(self, s):
        """lib.rich ＋ <<零件>>（有卡：綠色藥丸可點；沒卡：灰色）＋ ➔L05（可點回 ①）。"""
        t = lib.rich(s)

        def part(m):
            nm = html.unescape(m.group(1))
            if nm in self.cards:
                return f'<a class="pp on" href="#{self.cards[nm]}">{esc(nm)}</a>'
            return f'<span class="pp">{esc(nm)}</span>'
        t = re.sub(r"&lt;&lt;(.+?)&gt;&gt;", part, t)

        def lk(m):
            L = m.group(1)
            return f'<a class="lk" href="#{self.Ls[L]}">➔ {L}</a>' if L in self.Ls else f"➔ {L}"
        return re.sub(r"➔ ?([A-Z]{1,2}\d{1,2})", lk, t)


def exam_ids(aliases, keys=None):
    """16 年題庫被點名的題：題幹或正解選項出現任一別名（不分大小寫）。keys 給了就只算這幾章。"""
    pats = [re.compile(re.escape(a), re.I) for a in aliases]
    out = []
    for q in BANK:
        if keys and q["ch"][0] not in keys:
            continue
        txt = q["s"] + " " + " ".join(q["o"].get(a, "") for a in (q["a"] or ""))
        if any(p.search(txt) for p in pats):
            out.append(q["id"])
    return out


def nbadge(n):
    cls = "nb solid" if n >= 3 else "nb"
    return f'<span class="{cls}" title="16 年被點名次數">{n}</span>'


# ───────── 頁框 ─────────
def section(sid, title, sub, read, body, big=False, tone="grn"):
    bd = TONE[tone][0]
    cls = {True: "page big", False: "page", "tall": "page tall", "wide": "page wide nogrow"}[big]
    return (f'<section id="{sid}" class="{cls}"><header><a class="toc" href="#toc">← 目錄</a>'
            f'<h1 style="--hc:{bd}">{esc(title)}<span class="h1s">{lib.rich(sub)}</span></h1>'
            f'<div class="read">{lib.rich(read)}</div></header><main>{body}</main></section>')


# ───────── 目錄 ─────────
def p_toc(S, ctx, parts):
    route = "".join(f'<li><a href="#{sid}">{esc(t)}</a><span>{esc(d)}</span></li>' for sid, t, d in parts)
    cards = "".join(f'<li><a href="#{ctx.cards[c["name"]]}">{esc(c["name"])}</a>{"".join(verb_chip(v) for v in c.get("verbs", []))}</li>'
                    for c in S.get("cards", []))
    legend = "".join(f'<span class="lgv">{verb_chip(v)}<span>{esc(m)}</span></span>' for v, _, m in VERBS)
    pills = "　".join(f'<span class="pill" style="--bd:{bd};--bg:{bg}">{lab}</span>{t}' for (bd, bg, lab), t in
                     [(PILL["治"], "能做什麼"), (PILL["價"], "做不到、會被騙"), (PILL["性"], "條件與性質")])
    body = (f'<div class="tocg"><div><div class="one">{ctx.rich(S["one"])}</div>'
            f'<div class="bt">學習路線（照順序，全部可點）</div><ol class="route">{route}</ol></div>'
            f'<div><div class="bt">本章向量卡</div><ul class="cardl">{cards}</ul>'
            f'<div class="bt">封閉動詞（全書 {len(VERBS)} 個）</div><div class="lgw">{legend}</div>'
            f'<div class="lgp">{pills}　<span class="pp on">綠色藥丸</span>有卡、點了會跳　<span class="pp">灰色</span>本章沒卡　'
            f'{nbadge(3)}16 年被點名 ≥ 3 次</div></div></div>')
    return (f'<section id="toc" class="page"><header><h1 style="--hc:{TONE["grn"][0]}">{esc(S["name"])}｜精華 v2.0'
            f'<span class="h1s">理解交給 ①，記憶交給 ⓪；記不起來就點 ➔ L 回去重推</span></h1>'
            f'<div class="read">本精華依 essence-handout 方法製作：⓪ 門派＝① 的閘門（源、樣、選、測、算）；考 n 由 100–115 年 1280 題自動比對。{esc(S.get("note", ""))}</div></header>'
            f"<main>{body}</main></section>")


# ───────── ⓪ 門派擴散記憶圖 ─────────
def kl_html(k, ctx, side):
    see = "".join(f'<span class="see">{esc(x)}</span>' for x in k.get("see", [])) or '<span class="none">（沒有共同代號）</span>'
    look = (f'<div class="look"><div class="kn">{ctx.rich(k["name"])}</div><div class="row"><b>看到</b>{see}</div>'
            f'<div class="row"><b>摸到</b><span class="touch">{lib.rich(k["touch"])}</span></div>'
            f'{("<div class=tn>" + lib.rich(k["why"]) + "</div>") if k.get("why") else ""}</div>')
    rows = []
    for nm, d in k["items"]:
        dashed = nm.startswith("~")
        nm0 = nm[1:] if dashed else nm
        segs = "".join(f'<span class="{"seg red" if s.strip().startswith("!") else "seg"}">{ctx.rich(s.strip().lstrip("!"))}</span>'
                       for s in d.split("｜"))
        ids = exam_ids(ctx.S["alias"].get(nm0, [nm0]), ctx.S.get("keys")) if not dashed else []
        pill = (f'<span class="pp dash">{esc(nm0)}</span>' if dashed else ctx.rich(f"<<{nm0}>>"))
        rows.append(f'<div class="it">{pill}{"" if dashed else nbadge(len(ids))}<div class="segs">{segs}</div></div>')
    link = (f'<div class="link"><b>連動【{esc(k["link"][0])}】</b>{ctx.rich(k["link"][1])}</div>') if k.get("link") else ""
    comp = (f'<div class="comp"><div class="ax">{ctx.rich(k["axis"])}</div>{"".join(rows)}{link}</div>')
    inner = (comp + look) if side == "L" else (look + comp)
    return f'<div class="kl">{inner}</div>'


def sc_html(sc, ctx, side):
    gid = sc["gate"]
    bd, bg = gtone(gid)
    Ls = sorted({L for br in sc["br"] for L in br["L"]}, key=lambda x: (x[0], int(re.sub(r"\D", "", x) or 0)))
    lks = " ".join(ctx.rich(f"➔ {L}") for L in Ls)
    scb = (f'<a class="scb" id="sc-{gid}" href="#map-{gid}" style="--bd:{bd};--bg:{bg}"><b>{esc(sc["name"])}</b>'
           f'<span class="slo">{esc(sc["slogan"])}</span><span class="scl">{esc("、".join(Ls))}</span></a>')
    brs = []
    for br in sc["br"]:
        risk = {"red": " risk-r", "grn": " risk-g"}.get(br.get("risk"), "")
        bl = " ".join(ctx.rich(f"➔ {L}") for L in br["L"])
        brb = f'<div class="brb{risk}"><b>{esc(br["name"])}</b><span class="hint">{ctx.rich(br["hint"])}</span><span class="bls">{bl}</span></div>'
        kls = "".join(kl_html(k, ctx, side) for k in br["kl"])
        inner = (f'<div class="kls">{kls}</div>{brb}') if side == "L" else (f'{brb}<div class="kls">{kls}</div>')
        brs.append(f'<div class="br">{inner}</div>')
    inner = (f'<div class="brs">{"".join(brs)}</div>{scb}') if side == "L" else (f'{scb}<div class="brs">{"".join(brs)}</div>')
    return f'<div class="sc sc-{side}" style="--bd:{bd}">{inner}</div>'


def p_radial(S, ctx):
    R = S["radial"]
    left = [sc for sc in R["sects"] if sc.get("side") == "L"]
    right = [sc for sc in R["sects"] if sc.get("side") != "L"]
    legend = "".join(f'<span class="rl {k}">{esc(t)}</span>' for k, t in R.get("legend", []))
    body = (f'<div class="rad"><div class="rad-l">{"".join(sc_html(s, ctx, "L") for s in left)}</div>'
            f'<div class="rad-c"><div class="circle"><b>{esc(R["center"])}</b><span>{lib.rich(R["sub"])}</span></div>'
            f'<a class="tomap" href="#map">➔ 看各門派在 ① 大循環的哪個位置（位置對照）</a></div>'
            f'<div class="rad-r">{"".join(sc_html(s, ctx, "R") for s in right)}</div><svg class="wires"></svg></div>'
            f'<div class="rfoot"><div>{legend}　分工：⓪ 記憶（看到、摸到、Δ）　① 理解（推導鏈）　② 單一零件細節　｜　組成只寫 Δ；考 n＝16 年題幹或正解點名次數，≥ 3 實心</div>'
            f'<div class="cav">⚠ 比喻失效提醒：{lib.rich(R.get("caveat", ""))}</div></div>')
    return section("radial", f"⓪ 門派擴散記憶圖：{S['name']}", R["center"], "由內而外：中心比喻 → 門派（＝① 的閘門）→ 分支（➔ L 點回 ① 重推）→ 每類一列：外觀（看到＋摸到）與組成 Δ",
                   body, big=True)


# ───────── ⓪→① 位置對照 ─────────
def p_map(S, ctx):
    R = S["radial"]
    where = {}  # L → [(門派, 分支, [類別])]
    for sc in R["sects"]:
        for br in sc["br"]:
            for L in br["L"]:
                kls = [k["name"] for k in br["kl"] if not k.get("L") or L in k["L"]]
                where.setdefault(L, []).append((sc, br, kls))
    legend = "".join(f'<a class="mchip" href="#sc-{sc["gate"]}" style="--bd:{gtone(sc["gate"])[0]};--bg:{gtone(sc["gate"])[1]}">{esc(sc["name"])}</a>'
                     for sc in R["sects"])
    gates = []
    for g in S["gates"]:
        bd, bg = gtone(g["id"])
        rows = []
        for ln in g["L"]:
            L = ln["L"]
            left = f'<a class="lk" href="#{ctx.Ls[L]}">➔ {L}</a><span class="mln">{esc(ln["name"])}</span>'
            if L in where:
                right = "".join(f'<a class="mchip" href="#sc-{sc["gate"]}" style="--bd:{gtone(sc["gate"])[0]};--bg:{gtone(sc["gate"])[1]}">{esc(sc["name"])}</a>'
                                f'<span class="mbr">{esc(br["name"])}</span>{("<span class=mkl>（" + esc("、".join(k)) + "）</span>") if k else ""}'
                                for sc, br, k in where[L])
            else:
                right = '<span class="mnone">不屬任何門派（原理或代價：看 ① 推導）</span>'
            rows.append(f'<div class="mrow"><div class="ml">{left}</div><div class="mr">{right}</div></div>')
        gates.append(f'<div class="mgate" id="map-{g["id"]}" style="--bd:{bd};--bg:{bg}"><div class="mgh">{esc(g["name"])}</div>{"".join(rows)}</div>')
    body = (f'<div class="mlegend" id="map">門派（點了回 ⓪）：{legend}</div><div class="mgrid">{"".join(gates)}</div>'
            f'<div class="mfoot">讀法：左邊 ➔ L 點了去 ① 看推導鏈；右邊門派色塊點了回 ⓪ 看外觀與 Δ。閘門順序和 ① 一樣：源 → 樣 → 選 → 測 → 算。</div>')
    return section("map-page", "⓪→① 位置對照", "門派各在 ① 大循環的哪一格", "① 的縮小版：每條 L 一列，標出它屬於哪個門派、哪個分支、掛了哪些類別", body)


# ───────── ① 大循環推導版 ─────────
def lane(ln, ctx):
    verbs = "".join(verb_chip(v) for v in ln.get("v", []))
    proj = "".join(f'<div class="pj"><span class="pill" style="--bd:{PILL[k][0]};--bg:{PILL[k][1]}">{k}</span>'
                   f'<span class="pt">{ctx.rich(t)}</span></div>' for k, t in ln.get("proj", []))
    return (f'<div class="lane" id="{ctx.Ls[ln["L"]]}"><div class="eh"><span class="el">{esc(ln["L"])}</span>{verbs}'
            f'<b class="enm">{ctx.rich(ln["name"])}</b></div><div class="vec">{ctx.rich(ln["vec"])}</div><div class="pjs">{proj}</div>'
            f'<div class="note"></div></div>')


def p_loop(S, ctx, page_gates, idx, total):
    gates = []
    cols = S.get("loop_cols", 3)
    for i, gid in enumerate(page_gates):
        g = next(x for x in S["gates"] if x["id"] == gid)
        bd, bg = gtone(gid)
        row, c = divmod(i, cols)
        order = row * cols + (cols - 1 - c if row % 2 else c)  # 蛇形：偶數列反向
        arrow = ("↓" if c == cols - 1 else "→") if row % 2 == 0 else ("↓" if c == cols - 1 else "←")
        if i == len(page_gates) - 1:
            arrow = ""
        gates.append(f'<div class="gate" style="--bd:{bd};--bg:{bg};order:{order}"><div class="gh"><b>{esc(g["name"])}<span class="arr2">{arrow}</span></b>'
                     f'<span>閘門一句：{ctx.rich(g["one"])}</span></div><div class="lanes">{"".join(lane(ln, ctx) for ln in g["L"])}</div></div>')
    cond = ""
    if idx == 0 and S.get("cond"):
        cond = ('<div class="cond"><div class="bt">樣品條件 → 走哪條路</div>' +
                "".join(f'<div class="cd"><b>{ctx.rich(a)}</b><span>{ctx.rich(b)}</span></div>' for a, b in S["cond"]) + "</div>")
    cost = ""
    if idx == total - 1 and S.get("cost"):
        cost = ('<div class="cost"><div class="bt">騙子帶：讀數被誰騙（干擾、基質、假峰、系統誤差）</div><div class="costs">' +
                "".join(f'<div class="cs"><b>{ctx.rich(a)}</b><span>{ctx.rich(b)}</span></div>' for a, b in S["cost"]) + "</div></div>")
    snake = f'<div class="snake" style="--gc:{min(cols, len(page_gates))}">{"".join(gates)}</div>'
    body = (f'<div class="loopw">{cond}<div class="loopm">{snake}</div></div>{cost}')
    sub = "每條 L 先讀綠底推導鏈（本體）→ 再看投影（治＝能做什麼、價＝做不到或被騙、性＝條件）；藥丸點了跳到零件卡"
    title = "① 大循環推導版" + (f"（{idx + 1}／{total}）" if total > 1 else "")
    return section(f"loop{idx}" if idx else "loop", title, "源 → 樣 → 選 → 測 → 算", sub, body, big="wide")


# ───────── ② 向量卡 ─────────
def card(c, ctx):
    cid = ctx.cards[c["name"]]
    ids = exam_ids(ctx.S["alias"].get(c["name"], [c["name"]] + c.get("alias", [])), ctx.S.get("keys"))
    yrs = Counter(i[:5] for i in ids)
    rec = "".join(f'<span class="yr">{y}{"×" + str(n) if n > 1 else ""}</span>' for y, n in sorted(yrs.items())) or '<span class="none">16 年沒有點名</span>'
    left = "".join(f'<div class="kv"><b>{esc(k)}</b><span>{ctx.rich(v)}</span></div>' for k, v in c.get("prop", []))
    code = f'<div class="kv"><b>名稱</b><span><a class="lk" href="#names">{lib.rich(c["code"])}</a></span></div>' if c.get("code") else ""
    Ls = " ".join(ctx.rich(f"➔ {L}") for L in c.get("L", []))
    proj = "".join(f'<div class="pj3"><span class="grp">{esc(g)}</span><span class="pill" style="--bd:{PILL[k][0]};--bg:{PILL[k][1]}">{k}</span>'
                   f'<span class="pt">{ctx.rich(t)}</span></div>' for g, k, t in c.get("proj", []))
    iso = ("<div class=iso><b>孤點</b>" + "；".join(ctx.rich(x) for x in c["iso"]) + "</div>") if c.get("iso") else ""
    tags = "".join(f'<a class="tag" href="#tag-{slug(t)}">#{esc(t)}</a>' for t in c.get("tags", []))
    return (f'<div class="vc" id="{cid}"><div class="vcl"><div class="vcn">{esc(c["name"])}</div>'
            f'<div class="vcs">{lib.rich(c.get("sub", ""))}</div>{left}{code}'
            f'<div class="kv"><b>國考紀錄</b><span>{nbadge(len(ids))}{rec}</span></div></div>'
            f'<div class="vcr"><div class="eh">{"".join(verb_chip(v) for v in c.get("verbs", []))}<span class="loc">大循環位置 {Ls}</span></div>'
            f'<div class="vec">{ctx.rich(c["vec"])}</div><div class="pjs">{proj}</div>{iso}<div class="tags">{tags}</div></div></div>')


def p_cards(S, ctx):
    cs = S.get("cards", [])
    per = S.get("cards_per_page", 4)
    pages = []
    for i in range(0, len(cs), per):
        grp = cs[i:i + per]
        body = f'<div class="vcg">{"".join(card(c, ctx) for c in grp)}</div>'
        pages.append(section("cards" if i == 0 else f"cards{i}", f"② 零件向量卡（{i // per + 1}／{(len(cs) + per - 1) // per}）",
                             "每個零件一個本體，投影從本體長出來", "右欄：本體 → 投影（分組｜治價性）→ 孤點 → #共用本體；左欄：性質、名稱、國考紀錄（16 年題幹或正解點名）", body))
    return pages


# ───────── ③ 官能基 → 方法地形圖 ─────────
def p_terrain(S, ctx):
    rows = "".join(f'<tr><td class="th">{ctx.rich(a)}</td><td>{ctx.rich(b)}</td><td>{ctx.rich(c)}</td><td>{ctx.rich(d)}</td></tr>'
                   for a, b, c, d in S["terrain"])
    body = (f'<div class="blk tbl"><table><thead><tr><th style="width:18%">分子帶什麼（把柄）</th><th style="width:24%">本章用什麼</th>'
            f'<th style="width:34%">為什麼（本體）</th><th style="width:24%">代價</th></tr></thead><tbody>{rows}</tbody></table></div>'
            f'<div class="blk box" style="--bd:{TONE["grn"][0]};--bg:{TONE["grn"][1]}"><div class="bt" style="color:{TONE["grn"][0]}">讀法</div>'
            f'<p>{ctx.rich(S.get("terrain_read", ""))}</p></div>')
    return section("terrain", "③ 官能基 → 方法地形圖", "先看分子帶什麼把柄，再選零件", "一列一個把柄：分子有它 → 本章用哪個零件讀 → 為什麼讀得到 → 付出什麼代價", body)


# ───────── ④ 名稱與代號 ─────────
def p_names(S, ctx):
    rows = "".join(f'<tr><td class="th">{lib.rich(a)}</td><td>{lib.rich(b)}</td><td>{ctx.rich(c)}</td></tr>' for a, b, c in S["names"])
    body = (f'<div class="blk tbl"><table><thead><tr><th style="width:22%">代號／縮寫／詞根</th><th style="width:40%">拆開來看</th>'
            f'<th style="width:38%">本章成員</th></tr></thead><tbody>{rows}</tbody></table></div>')
    return section("names", "④ 名稱與代號", "名字裡的固定詞根與代號", "藥理用 INN 字根；藥分的「看到」是縮寫、USP 代號與詞尾。拆開來，名字就在說它做什麼", body)


# ───────── ⑤ #共用本體反查 ─────────
def p_tags(S, ctx):
    used = []
    for c in S.get("cards", []):
        for t in c.get("tags", []):
            if t not in used:
                used.append(t)
    rows = []
    for t in used:
        mine = " ".join(ctx.rich(f"<<{c['name']}>>") for c in S["cards"] if t in c.get("tags", []))
        other = "、".join(f'{x["chn"]} {x["n"]}' for x in sorted(SHARED["land"].get(t, []), key=lambda x: -x["n"]))
        rows.append(f'<div class="tg" id="tag-{slug(t)}"><div class="tgh">#{esc(t)}</div><div class="vec">{esc(ENGINE_TAGS.get(t, ""))}</div>'
                    f'<div class="row"><b>本章</b>{mine}</div><div class="row"><b>全書落地</b><span>{esc(other)}</span></div></div>')
    body = f'<div class="tgs">{"".join(rows)}</div>'
    return section("tags", "⑤ #共用本體反查", "同一個本體，在別章再撞見一次", "每個 #標籤＝全書 6 個共用本體之一；本章零件點了跳卡，全書落地列出各章題數（見 00 共用本體與全書總覽）", body)


# ───────── 舊頁（題型練習、v1.1）：用 lib 的排版，加上錨點與「← 目錄」 ─────────
def legacy_pages(spec_key, pages, prefix, main=None, tag=""):
    """舊版頁（題型練習、v1.1）接進 v2.0：換成主章名與帳別，去掉和 v2.0 ②–⑤ 撞號的圈號。"""
    S = load_spec(spec_key)
    M = main or S
    idx = json.load(open(os.path.join(REPO, "藥物分析_全景/app/data/index.json"), encoding="utf-8"))
    chs = {c["key"]: c for c in idx["chapters"]}
    keys = M.get("keys", [spec_key])
    c0 = chs.get(keys[0], {})
    acc, tint, ledger = LEDGER[M.get("field") or c0.get("field", "cnt")]
    ch = dict(name=M.get("name") or c0.get("name", spec_key), npages=len(pages), ver=M.get("ver", lib.VER))
    out = []
    for i, p in enumerate(pages):
        p = dict(p)
        lab = p.get("label") or {1: "精華① 翻譯座標", 2: "精華② 驗證座標", 3: "精華③ 考點補完"}.get(i + 1, "精華")
        lab = re.sub(r"^[①②③④⑤⑥⑦⑧⑨⓪]\s*", "", lab)
        p["label"] = tag + lab
        h = lib.page(ch, i + 1, p, acc, tint, ledger)
        h = h.replace('<section class="page"', f'<section id="{prefix}{i}" class="page legacy"', 1)
        h = h.replace("<header>", '<header><a class="toc" href="#toc">← 目錄</a>', 1)
        out.append(h)
    return out


CSS2 = r"""
@page big{size:2400px 1697px;margin:0}
section.big{width:2400px;height:1697px;page:big}
@page tall{size:2000px 2828px;margin:0}
section.tall{width:2000px;height:2828px;page:tall}
@page wide{size:2828px 4000px;margin:0}
section.wide{width:2828px;height:4000px;page:wide}
a{color:inherit;text-decoration:none}
.toc{position:absolute;right:34px;top:8px;font-size:.72em;color:#326991;font-weight:700}
header h1{color:var(--hc)}
.h1s{font-size:.6em;color:#46525a;margin-left:14px;font-weight:700}
.pp{display:inline-block;border:1.3px solid #9aa6ab;background:#eef1f4;color:#46525a;border-radius:10px;padding:0 7px;font-size:.86em;font-weight:700;margin:0 2px;line-height:1.45}
.pp.on{border-color:#356844;background:#e3f0e3;color:#356844}
.pp.dash{border-style:dashed}
.lk{color:#326991;font-weight:700;white-space:nowrap}
.nb{display:inline-block;min-width:1.5em;text-align:center;border:1.3px solid #326991;color:#326991;border-radius:50%;font:700 .74em "IBM Plex Mono",monospace;margin:0 3px;padding:0 2px}
.nb.solid{background:#326991;color:#fff}
.none{color:#8a969c;font-size:.86em}
/* 目錄 */
.tocg{display:grid;grid-template-columns:1.1fr .9fr;gap:24px}
.one{font-size:1.06em;border:2px solid #9e771c;background:#fdf3d6;border-radius:10px;padding:8px 14px;margin-bottom:10px}
.route{margin:0;padding-left:1.4em}.route li{margin:4px 0;font-size:1.05em}.route li a{font-weight:700;color:#326991;margin-right:10px}.route li span{color:#46525a;font-size:.9em}
.cardl{columns:2;margin:0 0 10px;padding-left:1.1em}.cardl li{margin:2px 0}.cardl a{font-weight:700;color:#356844;margin-right:6px}
.lgw{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2px 10px;font-size:.84em;margin-bottom:8px}.lgv{display:flex;gap:6px;align-items:baseline}
/* ⓪ */
.rad{position:relative;display:grid;grid-template-columns:1fr 300px 1fr;gap:26px;align-items:center;flex:1;min-height:0}
.rad-l,.rad-r{display:flex;flex-direction:column;gap:14px;justify-content:center;z-index:1}
.rad-c{display:flex;flex-direction:column;align-items:center;gap:14px;z-index:1}
.circle{width:290px;height:290px;border-radius:50%;border:4px solid #1f2a31;background:#fdf3d6;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:24px}
.circle b{font-family:"Noto Serif TC",serif;font-size:1.7em;line-height:1.25}.circle span{font-size:.92em;color:#46525a;margin-top:8px}
.tomap{font-size:.86em;color:#326991;font-weight:700;text-align:center}
.wires{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:visible}
.sc{display:flex;gap:10px;align-items:center}
.sc-L{justify-content:flex-end}
.scb{display:flex;flex-direction:column;gap:2px;border:2.5px solid var(--bd);background:var(--bg);border-radius:12px;padding:8px 10px;width:12em;flex:none}
.scb b{font-size:1.1em;color:var(--bd)}.slo{font-size:.84em}.scl{font-size:.76em;color:#46525a}
.brs{display:flex;flex-direction:column;gap:8px;flex:1;min-width:0}
.br{display:flex;gap:8px;align-items:center}
.sc-L .br{justify-content:flex-end}
.brb{border:1.8px solid var(--bd);background:#fff;border-radius:10px;padding:5px 8px;width:11em;flex:none;display:flex;flex-direction:column;gap:2px}
.brb.risk-r{border-color:#b72d4a;box-shadow:inset 0 0 0 1.5px #b72d4a}.brb.risk-g{border-color:#356844;box-shadow:inset 0 0 0 1.5px #356844}
.brb b{font-size:.98em}.hint{font-size:.8em;color:#46525a}.bls{font-size:.8em}
.kls{display:flex;flex-direction:column;gap:6px;flex:1;min-width:0}
.kl{display:grid;grid-template-columns:.85fr 1.15fr;gap:6px}
.sc-L .kl{grid-template-columns:1.15fr .85fr}
.look{border:1.5px solid #9aa6ab;border-radius:8px;padding:4px 7px;background:#fff;font-size:.88em}
.kn{font-weight:700;border-bottom:1px solid #d3d9dc;margin-bottom:2px}
.look .row{display:flex;gap:5px;align-items:baseline;flex-wrap:wrap}.look .row b{font-size:.84em;color:#61717a}
.see{border:1.3px solid #b0621a;background:#fbeadb;color:#b0621a;border-radius:10px;padding:0 6px;font-size:.86em;font-weight:700}
.touch{color:#356844;font-weight:700;font-family:"IBM Plex Mono","Noto Sans TC",monospace;font-size:.92em}
.tn{font-size:.8em;color:#8a969c}
.comp{border:1.5px solid var(--bd);border-radius:8px;padding:4px 7px;background:#fff;font-size:.88em}
.ax{font-weight:700;color:var(--bd);margin-bottom:2px}
.it{display:grid;grid-template-columns:auto auto 1fr;gap:4px;align-items:baseline;border-top:1px dotted #d3d9dc;padding:1px 0}
.segs{display:flex;flex-direction:column}.seg.red{color:#b72d4a;font-weight:700}
.link{margin-top:3px;border:1.5px dashed #685185;border-radius:6px;padding:1px 6px;color:#685185;font-size:.92em}.link b{margin-right:4px}
.rfoot{font-size:.84em;color:#46525a;border-top:1.5px solid #c9d2d6;padding-top:4px}
.rl{border-radius:5px;padding:0 6px;margin-right:6px;font-weight:700}.rl.red{border:2px solid #b72d4a;color:#b72d4a}.rl.grn{border:2px solid #356844;color:#356844}
.cav{color:#b0621a;font-weight:700}
/* 位置對照 */
.mlegend{font-size:.9em;margin-bottom:4px}
.mchip{display:inline-block;border:1.6px solid var(--bd);background:var(--bg);border-radius:8px;padding:0 7px;font-weight:700;font-size:.86em;margin:0 3px}
.mgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;align-items:start}
.mgate{border:2px solid var(--bd);border-radius:10px;padding:5px 8px;background:#fff}
.mgh{font-weight:700;color:var(--bd);background:var(--bg);border-radius:6px;padding:1px 6px;margin-bottom:3px}
.mrow{display:grid;grid-template-columns:1fr 1.1fr;gap:6px;border-top:1px dotted #d3d9dc;padding:2px 0;font-size:.9em}
.mln{margin-left:4px}.mbr{font-weight:700;margin-left:3px}.mkl{color:#46525a;font-size:.9em}
.mnone{border:1.3px dashed #9aa6ab;border-radius:6px;padding:0 5px;color:#61717a;font-size:.88em}
.mfoot{font-size:.84em;color:#46525a;margin-top:6px}
/* ① */
.loopw{display:flex;gap:14px;flex:1;min-height:0}
.cond{width:16em;flex:none;border:2px solid #685185;border-radius:10px;padding:6px 9px;background:#ece6f4;align-self:flex-start}
.cd{border-top:1px dotted #9aa6ab;padding:3px 0;font-size:.9em;display:flex;flex-direction:column}.cd b{color:#685185}
.loopm{flex:1;min-width:0;display:flex;flex-direction:column}
.snake{display:grid;grid-template-columns:repeat(var(--gc),minmax(0,1fr));column-gap:46px;row-gap:22px;align-items:stretch;flex:1;min-height:0}
.gate{border:2.5px solid var(--bd);border-radius:12px;padding:6px 8px;background:#fff;display:flex;flex-direction:column}
.arr2{float:right;color:var(--bd);font-size:1.2em}
.gh{background:var(--bg);border-radius:8px;padding:3px 8px;margin-bottom:5px;display:flex;flex-direction:column}.gh b{color:var(--bd);font-size:1.12em}.gh span{font-size:.86em}
.lanes{display:flex;flex-direction:column;gap:6px;flex:1}
.lane{border:1.3px solid #c9d2d6;border-radius:8px;padding:4px 7px;flex:1;display:flex;flex-direction:column}
.note{flex:1;min-height:3.6em;margin-top:2px;background-image:repeating-linear-gradient(to right,transparent 0 3px,#fff 3px 9px),repeating-linear-gradient(to bottom,transparent 0 calc(1.8em - 1.8px),#b9beb2 calc(1.8em - 1.8px) 1.8em)}
.pjs{display:flex;flex-direction:column;gap:1px}
.pj{display:grid;grid-template-columns:2em 1fr;gap:6px;align-items:baseline;border-bottom:1px dotted #d3d9dc;padding:1px 0}
.cost{border:2.5px solid #b72d4a;border-radius:10px;padding:5px 10px;background:#f8e5e8;margin-top:10px}
.costs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4px 14px}.cs{display:flex;flex-direction:column;font-size:.9em}.cs b{color:#b72d4a}
/* ② */
.vcg{display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:12px;flex:1;min-height:0}
.vc{display:grid;grid-template-columns:34% 66%;border:1.8px solid #9aa6ab;border-radius:12px;overflow:hidden}
.vcl{background:#f6f7f4;padding:7px 9px;border-right:1.3px solid #c9d2d6;display:flex;flex-direction:column;gap:3px}
.vcn{font-weight:700;font-size:1.25em;color:#356844}.vcs{font-size:.82em;color:#61717a}
.kv{display:flex;flex-direction:column;font-size:.88em;border-top:1px dotted #c9d2d6;padding-top:2px}.kv b{color:#61717a;font-size:.86em}
.yr{display:inline-block;font:.74em "IBM Plex Mono",monospace;border:1px solid #c9d2d6;border-radius:4px;padding:0 3px;margin:1px}
.vcr{padding:7px 10px;display:flex;flex-direction:column;gap:3px;min-width:0}
.loc{margin-left:auto;font-size:.84em}
.pj3{display:grid;grid-template-columns:4.2em 2em 1fr;gap:5px;align-items:baseline;border-bottom:1px dotted #d3d9dc;padding:1px 0}
.grp{font-size:.8em;color:#61717a;font-weight:700}
.tags{display:flex;gap:6px;flex-wrap:wrap}.tag{color:#685185;font-weight:700;font-size:.86em}
/* ⑤ */
.tgs{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.tg{border:1.8px solid #685185;border-radius:10px;padding:6px 10px}.tgh{font-weight:700;color:#685185;font-size:1.1em}
.tg .row{display:flex;gap:6px;align-items:baseline;flex-wrap:wrap;font-size:.92em;margin-top:3px}.tg .row b{color:#61717a;font-size:.86em}
td.th{font-weight:700}
"""

WIRES_JS = r"""
<script>
window.drawWires = function(){
  document.querySelectorAll('.rad').forEach(rad=>{
    const svg = rad.querySelector('svg.wires'); if(!svg) return;
    const R = rad.getBoundingClientRect(); const C = rad.querySelector('.circle').getBoundingClientRect();
    const cx = C.left + C.width/2 - R.left, cy = C.top + C.height/2 - R.top, r = C.width/2;
    let d = '';
    const curve = (x1,y1,x2,y2,col,w)=>{const mx=(x1+x2)/2; d += `<path d="M${x1},${y1} C${mx},${y1} ${mx},${y2} ${x2},${y2}" stroke="${col}" stroke-width="${w}" fill="none"/>`;};
    rad.querySelectorAll('.sc').forEach(sc=>{
      const left = sc.classList.contains('sc-L'); const col = getComputedStyle(sc).getPropertyValue('--bd');
      const b = sc.querySelector('.scb').getBoundingClientRect();
      const bx = (left? b.right : b.left) - R.left, by = b.top + b.height/2 - R.top;
      curve(cx + (left? -r : r), cy, bx, by, col, 3);
      sc.querySelectorAll('.br').forEach(br=>{
        const q = br.querySelector('.brb').getBoundingClientRect();
        const qx1 = (left? b.left : b.right) - R.left, qx2 = (left? q.right : q.left) - R.left;
        curve(qx1, by, qx2, q.top + q.height/2 - R.top, col, 2);
        br.querySelectorAll('.kl').forEach(kl=>{
          const k = kl.getBoundingClientRect();
          curve((left? q.left : q.right) - R.left, q.top + q.height/2 - R.top, (left? k.right : k.left) - R.left, k.top + k.height/2 - R.top, col, 1.2);
        });
      });
    });
    svg.innerHTML = d;
  });
};
</script>
"""


def check_links(doc):
    ids = set(re.findall(r'\sid="([^"]+)"', doc))
    hrefs = re.findall(r'href="#([^"]+)"', doc)
    missing = sorted({h for h in hrefs if h not in ids})
    return len(hrefs), missing


def build(key):
    S = load_spec("hb_" + key)
    ctx = Ctx(S)
    S.setdefault("alias", {})
    for c in S.get("cards", []):
        S["alias"].setdefault(c["name"], [c["name"]] + c.get("alias", []))
    # 頁序
    loop_pages = S.get("loop_pages", [[g["id"] for g in S["gates"]]])
    drills = load_spec(S["drills"])["PAGES"] if S.get("drills") else []
    v11 = [load_spec(S["v11"])[k] for k in ("p1", "p2", "p3", "p4", "p5") if k in load_spec(S["v11"])] if S.get("v11") else []
    cards_pages = p_cards(S, ctx)
    route = [("radial", "⓪ 門派擴散記憶圖", "記憶：看到、摸到、Δ"), ("map-page", "⓪→① 位置對照", "兩種切法怎麼對上"),
             ("loop", "① 大循環推導版", "理解：源 → 樣 → 選 → 測 → 算"), ("cards", "② 零件向量卡", f"{len(S.get('cards', []))} 張"),
             ("terrain", "③ 官能基 → 方法地形圖", "分子帶什麼 → 用什麼讀"), ("names", "④ 名稱與代號", "縮寫拆字、代號"),
             ("tags", "⑤ #共用本體反查", "同一個本體在別章")]
    if drills:
        route.append(("drill0", "題型練習", f"{len(drills)} 頁：先寫本體再推，詳解在下一頁"))
    if v11:
        route.append(("v110", "原精華 v1.1", "對答案用"))
    pages = [p_toc(S, ctx, route), p_radial(S, ctx), p_map(S, ctx)]
    pages += [p_loop(S, ctx, pg, i, len(loop_pages)) for i, pg in enumerate(loop_pages)]
    pages += cards_pages + [p_terrain(S, ctx), p_names(S, ctx), p_tags(S, ctx)]
    if drills:
        pages += legacy_pages(S["drills"], drills, "drill", S)
    if v11:
        pages += legacy_pages(S["v11"], v11, "v11", S, "v1.1 ")
    body = "".join(pages)
    doc = (f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><title>{esc(S["name"])}｜精華 v2.0</title>'
           f'{lib.font_css()}<style>{lib.CSS}{CSS2}</style></head><body>{body}{WIRES_JS}</body></html>')
    n, missing = check_links(doc)
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    hp = os.path.join(HERE, "out", f"hb_{key}.html")
    open(hp, "w", encoding="utf-8").write(doc)
    pdf = os.path.join(OUT, f'{S["file"]}_精華_v2_0.pdf')
    r = subprocess.run(["node", os.path.join(HERE, "hb_print.js"), hp, pdf], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip())
    print(f"links {n}  missing {len(missing)}", missing[:20])
    return pdf, missing


if __name__ == "__main__":
    bad = 0
    for k in sys.argv[1:]:
        _, miss = build(k)
        bad += len(miss)
    sys.exit(1 if bad else 0)
