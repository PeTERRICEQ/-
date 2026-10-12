"""把全景內容、L 精華卡、歷屆題整理成互動網頁要用的一份 JSON。
用法：python3 export_app.py questions_tagged.json lcards.json app_data.json
"""
import json, re, sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from tags import OBJ, PROP, CH_PROP, STA, LINE
import content as C

qsrc, csrc, out = sys.argv[1:4]
Q = json.load(open(qsrc, encoding='utf-8'))
CARDS = json.load(open(csrc, encoding='utf-8'))

CH_ORDER = ['光譜概論', 'UV', '螢光', 'IR', 'Raman', 'NMR', '原子光譜', '折光', '旋光',
            '萃取', '層析概論', 'TLC', 'HPLC', 'GC', 'SFC', 'CE', 'MS', '非水滴定', '水分', '灰分']
ALIAS = {'非水': '非水滴定', 'SFC／SFE': 'SFC', 'SFE': 'SFC'}
ONE_DIGIT = {'旋光', '折光', 'Raman', '光譜概論'}   # 這幾章的 L 編號不補零
CH_NAMES = sorted(set(CH_ORDER) | set(ALIAS), key=len, reverse=True)

def norm_ch(x): return ALIAS.get(x, x)
def norm_L(ch, num):
    n = int(num)
    return f'L{n}' if ch in ONE_DIGIT else f'L{n:02d}'
def lead_chs(text):
    """片段開頭的章名，加上括號裡「章 L…」形式的章名。"""
    found = []
    m = re.match(r'\s*(' + '|'.join(map(re.escape, CH_NAMES)) + r')(?=[\s、L（(]|$)', text)
    if m: found.append(norm_ch(m.group(1)))
    for m in re.finditer(r'(?:^|[（(、；\s])(' + '|'.join(map(re.escape, CH_NAMES)) + r')\s+(?:L\d|[^\s）)]*節|代表題)', text):
        c = norm_ch(m.group(1))
        if c not in found: found.append(c)
    # 「折光、旋光 固定…」這類並列開頭
    m = re.match(r'\s*((?:(?:' + '|'.join(map(re.escape, CH_NAMES)) + r')、)+(?:' + '|'.join(map(re.escape, CH_NAMES)) + r'))\s', text)
    if m:
        for c in m.group(1).split('、'):
            c = norm_ch(c)
            if c not in found: found.append(c)
    for m in re.finditer(r'（(' + '|'.join(map(re.escape, CH_NAMES)) + r')）', text):
        c = norm_ch(m.group(1))
        if c not in found: found.append(c)
    return found
def frag_list(s, sep='；'):
    out, prev = [], []
    for f in s.split(sep):
        f = f.strip()
        if not f: continue
        ch = lead_chs(f) or prev
        out.append(dict(t=f, ch=ch)); prev = ch
    return out
def first_L(ch, text):
    m = re.search(r'L(\d{1,2})', text)
    return norm_L(ch, m.group(1)) if (m and ch) else None

def ptags(text):
    return [k for k, (_, rx) in PROP.items() if rx.search(text)]
def stags(text): return [k for k, rx in STA.items() if rx.search(text)]
def ltags(text): return [k for k, rx in LINE.items() if rx.search(text)]

# ── 題目 ──
te_rx = [(i, [OBJ[k][1] for k in row[1]]) for i, row in enumerate(C.TE)]
qs = []
seen = set()
for r in Q:
    key = (r['ch'], r['id'])
    if key in seen: continue
    seen.add(key)
    t = r['txt']
    stem = re.sub(r'\[\[[^\]|]*\|([^\]]*)\]\]', r'\1', r['stem'])
    stem = re.sub(r'\[\[([^\]#|]*)(#[^\]]*)?\]\]', r'\1', stem)
    stem = re.sub(r'^\s*\^[\w-]+\s*$|<a id="[^"]*"></a>', '', stem, flags=re.M)
    stem = re.sub(r'^.*(來源|題本原題號|PDF p|答案身分|原年梯).*$', '', stem, flags=re.M)
    stem = re.sub(r'\*\*原題[^*]*\*\*', '', stem).replace('**', '')
    stem = re.sub(r'\n\s*\n+', '\n', stem).strip()
    Ls = sorted({norm_L(r['ch'], m.group(1)) for x in r['L'] for m in [re.search(r'l(\d{1,2})$', x, re.I)] if m})
    qs.append(dict(id=r['id'], ch=r['ch'], title=r['title'][:40], stem=stem[:700], ans=r['ans'][:12], L=Ls,
                   why=re.sub(r'\s*[、與和]?\s*\bF\d{2}\b', '', r.get('why', '')).replace('→  →', '→'), sec=r.get('sec', ''),
                   p=r.get('prop') or [CH_PROP[r['ch']]], s=stags(t), l=ltags(t),
                   te=[i for i, rx in te_rx if any(x.search(t) for x in rx)]))

def nid(rows): return len({q['id'] for q in rows})

