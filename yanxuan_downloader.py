import requests
from bs4 import BeautifulSoup
import time
import random

# 初始URL
url = "https://www.yanxuan.org/yanxuan/z/%E7%BD%AA%E6%A1%88%E6%95%85%E4%BA%8B%E9%A6%86/1%E7%9B%B2%E4%BA%BA%E6%9D%80%E4%BA%BA%E6%A1%88%E5%88%AB%E5%A4%BA%E8%B5%B0%E4%BA%BA%E5%BF%83%E4%B8%AD%E7%9A%84%E5%85%89/"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Origin": "https://www.yanxuan.org",
    "Referer": "https://www.yanxuan.org/",
}

# 打开文件
with open("novel.md", "w", encoding="utf-8") as f:
    while url:
        # 打印URL
        print(f"Trying URL: {url}")

        # 获取页面内容
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # 获取编码方式
        charset = soup.select_one("meta[charset]")["charset"]

        # 使用正确的编码解码
        html = response.content.decode(charset)

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html, "html.parser")

        # 提取标题和内容
        title = soup.select_one('//*[@id="post"]/h1').text
        content_src = soup.select('//*[@id="post"]/div[2]/p')

        # 去除最开头的三个和结束的7个
        content_src = content_src[3:-7]

        # 获取text
        content = "\n".join([p.text for p in content_src])

        # 写入文件
        f.write(f"## {title}\n\n{content}\n\n")

        # 找到下一页的链接
        next_page = soup.select_one('//*[@id="post"]/div[3]/div[2]/a')
        url = next_page["href"] if next_page else None

        # 暂停1-3秒
        time.sleep(random.randint(1, 3))
