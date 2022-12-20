import scrapy
from ershoufangspider.items import ErshoufangspiderItem

class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    # allowed_domains = ['ershoufang.com']
    # start_urls = ['https://cq.58.com/ershoufang/p'+str(i) for i in range(2,3)] #每页80个所以爬13页
    start_urls = ['https://cq.58.com/ershoufang/p3/']
    def parse(self, response):
        # print(response.text)
        for row in response.xpath('//*[@id="esfMain"]/section/section[3]/section[1]/section[2]/div'):
            item=ErshoufangspiderItem()
            item["title"]=row.xpath('./a/div[2]/div[1]//h3/text()').get()
            item["total_price"]=row.xpath('./a/div[2]/div[2]/p[1]//span/text()').get()
            item["a_price"]=row.xpath('./a/div[2]/div[2]/p[2]/text()').get()
            item["url_2"]=row.xpath('./a/@href').get().split('?auction')[0]
            url_2=item["url_2"]
            print(url_2)
            yield scrapy.Request(url_2,meta={"item":item},callback=self.detail_parse)
            # break

    def detail_parse(self,response):
        item=response.meta["item"]
        item["f_type"]=response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/i[1]/text()').get()\
        +response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/span[1]/text()').get()\
        +response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/i[2]/text()').get()\
        +response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/span[2]/text()').get()\
        +response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/i[3]/text()').get()\
        +response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/span[3]/text()').get()
        item["f_area"]=response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/i/text()').get()+'m²'
        item["f_fangx"]=response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[1]/i/text()').get()
        item["f_louc"]=response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/text()').get()
        item["f_zhuangx"]=response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/text()').get()
        item["f_year"]=response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[3]/div[2]/text()').get()
        item["f_xiaoqu"]=response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[1]/a[1]/text()').get()
        item["f_address"]=response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[2]/span[2]/a[1]/text()').get()\
        +response.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[2]/span[2]/a[2]/text()').get()
        # print(item["f_address"])
        yield item
