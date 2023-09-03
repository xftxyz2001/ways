# 一个简单的文档转markdown下载 from https://github.com/renyunkang/yuque-exporter

docURLs = [
    # "https://www.yuque.com/用户名/知识库名/文档ID",
]

# 查询参数
queryArgs = "/markdown?attachment=true&latexcode=false&anchor=false&linebreak=false"

import random
import time
from urllib.parse import unquote

import requests

for i, url in enumerate(docURLs):
    # 进度
    print(f"[{i+1}/{len(docURLs)}] " + url)

    # 获取
    fullURL = url + queryArgs
    r = requests.get(fullURL)

    # 保存
    filename = r.headers["Content-Disposition"]
    decoded_filename = unquote(filename.split("filename*=UTF-8''")[1])
    with open(decoded_filename, "wb") as f:
        f.write(r.content)
        f.close()
    print("done: " + decoded_filename)

    # 休眠
    time.sleep(random.randint(1, 5))
    # break