# ── L 精華卡 ──
cards = []
for c in CARDS:
    short = ' '.join([c['title'], c['ask'], c['chain']])
    p = ptags(short) or [CH_PROP[c['ch']]]
    cards.append(dict(c, p=p, s=stags(short), l=ltags(short + ' ' + c['trap'])))
order = {ch: i for i, ch in enumerate(CH_ORDER)}
cards.sort(key=lambda c: (order[c['ch']], int(re.sub(r'\D', '', c['L']) or 0)))

# ── Te 物件 ──
te = []
for i, (name, keys, props, sta, line, pos, reds) in enumerate(C.TE):
    rows = [q for q in qs if i in q['te']]
    n = nid(rows)
    frags = frag_list(pos)
    rd = [dict(type=a, t=b, cite=c, ch=lead_chs(c)) for a, b, c in reds]
    te.append(dict(i=i, name=name, n=n, nch=len({q['ch'] for q in rows}),
                   chs=Counter(q['ch'] for q in rows).most_common(), p=list(props), s=list(sta), line=line,
                   frags=frags, reds=rd, wave=1 if n >= 40 else 2 if n >= 20 else 3))

# ── 題目接回全景紅字：同一個 Te 物件、同一章、引用同一個 L ──
def cite_Ls(ch, cite):
    out = set()
    for seg in re.split(r'[、，]', cite):
        seg = seg.strip()
        c = lead_chs(seg)
        if (c and c[0] == ch) or (not c and ch):
            for a, b in re.findall(r'L(\d{1,2})(?:–L?(\d{1,2}))?', seg):
                for n in range(int(a), int(b or a) + 1): out.add(norm_L(ch, n))
    return out
for q in qs:
    q['red'] = []
    for ti in q['te']:
        for j, rd in enumerate(te[ti]['reds']):
            cl = cite_Ls(q['ch'], rd['cite'])
            if q['ch'] in rd['ch'] and len(cl) <= 2 and cl & set(q['L']):
                q['red'].append([ti, j])

# ── 線 ──
def mk_line(name, rule, known, chain, ti):
    rows = [q for q in qs if name in q['l']]
    nodes = []
    for a, b in chain:
        chs = lead_chs(a)
        ch = chs[0] if chs else None
        nodes.append(dict(label=a, t=b, ch=ch, L=first_L(ch, a)))
    return dict(name=name, rule=rule, known=known, ti=ti, n=nid(rows), nch=len({q['ch'] for q in rows}), nodes=nodes)
lines = [mk_line(*l) for l in C.LINES] + [mk_line(*C.FLOOR)]

# ── 性質 ──
CROSS = C.CROSS
props = []
for k, name, learn, methods, read in C.PROPS:
    rows = [q for q in qs if k in q['p']]
    split = frag_list
    props.append(dict(k=k, name=name, learn=learn, methods=methods, read=read, color=C.PROP_COLOR[k],
                      n=nid(rows), nch=len({q['ch'] for q in rows}),
                      cross=sum(1 for q in rows if CH_PROP[q['ch']] != k),
                      tool=split(CROSS[k][0]), trap=split(CROSS[k][1])))

# ── 五站與零件 ──
PARTS = C.PARTS
stations = [dict(k=k, job=j, parts=x, n=nid([q for q in qs if k in q['s']])) for k, j, x in C.STATIONS]
parts = {norm_ch(r[0]): dict(zip('源樣選測算', r[1:])) for r in PARTS}

# ── 章 ──
sk = {ch: (keys, entry) for ch, keys, entry in C.SKELETON}
ledger_of = {ch: name for name, _, chl, _ in C.LEDGERS for ch in chl}
chapters = []
for i, ch in enumerate(CH_ORDER):
    chapters.append(dict(code=f'c{i+1:02d}', name=ch, ledger=ledger_of[ch], n=sum(1 for q in qs if q['ch'] == ch),
                         main=CH_PROP[ch], parts=parts.get(ch, {}), entry=sk.get(ch, ([], ''))[1],
                         ncards=sum(1 for c in cards if c['ch'] == ch)))

# ── 格子熱度：性質 × 站 ──
grid = {k: {s: nid([q for q in qs if k in q['p'] and s in q['s']]) for s in '源樣選測算'} for k in PROP}

calc = [dict(name=n, ch=[norm_ch(x) for x in chl], f=f, w=w, ex=x, trap=t) for n, chl, f, w, x, t in C.CALC]
ledgers = [dict(name=n, plain=s, chs=chl, one=a, n=sum(1 for q in qs if q['ch'] in chl)) for n, s, chl, a in C.LEDGERS]

data = dict(meta=dict(NQ=len({q['id'] for q in qs}), NC=len(cards), ver='v0.1'),
            props=props, stations=stations, chapters=chapters, ledgers=ledgers, lines=lines, te=te,
            cards=cards, qs=qs, grid=grid, calc=calc, read_ways=C.READ_WAYS)
json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('ok', out, os.path.getsize(out) // 1024, 'KB', 'cards', len(cards), 'qs', len(qs), 'te', len(te))
