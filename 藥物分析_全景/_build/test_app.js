const { chromium } = require('playwright');
(async () => {
  const [file, shots] = process.argv.slice(2);
  const b = await chromium.launch();
  const errs = [];
  for (const [w, h, name, dark] of [[1280, 900, 'desk', false], [390, 844, 'phone', true]]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, colorScheme: dark ? 'dark' : 'light' });
    p.on('pageerror', e => errs.push(name + ' ' + e.message)); p.on('console', m => m.type() === 'error' && errs.push(name + ' console ' + m.text()));
    await p.goto('file://' + require('path').resolve(file));
    await p.waitForTimeout(600);
    await p.screenshot({ path: `${shots}/${name}-map.png`, fullPage: false });
    const sw = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    console.log(name, 'hscroll', sw);
    // 點格子
    await p.click('.cellbtn[data-a="荷"][data-b="選"]');
    await p.waitForTimeout(200);
    await p.screenshot({ path: `${shots}/${name}-cell.png`, fullPage: false });
    if (name === 'phone') await p.click('#focus .close');
    // 章節 + 複習
    await p.click('#v-ch'); await p.click('#m-rv'); await p.waitForTimeout(200);
    const masked = await p.$$eval('#main .u.m', a => a.length);
    await p.keyboard.press('Space'); await p.keyboard.press('j');
    await p.keyboard.press('Space'); await p.keyboard.press('k');
    const after = await p.$$eval('#main .u.m', a => a.length);
    const known = await p.$$eval('#main .u.known', a => a.length);
    console.log(name, 'masked', masked, 'after', after, 'known', known);
    await p.screenshot({ path: `${shots}/${name}-review.png`, fullPage: false });
    await p.click('#v-te'); await p.waitForTimeout(200);
    await p.screenshot({ path: `${shots}/${name}-te.png`, fullPage: false });
    await p.fill('#q', 'EOF'); await p.waitForTimeout(100);
    console.log(name, 'search', await p.$$eval('#res button', a => a.length));
    await p.keyboard.press('Enter'); await p.waitForTimeout(200);
    await p.screenshot({ path: `${shots}/${name}-search.png`, fullPage: false });
    await p.close();
  }
  console.log('errors', errs);
  await b.close();
})();
