const { chromium } = require('playwright');
(async () => {
  const [file, shot] = process.argv.slice(2);
  const b = await chromium.launch(); const errs = [];
  const p = await b.newPage({ viewport: { width: 1280, height: 1000 } });
  p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(file)); await p.waitForTimeout(500);
  await p.click('.cellbtn[data-a="荷"][data-b="選"]'); await p.waitForTimeout(200);
  await p.evaluate(() => { const q = document.querySelectorAll('#focus .q'); q[0].scrollIntoView(); });
  const btns = await p.$$('#focus [data-act="exp"]'); for (const x of btns.slice(0, 3)) await x.click();
  await p.evaluate(() => document.querySelectorAll('#focus .q')[0].scrollIntoView());
  await p.screenshot({ path: shot });
  console.log('errors', errs);
  await b.close();
})();
