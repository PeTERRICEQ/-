// 兩個瀏覽器環境（像兩台 iPad）共用一個模擬雲端 db，驗證筆記與進度同步
const {chromium}=require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)process.exitCode=1};
const store=new Map();const subs=[];let sid=0;
const parent=p=>p.split('/').slice(0,-1).join('/');
function snapFor(sub){if(sub.kind==='doc'){const d=store.get(sub.path);return {exists:!!d,id:sub.path.split('/').pop(),data:d||null}}
  return {docs:[...store].filter(([k])=>parent(k)===sub.path).map(([k,v])=>({id:k.split('/').pop(),data:v}))}}
async function push(changedPath){for(const s of subs){if((s.kind==='doc'&&s.path===changedPath)||(s.kind==='col'&&parent(changedPath)===s.path)){
  const snap=snapFor(s);if(s.kind==='col'){const prev=s.last||new Map();const now=new Map(snap.docs.map(d=>[d.id,JSON.stringify(d.data)]));
    snap.changes=[];for(const d of snap.docs){if(!prev.has(d.id))snap.changes.push({type:'added',id:d.id,data:d.data});else if(prev.get(d.id)!==now.get(d.id))snap.changes.push({type:'modified',id:d.id,data:d.data})}
    for(const id of prev.keys())if(!now.has(id))snap.changes.push({type:'removed',id,data:null});s.last=now;if(!snap.changes.length)continue}
  await s.page.evaluate(([id,sn])=>window.__dbpush(id,sn),[s.id,snap]).catch(()=>{})}}}
const mock=`(()=>{const cbs={};window.__dbpush=(id,sn)=>{const cb=cbs[id];if(!cb)return;
  if(sn.docs){cb({docs:sn.docs.map(d=>({id:d.id,exists:true,data:()=>d.data})),docChanges:()=>(sn.changes||sn.docs.map(d=>({type:'added',id:d.id,data:d.data}))).map(c=>({type:c.type,doc:{id:c.id,exists:c.type!=='removed',data:()=>c.data}})),metadata:{hasPendingWrites:false,fromCache:false}})}
  else cb({exists:sn.exists,id:sn.id,data:()=>sn.data,metadata:{hasPendingWrites:false,fromCache:false}})};
 const docRef=path=>({id:path.split('/').pop(),path,get:async()=>{const r=await window.__dbget(path);return {exists:!!r,data:()=>r,metadata:{hasPendingWrites:false}}},
   set:d=>window.__dbset(path,d),update:d=>window.__dbset(path,d),delete:()=>window.__dbdel(path),
   onSnapshot:(cb,err)=>{const id=Math.random().toString(36).slice(2);cbs[id]=cb;window.__dbsub('doc',path,id);return()=>delete cbs[id]},
   collection:sub=>colRef(path+'/'+sub)});
 const colRef=path=>({path,doc:id=>docRef(path+'/'+id),get:async()=>({docs:(await window.__dbcol(path)).map(([id,d])=>({id,exists:true,data:()=>d}))}),onSnapshot:(cb,err)=>{const id=Math.random().toString(36).slice(2);cbs[id]=cb;window.__dbsub('col',path,id);return()=>delete cbs[id]}});
 const db={doc:docRef,collection:colRef};
 window.claude={use:async n=>n==='db'?db:n==='user'?{id:async()=>'u1'}:null}})()`;
