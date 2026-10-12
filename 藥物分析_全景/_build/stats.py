import json, re, sys
from collections import Counter, defaultdict
from tags import OBJ, PROP, CH_PROP, STA, LINE, CALC_HINT, FORM
q = json.load(open('questions.json', encoding='utf-8'))
def clean(r):
    s = r['title'] + '\n' + r['stem']
    s = re.sub(r'\[\[[^\]]*\]\]|\^[\w-]+|<[^>]+>', ' ', s)
    s = re.sub(r'^.*(來源|PDF|題本|原年梯|任務).*$', ' ', s, flags=re.M) if r['ch'] not in ('非水滴定','旋光') else s
    return s
for r in q: r['txt'] = clean(r)
out = {}
# 物件
obj = {}
for name, (cat, rx) in OBJ.items():
    hit = [r for r in q if rx.search(r['txt'])]
    ids = {r['id'] for r in hit}
    chs = Counter(r['ch'] for r in hit)
    obj[name] = dict(cat=cat, n=len(ids), nch=len(chs), chs=dict(chs.most_common()))
out['obj'] = obj
# 性質
pc, pexp, cross = Counter(), 0, Counter()
for r in q:
    tags = [k for k, (_, rx) in PROP.items() if rx.search(r['txt'])]
    r['prop'] = tags or [CH_PROP[r['ch']]]
    if tags: pexp += 1
    for t in r['prop']:
        pc[t] += 1
        if t != CH_PROP[r['ch']]: cross[t] += 1
out['prop'] = {k: dict(name=PROP[k][0], n=pc[k], cross=cross[k],
               chs=len({r['ch'] for r in q if k in r['prop']})) for k in PROP}
out['prop_explicit'] = pexp
# 站
sc = Counter(); none = 0
for r in q:
    r['sta'] = [k for k, rx in STA.items() if rx.search(r['txt'])]
    if not r['sta']: none += 1
    for k in r['sta']: sc[k] += 1
out['sta'] = dict(sc); out['sta_none'] = none
# 線
lc = {}
for k, rx in LINE.items():
    hit = [r for r in q if rx.search(r['txt'])]
    lc[k] = dict(n=len({r['id'] for r in hit}), chs=dict(Counter(r['ch'] for r in hit).most_common()))
out['line'] = lc
# 算式
def is_calc(r):
    if r['ch'] in ('非水滴定', '旋光'):
        return bool(re.search(r'[÷×]|＝\s*[-−+]?\d', r['txt']))
    opts = re.findall(r'(?:\(|\*\*|^-\s*\**\(?)[A-D](?:\)|\*\*)\**\s*([^\n]{0,40})', r['txt'], re.M)
    num = [o for o in opts if re.match(r'\s*[-−+]?\s*\$?\s*[\d.]+\s*(%|nm|mg|mL|cm|ppm|Hz|min|°|μ|g|N|M|kJ|\$|$|\s|：|,|，|×|/)', o)]
    return len(opts) >= 3 and len(num) >= 3
calc = [r for r in q if is_calc(r)]
fc = {}
for k, rx in FORM.items():
    hit = [r for r in calc if rx.search(r['txt'])]
    fc[k] = dict(n=len(hit), chs=dict(Counter(r['ch'] for r in hit).most_common()))
out['calc_n'] = len(calc); out['form'] = fc
out['N'] = len({r['id'] for r in q}); out['rows'] = len(q)
json.dump(out, open('stats.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(q, open('questions_tagged.json', 'w', encoding='utf-8'), ensure_ascii=False)
if '-v' in sys.argv:
    print('N', out['N'], 'prop explicit', pexp, 'sta none', none, 'calc', len(calc))
    for k, v in sorted(obj.items(), key=lambda x: -x[1]['n']): print(f"{v['n']:4d} {v['nch']:2d}章 {v['cat']} {k} | {v['chs']}")
    print(out['prop']); print(out['sta'])
    for k, v in lc.items(): print(k, v['n'], len(v['chs']), v['chs'])
    for k, v in fc.items(): print(k, v['n'], v['chs'])
