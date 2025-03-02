import json
import os
import time

import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.edge.options import Options


class LinovelibCrawler:

    def start_edge(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Edge(options=options)

    # 初始化
    def __init__(self, novel_id):
        self.novel_id = novel_id
        self.sava_filename = f"{novel_id}.md"

        self.base_url = "https://www.linovelib.com"
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
        }
        self.min_request_interval = 3  # 两次请求的最小间隔
        self.last_request_time = time.time() - self.min_request_interval
        self.max_retry = 3  # 最大重试次数

        self.start_edge()

    # 获取html
    def fetch_html(self, url):
        if not url.startswith("http"):
            url = self.base_url + url

        # 距离上次请求时间的时间
        time_since_last_request = time.time() - self.last_request_time
        if time_since_last_request < self.min_request_interval:
            time.sleep(self.min_request_interval - time_since_last_request)
        self.last_request_time = time.time()

        for attempt in range(self.max_retry):
            try:
                print(f"请求页面: {url}")
                # response = self.session.get(url, headers=self.headers)
                # response.raise_for_status()
                # return etree.HTML(response.text)

                self.driver.get(url)
                time.sleep(2)  # 等待2秒，以便页面加载完全
                return etree.HTML(self.driver.page_source)
            except Exception as e:
                print(f"请求页面失败: {e}")
                if attempt < 2:
                    print(f"将在 {5 * (attempt + 1)} 秒后重试...")
                    time.sleep(5 * (attempt + 1))
                else:
                    print("已达到最大重试次数，程序退出...")
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

    # 解析章节内容
    def parse_content(self, tree):
        # mlfy_main_text = tree.xpath('//div[@id="mlfy-main-text"]')
        # chapter_name = mlfy_main_text.xpath('/h1/text()')[0]
        contents = ""
        while True:
            content = tree.xpath('//div[@id="TextContent"]//text()')
            contents += "\n".join(content) + "\n\n"
            # next_page = tree.xpath('//div[@class="mlfy-page"]/a[5]/@href')[0]
            next_page = tree.xpath('//div[@class="mlfy_page"]/a[5]/@href')[0]
            # 如果下一页链接/后面不存在下划线则说明章节结束
            if next_page.split("/")[-1].find("_") == -1:
                break
            # new_url = next_page
            # if not new_url.startswith("http"):
            #     new_url = self.base_url + new_url
            # tree = self.fetch_html(new_url)
            tree = self.fetch_html(next_page)
        adstr = """style_tp();





(adsbygoogle = window.adsbygoogle || []).push({});




    """
        contents = contents.replace(adstr, "")
        return contents

    def save_catalog(self):
        try:
            with open(f".{self.novel_id}.log", "w", encoding="utf-8") as f:
                json.dump(self.catalog, f)
            print("章节信息保存成功.")
        except Exception as e:
            print(f"章节信息保存失败: {e}")

    def load_catalog(self):
        if os.path.exists(f".{self.novel_id}.log") and os.path.exists(
            self.sava_filename
        ):
            try:
                with open(f".{self.novel_id}.log", "r", encoding="utf-8") as f:
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
            os.remove(f".{self.novel_id}.log")
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
                content = self.parse_content(content_html)
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
    novel_id = 4515
    crawler = LinovelibCrawler(novel_id)
    crawler.download()

# <script>;eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('b 3=c d();3.e(`@0-f{0-4:1;0-g:h;i:5(\'/6/0/1.7\')8(\'7\'),5(\'/6/0/1.j\')8(\'k\')}#l p:m-n-o-q(2){0-4:"1"!r}`);9.a=[...9.a,3];',28,28,'font|read||sheet|family|url|public|woff2|format|document|adoptedStyleSheets|const|new|CSSStyleSheet|replaceSync|face|display|block|src|ttf|truetype|TextContent|nth|last|of||type|important'.split('|'),0,{}));</script><!--<script async src='/scripts/code.min.js?0128b5'></script>-->

# const sheet = new CSSStyleSheet();
# sheet.replaceSync(
#   `@font-face{font-family:read;font-display:block;src:url(\'/public/font/read.woff2\')format(\'woff2\'),url(\'/public/font/read.ttf\')format(\'truetype\')}#TextContent p:nth-last-of-type(2){font-family:"read"!important}`
# );
# document.adoptedStyleSheets = [...document.adoptedStyleSheets, sheet];

# @font-face {
#   font-family: read;
#   font-display: block;
#   src: url('/public/font/read.woff2')format('woff2'),url('/public/font/read.ttf')format('truetype');
# }
# #TextContent p:nth-last-of-type(2) {
#   font-family: "read" !important;
# }

# MI LANTING_GB OUTSIDE YS · Regular · Version 2.3.3;GB Outside YS Regular · 共 37442 个字符形
# 怎么解决这个字体问题呢？
