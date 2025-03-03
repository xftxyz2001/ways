import json
import os
import re
import time

import ddddocr
import requests
from lxml import etree
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.edge.options import Options


class LinovelibCrawler:

    def start_edge(self):
        print("正在启动Edge浏览器...")
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Edge(options=options)
        time.sleep(2)

    # 初始化
    def __init__(self, novel_id):
        print("正在初始化...")
        self.novel_id = novel_id
        self.sava_filename = f"{novel_id}.md"

        self.base_url = "https://www.linovelib.com"
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
        }
        self.min_request_interval = 2  # 两次请求的最小间隔
        self.max_request_interval = 10
        self.request_interval = self.min_request_interval
        self.last_request_time = time.time() - self.min_request_interval
        self.max_retry = 5  # 最大重试次数

        self.min_wait_time = 2
        self.max_wait_time = 10
        self.wait_time = self.min_wait_time

        self.ocr = ddddocr.DdddOcr(beta=True, show_ad=False)

        self.start_edge()

    # 获取html
    def fetch_html(self, url):
        if not url.startswith("http"):
            url = self.base_url + url

        # 距离上次请求时间的时间
        time_since_last_request = time.time() - self.last_request_time
        if time_since_last_request < self.request_interval:
            time.sleep(time_since_last_request)
        self.last_request_time = time.time()

        for attempt in range(max(self.max_retry, 3)):
            try:
                print(f"请求页面: {url}")
                # response = self.session.get(url, headers=self.headers)
                # response.raise_for_status()
                # return etree.HTML(response.text)

                if attempt == 1:  # 第二次重试，刷新
                    self.driver.refresh()
                else:
                    self.driver.get(url)
                time.sleep(self.wait_time)  # 等待，以便页面加载完全

                page_source = self.driver.page_source
                if "（內容加載失敗！請刷新或更換瀏覽器）" in page_source:
                    with open(
                        f".page_source-{time.time()}.html", "w", encoding="utf-8"
                    ) as f:
                        f.write(page_source)
                    if self.wait_time < self.max_wait_time:
                        self.wait_time *= 2
                    raise Exception("页面加载失败，请刷新或更换浏览器")

                self.wait_time = self.min_wait_time
                self.request_interval = self.min_request_interval
                return etree.HTML(page_source)
            except Exception as e:
                print(f"请求页面失败: {e}")
                if self.request_interval < self.max_request_interval:
                    self.request_interval *= 2

                if attempt <= self.max_retry // 2:  # 前三次
                    print(f"将在 {self.request_interval} 秒后重试...")
                    continue

                self.driver.quit()
                self.start_edge()

        print("已达到最大重试次数，程序即将退出...")
        exit()

    # 解析章节
    def parse_catalog(self, tree):
        self.book_title = tree.xpath('//div[@class="book-meta"]/h1/text()')[0]

        # 卷列表
        volume_list = []
        x_volumes = tree.xpath(
            '//div[@id="volume-list"]//div[@class="volume clearfix"]'
        )
        for x_volume in x_volumes:
            # 卷名
            # volume_name = x_volume.xpath('//h2[@class="v-line"]/text()')[0]
            volume_name = x_volume.xpath('./div[@class="volume-info"]/h2/text()')[0]

            # 章节列表
            chapter_list = []
            # x_chapters = x_volume.xpath('//ul[@class="chapter-list clearfix"]/li/a')
            x_chapters = x_volume.xpath('./ul[@class="chapter-list clearfix"]/li/a')
            for x_chapter in x_chapters:
                # 章节名
                chapter_name = x_chapter.xpath("text()")[0]
                # 章节链接
                chapter_link = x_chapter.xpath("@href")[0]
                chapter = {
                    "name": chapter_name,
                    "link": chapter_link,
                    "status": "not_started",
                }
                chapter_list.append(chapter)
            volume = {
                "name": volume_name,
                "chapters": chapter_list,
                "status": "not_started",
            }
            volume_list.append(volume)
        self.catalog = volume_list

    # 解码文本
    def decode_text(self, text):
        font_path = "./read.woff2"
        if not os.path.exists(font_path):
            print("正在下载字体文件...")
            font_url = self.base_url + "/public/font/read.woff2"
            with open(font_path, "wb") as f:
                f.write(requests.get(font_url).content)
            print("字体文件下载完成！")

        img_size = 1024
        img = Image.new("1", (img_size * len(text), img_size), 255)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, img_size)
        draw.text((0, -200), text, font=font)
        return self.ocr.classification(img)

    # 解析一页小说
    def parse_page(self, tree):
        # 检查是否有字体样式加密，并记录加密的p
        has_font_style = False
        if tree.xpath('//head/script[contains(text(),"adoptedStyleSheets")]'):
            has_font_style = True
            # 获取#TextContent p:nth-last-of-type(2)
            # p_last2 = tree.xpath('//div[@id="TextContent"]/p[last()-1]')[0]
            p_last2 = tree.xpath('//div[@id="TextContent"]/p')[-2]
            content_of_p_last2 = self.decode_text("".join(p_last2.xpath("text()")))

        contents = []
        # 处理TextContent中的p br img标签
        elements = tree.xpath('//div[@id="TextContent"]/*')
        for element in elements:
            if element.tag == "p":
                if has_font_style and element == p_last2:
                    contents.append(content_of_p_last2)
                    continue
                contents.append("".join(element.xpath("text()")))
            elif element.tag == "br":
                contents.append("\n")
            elif element.tag == "img":
                img_src = element.get("data-src") or element.get("src")
                contents.append(f"![image]({img_src})\n\n")

        return "\n".join(contents)

    # 解析章节内容
    def parse_chapter(self, tree):
        contents = []
        while True:
            contents.append(self.parse_page(tree))

            next_page = tree.xpath('//div[@class="mlfy_page"]/a[5]/@href')[0]
            # 如果下一页链接/后面不存在下划线则说明章节结束
            if next_page.split("/")[-1].find("_") == -1:
                break
            tree = self.fetch_html(next_page)

        return "\n".join(contents)

    def save_catalog(self):
        try:
            with open(f".{self.novel_id}.log.json", "w", encoding="utf-8") as f:
                json.dump(self.catalog, f)
            print("章节信息保存成功.")
        except Exception as e:
            print(f"章节信息保存失败: {e}")

    def load_catalog(self):
        if os.path.exists(f".{self.novel_id}.log.json") and os.path.exists(
            self.sava_filename
        ):
            try:
                with open(f".{self.novel_id}.log.json", "r", encoding="utf-8") as f:
                    self.catalog = json.load(f)
                print(f"章节信息已读取.")
                return
            except Exception as e:
                print(f"章节信息读取失败: {e}")

        print(f"获取章节目录...")
        catalog_url = f"{self.base_url}/novel/{self.novel_id}/catalog"

        catalog_html = self.fetch_html(catalog_url)
        self.parse_catalog(catalog_html)
        self.save_catalog()

        with open(self.sava_filename, "w", encoding="utf-8") as f:
            f.write(f"{self.book_title}\n---\n")

    def delete_catalog(self):
        try:
            os.remove(f".{self.novel_id}.log.json")
        except Exception as e:
            print(f"章节信息删除失败: {e}")

    def download(self):
        print(f"开始下载 {self.novel_id}")
        self.load_catalog()

        # for volume_name, chapters in self.catalog:
        for volume in self.catalog:
            if volume["status"] == "completed":
                continue

            volume_name = volume["name"]
            print(f"当前卷: {volume_name}")
            chapters = volume["chapters"]
            if volume["status"] == "not_started":
                with open(self.sava_filename, "a", encoding="utf-8") as f:
                    f.write(f"\n# {volume_name}\n\n")

                volume["status"] = "in_progress"
                self.save_catalog()

            # for chapter_title, chapter_link in chapters:
            for chapter in chapters:
                if chapter["status"] == "completed":
                    continue

                chapter_title = chapter["name"]
                print(f"当前章节: {chapter_title}")
                if chapter["status"] == "not_started":
                    with open(self.sava_filename, "a", encoding="utf-8") as f:
                        f.write(f"## {chapter_title}\n\n")

                    chapter["status"] = "in_progress"
                    self.save_catalog()

                chapter_link = chapter["link"]
                content_html = self.fetch_html(chapter_link)
                content = self.parse_chapter(content_html)
                with open(self.sava_filename, "a", encoding="utf-8") as f:
                    f.write(f"{content}\n\n")
                chapter["status"] = "completed"
                self.save_catalog()
            volume["status"] = "completed"
            self.save_catalog()

        self.driver.quit()
        self.delete_catalog()
        print(f"{self.novel_id} 下载完成")


if __name__ == "__main__":
    input_id = input(
        "请输入小说ID或粘贴网址\neg.(1)4521\n   (2)https://www.linovelib.com/novel/4521.html\n   (3)https://www.linovelib.com/novel/4521/catalog\n>>>"
    )
    novel_id = re.findall(r"\d+", input_id)[0]
    print(f"小说ID已获取: {novel_id}")
    crawler = LinovelibCrawler(novel_id)
    crawler.download()
