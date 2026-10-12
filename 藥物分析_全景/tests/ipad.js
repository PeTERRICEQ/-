// iPad 直放與橫放：版面不溢出、圖上開卡、焦點欄點 L、← 返回
const {chromium}=require(process.env.PW||'/opt/node22/lib/node_modules/playwright');
const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)process.exitCode=1};
(async()=>{const b=await chromium.launch();
for(const [name,w,h] of [['mini',744,1133],['pro11',834,1194],['pro129',1024,1366],['pro11L',1194,834],['pro129L',1366,1024]]){
 const ctx=await b.newContext({viewport:{width:w,height:h},hasTouch:true,deviceScaleFactor:1});const p=await ctx.newPage();const e=[];p.on('pageerror',x=>e.push(x.message));
 const H=()=>p.evaluate(()=>location.hash);
 await p.goto('http://localhost:8766/index.html#c.ir');await p.waitForTimeout(700);
 await p.goto('http://localhost:8766/index.html#g.ir.micro');await p.waitForTimeout(900);
 await p.evaluate(()=>{const t=[...document.querySelectorAll('#figwrap .svl')].find(x=>x.textContent==='L07');t.dispatchEvent(new MouseEvent('click',{bubbles:true}))});await p.waitForTimeout(600);
 const h0=await H();
 const l=await p.$('#focus div.also a[href^="#k."],#focus .qrow,#focus .fk a[href^="#m."]');let h1='',h2='';
 if(l){await l.tap();await p.waitForTimeout(500);h1=await H();await p.tap('#back');await p.waitForTimeout(500);h2=await H()}
 const sw=await p.evaluate(()=>[document.documentElement.scrollWidth,innerWidth]);
 for(const r of ['home','fp','mx','te.4','c.hplc']){await p.goto('http://localhost:8766/index.html#'+r);await p.waitForTimeout(500);
   const s=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);if(s)e.push('hscroll '+r)}
 await p.screenshot({path:`/tmp/yf_ipad_${name}.png`});
 ok(h0==='#g.ir.micro.l7'&&!!l&&h2===h0&&sw[0]<=sw[1]+1&&e.length===0,`${name} ${w}×${h} fig→${h0} tap→${h1} back→${h2} hscroll=${sw[0]>sw[1]} errs=${e}`);await ctx.close()}
await b.close()})();
