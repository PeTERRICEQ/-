import json,re,sys,difflib,collections
SP=sys.argv[1]; D='/home/user/-/藥物分析_全景/app/data/'
k=json.load(open(SP+'/k16/k16.json'))
qj={x['id']:x for x in json.load(open(D+'q.json'))}
tr={}
for x in json.load(open(SP+'/trad/trad.json')):
    s,n=x['id'].rsplit('-',1); tr[f'{s}-{int(n)}']=x
def norm(s): return re.sub(r'[\W_]+','',s or '').lower()
out=[];stat=collections.Counter();mism=[]
for q in k['q']:
    if q['code']=='2307' and q['sess']=='106-2': continue
    if q['n']>40: continue
    e=dict(id=q['id'],sess=q['sess'],n=q['n'],s=q['s'],o=q['o'],a=q['a'],ok=q['ok'])
    src=None
    if q['id'] in qj: src=('q',qj[q['id']])
    elif q['id'] in tr: src=('t',tr[q['id']])
    if src:
        r=difflib.SequenceMatcher(None,norm(q['s'])[:80],norm(src[1]['s'])[:80]).ratio()
        if r<0.5: mism.append((q['id'],round(r,2),q['s'][:40],src[1]['s'][:40])); stat['mismatch']+=1
        else:
            stat[src[0]]+=1
            if src[0]=='q': e.update(ch=src[1]['ch'],f=src[1].get('f'),tag='q')
            else: e.update(trad=src[1]['ch'],chn=src[1]['chn'],tag='t')
            if src[1].get('a') and q['a'] and src[1]['a']!=q['a'] and q['a']!='#': mism.append((q['id'],'ANS',q['a'],src[1]['a']))
            if not q['a']: e['a']=src[1].get('a'); e['a_src']='bank'
    else: stat['new']+=1
    out.append(e)
print(stat,len(out))
for m in mism: print(m)
json.dump(out,open(SP+'/k16/yf.json','w'),ensure_ascii=False,indent=0)
