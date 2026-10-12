import json, re, sys
sys.path.insert(0, '.')
from tags import OBJ
from collections import Counter, defaultdict
q = json.load(open('questions_tagged.json', encoding='utf-8'))
def normL(x):
    m = re.search(r'l(\d{1,2})$', x, re.I)
    return 'L' + m.group(1) if m else None
rep = {}
for name, (cat, rx) in OBJ.items():
    hit = [r for r in q if rx.search(r['txt'])]
    if not hit: continue
    Ls = defaultdict(Counter)
    for r in hit:
        for x in r['L']:
            n = normL(x)
            if n: Ls[r['ch']][n] += 1
    rep[name] = dict(cat=cat, n=len({r['id'] for r in hit}), chs=dict(Counter(r['ch'] for r in hit).most_common()),
                     L={c: [l for l, _ in v.most_common(3)] for c, v in Ls.items()},
                     samples=[f"{r['ch']}|{r['id']}|{(r['title'] if len(r['title'])>3 and not re.match(r'^[\d\-]+', r['title']) else re.sub(r'\s+',' ',re.sub(r'[*#^]|\(?[A-D]\)?','',r['txt']))[:60])[:60]}" for r in hit[:12]])
json.dump(rep, open('objreport.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in sorted(rep.items(), key=lambda x: -x[1]['n'])[:int(sys.argv[1]) if len(sys.argv)>1 else 200]:
    print(f"## {k} {v['n']}題 {len(v['chs'])}章 {v['chs']}\n L={v['L']}")
    for s in v['samples']: print('   ', s)
