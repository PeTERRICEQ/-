// HTML → PDF：每頁太滿就把字縮小，直到放得下一頁；回報每頁最後的字級
// 用法：node print.js in.html out.pdf
const {chromium} = require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1600, height: 1131}});
  await p.goto('file://' + inp, {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  const fit = await p.evaluate(() => {
    const res = [];
    for (const pg of document.querySelectorAll('.page')) {
      let fs = 15;
      const over = () => {
        const m = pg.querySelector('main');
        return m.scrollHeight > m.clientHeight + 1 || pg.scrollHeight > pg.clientHeight + 1 ||
          [...pg.querySelectorAll('.col,.full,.blk')].some(e => e.scrollWidth > e.clientWidth + 2);
      };
      pg.style.setProperty('--fs', fs + 'px');
      while (over() && fs > 9) { fs -= 0.25; pg.style.setProperty('--fs', fs + 'px'); }
      res.push(fs);
    }
    return res;
  });
  await p.evaluate(require('./rules.js'));
  await p.pdf({path: out, width: '1600px', height: '1131px', printBackground: true, preferCSSPageSize: true});
  console.log(out.split('/').pop(), '字級', fit.map(x => x + 'px').join(' '));
  await b.close();
})();
