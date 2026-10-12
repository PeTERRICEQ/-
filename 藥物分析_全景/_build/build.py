"""產生《藥物分析｜理化性質全景》HTML。
用法：python3 build.py <題庫 questions_tagged.json> <輸出.html> [--font-css 本機字型 css]
數字全部由題庫現算；文字在 content.py。
"""
import json, re, sys, html
from collections import Counter
sys.path.insert(0, __import__('os').path.dirname(__file__))
from tags import OBJ, PROP, CH_PROP, STA, LINE
import content as C

src, out = sys.argv[1], sys.argv[2]
font_css = sys.argv[sys.argv.index('--font-css') + 1] if '--font-css' in sys.argv else None
Q = json.load(open(src, encoding='utf-8'))
NQ = len({r['id'] for r in Q})
VER = 'v0.1'
TITLE = '藥物分析｜理化性質全景'
e = html.escape

def hits(keys):
    rx = [OBJ[k][1] for k in keys]
    return [r for r in Q if any(x.search(r['txt']) for x in rx)]
def nid(rows): return len({r['id'] for r in rows})
def chs(rows): return Counter(r['ch'] for r in rows)

# ── 統計 ──
prop_n, prop_cross, prop_ch = Counter(), Counter(), {}
explicit = 0
for r in Q:
    t = [k for k, (_, rx) in PROP.items() if rx.search(r['txt'])]
    if t: explicit += 1
    r['p'] = t or [CH_PROP[r['ch']]]
    for k in r['p']:
        prop_n[k] += 1
        prop_ch.setdefault(k, set()).add(r['ch'])
        if k != CH_PROP[r['ch']]: prop_cross[k] += 1
sta_n = Counter(k for r in Q for k, rx in STA.items() if rx.search(r['txt']))
line_rows = {k: [r for r in Q if rx.search(r['txt'])] for k, rx in LINE.items()}
ledger_n = {name: sum(1 for r in Q if r['ch'] in chl) for name, _, chl, _ in C.LEDGERS}
ch_n = Counter(r['ch'] for r in Q)

# Te 第一層
te = []
for name, keys, props, sta, line, pos, reds in C.TE:
    rows = hits(keys)
    te.append(dict(name=name, n=nid(rows), nch=len(chs(rows)), chs=chs(rows), props=props, sta=sta, line=line,
                   pos=pos, reds=reds, ids={r['id'] for r in rows}))
te.sort(key=lambda x: -x['n'])
tier1_ids = set().union(*[t['ids'] for t in te])
waves = [('第一波', '題數 ≥ 40', [t for t in te if t['n'] >= 40]),
         ('第二波', '題數 20–39', [t for t in te if 20 <= t['n'] < 40]),
         ('第三波', '題數 < 20', [t for t in te if t['n'] < 20])]
# 第二層
sk = []
for ch, keys, entry in C.SKELETON:
    items = []
    ids = set()
    for k in keys:
        rows = [r for r in hits([k]) if r['ch'] == ch]
        if rows:
            items.append((k, nid(rows))); ids |= {r['id'] for r in rows}
    sk.append((ch, sorted(items, key=lambda x: -x[1]), entry, ids))
tier2_ids = set().union(*[s[3] for s in sk]) - tier1_ids
tier3_n = NQ - len(tier1_ids | tier2_ids)

# 算式
def is_calc(r):
    if r['ch'] in ('非水滴定', '旋光'):
        return bool(re.search(r'[÷×]|＝\s*[-−+]?\d', r['txt']))
    opts = re.findall(r'(?:\(|\*\*|^-\s*\**\(?)[A-D](?:\)|\*\*)\**\s*([^\n]{0,40})', r['txt'], re.M)
    num = [o for o in opts if re.match(r'\s*[-−+]?\s*\$?\s*[\d.]+\s*(%|nm|mg|mL|cm|ppm|Hz|min|°|μ|g|N|M|kJ|\$|$|\s|：|,|，|×|/)', o)]
    return len(opts) >= 3 and len(num) >= 3
