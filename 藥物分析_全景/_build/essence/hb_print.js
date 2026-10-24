// 精華 v2.0（essence-handout）用：HTML → PDF。每頁各自縮字到放得下；大頁（.big）用另一個 @page 尺寸；
// 產生 PDF 書籤（outline），並回報每頁字級。用法：node hb_print.js in.html out.pdf
const {chromium} = require(process.env.PW || '/opt/node22/lib/node_modules/playwright');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 2400, height: 2828}});
  await p.goto('file://' + inp, {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  const fit = await p.evaluate(() => {
    const res = [];
    for (const pg of document.querySelectorAll('section.page')) {
      let fs = 15;
      const over = () => {
        const m = pg.querySelector('main');
        return (m && m.scrollHeight > m.clientHeight + 1) || pg.scrollHeight > pg.clientHeight + 1 ||
          [...pg.querySelectorAll('.col,.full,.blk,.kl,.scb,.brb,.lane')].some(e => e.scrollWidth > e.clientWidth + 2);
      };
      pg.style.setProperty('--fs', fs + 'px');
      while (over() && fs > 9) { fs -= 0.25; pg.style.setProperty('--fs', fs + 'px'); }
      res.push(fs);
    }
    if (window.drawWires) window.drawWires();
    return res;
  });
  await p.pdf({path: out, printBackground: true, preferCSSPageSize: true, outline: true, tagged: true});
  console.log(out.split('/').pop(), '頁數', fit.length, '最小字級', Math.min(...fit) + 'px', '字級', fit.map(x => x).join(' '));
  await b.close();
})();
