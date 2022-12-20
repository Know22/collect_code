import scrapy
from anjukespider.items import AnjukespiderItem
class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    # allowed_domains = ['anjuke.com']
    # start_urls = ['https://chongqing.anjuke.com/sale/p'+str(i) for i in range(1,14)] #每页80个所以爬13页]

    def parse(self, response):
        obj=response.xpath('//section[@class="list"]/div')
        for row in obj[2:-1]:
            item=AnjukespiderItem()
            item['loupan'] = row.xpath('.//p[@class="property-content-info-comm-name"]/text()').get().strip()
            item['address'] = row.xpath('.//p[@class="property-content-info-comm-address"]/span[1]/text()').get().strip()\
                      +row.xpath('.//p[@class="property-content-info-comm-address"]/span[2]/text()').get().strip()\
                      +row.xpath('.//p[@class="property-content-info-comm-address"]/span[3]/text()').get().strip()
            item['a_price'] = row.xpath('.//p[@class="property-price-average"]/text()').get().strip()
            item['total_price'] = row.xpath('.//p[@class="property-price-total"]/span[1]/text()').get().strip()+'万'
            item['f_type'] = row.xpath('.//div[@class="property-content-info"]/p[1]/span[1]/text()').get().strip()+'室'\
            +row.xpath('.//div[@class="property-content-info"]/p[1]/span[3]/text()').get().strip()+'厅'\
            +row.xpath('.//div[@class="property-content-info"]/p[1]/span[5]/text()').get().strip()+'卫'
            item['area'] = row.xpath('.//div[@class="property-content-info"]/p[2]/text()').get().strip()
            year = row.xpath('.//div[@class="property-content-info"]/p[5]/text()').get()
            if year==None:
                item['year'] =''
            else:
                item['year'] =year.strip()
            url = row.xpath('./a/@href').get().strip().split('?auction')[0]
            # print(item['loupan'],item['address'],item['a_price'],item['total_price'],item['f_type'],item['area'],item['year'],url)
            print(url)
            yield scrapy.Request(url, meta={"item": item}, callback=self.detail_parse)
            # break
    def detail_parse(self,response):
        item=response.meta["item"]
        item['man']=response.xpath('//div[@class="maininfo-broker-info-name"]/text()').get().strip()
        # print(item['man'])
        yield item

