import subprocess,re,glob,os,sys,json
R,OUT=sys.argv[1],sys.argv[2]
FIX={'86dxr7-Q.pdf':'100-1','C1bCVD-Q.pdf':'100-2','SfDzIo-Q.pdf':'101-1'}
PUA={'':'A','':'B','':'C','':'D'}
FW=str.maketrans('ＡＢＣＤ０１２３４５６７８９','ABCD0123456789')
def txt(f,m='-raw'): return subprocess.run(['pdftotext',m,f,'-'],capture_output=True,text=True).stdout
def meta(f,t):
    s=re.sub(r'\s+','',t); b=os.path.basename(f)
    ym=re.search(r'(1[01]\d)年第([一二])次',s)
    sess=FIX.get(b) or (ym.group(1)+'-'+('1' if ym.group(2)=='一' else '2'))
    code=(re.search(r'代號：?(\d{4})',s) or re.search(r'試題代號：?(\d{4})',s)).group(1)
    return sess,code
def parse_q(t):
    for k,v in PUA.items(): t=t.replace(k,'\n'+v+'.')
    lines=[l.strip() for l in t.split('\n')]
    # drop page headers/footers
    keep=[]
    for l in lines:
        if not l: continue
        if re.match(r'^(代\s*號|頁次|類\s*科|科\s*目|考試時間|等\s*別|※|座號|本科目|本試題)',l): continue
        if re.search(r'(專門職業及技術人員|專技高考|分階段考|醫事檢驗師、|治療師考試|獸醫師、助產師)',l): continue
        if re.match(r'^頁次|^\d+－\d+$|^第\s*\d+\s*頁',l): continue
        keep.append(l)
    qs={}; cur=None; n=1
    for l in keep:
        m=re.match(r'^(\d{1,2})\s*[.、．]?\s*(.*)$',l)
        if m and int(m.group(1))==n and (m.group(2) or True):
            # avoid treating numeric option content as new question: require next expected number
            cur=n; qs[cur]=[m.group(2)]; n+=1; continue
        if cur: qs[cur].append(l)
    out={}
    for k,ls in qs.items():
        body='\n'.join(ls)
        parts=re.split(r'(?:^|\n|\s)([A-D])\s*[.．]\s*',body)
        stem=parts[0].strip(); opts={}
        for i in range(1,len(parts)-1,2):
            if parts[i] not in opts: opts[parts[i]]=parts[i+1].strip()
        out[k]=dict(s=re.sub(r'\s*\n\s*','',stem) if re.search(r'[一-鿿]',stem) else stem.replace('\n',' '),o={a:re.sub(r'\s*\n\s*',' ',v) for a,v in opts.items()},ok=sorted(opts)==list('ABCD'))
    return out
def parse_s(t):
    t=t.translate(FW)
    ans={}
    nums=[];
    lines=t.split('\n')
    for i,l in enumerate(lines):
        if l.strip().startswith('題號'):
            ns=re.findall(r'\d+',l)
            # answers on following line starting with 答案
            for j in range(i+1,min(i+4,len(lines))):
                if lines[j].strip().startswith('答案'):
                    a=re.findall(r'[A-D#]',lines[j].replace('答案',''))
                    for x,y in zip(ns,a): ans[int(x)]=y
                    break
    note=''
    m=re.search(r'備\s*註\s*[:：](.*)',t,re.S)
    if m: note=re.sub(r'\s+','',m.group(1))
    return ans,note
Q={};S={}
for f in sorted(glob.glob(R+'/*.pdf')):
    t=txt(f); sess,code=meta(f,t)
    if '標準答案' in re.sub(r'\s','',t)[:200]: S[(sess,code)]=dict(zip(('a','note'),parse_s(txt(f,'-layout'))),file=os.path.basename(f))
    else: Q[(sess,code)]=dict(q=parse_q(t),file=os.path.basename(f))
res=[]
for (sess,code),d in sorted(Q.items()):
    sa=S.get((sess,code))
    for k,v in sorted(d['q'].items()):
        a=sa['a'].get(k) if sa else None
        res.append(dict(id=f'{sess}-{k}',sess=sess,code=code,n=k,a=a,**v))
    print(sess,code,d['file'],'Q',len(d['q']),'bad',sum(not v['ok'] for v in d['q'].values()),'S',sa['file'] if sa else None,len(sa['a']) if sa else 0,(sa or {}).get('note','')[:80])
for k in S:
    if k not in Q: print('answers without Q',k,S[k]['file'])
json.dump(dict(q=res,s={f'{a}|{b}':v for (a,b),v in S.items()}),open(OUT,'w'),ensure_ascii=False,indent=0)
