// 92 張圖都載得出；章圖上的 L／M／第N站、全科圖上的章名／帳名／圖號可點；點了開卡、圖不動
const {chromium}=require(process.env.PW||'/opt/node22/lib/node_modules/playwright');
const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)process.exitCode=1};
(async()=>{const b=await chromium.launch();
for(const [w,h] of [[1366,860],[390,844]]){
const ctx=await b.newContext({viewport:{width:w,height:h}});const p=await ctx.newPage();const errs=[],bad=[];
p.on('pageerror',e=>errs.push(e.message));p.on('response',r=>{if(r.status()>=400)bad.push(r.url())});
const H=()=>p.evaluate(()=>location.hash);
await p.goto('http://localhost:8766/index.html#c.hplc');await p.waitForTimeout(800);
ok(await p.$$eval('.fthumb',a=>a.length)===5,w+' hplc strip 5 thumbs');
await p.click('.fthumb[href="#g.hplc.micro"]');await p.waitForTimeout(800);
const n=await p.$$eval('#figwrap .svl',a=>a.length);ok(n>5,w+' micro links '+n);
await p.evaluate(()=>{const e=[...document.querySelectorAll('#figwrap .svl')].find(x=>x.textContent==='L09');e.dispatchEvent(new MouseEvent('click',{bubbles:true}))});await p.waitForTimeout(500);
ok((await H())==='#g.hplc.micro.l9',w+' L09 click -> '+await H());
ok(!!await p.$('#figwrap svg'),w+' figure still there');
ok((await p.textContent('#focus h2')).length>3,w+' card in focus: '+(await p.textContent('#focus h2')));
ok(await p.$$eval('#figwrap .svl.on',a=>a.length)>0,w+' L09 highlighted in fig');
await p.goBack();await p.waitForTimeout(500);ok(await H()==='#g.hplc.micro',w+' back to fig');
await p.keyboard.press('ArrowRight');await p.waitForTimeout(600);ok(await H()==='#g.hplc.map',w+' → next fig '+await H());
await p.click('[data-act="zoom"][data-z="1"]');await p.waitForTimeout(100);
const sw=await p.evaluate(()=>[document.documentElement.scrollWidth,document.documentElement.clientWidth]);ok(sw[0]<=sw[1]+1,w+' no page hscroll when zoomed '+sw);
await p.goto('http://localhost:8766/index.html#g.gt.g0');await p.waitForTimeout(900);
const g=await p.$$eval('#figwrap .svl',a=>a.map(x=>x.getAttribute('data-h')));
ok(g.some(x=>x.startsWith('c.'))&&g.some(x=>x.startsWith('f.'))&&g.some(x=>x.startsWith('g.gt.'))&&g.some(x=>x.startsWith('k.')),w+' gt links chapter/field/fig/L '+g.length);
await p.goto('http://localhost:8766/index.html#g.pol.micro');await p.waitForTimeout(900);
ok(await p.$$eval('#figwrap .svl[data-h^="m.pol."]',a=>a.length)>=7,w+' 旋光 M01–M07 linked');
const figs=await p.evaluate(()=>Object.entries(IDX.figs).flatMap(([k,fs])=>fs.map(f=>'g.'+k+'.'+f[0])));
let tot=0;const zero=[];
for(const f of figs){await p.evaluate(h=>location.hash=h,f);await p.waitForFunction(h=>document.querySelector('#figwrap')?.dataset.fig===h.slice(2),f,{timeout:8000}).catch(()=>bad.push('nosvg '+f));
 const c=await p.$$eval('#figwrap .svl',a=>a.length);tot+=c;if(!c)zero.push(f)}
ok(zero.length<=2,w+' figures '+figs.length+' links total '+tot+' no-link figs '+zero);
ok(errs.length===0&&bad.length===0,w+' errors '+errs.concat(bad).slice(0,5));
await ctx.close()}
await b.close()})();