calc = [r for r in Q if is_calc(r)]
calc_n = {name: sum(1 for r in calc if r['ch'] in chl) for name, chl, *_ in C.CALC}
NCALC = nid(calc)

# ── HTML 小工具 ──
def badge(ch, big=False):
    return f'<span class="bd{" big" if big else ""}" style="background:{C.PROP_COLOR[ch]}">{ch}</span>'
def badges(s): return ''.join(badge(c) for c in s) if s else '<span class="muted">—</span>'
def st(s): return ''.join(f'<span class="st">{c}</span>' for c in s)
def red_type(t): return f'<span class="rt rt-{ {"把柄錯":"a","條件錯":"b","讀數錯":"c"}[t] }">{t}</span>'
def cite(s): return f'<span class="cite">{e(s)}</span>'
NAV = ['① 總覽', '② Te 作戰表', '③ 算式樓梯', '④ 九條線', '⑤ 五站零件表', '⑥ 性質跨章表', '⑦ 地板與失效處']
def nav(i):
    return '<div class="nav">' + ' › '.join(f'<b>{n}（你在這裡）</b>' if j == i else n for j, n in enumerate(NAV)) + '</div>'
def chlist(c, k=6): return '、'.join(f'{a} {b}' for a, b in c.most_common(k))

P = []  # 頁面片段

# ═════ ① 總覽 ═════
prop_rows = ''.join(
    f'<tr><td>{badge(k, True)}</td><td><b>{e(n)}</b></td><td>{e(w)}</td><td>{e(m)}</td><td>{e(rd)}</td>'
    f'<td class="num">{prop_n[k]}</td><td class="num">{prop_cross[k]}</td><td class="num">{len(prop_ch.get(k, ()))}</td></tr>'
    for k, n, w, m, rd in C.PROPS)
EXS = C.STATION_EXAMPLES
sta_rows = ''.join(
    f'<tr><td><span class="st big">{k}</span></td><td><b>{e(j)}</b></td>' + ''.join(f'<td>{e(row[i+1])}</td>' for row in EXS) +
    f'<td class="num">{sta_n[k]}</td></tr>' for i, (k, j, x) in enumerate(C.STATIONS))
sta_head = '<th>站</th><th>工作</th>' + ''.join(f'<th>{e(row[0])}</th>' for row in EXS) + '<th>題數</th>'
led_rows = ''.join(f'<tr><td><b>{n}</b></td><td>{e(s)}</td><td>{"、".join(chl)}</td><td>{e(a)}</td><td class="num">{ledger_n[n]}</td></tr>'
                   for n, s, chl, a in C.LEDGERS)
top_cross = max(prop_cross, key=prop_cross.get)
line_idx = ''.join(f'<tr><td><b>{e(n)}</b></td><td>{e(r)}</td><td>{e(k)}</td><td class="num">{nid(line_rows[n])}</td><td class="num">{len(chs(line_rows[n]))}</td></tr>'
                   for n, r, k, *_ in C.LINES + [C.FLOOR])
