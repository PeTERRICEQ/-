"""藥分全景（新版）資料：沿用藥理藥化全景網頁的格式。
輸入：../app_data.json（export_app.py 產生）、各章圖組（figs_src.py 產生）、全科圖0–6、_generator/common.py（五格指紋）。
輸出：../../app/data/index.json、q.json、ch/<章>.json；../../app/fig/*.svg
用法：python3 pan/export.py"""
import glob, html, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(BUILD, "../.."))
APP = os.path.join(REPO, "藥物分析_全景", "app")
FIGROOT = os.path.join(REPO, "藥物分析_全科大中小循環")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(FIGROOT, "_generator"))
from mount import mounts, texts  # noqa: E402
import common as G  # noqa: E402

D = json.load(open(os.path.join(BUILD, "app_data.json"), encoding="utf-8"))

# ───────── 名稱 ─────────
KEY = {"光譜概論": "spec", "UV": "uv", "螢光": "flu", "IR": "ir", "Raman": "ram", "NMR": "nmr", "原子光譜": "aas",
       "折光": "ri", "旋光": "pol", "萃取": "ext", "層析概論": "chr", "TLC": "tlc", "HPLC": "hplc", "GC": "gc",
       "SFC": "sfc", "CE": "ce", "MS": "ms", "非水滴定": "naq", "水分": "kf", "灰分": "ash"}
SPECK = {"sp": "spec", "uv": "uv", "fl": "flu", "ir": "ir", "rm": "ram", "nmr": "nmr", "at": "aas", "ri": "ri",
         "or": "pol", "ex": "ext", "chr": "chr", "tlc": "tlc", "hplc": "hplc", "gc": "gc", "sfc": "sfc", "ce": "ce",
         "ms": "ms"}
SPEC = {SPECK[k]: v for k, v in G.BY.items()}
FPD = {SPECK[k]: v for k, v in G.FP.items()}
# 圖上的帳名
LEDGER = {"光帳": "nrg", "賽跑帳": "time", "秤重帳": "mz", "點數帳": "cnt"}
RENAME = [("光帳", "能量帳"), ("賽跑帳", "時間帳"), ("秤重帳", "質荷帳")]
FIELDS = [
    dict(key="nrg", name="能量帳", roman="Ⅰ", probe="光子", handle="能階差、極化率、光速差", axis="能量軸 λ、ṽ、δ；單一數值 n、a",
         desc="光子 × 能階：分子只吃剛好對得上的光（光譜 9 章）"),
    dict(key="time", name="時間帳", roman="Ⅱ", probe="第二相、電場", handle="相間分配；電荷與大小", axis="時間或距離 tR、Rf、tm",
         desc="第二相 × 分配：越愛待在固定相的越晚出來（分離 7 章）"),
    dict(key="mz", name="質荷帳", roman="Ⅲ", probe="先游離，再用電場、磁場或飛行時間分選", handle="質量與電荷", axis="m／z",
         desc="電荷 × 質量：先讓它帶電，再秤重（MS）"),
    dict(key="cnt", name="點數帳", roman="Ⅳ", probe="滴定液、試劑、高溫", handle="化學計量", axis="體積、重量",
         desc="一個換一個地數，或直接秤；不必畫標準曲線（非水滴定、水分、灰分）"),
]
ALIAS = {"非水": "naq", "層析": "chr", "原子": "aas", "UV-Vis": "uv", "SFC／SFE": "sfc", "拉曼": "ram"}
BCODE = {"色": "co", "骨": "sk", "量": "ma", "極": "po", "荷": "ch", "揮": "vo", "手": "ci", "晶": "cr", "元": "el",
         "反": "re", "整": "wh"}


def ren(s):
    for a, b in RENAME:
        s = s.replace(a, b)
    return s


def keyof(name):
    if name in KEY:
        return KEY[name]
    return ALIAS.get(name)


def lnum(lab):
    m = re.search(r"(\d+)$", lab or "")
    return int(m.group(1)) if m else None


def cite(label):
    """「CE L08–L11」「GC L04、L07」「非水 溶劑節」→ (章 key, [L 號])"""
    label = label.strip()
    names = sorted(list(KEY) + list(ALIAS), key=len, reverse=True)
    for nm in names:
        if label.startswith(nm):
            k = keyof(nm)
            rest = label[len(nm):]
            ns = []
            for a, b in re.findall(r"L?(\d+)(?:\s*[–\-~]\s*L?(\d+))?", rest):
                a = int(a)
                ns += list(range(a, int(b) + 1)) if b else [a]
            return k, ns
    return None, []


