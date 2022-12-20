# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoufangspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#卖点
    total_price = scrapy.Field()#总价
    a_price = scrapy.Field()#单价
    url_2 = scrapy.Field()#详情url
    f_type = scrapy.Field()#户型
    f_area = scrapy.Field()#面积
    f_fangx = scrapy.Field()#方向
    f_louc = scrapy.Field()#楼层
    f_zhuangx = scrapy.Field()#装修
    f_year = scrapy.Field()#年代
    f_xiaoqu = scrapy.Field()#小区
    f_address = scrapy.Field()#地址

