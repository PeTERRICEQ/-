const {chromium}=require(process.env.PW || '/opt/node22/lib/node_modules/playwright');const fs=require('fs');
const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)process.exitCode=1};
const U='http://localhost:8766/index.html#';
(async()=>{const b=await chromium.launch();
 // A：有 downloads 能力（模擬）
 const A=await (await b.newContext({viewport:{width:1194,height:834}})).newPage();const errs=[];A.on('pageerror',e=>errs.push(e.message));
 let saved=null;await A.exposeFunction('__save',(name,data)=>{saved={name,data}});
 await A.addInitScript(()=>{window.claude={use:async n=>n==='downloads'?{save:async o=>window.__save(o.filename,typeof o.data==='string'?o.data:'')}:null}});
 const write=async(p,route,text)=>{await p.goto(U+route);await p.waitForTimeout(700);await p.click('#noteblk [data-act=nedit]');await p.fill('#nta',text);await p.click('[data-act=ndone]');await p.waitForTimeout(200)};
 await write(A,'k.uv.l3','A：A＝εbc 直線');await write(A,'c.ir','A：彈簧琴');await write(A,'q.114-1-37','A：Joule heating');
 await A.goto(U+'c.hplc');await A.waitForTimeout(500);await A.click('button[data-act=review]');await A.waitForTimeout(400);await A.keyboard.press(' ');await A.keyboard.press('j');await A.waitForTimeout(300);
 await A.goto(U+'notes');await A.waitForTimeout(600);await A.click('[data-act=bkdl]');await A.waitForTimeout(500);
 ok(saved&&saved.name.endsWith('.json'),'A 備份下載 '+(saved&&saved.name));
 const bk=JSON.parse(saved.data);ok(Object.keys(bk.notes).length===3&&Object.keys(bk.progress.m).length===1,'備份含 3 則筆記＋1 張進度');
 await A.click('[data-act=bkmd]');await A.waitForTimeout(400);ok(saved.name.endsWith('.md')&&saved.data.includes('A：彈簧琴'),'可閱讀版 .md');
 fs.writeFileSync('/tmp/yf_bk.json',JSON.stringify(bk));
 // B：沒有任何雲端／下載能力；先有一則較新的同格筆記
 const B=await (await b.newContext({viewport:{width:834,height:1194},hasTouch:true})).newPage();B.on('pageerror',e=>errs.push(e.message));
 await write(B,'c.ir','B：這台比較新');
 await B.goto(U+'notes');await B.waitForTimeout(600);await B.click('[data-act=bkload]');await B.setInputFiles('#bkfile','/tmp/yf_bk.json');await B.waitForTimeout(300);
 await B.click('[data-act=bkapply]');await B.waitForTimeout(800);const r1=await B.textContent('#bkres');
 ok(/新增 2 則/.test(r1)&&/略過 1 則/.test(r1)&&/進度更新 1 張/.test(r1),'B 用檔案加載：'+r1.trim());
 ok((await B.textContent('#stage')).includes('A：A＝εbc 直線')&&(await B.textContent('#stage')).includes('B：這台比較新'),'較新的保留、新的加入');
 // 覆蓋模式＋貼上
 await B.click('[data-act=bkload]');await B.fill('#bkpaste',JSON.stringify(bk));await B.check('#bkover');await B.click('[data-act=bkapply]');await B.waitForTimeout(800);
 ok((await B.textContent('#stage')).includes('A：彈簧琴'),'勾「以備份為準」貼上後覆蓋：'+(await B.textContent('#bkres')).trim());
 await B.goto(U+'c.hplc');await B.waitForTimeout(600);ok((await B.textContent('[data-progtext=hplc]')).startsWith('1／'),'B 進度跟著帶過來');
 await B.goto(U+'k.uv.l3');await B.waitForTimeout(600);ok((await B.textContent('#noteblk')).includes('A：A＝εbc'),'格子裡看得到加載的筆記');
 // 不能存檔的環境：顯示可複製的內容
 await B.goto(U+'notes');await B.waitForTimeout(500);await B.click('[data-act=bkdl]');await B.waitForTimeout(300);
 const t=await B.inputValue('#bktext').catch(()=>'');ok(t.includes('"notes-backup"'),'不能存檔時改成顯示內容可複製');
 // 錯誤輸入
 await B.click('[data-act=bkload]');await B.fill('#bkpaste','亂打的');await B.click('[data-act=bkapply]');await B.waitForTimeout(200);ok((await B.textContent('#bkres')).includes('讀不懂'),'亂貼會提示');
 await B.setViewportSize({width:834,height:1194});ok(await B.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'iPad 無水平捲動');
 await B.screenshot({path:'/tmp/yf_backup.png'});ok(errs.length===0,'無錯誤 '+errs);await b.close()})();
