import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from rulespider.items import RulespiderItem
from rulespider.items import DetailItem

class GcxySpider(CrawlSpider):
    name = 'gcxy'
    # allowed_domains = ['xxx.com']
    start_urls = ['http://www.cqie.edu.cn/html/2/tzgg/Index.shtml']
    #此项目采用广度优先爬取
    rules = (
        Rule(LinkExtractor(allow=r'http://www.cqie.edu.cn/html/2/tzgg/List_\d+.shtml'), callback='parse_item', follow=True), \
        Rule(LinkExtractor(allow=r'http://www.cqie.edu.cn/html/2/content/\d+/\d+/\d+.shtml'), callback='detail_parse', follow=False)
    )
#/html/2/content/22/05/42312.shtml
    def parse_item(self, response):
        # print(response)
        # obj=response.xpath('//*[@id="colR"]/div[2]/dl/dd/ul/li')
        # for row in obj:
        #     item = RulespiderItem()
        #     title=row.xpath('./a/text()').get().strip().replace('\n','')
        #     new_time=row.xpath('./span/text()').get().strip().replace('\n','')
        #     item['title']=title
        #     item['new_time']=new_time
        #     yield item
        pass
    def detail_parse(self,response):
        title_two=response.xpath('//*[@id="text"]/h1/text()').get().strip().replace('\n','')
        scan_num=response.xpath('//*[@id="text"]/h4/text()').get().strip().replace('\n','')
        item=DetailItem()
        item['title_two']=title_two
        item['scan_num']=scan_num
        yield item
#注意内容的 空白处理 和 换行处理，否则会对后面的存储产生影响
