# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
from scrapy.http import HtmlResponse

class SeleniumMiddleware:
    def __init__(self):
        self.opt=Options()
        # self.opt.add_argument('--headless')
        # self.opt.add_argument('--disable-gpu')
        self.opt.add_experimental_option('excludeSwitches', ['enable-logging'])#禁止打印日志
        self.web = Chrome(options=self.opt)
    def process_request(self, request, spider):
        self.web.get(request.url)
        time.sleep(3)
        text=self.web.page_source
        self.web.close()
        resp=HtmlResponse(url=request.url,body=text,request=request,encoding='utf-8')

        return resp


