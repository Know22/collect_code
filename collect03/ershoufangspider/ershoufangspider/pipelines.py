# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

# class ErshoufangspiderPipeline:
#     def process_item(self, item, spider):
#         return item

class MYSQLPipeline:
    con=None
    cur=None
    def open_spider(self,spider):
        self.con = pymysql.connect(host='localhost', user='root', password='root', database='supermarket', port=3306)
        self.cur = self.con.cursor()
    def process_item(self, item, spider):
        values=(item["title"],item["total_price"],item["a_price"],item["url_2"],item["f_type"],item["f_area"],\
                item["f_fangx"],item["f_louc"],item["f_zhuangx"],item["f_year"],item["f_xiaoqu"],item["f_address"])
        sql="insert into ershoufang(title,total_price,a_price,url_2,f_type,f_area,f_fangx,f_louc,f_zhuangx,f_year,f_xiaoqu,f_address) " \
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            self.cur.execute(sql,values)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        return item
    def close_spider(self,spider):
        self.cur.close()
        self.con.close()