(async()=>{const b=await chromium.launch();const pages=[];
for(const [w,h] of [[834,1194],[1366,1024]]){const ctx=await b.newContext({viewport:{width:w,height:h},hasTouch:true});
  await ctx.exposeBinding('__dbget',(src,p)=>store.get(p)||null);
  await ctx.exposeBinding('__dbcol',(src,p)=>[...store].filter(([k])=>parent(k)===p).map(([k,v])=>[k.split('/').pop(),v]));
  await ctx.exposeBinding('__dbset',async(src,p,d)=>{store.set(p,JSON.parse(JSON.stringify(d)));await push(p)});
  await ctx.exposeBinding('__dbdel',async(src,p)=>{store.delete(p);await push(p)});
  await ctx.exposeBinding('__dbsub',async(src,kind,path,id)=>{const s={kind,path,id,page:src.page};subs.push(s);const sn=snapFor(s);
    if(kind==='col'){s.last=new Map(sn.docs.map(d=>[d.id,JSON.stringify(d.data)]))}setTimeout(()=>src.page.evaluate(([id,sn])=>window.__dbpush(id,sn),[id,sn]).catch(()=>{}),30)});
  await ctx.addInitScript(mock);const p=await ctx.newPage();const e=[];p.on('pageerror',x=>e.push(x.message));p.errs=e;pages.push(p)}
const [A,B]=pages;
// 舊版（v1）把每章進度存在 data/users/<id>/c02：開新版時要自動帶入
store.set('data/users/u1/c02',{k:{'L|UV|L03':1,'L|UV|L05':0},ch:'UV'});
for(const p of pages){await p.goto('http://localhost:8766/index.html#k.uv.l3');await p.waitForTimeout(1200)}
ok((await A.textContent('#nstat')).includes('已同步'),'A 顯示已同步到帳號');
{const m=(store.get('data/users/u1/progress')||{}).m||{};ok(m['c:uv.l3']&&m['c:uv.l3'][0]==='J'&&m['c:uv.l5']&&m['c:uv.l5'][0]==='K','舊版雲端進度帶入 '+JSON.stringify(m));ok((store.get('data/users/u1/progress')||{}).mig===1,'搬過一次就標記')}
await A.click('#noteblk [data-act=nedit]');await A.waitForTimeout(200);
await A.fill('#nta','A＝εbc 是直線；**T 是指數**\n對照 L4');await A.waitForTimeout(1500);
ok([...store.keys()].some(k=>k.endsWith('/notes/k.uv.l3')),'筆記寫進雲端 '+[...store.keys()].join(','));
await B.waitForTimeout(500);
const tb=await B.textContent('#noteblk');ok(tb.includes('A＝εbc'),'B 不重新整理就看到 A 的筆記');
ok(await B.$('#noteblk .ntext a[href="#k.uv.l4"]')!==null,'筆記裡的 L4 變成連結');
ok(await B.$('#noteblk .ntext b')!==null,'**粗體** 有效');
// B 改、A 看到
await B.click('#noteblk [data-act=nedit]');await B.fill('#nta','B 改過的版本');await B.click('[data-act=ndone]');await B.waitForTimeout(1500);
await A.click('[data-act=ndone]');await A.waitForTimeout(600);
ok((await A.textContent('#noteblk')).includes('B 改過的版本'),'A 看到 B 的修改');
// 章頁標記與筆記總表
await A.goto('http://localhost:8766/index.html#c.uv');await A.waitForTimeout(1200);
ok(!!await A.$('.lrow.has-note[data-card="uv.l3"]'),'章頁 L3 有 ✎ 標記');
await A.goto('http://localhost:8766/index.html#notes');await A.waitForTimeout(1200);
ok((await A.textContent('#stage')).includes('B 改過的版本'),'我的筆記總表列出');
await A.click('.nitem');await A.waitForTimeout(800);ok((await A.evaluate(()=>location.hash)).includes('uv.l3'),'點筆記回到那一格');
// 搜尋筆記
await A.keyboard.press('/');await A.fill('#sq','改過');await A.waitForTimeout(300);ok((await A.textContent('#sres')).includes('筆記'),'搜尋找得到筆記');await A.keyboard.press('Escape');
// 其他格：題目、M 站、章、圖
for(const r of ['q.114-1-37','m.uv.1','c.ir','g.ir.macro','f.time','home','s.4']){await A.goto('http://localhost:8766/index.html#'+r);await A.waitForTimeout(700);ok(!!await A.$('#noteblk'),'有筆記欄：'+r)}
// 刪除：清空
await A.goto('http://localhost:8766/index.html#k.uv.l3');await A.waitForTimeout(900);await A.click('#noteblk [data-act=nedit]');await A.fill('#nta','');await A.keyboard.press('Escape');await A.waitForTimeout(1500);
ok(![...store.keys()].some(k=>k.endsWith('/notes/k.uv.l3')),'清空後雲端刪除');
await B.waitForTimeout(500);ok((await B.$('#noteblk.empty'))!==null,'B 也跟著清空');
// 進度同步
await A.goto('http://localhost:8766/index.html#c.hplc');await A.waitForTimeout(800);await A.click('button[data-act=review]');await A.waitForTimeout(500);await A.keyboard.press(' ');await A.keyboard.press('j');await A.waitForTimeout(2200);
await B.goto('http://localhost:8766/index.html#c.hplc');await B.waitForTimeout(1500);ok((await B.textContent('[data-progtext=hplc]')).startsWith('1／'),'B 看到 A 的複習進度 '+await B.textContent('[data-progtext=hplc]'));
ok(A.errs.length===0&&B.errs.length===0,'無錯誤 '+A.errs.concat(B.errs));
await b.close()})();
