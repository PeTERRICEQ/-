// 每一個路由都能開、每一個內部連結都解析得到；抽 40 個跳轉＋返回
const {chromium}=require(process.env.PW||'/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1366,height:900}});const errs=[];p.on('pageerror',x=>errs.push(x.message));
await p.goto('http://localhost:8766/index.html#home');await p.waitForTimeout(800);
const routes=await p.evaluate(()=>{const r=['home','mx','fp','te','notes'];IDX.fields.forEach(f=>r.push('f.'+f.key));
 IDX.chapters.forEach(c=>{r.push('c.'+c.key,'r.'+c.key+'.0');c.M.forEach((m,i)=>r.push('m.'+c.key+'.'+i));c.L.forEach(l=>r.push('k.'+c.key+'.'+l.id));
   (c.fp||[]).forEach((x,i)=>r.push('fp.'+c.key+'.'+(i+1)));if(c.fp)r.push('fp.'+c.key)});
 S.qs.forEach(q=>r.push('q.'+q.id));[1,2,3,4].forEach(n=>r.push('s.'+n));IDX.lines.forEach(l=>r.push('l.'+l.n));
 IDX.badges.forEach(([g])=>{r.push('mx.'+BCODE[g]);IDX.fields.forEach(f=>r.push('mx.'+BCODE[g]+'.'+f.key));[0,1,2,3,4].forEach(z=>r.push('mx.'+BCODE[g]+'.z'+z))});
 IDX.te.forEach((t,i)=>r.push('te.'+i));return r});
console.log('routes',routes.length);
const seen=new Set(),bad=[];let hrefs=0;
for(const r of routes){await p.evaluate(h=>{location.hash=h},r);await p.waitForFunction(h=>S.cur===h,r,{timeout:5000}).catch(()=>bad.push(['timeout',r]));
 const pr=await p.evaluate(h=>{const x=parse(h);return h==='home'||x.lv>0||x.lens||x.four||x.line||x.g?'ok':'unparsed'},r);if(pr!=='ok')bad.push(['route',r]);
 if(r.startsWith('q.'))await p.evaluate(()=>reveal());
 const res=await p.evaluate(()=>{const out=[];document.querySelectorAll('#stage a[href^="#"],#focus a[href^="#"],#crumb a').forEach(a=>out.push(a.getAttribute('href').slice(1)));return out});
 for(const h of res){if(seen.has(h)||h==='')continue;seen.add(h);hrefs++;
   const v=await p.evaluate(h=>{const r=parse(h);if(h!=="home"&&r.lv===0&&!r.lens&&!r.four&&!r.line&&!r.g)return 'unparsed';
     if(r.lens==='mx'&&h.split('.').length>1&&!r.b)return 'badmx';if(r.lens==='fp'&&h.split('.').length>1&&!r.c)return 'badfp';
     if(r.a){return loadCh(r.ch).then(()=>S.chData[r.ch].cards[r.a]?'ok':'nocard')}return 'ok'},h);
   if(v!=='ok')bad.push([v,h,'from',r])}}
console.log('unique hrefs',hrefs,'bad',bad.length,JSON.stringify(bad.slice(0,15)));
const sample=[...seen].filter((h,i)=>i%Math.max(1,Math.floor(seen.size/40))===0).slice(0,40);let backOK=0;
for(const h of sample){if(h==='c.uv')continue;await p.evaluate(()=>{location.hash='c.uv'});await p.waitForFunction(()=>S.cur==='c.uv');
 await p.evaluate(h=>{location.hash=h},h);await p.waitForFunction(h=>S.cur===h,h);await p.goBack();await p.waitForFunction(()=>S.cur==='c.uv',null,{timeout:3000}).then(()=>backOK++).catch(()=>bad.push(['back',h]))}
console.log('jump+back',backOK,'/',sample.length,'pageerrors',errs.length,errs.slice(0,5));
if(bad.length||errs.length)process.exitCode=1;
await b.close()})();
