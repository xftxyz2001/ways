import random
import time
from urllib.parse import urlparse

import requests
from lxml import etree

# 初始URL
url = "https://quanben-xiaoshuo.com/n/heidaoyishidao/1.html"
parsed_url = urlparse(url)
base_url = parsed_url.scheme + "://" + parsed_url.netloc

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Origin": base_url,
    "Referer": base_url + "/",
}

# 打开文件
with open("novel.md", "w", encoding="utf-8") as f:
    while url:
        print(f"try: {url}")
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)

        # 提取数据
        title = html.xpath('//h1[@class="title"]/text()')[0]
        content_src = html.xpath('//*[@id="articlebody"]/p/text()')
        content = "\n".join(content_src)

        # 写入文件
        f.write(f"## {title}\n\n")
        f.write(f"{content}\n\n")

        try:
            next_page = html.xpath('//a[@rel="next"]/@href')[0]
            # 下一页
            if not next_page.startswith("http"):
                url = base_url + next_page
        except:
            break

        time.sleep(random.random() * 2)