P.append(f'''
<section class="sec">{nav(0)}
<h1>{TITLE}｜訊號鏈點位圖：每一個考點釘在哪裡</h1>
<p class="lead">儀器的擺放順序剛好就是資訊流動的方向：<b>源 → 樣 → 選 → 測 → 算</b>＝從一顆藥走到一個數字。由左往右讀，就是由藥往答案讀。<span class="muted">{VER}｜資料：20 章建構講義、{NQ} 題（102-1～114-1）。</span></p>
<div class="two">
 <div class="box gen"><h3>生成句</h3>
  <p>每一個考點都是一枚釘子：<b>釘在訊號鏈的哪一站（在哪）× 抓藥物的哪一欄理化性質（徽章）× 掛在哪條線上（為什麼同一個條件會在別章重演）</b>。</p>
  <p>性質的種類少、方法多，同一欄性質被重複用在很多章：<b>在這一章它是分離或偵測的依據＝方法，在別章同一欄就是條件或陷阱</b>。</p>
  <p class="mother"><b>母句</b>　分析只問兩件事：是誰、有多少。做法永遠一樣：從理化性質表挑一欄它和別人不一樣的地方 → 讓這個不一樣變成看得見的位置或大小 → 拿標準品對照：位置換成身分，大小換成數量。</p>
 </div>
 <div class="box"><h3>三種讀法</h3><ol class="plain">{''.join(f"<li>{e(x)}</li>" for x in C.READ_WAYS)}</ol></div>
</div>

<h2>徽章＝藥物的理化性質（11 欄）</h2>
<p class="note">藥典的每一份藥品資料都列著同一組欄位。藥物分析只做一件事：<b>把這張表的每一欄，各自做成一種儀器</b>。題目問「哪個方法不適合」，就是在問這顆藥缺了哪一欄。</p>
<table class="t"><thead><tr><th>徽</th><th>性質</th><th>你在哪學過</th><th>用來讀它的方法</th><th>讀數（座標）</th><th>題數</th><th>在別章出現</th><th>章數</th></tr></thead><tbody>{prop_rows}</tbody></table>
<p class="cap">題數＝題幹或選項點名這一欄的題目數（一題可掛多欄；沒點名任何一欄時算該章的主把柄）。「在別章出現」＝出現在不是以它為主把柄的章，這就是跨章陷阱的來源。</p>
<div class="two">
<div class="box"><h3>每一張圖都只有三種讀數</h3>
<p><b>位置 → 是誰</b>　λmax、波數、δ、tR、Rf、m/z。只能支持身分，不能單獨證明。</p>
<p><b>大小 → 有多少</b>　A、F、峰面積、積分、豐度、滴定體積、殘渣重。要先校正才是濃度。</p>
<p><b>形狀 → 環境或品質</b>　峰寬、拖尾、裂分、同位素峰群。先列可能原因，再用另一個讀數區分。</p></div>
<div class="box"><h3>陷阱只有三種（紅字的讀法）</h3>
<p>{red_type("把柄錯")} 方法要抓的那一欄，這顆藥沒有：不揮發的藥進 GC、沒有發色基用 UV、溶解後問晶型。<b>回 M01。</b></p>
<p>{red_type("條件錯")} 欄位對了，但條件破壞了規則：pH 太靠近 pKa、溫度沒固定、濃度超出直線段。<b>回 M02。</b></p>
<p>{red_type("讀數錯")} 單位、方向或分母讀錯：%T 當 A、Hz 當 ppm、m/z 當分子量。<b>回 M03／M04。</b></p></div>
</div>

<div class="pb"></div>{nav(0)}
<h2>在哪＝訊號鏈五站：同一個五站，在不同方法裡長什麼樣</h2>
<table class="t sta"><thead><tr>{sta_head}</tr></thead><tbody>{sta_rows}</tbody></table>
<p class="cap">和你原本的四站一對一：M01＝問題＋樣，M02＝源＋選，M03＝測，M04＝算。M 站是做題的順序，五站是儀器上的零件位。題數＝題幹點名這一站的零件或步驟。</p>
<h2>四本帳＝依座標分家</h2>
<table class="t"><thead><tr><th>帳</th><th>白話</th><th>章</th><th>一句話</th><th>題數</th></tr></thead><tbody>{led_rows}</tbody></table>
<p class="cap">光帳只需要一條高中物理：電磁波順序 無線電波（NMR）→ 紅外（IR，鍵在抖）→ 可見、紫外（UV，電子在跳）→ X 光（晶體），越往右能量越大。</p>
<h2>線＝九條跨章規則＋一個地板（細節見 ④）</h2>
<table class="t"><thead><tr><th>線</th><th>規則</th><th>你已經會的版本</th><th>題數</th><th>章數</th></tr></thead><tbody>{line_idx}</tbody></table>
<div class="box check"><h3>用資料驗一次</h3>
<p>20 章題庫共 <b>{NQ}</b> 題（25 次考試，平均每次約 {NQ/25:.0f} 題）。其中 <b>{explicit}</b> 題（{explicit/NQ:.0%}）的題幹或選項直接點名了至少一欄藥物性質；其餘 {NQ-explicit} 題多是零件名稱或純計算。</p>
<p>跨章最多的一欄是 {badge(top_cross)} <b>{dict((k,n) for k,n,*_ in C.PROPS)[top_cross]}</b>：{prop_cross[top_cross]} 題出現在不以它為主把柄的章。最大的兩條線是 <b>分配線</b>（{nid(line_rows["分配線"])} 題）與 <b>酸鹼線</b>（{nid(line_rows["酸鹼線"])} 題，跨 {len(chs(line_rows["酸鹼線"]))} 章）。計算題約 {NCALC} 題（{NCALC/NQ:.0%}），其餘都是觀念題。</p>
</div>
</section>''')

