// 手寫格線改成真的向量線（取代 CSS repeating-linear-gradient）。
// 原因：Chromium 把重複漸層輸出成 PDF tiling pattern，MarginNote／iPad PDFKit 放大縮小或快速捲動時
// 常常畫不出來，整頁變白。改成一條一條的線（div 的 border），每個閱讀器都畫得動。
// 在瀏覽器裡執行：page.evaluate(require('./rules.js'))，要在字級定好之後呼叫。
module.exports = () => {
  let n = 0;
  for (const el of document.querySelectorAll('.note,.dq-r')) {
    const fs = parseFloat(getComputedStyle(el).fontSize);
    const note = el.classList.contains('note');
    const pitch = (note ? 1.8 : 1.7) * fs;
    const color = note ? '#b9beb2' : '#c4c8be';
    el.style.backgroundImage = 'none';
    if (getComputedStyle(el).position === 'static') el.style.position = 'relative';
    const h = el.clientHeight;
    for (let y = pitch; y <= h + 0.5; y += pitch) {
      const d = document.createElement('div');
      d.style.cssText = `position:absolute;left:0;right:0;top:${(y - 1.6).toFixed(2)}px;height:0;` +
        `border-top:1.6px ${note ? 'dashed' : 'solid'} ${color};pointer-events:none`;
      el.appendChild(d);
      n++;
    }
  }
  return n;
};
