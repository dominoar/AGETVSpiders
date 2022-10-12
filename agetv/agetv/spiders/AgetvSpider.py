import logging

import scrapy
from scrapy import Request
from scrapy.http import Response

from agetv.items import VideoItem


class AgetvRanksSpider(scrapy.Spider):
    name = 'AGE动漫网'
    allowed_domains = ['https://agemys.cc']

    # start_urls = ['https://www.agemys.cc/rank?tag=catyear&value=&page=2']

    rank_number = 0

    def start_requests(self):
        # for i in range(1, 51):
        yield Request(url=f'https://www.agemys.cc/rank?tag=catyear&value=&page={1}')
        logging.info(f'[----------开始请求第{1}页排行----------]')

    # 转接每一个资源请求到 video_parse进行解析
    def parse(self, response: Response, **kwargs):
        self.rank_number = self.rank_number + 1
        rank_temp = self.rank_number
        logging.info(f'[----------开始解析第{rank_temp}页的排行页----------]')
        video_urls = response.xpath('//li[contains(@class,"rank_text")]/a/@href').extract()
        video = VideoItem()
        # for video_url in video_urls:
        yield Request(method='GET', url=self.allowed_domains[0] + video_urls[0], callback=self.video_parse,
                      meta={'video': video},
                      dont_filter=True)
        # logging.info(f'[----------第{rank_temp}页的排行已经解析完毕----------]')

        # 解析每一个资源

    def video_parse(self, resp: Response):
        logging.info('[----------开始解析数据----------]')
        video = resp.meta['video']
        video['v_title'] = resp.xpath('//div[@class="blockcontent"]/h4/text()')[0].extract()
        video_tag = resp.xpath('//span[@class="detail_imform_value"]/text()').extract()
        video['v_address'] = video_tag[0]
        video['v_arime_type'] = video_tag[1]
        video['v_original_name'] = video_tag[2]
        video['v_other_name'] = video_tag[3]
        video['v_author'] = video_tag[4]
        video['v_production'] = video_tag[5]
        video['v_first_time'] = video_tag[6]
        video['v_play_status'] = video_tag[7]
        video['v_plot_type'] = video_tag[8]
        video['v_label'] = video_tag[9]
        video['v_original_web'] = video_tag[10]
        video['v_home'] = resp.url
        # 解析播放链接
        movurls = resp.xpath('//div[@class="movurl"]')
        video_links = []
        for movurl in movurls:
            urls = movurl.xpath('./ul//li/a/@href').extract()
            for i in range(0, len(urls)):
                urls[i] = self.allowed_domains[0] + urls[i]
            video_links.append(urls)
        video['v_urls'] = video_links
        yield video
