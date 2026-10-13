import json,sys,collections
SP=sys.argv[1]+'/k16/'
d=json.load(open(SP+'yf.json'))
w={}
for f in ('w1_out1.json','w1_out2.json'): w.update(json.load(open(SP+f)))
miss=[]
for q in d:
    if q.get('tag')!='q':
        if q['id'] in w: q['ch']=w[q['id']]['ch']; q['note']=w[q['id']].get('note')
        else: miss.append(q['id'])
d+=json.load(open(SP+'add110_1.json'))
for q in d:
    for k in ('tag','trad','chn','f','src'): q.pop(k,None)
d.sort(key=lambda q:(q['sess'],q['n']))
print('missing',miss,'total',len(d))
json.dump(d,open(SP+'yf_all.json','w'),ensure_ascii=False,indent=0)
c=collections.Counter(q['ch'][0] for q in d)
old=collections.Counter(q['ch'][0] for q in d if int(q['sess'][:3])<=107)
new=collections.Counter(q['ch'][0] for q in d if int(q['sess'][:3])>=108)
for k,v in c.most_common(): print(f'{k:6}{v:5}{old[k]:5}{new[k]:5}')
