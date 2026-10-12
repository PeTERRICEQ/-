"""從 20 章建構講義抽出歷屆題：章、題號、題幹＋選項、題本答案、回查 L。"""
import re, glob, os, json, sys
CH = {'1be15b6f':'CE','2bbd080b':'光譜概論','2cf1fd9f':'UV','3469a43c':'非水滴定','448d15a9':'旋光',
      '46c9d32d':'HPLC','52cd3266':'灰分','57b57513':'原子光譜','7170a493':'IR','76c9fdd4':'萃取',
      '946ce2d2':'Raman','a24b26a4':'層析概論','a5fee3b8':'SFC','af08da8a':'折光','b178dc9f':'MS',
      'be86ea18':'TLC','c77f3c0b':'螢光','d9f42c87':'GC','eb4f5773':'水分','fd7d45ef':'NMR'}
if __name__ == '__main__':
    SRC = sys.argv[1]
    OUT = sys.argv[2]
    ID = re.compile(r'(1[01]\d)\s*-\s*([12])\s*(?:#\s*|-\s*|第\s*)(\d{1,2})(?!\d)')
    HEAD = re.compile(r'^#{3,4} *Q ?\d{1,3}[｜|].*$', re.M)
    rows = []
    IMG = re.compile(r'!\[[^\]]*\]\(data:[^)]*\)|<img[^>]*>|data:image/[a-z]+;base64,[A-Za-z0-9+/=]+')
    STOP = ['<details', '**題幹觸發', '**逐項判讀', '題本印刷答案', '**題本答案', '**真正問什麼']
    for f in sorted(glob.glob(os.path.join(SRC, '*.md'))):
        ch = CH[os.path.basename(f)[:8]]
        t = open(f, encoding='utf-8').read()
        heads = list(HEAD.finditer(t))
        if heads:
            for i, h in enumerate(heads):
                m = ID.search(h.group(0))
                if not m:
                    continue
                end = heads[i+1].start() if i+1 < len(heads) else min(len(t), h.end()+6000)
                block = IMG.sub('［圖］', t[h.end():end])
                mo = re.search(r'\(A\)|\*\*A\*\*|^\s*-?\s*A[\.、．\s]', block, re.M)
                o = mo.start() if mo else 0
                cuts = [i for i in (block.find(k, o) for k in STOP) if i > o]
                cut = min(cuts) if cuts else min(len(block), 1500)
                stem = block[:cut]
                det = block[cut:]
                ans = re.search(r'(?:題本印刷答案|題本答案|答案)[：:]\**\s*\(?([A-E])', block)
                ls = sorted(set(re.findall(r'[#^|｜]((?:[A-Za-z]{2,4}-)?(?:[a-z]-)?l\d{1,2}|L\d{1,2})\b', det, re.I)))
                rows.append(dict(ch=ch, id=f"{m.group(1)}-{m.group(2)}-{int(m.group(3)):02d}",
                                 title=h.group(0).split('｜', 2)[-1].strip(), stem=stem.strip(),
                                 ans=ans.group(1) if ans else '', L=ls))
        else:  # 非水、旋光：用完整打靶表
            for line in t.splitlines():
                if line.startswith('|') and ID.search(line.split('|')[1] if line.count('|') > 3 else ''):
                    cells = [c.strip() for c in line.strip('|').split('|')]
                    m = ID.search(cells[0])
                    rows.append(dict(ch=ch, id=f"{m.group(1)}-{m.group(2)}-{int(m.group(3)):02d}",
                                     title=cells[1], stem=' '.join(cells[1:4]), ans=cells[2][:20], L=[]))
    # 去重（同章同題號保留第一筆）
    seen, uniq = set(), []
    for r in rows:
        k = (r['ch'], r['id'])
        if k not in seen:
            seen.add(k); uniq.append(r)
    json.dump(uniq, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    from collections import Counter
    c = Counter(r['ch'] for r in uniq)
    print(len(uniq), 'rows;', len({r['id'] for r in uniq}), 'unique ids')
    print(sorted(c.items(), key=lambda x: -x[1]))
    print('no-answer', sum(1 for r in uniq if not r['ans']), 'no-L', sum(1 for r in uniq if not r['L']))