# ═════ ② Te 作戰表 ═════
def te_table(rows, start):
    out = []
    for i, t in enumerate(rows, start):
        reds = '<br>'.join(f'{red_type(a)} <span class="red">{e(b)}</span> {cite(c)}' for a, b, c in t['reds'])
        out.append(f'<tr><td class="num">{i}</td><td><b>{e(t["name"])}</b></td>'
                   f'<td class="num"><b>{t["n"]}</b> 題<br><span class="muted">{t["nch"]} 章</span></td>'
                   f'<td>{badges(t["props"])}<br>{st(t["sta"])}</td><td>{e(t["pos"])}</td><td>{reds}</td></tr>')
    return ''.join(out)
te_head = '<thead><tr><th>#</th><th>物件</th><th>題數</th><th>性質／站</th><th>正向身分（章）</th><th>紅字：哪一種錯（章 L）</th></tr></thead>'
wave_html = ''
k = 1
for wname, wcond, rows in waves:
    wave_html += f'<h2>Te｜第一層 {wname}（{wcond}，{len(rows)} 項）</h2><table class="t te">{te_head}<tbody>{te_table(rows, k)}</tbody></table>'
    wave_html += f'<p class="ok">✓ 這一波讀完的判準：每一列都能不看表說出「它坐哪一站、抓哪一欄性質」和「每條紅字是哪一種錯」。說不出來的列，只回查那一列的章 L。</p>'
    k += len(rows)
sk_rows = ''.join(f'<tr><td><b>{ch}</b></td><td>{"、".join(f"{e(a)} {b}" for a, b in items) or "—"}</td><td>{e(entry)}</td></tr>' for ch, items, entry, _ in sk)
abbr_rows = ''.join(f'<tr><td><b>{e(a)}</b></td><td>{st(b[0]) if b[0] in "源樣選測算" else e(b)}{e(b[1:]) if b[0] in "源樣選測算" else ""}</td><td>{e(c)}</td><td>{e(d)}</td></tr>' for a, b, c, d in C.ABBR)
P.append(f'''
<section class="sec keep">{nav(1)}
<h1>Te｜作戰排序表</h1>
<div class="box rules"><h3>這一頁只有三條規則（避免迷航）</h3><ol class="plain">
<li>① 一次只讀一波：由上往下，讀完一波的判準才往下；不要跳到第二層。</li>
<li>② 每列只做兩件事：說出它坐哪一站、抓哪一欄性質（中欄）；說出每條紅字是 {red_type("把柄錯")}、{red_type("條件錯")} 還是 {red_type("讀數錯")}（右欄）。</li>
<li>③ 卡住才回查、查完就回來：只查那一列紅字標的「章 L」；九條線、零件表、跨章表是工具箱，不是下一站。</li></ol></div>
<div class="funnel">
 <div><b>{NQ}</b><span>全部題目</span></div><i>→</i>
 <div class="hl"><b>{len(tier1_ids)}</b><span>第一層：跨 3 章以上的物件<br>（{len(te)} 項，{len(tier1_ids)/NQ:.0%}）</span></div><i>→</i>
 <div><b>{len(tier2_ids)}</b><span>第二層：各章骨架<br>（{len(tier2_ids)/NQ:.0%}）</span></div><i>→</i>
 <div><b>{tier3_n}</b><span>第三層：長尾＋縮寫文法<br>（{tier3_n/NQ:.0%}）</span></div>
</div>
<p class="note">題數＝去重後，題幹或選項點名它的題目數。一題可以同時點名好幾個物件，所以各列加總會超過總數。</p>
{wave_html}
<h2>Te｜第二層：各章骨架（物件主要只出現在這一章）</h2>
<p class="note">每一列只做一件事：說出這一章的骨架「靠哪一欄性質撐起來」，右欄就是推理入口；卡住時沿那條線回去。數字＝該章點名題數。</p>
<table class="t"><thead><tr><th>章</th><th>骨架物件（題數）</th><th>推理入口：性質 → 線</th></tr></thead><tbody>{sk_rows}</tbody></table>
<p class="ok">✓ 讀完的判準：每一章能說出一個骨架物件和它的性質。例：NMR 化學位移 → 骨 → 歸一線（ppm 已除掉磁場）。</p>
<h2>Te｜第三層：長尾不背，先拆縮寫，再問一句</h2>
<table class="t"><thead><tr><th>縮寫的樣子</th><th>先猜站</th><th>再問一句</th><th>例</th></tr></thead><tbody>{abbr_rows}</tbody></table>
<p class="note">用法：只在考場遇到陌生縮寫時用。拆完先放上五站，再問它抓哪一欄性質，通常就能排除兩個選項。</p>
</section>''')

