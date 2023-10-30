from selenium import webdriver
import time
from lxml import etree
import os
import requests
import re
from sys import exit

# 基础配置项
executable_path = './msedgedriver.exe'
base_url = 'https://lol.qq.com/data/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
}
print('-'*30, 'XF LOL skin downloader', '-'*30)
input('请确认msedgedriver.exe(https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)存在，确认动作完成后，轻击回车以继续：')

# 加载Edge
try:
    d = webdriver.Edge(executable_path=executable_path)
except:
    print('驱动加载失败，请检查。')
    input('press any key to exit')
    exit(1)

# 获取英雄列表
try:
    print('try：info-heros.shtml')
    d.get(base_url + 'info-heros.shtml')
except:
    print('get info-heros error')
    input('press any key to exit')
    exit(1)

tree_baseurl = etree.HTML(d.page_source)
hero_list = tree_baseurl.xpath('//ul[@id="jSearchHeroDiv"]/li/a/@href')

# 遍历英雄
for hero in hero_list:
    # 拼接详情页地址,延时访问
    defail_url = base_url + hero
    try:
        d.get(defail_url)
        time.sleep(2)
    except:
        print('get', defail_url, 'error')
        input('press any key to exit')
        exit(1)

    # 获取英雄名字及称号
    tree_defail_url = etree.HTML(d.page_source)
    hero_name = tree_defail_url.xpath('//h1[@id="DATAname"]/text()')
    hero_title = tree_defail_url.xpath('//h2[@id="DATAtitle"]/text()')

    # 如果文件夹不存在就创建文件夹
    hero_path = hero_name[0]+' '+hero_title[0]
    hero_path = re.sub(r'[/\\:*?"<>|]', '-', hero_path)
    try:
        if not os.path.exists(hero_path):
            os.makedirs(hero_path)
    except:
        print('makedirs error')
        input('press any key to exit')
        exit(1)

    # 获取皮肤名及地址列表
    skin_name_list = tree_defail_url.xpath('//ul[@id="skinNAV"]/li/a/img/@alt')
    skin_img_list = tree_defail_url.xpath('//ul[@id="skinNAV"]/li/a/img/@src')

    print(skin_name_list)
    # 遍历每一张皮肤图片
    for i in range(len(skin_img_list)):
        # 拼接链接,延时访问
        img_url = skin_img_list[i].replace('small', 'big')
        time.sleep(1)
        try:
            r = requests.get(img_url, headers=headers, stream=True)

            # 创建文件写入图片数据
            # img_path = './'+hero_path+'/' + skin_name_list[i]+'.jpg'
            img_path = './'+hero_path+'/' + \
                re.sub(r'[/\\:*?"<>|]', '-', skin_name_list[i])+'.jpg'
            # img_path = re.sub(r'[/\\:*?"<>|]', '-', img_path)
            print(img_path)
            with open(img_path, 'wb') as fp:
                fp.write(r.content)
        except:
            print('image requests failed')

print('下载完成,ヾ(￣▽￣)Bye~Bye~\n\n\t\t\t\t--by XF(QQ:2581011320)')
input('press any key to continue')
