import re
import time
from urllib.parse import urlparse

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 创建一个新的Chrome浏览器实例
driver = webdriver.Edge()

url = "https://www.hetushu.com/book/872/551181.html"
content_startflag = r"\r\n手机阅读请点击或扫描二维码\r\n"
content_endflag = r"第一卷 六年之前"

parsed_url = urlparse(url)
base_url = parsed_url.scheme + "://" + parsed_url.netloc


with open("novel.md", "w", encoding="utf-8") as f:
    while url:
        # 打开网页
        print(f"try: {url}")
        driver.get(url)

        # 显式等待，直到页面中出现#content元素
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content"))
        )
        time.sleep(2)  # 等待2秒，以便页面加载完全

        # 模拟全选、复制
        driver.find_element(By.CSS_SELECTOR, "html").send_keys(Keys.CONTROL, "a")
        driver.find_element(By.CSS_SELECTOR, "html").send_keys(Keys.CONTROL, "c")

        # 获取剪贴板内容
        clipboard_content = pyperclip.paste()
        pattern = re.compile(content_startflag + "(.*)" + content_endflag, re.S)
        content = re.findall(pattern, clipboard_content)[0]
        f.write(f"# {content}")

        # 获取下一章的链接
        try:
            next_chapter = driver.find_element(By.CSS_SELECTOR, "#next").get_attribute(
                "href"
            )
            if not next_chapter.startswith("http"):
                url = base_url + next_chapter
            else:
                url = next_chapter
        except:
            break

# 关闭浏览器
driver.quit()
