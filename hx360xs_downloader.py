import random
import re
import time
from urllib.parse import urlparse

import requests
from lxml import etree

# 初始URL
url = "https://h.x360xs.com/book/232880/111094764.html"
parsed_url = urlparse(url)
base_url = parsed_url.scheme + "://" + parsed_url.netloc

# 存储上次的标题
last_title = None

# 尝试加载断点续传
try:
    with open("novel.md.cut", "r", encoding="utf-8") as f:
        last_record = f.readlines()[-1].strip()
        last_url, llast_title = last_record.split("\t")
        parsed_last_url = urlparse(last_url)
        base_last_url = parsed_last_url.scheme + "://" + parsed_last_url.netloc
        if base_last_url == base_url:
            url = last_url
            last_title = llast_title
            print(f"load: {last_url}")
except:
    pass

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Origin": "https://h.x360xs.com",
    "Referer": "https://h.x360xs.com/",
}

# 打开文件
with open("novel.md", "a", encoding="utf-8") as f, open(
    "novel.md.cut", "a", encoding="utf-8"
) as f_cut:
    while url:
        # 打印URL
        print(f"try: {url}")
        # 写入断点续传
        f_cut.write(f"{url}\t{last_title if last_title else ''}\n")

        # 获取页面内容
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)

        # 提取标题和内容
        title = html.xpath('//*[@id="readercontainer"]/div/h3/text()')[0]
        print(f"get: {title}")
        content_src = html.xpath('//div[@class="chapter"]/div/p/text()')

        # 处理标题
        try:
            title = re.match(r"(.*?)(?=\（)", title).group(1)
        except:
            pass

        # 获取text并处理
        content_process = []
        for text in content_src:
            if text.count("（本章节未完结，点击下一页翻页继续阅读）") > 0:
                # 含有前导空格直接continue、否则替换为空
                if text.startswith("（本章节未完结，点击下一页翻页继续阅读）"):
                    text = ""
                else:
                    continue
            else:
                text = text.lstrip()
                if text == "&nbsp":
                    continue
            content_process.append(text)
        content = "\n".join(content_process)

        # 写入文件
        if title != last_title:
            if last_title:
                f.write("\n\n")
            f.write(f"## {title}\n\n")
        f.write(f"{content}")

        # 更新上次的标题
        last_title = title

        # 找到下一页的链接
        try:
            next_page_flag = html.xpath('//*[@class="abcdYe"]')[0]
            next_page_script = html.xpath(
                '//script[contains(text(), "__XSXSXS")]/text()'
            )[0]
            match = re.search(
                r"__XSXSXS\|(.*)\|(.*)\|(.*)\|x360xs\|html\|https\|h\|com\|var",
                next_page_script,
            )
            url = f"https://h.x360xs.com/{match.group(2)}/{match.group(1)}/{match.group(3)}.html"
        except:
            # 找到下一章的链接
            try:
                next_chapter_flag = html.xpath('//*[@id="btnNext"]')[0]
                url = next_chapter_flag.attrib["href"]
                if not url.endswith(".html"):
                    break  # 结束
                if not url.startswith("http"):
                    url = base_url + url
            except:
                break

        # 暂停1-3秒
        time.sleep(random.randint(1, 3))
