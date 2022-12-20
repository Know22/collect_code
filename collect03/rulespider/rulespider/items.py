# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class RulespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title = scrapy.Field()
    # new_time = scrapy.Field()

class DetailItem(scrapy.Item):
    title_two = scrapy.Field()
    scan_num = scrapy.Field()
