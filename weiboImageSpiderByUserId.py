import requests
from lxml import etree
import time

# 非必要无需关心内部实现细节，使用示例：
'''
from weiboImageSpiderByUserId import WeiboImageSpiderByUserIdDownloader
spider = WeiboImageSpiderByUserIdDownloader(
    userId='2623471650',
    cookie='_T_WM=4776f3ee682cc7a906bfa2d222031c8d; SUB=_2A25MMKODDeRhGeVG6FYW8ivOyjuIHXVv2s3LrDV6PUJbktB-LXaskW1NT7uPq00tQ1B2mkCzsf4qrFlsYeYw64d4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWECVmxeRP9endsyagjio9j5NHD95Q01heXS0zfeo2NWs4DqcjLHFH81C-ReF-4BCH8Sb-41C-4eEH8SCHWxC-RSEH8SCHWxC-41Btt'
)
spider.start()
'''
# 当然，构造方法中还有更多的参数可以指定，但只有上述两个是必须的


class WeiboImageSpiderByUserIdDownloader:

    ########## 配置 ##########
    def __init__(self, userId='3834725217', startPageNumber=1, endPageNumber=1, cookie='__', request_delay=1, down_load_to='./'):
        '''
            userId 目标用户ID
            maxPage 爬取截至页码[1，~]
            cookie 具有时效性，可从开发人员工具中获取
            request_delay 请求时延，避免访问过于频繁而出现访问失败
            down_load_to 图片目标目录
        '''
        self.userId = userId
        self.startPageNumber = startPageNumber
        self.maxPage = endPageNumber
        self.cookie = cookie
        self.headers = {
            'cookie': cookie,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
        }
        self.request_delay = request_delay
        self.down_load_to = down_load_to

    ########## 全局变量定义 ##########
    '''
    img_file_count 当前共下载图片数(修改会影响控制台输出和输出的文件名)
    headers = 包含cookie和ua的字典,不建议修改
    '''
    img_file_count = 0

    ########## 函数定义 ##########

    def get_tree_by_url(self, url):
        time.sleep(self.request_delay)
        response = requests.get(url, headers=self.headers)
        tree = etree.HTML(response.content)
        return tree

    def get_tree(self, userId, page):
        base_url = 'https://weibo.cn/u/'
        url = base_url + userId + '?page=' + str(page)
        time.sleep(self.request_delay)
        response = requests.get(url, headers=self.headers)
        tree = etree.HTML(response.content)
        return tree

    def down_load_image(self, img_url):
        print(self.img_file_count, img_url)
        time.sleep(self.request_delay)
        response = requests.get(img_url, headers=self.headers)
        # response.content就是图片的2进制数据
        file_name = self.down_load_to + 'img_' + str(self.img_file_count) + \
            ('.gif' if response.content[0:3] == b'GIF' else '.jpg')
        self.img_file_count += 1
        with open(file_name, 'wb') as fp:
            fp.write(response.content)

    ########## 主体函数 ##########

    def start(self):
        for page in range(self.startPageNumber, self.maxPage+1):
            page_tree = self.get_tree(userId=self.userId, page=page)
            yuantu_list = []

            # 处理一页组图（提取组图的所有原图）
            zutu_list = page_tree.xpath(
                '//*[@id]/div[1]/a[contains(text(),"组图")]/@href')
            for zutu in zutu_list:
                # 提取一组原图
                zutu_tree = self.get_tree_by_url(zutu)
                yuantu_list_no_head = zutu_tree.xpath(
                    '//a[contains(text(),"原图")]/@href')
                for i in range(len(yuantu_list_no_head)):
                    yuantu_list_no_head[i] = 'https://weibo.cn' + \
                        yuantu_list_no_head[i]
                yuantu_list.extend(yuantu_list_no_head)

            # 处理独立原图（提取单张没有组图的原图）
            yuantu_list.extend(page_tree.xpath('//*[@id]/div[2]/a[2]/@href'))

            # 下载图片
            for yuantu in yuantu_list:
                self.down_load_image(yuantu)
