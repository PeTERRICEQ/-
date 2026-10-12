#!/bin/sh
# 本機測試：把 app/藥分全景.html 包成發佈時的同樣骨架，在 8766 埠提供
# 用法：sh tests/serve.sh /tmp/yf-wt  然後 PW=/opt/node22/lib/node_modules/playwright node tests/interact.js
W=${1:-/tmp/yf-wt}; HERE=$(cd "$(dirname "$0")/.." && pwd)
mkdir -p "$W" && ln -sfn "$HERE/app/data" "$W/data" && ln -sfn "$HERE/app/fig" "$W/fig"
{ printf '<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}img{max-width:100%%}[hidden]{display:none!important}</style></head><body>'; cat "$HERE/app/藥分全景.html"; printf '</body></html>'; } > "$W/index.html"
cd "$W" && exec python3 -m http.server 8766
