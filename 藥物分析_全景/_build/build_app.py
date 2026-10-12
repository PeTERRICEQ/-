"""把 app_data.json 塞進 app_template.html，產生可發布的單一網頁。"""
import json, sys
tpl, data, out = sys.argv[1:4]
d = open(data, encoding='utf-8').read().replace('</', '<\\/')
open(out, 'w', encoding='utf-8').write(open(tpl, encoding='utf-8').read().replace('__DATA__', d))
print('ok', out)
