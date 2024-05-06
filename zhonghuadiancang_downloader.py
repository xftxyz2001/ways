import requests
from lxml import etree
import time
import random
import tqdm
import re


book_page_url = "https://www.zhonghuadiancang.com/waiguomingzhu/11377/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "Host": "www.zhonghuadiancang.com",
    "Referer": book_page_url,
}


def get_content(url, max_retry=3):
    for i in range(max_retry):
        try:
            time.sleep(random.random() * 3)
            response = requests.get(url, headers=headers)
            html = etree.fromstring(response.content, etree.HTMLParser())
            return html
        except Exception as e:
            print(f"Failed to get content from {url}, retrying... ({i+1}/{max_retry})")
            time.sleep(5)  # wait for 5 seconds before retrying
    raise Exception(f"Failed to get content from {url} after {max_retry} retries.")


def get_chapter_urls():
    html = get_content(book_page_url)
    book_name = html.xpath("//h1/text()")[0]
    book_name = book_name.strip()
    links = html.xpath('//*[@id="booklist"]/li/a')
    return book_name, links


def content_process(content_origin):
    content = []
    for line in content_origin:
        line = re.sub(r"([\\`*_\[\]()~#\+\-£\.!])", r"\\\1", line)
        content.append(line)
    return "\n".join(content)


if __name__ == "__main__":
    book_name, links = get_chapter_urls()
    print(f"Downloading {book_name}...")

    with open(book_name + ".md", "w", encoding="utf-8") as f:
        for link in tqdm.tqdm(links):
            title = link.text
            content_url = link.get("href")
            content_html = get_content(content_url)
            content_origin = content_html.xpath('//*[@id="content"]/p/text()')
            content = content_process(content_origin)

            f.write("## " + title + "\n")
            f.write(content + "\n\n")

    print("Done!")