# ───────── 文字 → HTML（移植自舊網頁的 tex()） ─────────
def tex(s):
    def one(m):
        x = m.group(1)
        x = re.sub(r"\\(?:mathrm|text|operatorname|mathbf)\{([^}]*)\}", r"\1", x)
        x = re.sub(r"\\frac\{([^}]*)\}\{([^}]*)\}", r"(\1)／(\2)", x)
        for a, b in [(r"\\times", "×"), (r"\\cdot", "·"), (r"\\leq?", "≤"), (r"\\geq?", "≥"), (r"\\approx", "≈"),
                     (r"\\propto", "∝"), (r"\\to", "→"), (r"\\Delta", "Δ"), (r"\\lambda", "λ"), (r"\\nu", "ν"),
                     (r"\\mu", "μ"), (r"\\alpha", "α"), (r"\\varepsilon|\\epsilon", "ε"), (r"\\pm", "±"),
                     (r"\\qquad|\\quad|\\;|\\,", " "), (r"\\left|\\right", "")]:
            x = re.sub(a, b, x)
        x = re.sub(r"\\[a-zA-Z]+", "", x)
        return re.sub(r"[{}^_]", "", x)
    s = re.sub(r"\$\$(.+?)\$\$", lambda m: "\x00" + one(m) + "\x01", s, flags=re.S)
    s = re.sub(r"\$([^$]*)\$", one, s)
    return s


def inline(s):
    s = html.escape(tex(s), quote=False)
    s = re.sub(r"\*\*([^*\n]+)\*\*", r"<b>\1</b>", s)
    s = s.replace("\x00", '<span class="eq">').replace("\x01", "</span>")
    return s


def md(s):
    """段落、表格、編號；單行換行保留。"""
    s = (s or "").strip()
    if not s:
        return ""
    out = []
    for blk in re.split(r"\n\s*\n", s):
        lines = blk.split("\n")
        if all(l.strip().startswith("|") for l in lines if l.strip()):
            rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines if l.strip()]
            rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
            h = "<table>" + "".join(
                "<tr>" + "".join(f"<{'th' if i == 0 else 'td'}>{inline(c)}</{'th' if i == 0 else 'td'}>" for c in r) + "</tr>"
                for i, r in enumerate(rows)) + "</table>"
            out.append(h)
        elif re.fullmatch(r"\s*\$\$.+\$\$\s*", blk, flags=re.S):
            out.append(f'<p class="eqb">{inline(blk.strip())}</p>')
        else:
            out.append("<p>" + "<br>".join(inline(l) for l in lines) + "</p>")
    return "".join(out)


def plain(s):
    return tex(s or "").replace("\x00", "").replace("\x01", "")


# ───────── 題目 ─────────
OPT = re.compile(r"^\s*-?\s*\(([A-E])\)\s*(.*)$")


def split_stem(stem):
    s, o, cur = [], {}, None
    for line in stem.split("\n"):
        m = OPT.match(line)
        if m:
            cur = m.group(1)
            o[cur] = m.group(2).strip()
        elif cur and line.strip():
            o[cur] += "\n" + line.strip()
        else:
            s.append(line)
    stem = "\n".join(s).strip()
    stem = re.sub(r"^\d{1,2}\.\s*", "", stem)
    return plain(stem), {k: plain(v) for k, v in o.items()}


