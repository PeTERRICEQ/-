// 跳轉與返回、選取保留、題目、複習、舊版進度遷移、搜尋、手機抽屜、主題
const {chromium}=require(process.env.PW||'/opt/node22/lib/node_modules/playwright');
const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)process.exitCode=1};
const U='http://localhost:8766/index.html#';
(async()=>{const b=await chromium.launch();
for(const [w,h] of [[1366,860],[390,844]]){
 const ctx=await b.newContext({viewport:{width:w,height:h}});const p=await ctx.newPage();const errs=[];
 p.on('pageerror',e=>errs.push(e.message));
 // 舊版藥分全景的本機進度
 await ctx.addInitScript(()=>{if(!localStorage.getItem('pan.mig'))localStorage.setItem('yfqj:prog',JSON.stringify({'L|HPLC|L09':1,'L|非水滴定|NAT03':0,'P|UV|源':1}))});
 const H=()=>p.evaluate(()=>location.hash);
 await p.goto(U+'home');await p.waitForTimeout(800);
 const pm=await p.evaluate(()=>JSON.parse(localStorage.getItem('pan.prog')).m);
 ok(pm['c:hplc.l9']?.[0]==='J'&&pm['c:naq.l3']?.[0]==='K'&&Object.keys(pm).length===2,w+' 舊版進度遷移 '+JSON.stringify(pm));
 await p.click('a.chip[href="#c.hplc"]');await p.waitForTimeout(400);
 ok((await p.textContent('#crumb')).includes('時間帳'),w+' crumb 時間帳');
 await p.click('.lrow a[href="#k.hplc.l9"]');await p.waitForTimeout(400);
 ok(!!await p.$('.lrow.state-J[data-card="hplc.l9"]'),w+' 遷移的 J 顯示在 L09');
 const y1=await p.evaluate(()=>scrollY);
 const link=await p.$('#focus .also a[href^="#k.ext."]');ok(!!link,w+' 酸鹼線 also-link to 萃取');
 await link.click();await p.waitForTimeout(400);
 ok((await H()).startsWith('#k.ext.'),w+' jumped to '+await H());
 ok((await p.textContent('#crumb')).includes('萃取'),w+' crumb shows 萃取');
 await p.goBack();await p.waitForTimeout(500);
 ok(await H()==='#k.hplc.l9',w+' browser back -> HPLC L09');
 const y2=await p.evaluate(()=>scrollY);ok(Math.abs(y1-y2)<5,w+` scroll restored ${y1} vs ${y2}`);
 ok(!!await p.$('.lrow.sel[data-card="hplc.l9"]'),w+' L09 highlighted');
 await p.keyboard.press('Backspace');await p.waitForTimeout(500);ok(await H()==='#c.hplc',w+' Backspace -> chapter '+await H());
 await p.click('a[href="#k.hplc.l10"]');await p.waitForTimeout(300);
 await p.click('#back');await p.waitForTimeout(600);ok(await H()==='#c.hplc',w+' ← button -> chapter '+await H());
 // 選取在視角之間保持：HPLC → 五格矩陣
 await p.keyboard.press('3');await p.waitForTimeout(400);ok(!!await p.$('[data-fprow="hplc"]>th.sel'),w+' 五格矩陣亮 HPLC 列');
 await p.click('[data-fpcell="hplc.4"] a');await p.waitForTimeout(400);ok((await p.textContent('#focus')).includes('同一欄'),w+' 五格格子 → 同一欄');
 // 題目
 await p.goto(U+'q.114-1-37');await p.waitForTimeout(500);
 ok(!(await p.textContent('#focus')).includes('答案：'),w+' answer hidden first');
 await p.keyboard.press(' ');await p.waitForTimeout(200);
 ok((await p.textContent('#focus')).includes('答案：'),w+' Space reveals');
 ok(!!await p.$('.opt.ans'),w+' answer option marked');
 ok(!!await p.$('#focus a.btn[href^="#g.ce."]'),w+' 一顆看圖按鈕');
 // 有紅線的題 → 依類型開對應的圖
 const rq=await p.evaluate(()=>{const q=S.qs.find(q=>q.red.length&&IDX.te[q.red[0][0]].reds[q.red[0][1]].type==='條件錯'&&IDX.figs[q.ch[0]]);return q&&q.id});
 await p.goto(U+'q.'+rq);await p.waitForTimeout(500);await p.keyboard.press(' ');await p.waitForTimeout(200);
 ok(!!await p.$('#focus a.btn[href*=".inst"]'),w+' 條件錯 → 儀器與操作圖 '+rq);
 // 複習
 await p.goto(U+'c.uv');await p.waitForTimeout(400);
 await p.click('button[data-act="review"]');await p.waitForTimeout(400);
 const h1=await H();ok(h1.startsWith('#k.uv.'),w+' review starts at '+h1);
 ok(!!await p.$('#focus .cover'),w+' card covered');
 await p.keyboard.press(' ');await p.waitForTimeout(150);ok(!await p.$('#focus .cover'),w+' Space uncovers');
 await p.keyboard.press('j');await p.waitForTimeout(400);const h2=await H();ok(h2!==h1,w+' J advances to '+h2);
 await p.keyboard.press('k');await p.waitForTimeout(400);
 const pr=await p.evaluate(()=>JSON.parse(localStorage.getItem('pan.prog')).m);ok(Object.keys(pr).length===4,w+' progress saved '+Object.keys(pr).length);
 await p.keyboard.press('m');await p.waitForTimeout(150);
 // 搜尋
 await p.goto(U+'home');await p.waitForTimeout(400);
 await p.keyboard.press('/');await p.fill('#sq','Beer');await p.waitForTimeout(200);
 const n=await p.$$eval('#sres a',a=>a.length);ok(n>0,w+' search results '+n);
 await p.keyboard.press('Enter');await p.waitForTimeout(500);ok((await H())!=='#home',w+' search Enter -> '+await H());
 await p.keyboard.press('/');await p.fill('#sq','ESI');await p.waitForTimeout(200);
 const t=await p.$$eval('#sres a .t',a=>a.slice(0,40).map(x=>x.textContent));ok(t.length&&t.every(x=>x.includes('ESI')),w+' case-sensitive ESI: '+t.length);
 await p.keyboard.press('Escape');
 if(w<500){await p.goto(U+'c.hplc');await p.waitForTimeout(300);await p.click('a[href="#k.hplc.l9"]');await p.waitForTimeout(300);
   ok(await p.evaluate(()=>document.body.classList.contains('sheet')),w+' sheet open');
   await p.click('#focus [data-act="back"]');await p.waitForTimeout(600);ok(await H()==='#c.hplc',w+' sheet close -> '+await H());}
 await p.click('#bTheme');const th=await p.evaluate(()=>document.documentElement.dataset.theme);ok(!!th,w+' theme -> '+th);
 for(const r of ['home','fp','mx','te','c.naq','g.gt.g6']){await p.goto(U+r);await p.waitForTimeout(400);
   ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),w+' no hscroll '+r)}
 ok(errs.length===0,w+' no page errors '+errs.join('|'));
 await ctx.close()}
await b.close()})();
