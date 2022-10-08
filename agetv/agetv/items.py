# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AgetvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class VideoItem(scrapy.Item):
    v_title = scrapy.Field()
    v_address = scrapy.Field()
    v_title2 = scrapy.Field()
    v_title3 = scrapy.Field()
    v_original = scrapy.Field()
    v_company = scrapy.Field()
    v_last_time = scrapy.Field()
    v_state = scrapy.Field()
    v_tags = scrapy.Field()
    v_official_web =scrapy.Field()
