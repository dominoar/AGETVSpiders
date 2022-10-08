import sys

import scrapy
from lxml import etree
from scrapy import Request
from scrapy.http import Response

# 标记一下IO出去时，排行页的顺序
page_number = 0


class AgetvRanksSpider(scrapy.Spider):
    name = 'AGE排行页'
    allowed_domains = ['https://agemys.cc']

    # start_urls = ['https://www.agemys.cc/rank?tag=catyear&value=&page=2']

    def start_requests(self):
        for i in range(1, 51):
            yield Request(url=f'https://www.agemys.cc/rank?tag=catyear&value=&page={i}')

    def parse(self, response: Response, **kwargs):
        global page_number
        # 将每一页排行写出到本地
        try:
            file = open(file=f'/html/AGETV/index{page_number}.html', mode='w+', encoding="UTF-8")
            page_number = page_number + 1
            file.writelines(response.text)
            file.close()
        except Exception as e:
            print(e.args, e)


class AgetvResourcePageSpider(scrapy.Spider):
    name = 'AGE资源页爬取'
    allowed_domains = ['https://agemys.cc']

    # start_urls = ['D:/html/AGETV/index0.html']

    def start_requests(self):
        page = 1
        for i in range(0, 50):
            lxml = etree.parse(f'/html/AGETV/index{i}.html', etree.HTMLParser())
            urls = lxml.xpath('//li[contains(@class,"rank_text")]/a/@href')
            for url in urls:
                url = 'https://agemys.cc/' + url
                yield Request(url=url)
            print(f'--------- 开始抓取第{page}组数据---------- ')
            page = page + 1

    def parse(self, response, **kwargs):
        global page_number
        try:
            file = open(file=f'/html/AGETV/Video/index{page_number}.html', mode='w+', encoding="UTF-8")
            page_number = page_number + 1
            file.writelines(response.text)
            file.close()
            print(f'-----------成功抓取第{page_number}跳数据------------')
        except Exception as e:
            print(e.args, e)


class AgeResultSpider(scrapy.Spider):
    name = 'AGE资源页爬取'
    allowed_domains = ['https://agemys.cc']

    def start_requests(self):
        for i in range(0, 31367):
            yield Request(url=f'/html/AGETV/Video/index{i}.html')

    def parse(self, response: Response, **kwargs):
        pass