# ═════ ③ 算式樓梯 ═════
calc_rows = ''.join(
    f'<tr><td class="num">{i}</td><td><b>{e(n)}</b></td><td class="num">{calc_n[n]}</td><td class="f">{e(f)}</td><td>{e(w)}</td><td>{e(x)}</td><td class="red">{e(t)}</td></tr>'
    for i, (n, _, f, w, x, t) in enumerate(sorted(C.CALC, key=lambda c: -calc_n[c[0]]), 1))
P.append(f'''
<section class="sec">{nav(2)}
<h1>算式樓梯：計算題只有九個家族</h1>
<p class="lead">計算題約 {NCALC} 題（{NCALC/NQ:.0%}）。每一個家族都只有一步：<b>先問分母裡除掉了什麼</b>（歸一線），再代數字。由上往下＝題數由多到少。</p>
<table class="t calc"><thead><tr><th>#</th><th>家族</th><th>題數</th><th>式子</th><th>白話</th><th>一步驗算</th><th>讀數錯陷阱</th></tr></thead><tbody>{calc_rows}</tbody></table>
<p class="cap">題數＝選項有三個以上是數字的題目，依章歸到家族；非水滴定與旋光依打靶表的算式判定。屬於量級估計。</p>
<div class="two">
<div class="box"><h3>兩條萬用式（所有家族都是它們的特例）</h3>
<p><b>① 讀數＝斜率 × 量＋空白</b>　Beer、螢光、峰面積、qNMR、滴定體積都是這一條。斜率要用標準品量出來的是<b>相對法</b>；斜率天生就知道（化學計量、氫核數、電量）的是<b>絕對法</b>。</p>
<p><b>② 解析度＝位置差 ÷ 寬度</b>　層析 Rs、MS m／Δm、NMR Δν／J 都是這一條。想分開只有兩招：拉開位置，或壓窄寬度。</p></div>
<div class="box"><h3>單位先過關</h3>
<p>l 用 dm、c 用 g／100 mL（旋光）；1 dm＝100 mm。波長 nm、波數 cm⁻¹：ṽ＝10⁷／λ。ppm＝Hz ÷ MHz。濃度 → 量：m＝c×V。稀釋倍數最後才乘回去。</p>
<p class="red">算出來差 10 倍或 100 倍：先查單位與稀釋倍數，不是先查公式。</p></div>
</div>
</section>''')

# ═════ ④ 九條線 ═════
def line_block(name, rule, known, chain, ti, data=True):
    rows = line_rows.get(name, [])
    meta = f'<span class="muted">{nid(rows)} 題｜{len(chs(rows))} 章</span>' if data and rows else ''
    ch = '<span class="arr">→</span>'.join(f'<span class="node"><b>{e(a)}</b><br>{e(b)}</span>' for a, b in chain)
    return (f'<div class="line"><div class="lh"><b class="ln">{e(name)}</b>　{e(rule)}　{meta}</div>'
            f'<div class="known">你已經會的版本：{e(known)}</div><div class="chain">{ch}</div>'
            f'<div class="ti">Ti：{e(ti)}</div></div>')