def main():
    cards = D["cards"]
    chs = D["chapters"]
    props = {p["k"]: p for p in D["props"]}

    # L 卡
    Lmeta = {}  # (chkey, n) -> card
    for c in cards:
        k = KEY[c["ch"]]
        Lmeta[(k, lnum(c["L"]))] = c

    # 題目：同 id 同題幹 → 合併；不同題 → 加 b
    qs, byid = [], {}
    for q in D["qs"]:
        k = KEY[q["ch"]]
        s, o = split_stem(q["stem"])
        ln = [[k, f"l{lnum(L)}", "講義"] for L in q["L"] if (k, lnum(L)) in Lmeta]
        red = [r for r in q["red"]]
        if q["id"] in byid:
            p = byid[q["id"]]
            if re.sub(r"\W", "", p["s"])[:24] == re.sub(r"\W", "", s)[:24]:
                if k not in p["ch"]:
                    p["ch"].append(k)
                p["ln"] += [x for x in ln if x not in p["ln"]]
                p["red"] += [x for x in red if x not in p["red"]]
                p["te"] = sorted(set(p["te"]) | set(q["te"]))
                continue
            qid = q["id"] + "b"
        else:
            qid = q["id"]
        yr, ex, no = q["id"].split("-")
        ent = dict(id=qid, t=plain(q["title"]), s=s, o=o, a=q["ans"], ch=[k], f=None, b=(q["p"] or [None])[0],
                   ps=q["p"], st=q["s"], ln=ln, why=plain(q["why"]), red=red, te=q["te"], l=q["l"],
                   src=[[f"{yr} 年第 {ex} 次", int(no)]])
        byid[q["id"]] = ent
        qs.append(ent)
    CHF = {KEY[c["name"]]: LEDGER[c["ledger"]] for c in chs}
    for q in qs:
        q["f"] = CHF[q["ch"][0]]
    qcount = {}
    for q in qs:
        for c, a, _ in q["ln"]:
            qcount[(c, a)] = qcount.get((c, a), 0) + 1

    # 章
    os.makedirs(os.path.join(APP, "data", "ch"), exist_ok=True)
    out_ch = []
    for c in chs:
        name, k = c["name"], KEY[c["name"]]
        mine = sorted([x for x in cards if x["ch"] == name], key=lambda x: lnum(x["L"]))
        Ls = [dict(n=lnum(x["L"]), tag=x["L"], name=plain(x["title"]), badge=(x["p"] or [None])[0], id=f"l{lnum(x['L'])}",
                   q=qcount.get((k, f"l{lnum(x['L'])}"), 0), p=x["p"], s=x["s"]) for x in mine]
        sp = SPEC.get(k)
        M = []
        figdir = os.path.join(FIGROOT, "各章圖組", name)
        if os.path.isdir(figdir):
            mt = mounts(name)
            f1 = glob.glob(os.path.join(figdir, "*圖1_*.svg"))[0]
            sname = {}
            for t, fs in texts(open(f1, encoding="utf-8").read()):
                m = re.match(r"^(?:M0(\d)|第(\d)站)\s*[｜ ]\s*(.+)$", t)
                if m and fs >= 26:
                    sname.setdefault(int(m.group(1) or m.group(2)), re.sub(r"｜L\d.*$", "", m.group(3)))
            parts = c["parts"]
            P4 = {2: ["源", "樣", "選"], 3: ["測"], 4: ["算"]}
            for i in sorted(sname):
                note = ""
                if k == "pol":
                    four = {1: 1, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4}[i]
                    note = f"四站對照：M0{four}"
                    if i == 7:
                        sname[i] = "可信度條件"
                        note += "；不在分母：會改變 [α]；操作：會改變 a 的可信度"
                elif sp:
                    note = sp["M"][i - 1]
                pk = P4.get(i, []) if k != "pol" else {1: [], 2: ["樣"], 3: ["源", "選"], 4: [], 5: ["測"], 6: ["算"], 7: []}[i]
                M.append(dict(code=f"M0{i}", desc=sname[i], note=plain(note),
                              parts=[[p, parts[p]] for p in pk if parts.get(p)],
                              Ls=[n for n, v in sorted(mt.items()) if v == i]))
            known = {l["n"] for l in Ls}
            for m in M:
                m["Ls"] = [n for n in m["Ls"] if n in known]
        ent = dict(key=k, name=name, field=LEDGER[c["ledger"]], handout=True, q=sum(1 for q in qs if k in q["ch"]),
                   mid=sp["arche"] if sp else ren(c["entry"]), core=sp["eq"] if sp else "；".join(f"{a} {b}" for a, b in c["parts"].items()),
                   line=sp["line"] if sp else "", trap=sp["trap"] if sp else "", loops=sp["loops"] if sp else "",
                   parts=c["parts"], main=c["main"], fp=FPD.get(k), M=M, L=Ls, F=[])
        out_ch.append(ent)
        cd = {}
        for x in mine:
            body = ""
            if x["ask"] and x["ask"] != x["title"]:
                body += f'<p class="ask">先問：{inline(x["ask"])}</p>'
            if x["chain"]:
                body += f'<div class="chain">{md(x["chain"])}</div>'
            if x["ex"]:
                body += f'<div class="kv"><b>例子</b>{md(x["ex"])}</div>'
            if x["trap"]:
                body += f'<div class="kv trapk"><b>易錯</b>{md(x["trap"])}</div>'
            if x["why"]:
                body += f'<details class="why"><summary>白話理由</summary>{md(x["why"])}</details>'
            if x["q"]:
                q0 = re.sub(r"^閉卷自問\s*[｜|:：]\s*", "", x["q"])
                ql = "回答上面的「先問」" if q0 == x["ask"] else inline(q0)
                body += f'<details class="selfq"><summary><b>閉卷</b> {ql}</summary>{md(x["ans"])}</details>'
            cd[f"l{lnum(x['L'])}"] = dict(t=plain(x["title"]), k="L", h=body)
        json.dump(dict(key=k, cards=cd), open(os.path.join(APP, "data", "ch", k + ".json"), "w", encoding="utf-8"),
                  ensure_ascii=False, separators=(",", ":"))

    # 跨章線
    COL = {"酸鹼線": 2, "分配線": 2, "標準曲線線": 5, "空白線": 5, "歸一線": 3, "解析度線": 4, "溫度線": 5, "雜訊地板": 4}
    lines = []
    for i, l in enumerate(D["lines"]):
        stops, nodes = {}, []
        for nd in l["nodes"]:
            ck, ns = cite(nd["label"])
            ns = [n for n in ns if ck and (ck, n) in Lmeta]
            if ck and ns:
                stops.setdefault(ck, [])
                stops[ck] += [n for n in ns if n not in stops[ck]]
            nodes.append(dict(label=nd["label"], t=plain(nd["t"]), ch=ck, Ls=ns))
        lines.append(dict(n=i + 1, name=l["name"], rule=plain(l["rule"]), known=plain(l.get("known", "")),
                          ti=plain(l.get("ti", "")), col=COL.get(l["name"]), nodes=nodes, stops=[[c, ns] for c, ns in stops.items()]))

    # Te 作戰表
    te = []
    for t in D["te"]:
        reds, cs = [], []
        for r in t["reds"]:
            ck, ns = cite(r["cite"])
            ns = [n for n in ns if ck and (ck, n) in Lmeta]
            reds.append(dict(type=r["type"], t=plain(r["t"]), cite=r["cite"], ch=[keyof(x) for x in r["ch"] if keyof(x)],
                             L=[[ck, f"l{n}"] for n in ns]))
            cs += [[ck, f"l{n}"] for n in ns if [ck, f"l{n}"] not in cs]
        te.append(dict(i=t["i"], w=t["name"], n=t["n"], chs=[[keyof(a), b] for a, b in t["chs"] if keyof(a)],
                       ch=[keyof(a) for a, b in t["chs"] if keyof(a)], p=t["p"], s=t["s"], line=t["line"], wave=t["wave"],
                       frags=[dict(t=plain(f["t"]), ch=[keyof(x) for x in f["ch"] if keyof(x)]) for f in t["frags"]],
                       reds=reds, cards=cs, qs=[q["id"] for q in qs if t["i"] in q["te"]], q=sum(1 for q in qs if t["i"] in q["te"])))

    # 圖
    figs = {}
    os.makedirs(os.path.join(APP, "fig"), exist_ok=True)
    KINDS = [("macro", "圖1", "大循環母圖", "先看"), ("micro", "圖2", "小循環掛載點", "讀 L 時"),
             ("map", "圖3", "方法分類對照", "比方法"), ("inst", "圖4", "儀器與操作", "條件錯了看這"),
             ("calc", "圖5", "公式與誤差", "讀數錯了看這")]

    def wh(p):
        t = open(p, encoding="utf-8").read(3000)
        vb = re.search(r'viewBox="[\d.\s-]+?([\d.]+)\s+([\d.]+)"', t)
        return (round(float(vb.group(1))), round(float(vb.group(2)))) if vb else (1900, 1400)

    for c in out_ch:
        d = os.path.join(FIGROOT, "各章圖組", c["name"])
        if not os.path.isdir(d):
            continue
        lst = []
        for kind, no, lab, use in KINDS:
            src = glob.glob(os.path.join(d, f"*_{no}_*.svg"))[0]
            dst = f"fig/{c['key']}-{kind}.svg"
            shutil.copyfile(src, os.path.join(APP, dst))
            w, h = wh(src)
            lst.append([kind, f"{no} {lab}", dst, w, h, use])
        figs[c["key"]] = lst
    GT = [("g0", "圖0 翻譯＋驗證總圖", "先看"), ("g1", "圖1 能量帳：光譜九章", "能量帳"), ("g2", "圖2 時間帳：分離七章", "時間帳"),
          ("g3", "圖3 質荷帳與偵測接點", "質荷帳"), ("g4", "圖4 讀數校正與回查總表", "錯題路由"),
          ("g5", "圖5 跨科類比：藥理型別與藥動同構", "跨科"), ("g6", "圖6 五格指紋矩陣", "比章")]
    gl = []
    for (g, lab, use), fn in zip(GT, [G.FILES[i] for i in range(7)]):
        src = os.path.join(FIGROOT, fn)
        dst = f"fig/gt-{g}.svg"
        shutil.copyfile(src, os.path.join(APP, dst))
        w, h = wh(src)
        gl.append([g, lab, dst, w, h, use])
    figs["gt"] = gl

    idx = dict(
        fields=FIELDS,
        chapters=out_ch,
        badges=[[p["k"], p["name"]] for p in D["props"]],
        bcode=BCODE,
        props={p["k"]: dict(name=p["name"], learn=p["learn"], methods=p["methods"], read=p["read"], color=p["color"],
                            tool=[dict(t=plain(x["t"]), ch=[keyof(y) for y in x["ch"] if keyof(y)]) for x in p["tool"]],
                            trap=[dict(t=plain(x["t"]), ch=[keyof(y) for y in x["ch"] if keyof(y)]) for x in p["trap"]])
               for p in D["props"]},
        stations=[dict(k=s["k"], job=s["job"], parts=s["parts"]) for s in D["stations"]],
        four=[dict(code="M01", name="先定問題", ask="要知道什麼？身分、含量、雜質、結構、晶型、元素？先決定要保留什麼。", parts=[]),
              dict(code="M02", name="準備與測量", ask="讓藥能被碰到，再依性質展開成座標。", parts=["源", "樣", "選"]),
              dict(code="M03", name="讀訊號", ask="把「到了」變成讀數：位置＝是誰，大小＝多少，形狀＝環境或品質。", parts=["測"]),
              dict(code="M04", name="核對結論", ask="讀數換回答案；只說資料支持的話。", parts=["算"])],
        fpq=[list(x) for x in G.FP_Q],
        fpsum=[["① 探針只有四種", ["光子（含雷射、偏極光）", "第二相（液、固、氣、超臨界）", "電場", "先游離，再用電場、磁場或飛行時間分選"]],
               ["② 把柄只有六種", ["能階差", "極化率改變", "光速差（n、左右圓偏光）", "相間分配", "電荷與大小", "質量與電荷"]],
               ["③ 座標只有四種", ["能量軸：λ、ṽ、δ", "時間或距離：tR、Rf、tm", "m／z", "單一數值：n、a", "三讀數一律是位置／大小／形狀"]],
               ["④ 寬度有三個來源", ["物理展寬：擴散、質傳、熱、去相位、能階疊加", "樣品與操作：超載、接觸、製樣、點樣", "儀器分辨力：狹縫、解析度、磁場均勻度"]],
               ["⑤ 騙子有三種", ["背景加進來：散射、螢光、流失、空白", "別人冒充：共洗脫、同 Rf、同名目質量、相近譜線", "條件偷改：溫度、pH、EOF、壓力、基質效應"]]],
        reds=[["把柄錯", "選錯方法或性質：這個分子根本沒有這把柄", "micro"],
              ["條件錯", "條件偷改了讀數：溫度、pH、溶劑、製樣", "inst"],
              ["讀數錯", "讀錯軸、單位或公式", "calc"]],
        lines=lines, te=te, calc=[dict(name=x["name"], ch=[keyof(y) for y in x["ch"] if keyof(y)], f=plain(x["f"]),
                                       w=plain(x["w"]), ex=plain(x["ex"]), trap=plain(x["trap"])) for x in D["calc"]],
        figs=figs, ledgers=[dict(key=LEDGER[l["name"]], plain=l["plain"], one=l["one"]) for l in D["ledgers"]],
    )
    json.dump(idx, open(os.path.join(APP, "data", "index.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    json.dump(qs, open(os.path.join(APP, "data", "q.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    nL = sum(len(c["L"]) for c in out_ch)
    print(f"章 {len(out_ch)}｜L {nL}｜題 {len(qs)}｜回查 {sum(len(q['ln']) for q in qs)}｜線 {len(lines)}｜Te {len(te)}｜圖 {sum(len(v) for v in figs.values())}")
    unm = [(c["key"], l["n"]) for c in out_ch if c["M"] for l in c["L"] if not any(l["n"] in m["Ls"] for m in c["M"])]
    print("沒掛上 M 的 L：", unm)
    bad = [x["label"] for l in lines for x in l["nodes"] if not x["ch"]]
    print("線上認不出章的站：", bad)


if __name__ == "__main__":
    main()
