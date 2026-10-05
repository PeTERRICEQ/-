// Render each SVG in Chromium, measure real glyph boxes, report layout faults, save PNG.
// usage: node check.js out_dir file1.svg file2.svg ...
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const outDir = process.argv[2];
  const files = process.argv.slice(3);
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  let total = 0;
  for (const f of files) {
    const svg = fs.readFileSync(f, 'utf8');
    const m = svg.match(/viewBox="0 0 (\d+) (\d+)"/);
    const W = +m[1], H = +m[2];
    await page.setViewportSize({ width: W, height: Math.min(H, 16000) });
    await page.setContent(`<html><body style="margin:0">${svg}</body></html>`);
    await page.waitForTimeout(200);
    const issues = await page.evaluate(([W, H]) => {
      const out = [];
      const texts = [...document.querySelectorAll('text')];
      const boxes = texts.map(t => {
        const b = t.getBBox();
        return { t, x: b.x, y: b.y, r: b.x + b.width, btm: b.y + b.height, s: t.textContent.slice(0, 40) };
      });
      for (const b of boxes) {
        if (b.x < 0 || b.r > W || b.y < 0 || b.btm > H) out.push(`OUT-OF-CANVAS: ${b.s}`);
        const id = b.t.getAttribute('data-b');
        if (id) {
          const r = document.getElementById(id);
          if (!r) { out.push(`NO-BOX ${id}: ${b.s}`); continue; }
          const x = +r.getAttribute('x'), y = +r.getAttribute('y');
          const w = +r.getAttribute('width'), h = +r.getAttribute('height');
          const pad = 6;
          if (b.x < x + pad || b.r > x + w - pad || b.y < y + 2 || b.btm > y + h - 2)
            out.push(`OVERFLOW ${id} by r=${(b.r - (x + w - pad)).toFixed(0)} b=${(b.btm - (y + h - 2)).toFixed(0)}: ${b.s}`);
        }
      }
      for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
        const a = boxes[i], c = boxes[j];
        const ox = Math.min(a.r, c.r) - Math.max(a.x, c.x);
        const oy = Math.min(a.btm, c.btm) - Math.max(a.y, c.y);
        if (ox > 2 && oy > 4) out.push(`TEXT-OVERLAP: "${a.s}" x "${c.s}"`);
      }
      // arrows crossing text
      const segs = [];
      document.querySelectorAll('polyline.arrow').forEach(p => {
        const pts = p.getAttribute('points').trim().split(/\s+/).map(q => q.split(',').map(Number));
        for (let i = 0; i < pts.length - 1; i++) segs.push([pts[i], pts[i + 1]]);
      });
      const hit = (s, b) => {
        // sample along segment
        const [[x1, y1], [x2, y2]] = s;
        const n = Math.ceil(Math.hypot(x2 - x1, y2 - y1) / 4) + 1;
        for (let k = 0; k <= n; k++) {
          const x = x1 + (x2 - x1) * k / n, y = y1 + (y2 - y1) * k / n;
          if (x > b.x + 1 && x < b.r - 1 && y > b.y + 3 && y < b.btm - 3) return true;
        }
        return false;
      };
      for (const s of segs) for (const b of boxes) if (hit(s, b)) out.push(`ARROW-THROUGH-TEXT: ${b.s}`);
      return out;
    }, [W, H]);
    total += issues.length;
    console.log(`== ${path.basename(f)}  ${W}x${H}  issues=${issues.length}`);
    issues.slice(0, 60).forEach(s => console.log('   ' + s));
    const png = path.join(outDir, path.basename(f).replace(/\.svg$/, '.png'));
    await page.screenshot({ path: png, fullPage: true });
  }
  await browser.close();
  console.log('TOTAL ISSUES', total);
})();
