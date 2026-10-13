"""從 20 章講義抽出每個 L 小節的精華：標題、先問、短鏈（機轉）、立即用一次（例子）、易錯、閉卷自問與答案。"""
import re, glob, os, json, sys
from parse_q import CH, chof  # 章名對照
SRC, OUT = sys.argv[1], sys.argv[2]
HEAD = re.compile(r'^(#{2,4}) *(L\d{1,2})(?:·[^｜|]*)?[｜|：: ]\s*(.+)$', re.M)
IMG = re.compile(r'!\[[^\]]*\]\(data:[^)]*\)|<img[^>]*>')
def clean(s):
    s = IMG.sub('', s)
    s = re.sub(r'\[\[[^\]|]*\|([^\]]*)\]\]', r'\1', s)       # [[x|顯示]] → 顯示
    s = re.sub(r'\[\[([^\]#|]*)(#[^\]]*)?\]\]', r'\1', s)    # [[x]] → x
    s = re.sub(r'<a id="[^"]*"></a>|\^[\w-]+\s*$', '', s, flags=re.M)
    s = re.sub(r'\*\*', '', s)
    return re.sub(r'[ \t]+\n', '\n', s).strip()
def field(block, names):
    for n in names:
        m = re.search(r'\*\*[^*\n]{0,14}?' + n + r'[：:]\*\*\s*(.+?)(?=\n\s*\n|\n\*\*|\n<details|\n\^|\Z)', block, re.S)
        if m: return clean(m.group(1))
    return ''
out = []
for f in sorted(glob.glob(os.path.join(SRC, '*.md'))):
    ch = chof(f)
    t = open(f, encoding='utf-8').read()
    hs = [h for h in HEAD.finditer(t)]
    seen = set()
    for i, h in enumerate(hs):
        lid = 'L' + str(int(h.group(2)[1:])).zfill(2 if ch not in ('旋光','折光','Raman','光譜概論') else 1)
        if lid in seen: continue
        end = hs[i+1].start() if i+1 < len(hs) else h.end() + 8000
        nxt = re.search(r'^#{1,' + str(len(h.group(1))) + r'} ', t[h.end():end], re.M)
        block = t[h.end(): h.end() + nxt.start()] if nxt else t[h.end():end]
        ask = field(block, ['先問', '情境'])
        chain = field(block, ['短鏈', '短推理', '機轉', '一句話', '鏈'])
        if not chain:
            m = re.search(r'^>\s*(.+)$', block, re.M)
            chain = clean(m.group(1)) if m else ''
        why = field(block, ['白話理由', '為什麼', '理由'])
        if not why:  # 第一個普通段落
            for para in re.split(r'\n\s*\n', block):
                p = para.strip()
                if p and not p.startswith(('**', '>', '<', '^', '|', '-', '#', '[[', '做題', '回跳', '來源')):
                    why = clean(p); break
        ex = field(block, ['立即用一次', '代表例子', '具體例子', '立刻用', '例子', '動手看'])
        trap = field(block, ['條件／易錯', '最容易錯', '條件與陷阱', '易錯', '條件'])
        q = field(block, ['閉卷自問', '閉卷問'])
        ans = ''
        m = re.search(r'<details>\s*<summary>([^<]*)</summary>(.*?)</details>', block, re.S)
        if m:
            sm = clean(m.group(1))
            if not q and ('？' in sm or '回答' in sm or '說出' in sm):
                q = re.sub(r'^.*?(回答|說出[^：:]*)[：:]', '', sm)
            if not ask and q: ask = q
            ans = clean(m.group(2))[:400]
        if not (chain or ex or why): continue
        seen.add(lid)
        out.append(dict(ch=ch, L=lid, title=clean(h.group(3))[:60], ask=ask[:160], chain=chain[:260],
                        why=why[:420], ex=ex[:320], trap=trap[:240], q=q[:200], ans=ans))
# 非水滴定沒有 L 小節：改用 NAT 必背卡
for f in glob.glob(os.path.join(SRC, '3469a43c-*.md')) + glob.glob(os.path.join(SRC, '*_非水滴定_*.md')):
    t = open(f, encoding='utf-8').read()
    for m in re.finditer(r'^> \[!note\][^\n]*?(NAT\d+)｜([^\n]+)\n((?:>.*\n?)+)', t, re.M):
        body = re.sub(r'^> ?', '', m.group(3), flags=re.M)
        fact = field(body, ['完整事實'])
        if not fact:
            mm = re.search(r'\*\*完整事實[：:]\*\*(.*?)(?=\n\*\*成立|\Z)', body, re.S)
            fact = clean(mm.group(1)) if mm else ''
        out.append(dict(ch='非水滴定', L=m.group(1), title=clean(m.group(2))[:60], ask='', chain=fact[:300], why='',
                        ex='', trap=field(body, ['會接到的核心判讀'])[:240], q='', ans=''))
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
from collections import Counter, defaultdict
c = Counter(r['ch'] for r in out)
miss = defaultdict(lambda: Counter())
for r in out:
    for k in ('ask', 'chain', 'ex', 'trap', 'q'):
        if not r[k]: miss[r['ch']][k] += 1
print(len(out))
for ch, n in sorted(c.items(), key=lambda x: -x[1]): print(ch, n, dict(miss[ch]))
