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
    // ① 大循環（.wide）照藥理藥化做法：字級固定，頁面往下長到放得下，剩下的空間給每條 L 的手寫線
    const css = [];
    document.querySelectorAll('section.wide').forEach((pg, i) => {
      pg.style.setProperty('--fs', '17px');
      const sn = pg.querySelector('.snake'), lw = pg.querySelector('.loopw');
      const need = Math.max(sn ? sn.scrollHeight - sn.clientHeight : 0, lw ? lw.scrollHeight - lw.clientHeight : 0);
      const h = Math.max(2000, Math.ceil(pg.clientHeight + need + 120));
      const nm = 'wide' + i;
      css.push(`@page ${nm}{size:2828px ${h}px;margin:0}`);
      pg.style.height = h + 'px'; pg.style.page = nm;
    });
    const st = document.createElement('style'); st.textContent = css.join('\n'); document.head.appendChild(st);
    const res = [];
    for (const pg of document.querySelectorAll('section.page')) {
      let fs = pg.classList.contains('wide') ? 17 : 15;
      const over = () => {
        const m = pg.querySelector('main');
        return (m && m.scrollHeight > m.clientHeight + 1) || pg.scrollHeight > pg.clientHeight + 1 ||
          [...pg.querySelectorAll('.col,.full,.blk,.kl,.scb,.brb,.lane')].some(e => e.scrollWidth > e.clientWidth + 2) ||
          [...pg.querySelectorAll('.snake,.loopw')].some(e => e.scrollHeight > e.clientHeight + 1);
      };
      pg.style.setProperty('--fs', fs + 'px');
      while (over() && fs > 9) { fs -= 0.25; pg.style.setProperty('--fs', fs + 'px'); }
      // 內容少的頁往上放大（題型練習頁不放大，留手寫空間）
      if (fs === 15 && !pg.classList.contains('legacy') && !pg.classList.contains('nogrow')) {
        while (fs < 20) {
          pg.style.setProperty('--fs', (fs + 0.5) + 'px');
          if (over()) { pg.style.setProperty('--fs', fs + 'px'); break; }
          fs += 0.5;
        }
      }
      res.push(fs);
    }
    if (window.drawWires) window.drawWires();
    return res;
  });
  await p.pdf({path: out, printBackground: true, preferCSSPageSize: true, outline: true, tagged: true});
  console.log(out.split('/').pop(), '頁數', fit.length, '最小字級', Math.min(...fit) + 'px', '字級', fit.map(x => x).join(' '));
  await b.close();
})();
