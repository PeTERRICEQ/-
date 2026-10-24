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
    // 每頁字級：版面不動，二分搜尋「放得下的最大字級」。
    // ① 大循環（.wide）固定 A 系直式比例 2828×4000，每條 L 至少留兩行手寫線（.note 的 min-height）。
    const st = document.createElement('style');
    st.textContent = '@page wide{size:2828px 4000px;margin:0} section.wide{height:4000px}';
    document.head.appendChild(st);
    const MAX = 34, MIN = 9;
    const res = [];
    for (const pg of document.querySelectorAll('section.page')) {
      const m = pg.querySelector('main');
      const drill = pg.querySelectorAll('.dq-grow');
      // 會裁切內容的盒子（overflow 不是 visible、或在 flex 裡被壓扁）：內容超出也算放不下
      const clip = [...pg.querySelectorAll('main *')].filter(e => getComputedStyle(e).overflow !== 'visible');
      const over = () => (m && m.scrollHeight > m.clientHeight + 1) || pg.scrollHeight > pg.clientHeight + 1 ||
        [...pg.querySelectorAll('.col,.full,.blk,.kl,.scb,.brb,.lane')].some(e => e.scrollWidth > e.clientWidth + 2) ||
        [...pg.querySelectorAll('.snake,.loopw,.vcg,.rad')].some(e => e.scrollHeight > e.clientHeight + 1) ||
        clip.some(e => e.scrollHeight > e.clientHeight + 1 || e.scrollWidth > e.clientWidth + 2) ||
        // 題型練習：每題「從本體推一次」至少留 5 行手寫線
        [...drill].some(e => e.clientHeight < 5 * 1.7 * parseFloat(getComputedStyle(e).fontSize) - 1);
      const set = v => pg.style.setProperty('--fs', v + 'px');
      let lo = MIN, hi = MAX;
      set(lo);
      if (!over()) {
        while (hi - lo > 0.25) { const mid = (lo + hi) / 2; set(mid); if (over()) hi = mid; else lo = mid; }
      }
      let fs = Math.floor(lo * 4) / 4;
      set(fs);
      while (over() && fs > MIN) { fs -= 0.25; set(fs); }
      res.push(fs);
    }
    if (window.drawWires) window.drawWires();
    return res;
  });
  await p.evaluate(require('./rules.js'));
  await p.pdf({path: out, printBackground: true, preferCSSPageSize: true, outline: true, tagged: true});
  console.log(out.split('/').pop(), '頁數', fit.length, '最小字級', Math.min(...fit) + 'px', '字級', fit.map(x => x).join(' '));
  await b.close();
})();
