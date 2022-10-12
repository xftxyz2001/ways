import re

import requests

url = input('请输入知乎文章链接（或键入回车仅输入文章ID）：')
if not url:
    baseurl = 'https://zhuanlan.zhihu.com/p/'
    pid = input(baseurl)
    url = baseurl + pid
api = 'https://pure-post.vercel.app/api/index?url=' + url + '&markdownHTML=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
print('正在获取数据...')
resp = requests.get(api, headers=headers)
resp.encoding = 'utf-8'
text = resp.text

print('正在处理数据...')
# 将多个空格替换为一个空格
text = re.sub(r' +', ' ', text)

# <p>(.*)</p> -> \1\n
text = re.sub(r'<p>(.*)</p>', r'\1\n', text)

# $$ -> $
text = re.sub(r'\$\$', r'$', text)

# ^\$(.*)\$$ -> $$\n\1\n$$
text = re.sub(r'^\$(.*)\$$', r'$$\n\1\n$$', text, flags=re.M)


# 保存为md文件
print('正在保存文件...')
with open(pid+'.md', 'w', encoding='utf-8') as f:
    f.write(text)
