const {chromium}=require(process.env.PW||'/opt/node22/lib/node_modules/playwright');
const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)process.exitCode=1};
const U='http://localhost:8766/index.html#';
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1366,height:860}})).newPage();const errs=[];
p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
const R=['home','f.nrg','f.cnt','c.uv','c.pol','c.naq','m.uv.1','m.pol.6','k.uv.l3','k.naq.l1','q.114-1-37','g.uv.macro','g.uv.micro.l3','g.gt.g0','g.gt.g6','r.uv.0','r.uv.3','s.2','l.1','mx','mx.co','mx.co.nrg','mx.co.z4','fp','fp.uv','fp.uv.5','te','te.0','notes','print'];
for(const r of R){await p.goto(U+r);await p.waitForTimeout(r.startsWith('g.')?900:350);
  const st=(await p.textContent('#stage')).length,fo=(await p.textContent('#focus')).length;
  ok(st>50&&!(await p.textContent('#stage')).includes('載入中'),`${r} stage ${st} focus ${fo} crumb=${(await p.textContent('#crumb'))}`)}
await p.goto(U+'g.uv.micro');await p.waitForTimeout(1200);ok(await p.$$eval('#figwrap .svl',a=>a.length)>5,'uv micro linkified '+await p.$$eval('#figwrap .svl',a=>a.length));
await p.goto(U+'g.gt.g0');await p.waitForTimeout(1200);ok(await p.$$eval('#figwrap .svl',a=>a.length)>5,'gt g0 linkified '+await p.$$eval('#figwrap .svl',a=>a.length));
await p.goto(U+'g.nmr.macro');await p.waitForTimeout(1200);ok(await p.$$eval('#figwrap .svl[data-h^="m.nmr"]',a=>a.length)>0,'nmr 第N站 linked');
ok(errs.length===0,'errors: '+errs.slice(0,5).join(' | '));
await b.close()})();