lines_html = ''.join(line_block(*l) for l in C.LINES)
P.append(f'''
<section class="sec">{nav(3)}
<h1>九條跨章線：為什麼一個條件的後果會跑到別的章</h1>
<p class="lead">每一條線都是一條你在藥動、藥理或臨床已經會的規則。格子是「章 L｜站名」，回各章建構講義的那一條小循環，就是完整的鏈。一個條件在一站改了一個量，效應就沿著線出現在下一章。</p>
{lines_html}
{line_block(*C.FLOOR)}
</section>''')

# ═════ ⑤ 五站零件表 ═════
parts_rows = ''.join('<tr>' + f'<td><b>{e(r[0])}</b><br><span class="muted">{ch_n.get(r[0].split("／")[0], "")} 題</span></td>' + ''.join(f'<td>{e(c)}</td>' for c in r[1:]) + '</tr>' for r in C.PARTS)
P.append(f'''
<section class="sec">{nav(4)}
<h1>五站零件表：同一個工作，每一章叫什麼零件</h1>
<p class="lead">往下讀一欄＝同一站換了 20 章的零件名（零件題的破解關鍵）；往右讀一列＝這一章的儀器由哪五個零件組成。題目給零件名，先放上這張表的某一格。</p>
<table class="t parts"><thead><tr><th>章</th>{''.join(f'<th>{st(s[0])} {e(s[1])}</th>' for s in C.STATIONS)}</tr></thead><tbody>{parts_rows}</tbody></table>
<div class="box"><h3>讀這張表的三個例子</h3><ol class="plain">
<li>① 「選」那一欄：單色器、干涉儀、管柱、薄板、質量分析器、毛細管、終點反應——全是同一件事：<b>依某一欄性質，把混在一起的東西排開</b>。差在排開的座標是能量、時間、質荷比還是體積。</li>
<li>② AAS 的選擇性主要來自「源」：中空陰極燈只放該元素的窄線。單色器擺在火焰後面，只是為了擋掉火焰自己的光。</li>
<li>③ 「測」那一欄的讀數方向不一定是正的：%T（吸越多越小）、ECD（量越多電流越小）、CE 間接 UV（負峰）。先問方向，再讀大小。</li></ol></div>
</section>''')

# ═════ ⑥ 性質跨章表 ═════
cross_rows = ''.join(
    f'<tr><td>{badge(k, True)}<br><b>{e(n)}</b><br><span class="muted">{prop_n[k]} 題｜{len(prop_ch.get(k, ()))} 章</span></td>'
    f'<td class="good">{e(C.CROSS[k][0])}</td><td class="bad">{e(C.CROSS[k][1])}</td></tr>'
    for k, n, *_ in C.PROPS)
P.append(f'''
<section class="sec">{nav(5)}
<h1>同一欄性質跨章：重複就是陷阱的來源</h1>
<p class="lead">綠框＝這一欄在這一章是分離或偵測的依據（方法）；紅框＝同一欄在別章變成條件、干擾或陷阱。題目給一顆藥，就把它的性質一欄一欄想一遍：<b>缺的欄＝不能用的方法，多的欄＝要控制的條件</b>。</p>
<table class="t cross"><thead><tr><th>性質</th><th>在這章是工具</th><th>在別章變成陷阱</th></tr></thead><tbody>{cross_rows}</tbody></table>
<div class="box"><h3>一顆藥走一遍：phenylephrine（含酚的弱鹼）</h3>
<p>{badge("色")} 有苯環 → UV 可測；{badge("荷")} 酚在鹼中變酚鹽 → λmax 紅移、A 增加（UV L11），所以 0.1 M HCl 與 0.1 M NaOH 的光譜不同；胺基是弱鹼 → 逆相 HPLC 要控制 pH，否則在矽醇上拖尾（HPLC L08–L09）；{badge("揮")} 極性高、怕熱 → 不直接進 GC；{badge("手")} 有掌性中心 → 可旋光。四欄性質，四個章的考點。</p></div>
</section>''')

