import scrapy


class DongtaiSpider(scrapy.Spider):
    name = 'dongtai'
    # allowed_domains = ['lagou.com']
    start_urls = ['http://www.bspider.top/jkwin/']

    def parse(self, response):
        obj=response.xpath('//*[@id="app"]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/ul/li')
        for row in obj:
            name=row.xpath('./a/div[2]//span[1]/text()').get()
            level=row.xpath('./a/div[2]//span[2]/text()').get()
            print(name,level)
