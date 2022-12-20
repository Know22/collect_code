import scrapy
from baiduspider.items import BaiduspiderItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        for row in response.xpath('//div[@id="s-top-left"]/a'):
            item=BaiduspiderItem()
            item['title']=row.xpath('text()').get() #获取文本
            item['url']=row.xpath('@href').get() #获取属性url
            yield item




