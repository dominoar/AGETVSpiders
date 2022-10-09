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
    v_arime_type = scrapy.Field()
    v_original_name = scrapy.Field()
    v_other_name = scrapy.Field()
    v_author = scrapy.Field()
    v_production = scrapy.Field()
    v_first_time = scrapy.Field()
    v_play_status = scrapy.Field()
    v_plot_type = scrapy.Field()
    v_label = scrapy.Field()
    v_original_web = scrapy.Field()
    v_home = scrapy.Field()
    v_urls = scrapy.Field()
