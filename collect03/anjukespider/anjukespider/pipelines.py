# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class AnjukespiderPipeline:
#     def process_item(self, item, spider):
#         return item
import pymysql

class MYSQLPipeline:
    con=None
    cur=None
    def open_spider(self,spider):
        self.con = pymysql.connect(host='localhost', user='root', password='root', database='supermarket', port=3306)
        self.cur = self.con.cursor()
    def process_item(self, item, spider):
        values=(item['loupan'],item['address'],item['a_price'],item['total_price'],item['f_type'],item['area'],item['year'],item['man'])
        sql="insert into anju(loupan,address,a_price,total_price,f_type,area,f_year,man) " \
            "values(%s,%s,%s,%s,%s,%s,%s,%s)"
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




