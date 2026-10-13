# 彙整 w2：每章 規則數、80% 需幾條、錨點比例、五軸分布、舊→新命中率（100–107 找規則，108–115 驗證）
import json,glob,sys,collections,random
SP=sys.argv[1]+'/k16/'
d={q['id']:q for q in json.load(open(SP+'yf_all.json'))}
lab={};K={}
for f in sorted(glob.glob(SP+'w2/g*_q.json')): lab.update(json.load(open(f)))
for f in sorted(glob.glob(SP+'w2/g*_k.json')): K.update(json.load(open(f)))
miss=[i for i,q in d.items() if i not in lab]
by=collections.defaultdict(list)
for i,l in lab.items():
    if i in d: by[d[i]['ch'][0]].append((i,l))
def yr(i): return int(i[:3])
rows=[]
AX=collections.Counter(); ALL=0
for ch,L in sorted(by.items(),key=lambda x:-len(x[1])):
    n=len(L); c=collections.Counter(l['k'] for _,l in L)
    cum=0;need=None
    for j,(k,v) in enumerate(c.most_common(),1):
        cum+=v
        if need is None and cum>=0.8*n: need=j
    anc=sum(v for k,v in c.items() if K.get(k,{}).get('type')=='A' or '.A' in k)
    old={l['k'] for i,l in L if yr(i)<=107}; new=[l['k'] for i,l in L if yr(i)>=108]
    hit=sum(1 for k in new if k in old)/max(1,len(new))
    # 只用規則（非錨點）時的新題命中
    newR=[k for k in new if '.A' not in k]; hitR=sum(1 for k in newR if k in old)/max(1,len(newR))
    ax=collections.Counter(l['ax'][0] for _,l in L); AX.update(ax); ALL+=n
    cov=collections.Counter(l.get('cov') for _,l in L)
    rows.append((ch,n,len(c),need,anc,hit,hitR,ax,cov))
print('未標記',len(miss),miss[:10])
print(f"{'章':6}{'題':>5}{'規則':>5}{'80%':>5}{'錨點題':>6}{'舊→新':>7}{'規則舊→新':>9}  五軸1-5        cov")
for ch,n,nk,need,anc,hit,hitR,ax,cov in rows:
    print(f"{ch:6}{n:5}{nk:5}{need:5}{anc:6}{hit:7.0%}{hitR:9.0%}  {[ax.get(a,0) for a in range(1,6)]}  {dict(cov)}")
print('全科五軸',{a:f'{AX[a]/ALL:.0%}' for a in range(1,6)},ALL)
