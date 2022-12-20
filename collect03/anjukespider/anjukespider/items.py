# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AnjukespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    loupan = scrapy.Field()#楼盘
    address = scrapy.Field()#地址
    a_price = scrapy.Field()#单价
    total_price = scrapy.Field()#总价
    f_type = scrapy.Field()#户型
    area = scrapy.Field()#面积
    year = scrapy.Field()#年代
    man = scrapy.Field()#经纪人

