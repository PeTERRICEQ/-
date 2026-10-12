// 用法：node print.js <輸入.html> <輸出.pdf> [截圖資料夾]
const { chromium } = require('playwright');
(async () => {
  const [inp, out, shots] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch());
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(inp), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;text-align:center;font-size:7px;color:#6b7480;font-family:Noto Sans TC,WenQuanYi Zen Hei,sans-serif">藥物分析｜理化性質全景 v0.1　第 <span class="pageNumber"></span>／<span class="totalPages"></span> 頁</div>' });
  if (shots) {
    await page.emulateMedia({ media: 'print' });
    await page.setViewportSize({ width: 794, height: 1123 });
    await page.screenshot({ path: shots + '/full.png', fullPage: true });
  }
  await browser.close();
})();