# ═════ ⑦ 地板與失效處 ═════
missing = 'CH1–5、CH7–9、CH12–17、CH25'
P.append(f'''
<section class="sec">{nav(6)}
<h1>雜訊地板與這張圖的失效處</h1>
<div class="box floor"><h3>雜訊地板：每一個讀數都要先浮出雜訊</h3>
<p>藥效要超過最低有效濃度才看得到；訊號也要高出雜訊才算「驗得到」。偵測極限約為雜訊的 3 倍，定量極限約為 10 倍。</p>
<ul class="plain">
<li><b>靈敏度不等於偵測極限</b>：斜率大＝靈敏度高；偵測極限還要看雜訊（光譜概論 L11）。把增益調大，訊號和雜訊一起放大，偵測極限不會變好。</li>
<li><b>累加 n 次，訊號對雜訊比提高 √n 倍</b>：NMR 掃描累加、FT 一次收全部波長，都是在墊高地板上的訊號。</li>
<li><b>為什麼螢光比 UV 靈敏</b>：螢光在暗背景上量亮光；UV 是在很亮的光裡量「少了一點點」。所以螢光檢品可以稀 10–100 倍（螢光 L01）。</li>
<li><b>Raman 訊號極弱</b>：散射光子裡只有極少數換了能量，所以要先濾掉 Rayleigh，還要躲螢光背景（Raman L5–L6）。</li></ul></div>
<div class="two">
<div class="box"><h3>這張圖的失效處</h3>
<p>{e(C.LIMITS["can"])}</p><p class="red">{e(C.LIMITS["cannot"])}</p><p>{e(C.LIMITS["badge"])}</p></div>
<div class="box"><h3>資料的邊界</h3>
<p>只含已上傳的 20 章。講義引用的教材章號顯示 <b>{missing}</b> 沒有上傳；從「ch10 傳統分析」的檔名看，多半是容量分析、電化學等傳統分析章。所以<b>點數帳目前只有 3 章（{ledger_n["點數帳"]} 題）</b>，補齊後題數與 Te 排序都會改。</p>
<p>標記方法：用關鍵字比對每一題的題幹與選項，不是人工逐題判讀；數字是量級，不是精確值。題本答案不是官方答案表。</p></div>
</div>
<div class="box"><h3>和 v1.0 圖組的關係</h3>
<p>圖0–圖6 退成工具箱：圖1–圖3＝三本帳的章卡；圖4＝讀數污染型與錯題救援；圖6 五格矩陣＝⑤ 五站零件表的前身。<b>入口只剩 ② Te 作戰表一頁。</b></p>
<p>和藥劑學《賦形劑全景》、藥理《器官點位圖》同構：賦形劑＝尺度 × 物理動作 × 物理線；藥＝器官 × 卡法 × 回授環；考點＝訊號鏈站 × 理化性質 × 跨章線。三張圖的地板分別是時間（Arrhenius）、清除（Dose×F／CL）、雜訊（S／N）。</p></div>
<p class="cap">依據：20 章建構講義（光譜 9 章、分離 7 章、MS、非水滴定、水分、灰分）與其中保留的 {NQ} 道歷屆題；v1.0 圖0–圖6。本圖是索引，不是完整教科書；條件與例外回各章的 L 看。{TITLE} {VER}</p>
</section>''')

CSS = open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'style.css'), encoding='utf-8').read()
font_link = (f'<link rel="stylesheet" href="{font_css}">' if font_css else
             '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap">')
doc = f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>{font_link}<style>{CSS}</style></head><body>{''.join(P)}</body></html>'''
open(out, 'w', encoding='utf-8').write(doc)
print('ok', out, 'NQ', NQ, 'tier1', len(tier1_ids), 'tier2', len(tier2_ids), 'tier3', tier3_n, 'calc', NCALC,
      'waves', [len(w[2]) for w in waves])
