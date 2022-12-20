# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class RulespiderPipeline:
#     def process_item(self, item, spider):
#         return item
import pymysql
#前面两个结合是使用广度优先爬取
# class RulespiderPipeline:
#     con=None
#     cur=None
#     def open_spider(self,spider):
#         self.con = pymysql.connect(host='localhost', user='root', password='root', database='study', port=3306)
#         self.cur = self.con.cursor()
#     def process_item(self, item, spider):
#         values=(item["title"],item["new_time"])
#         sql="insert into gcxy(title,new_time) values(%s,%s)"
#         try:
#             self.cur.execute(sql,values)
#             self.con.commit()
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#         return item
#     def close_spider(self,spider):
#         self.cur.close()
#         self.con.close()
class RulespiderPipeline:
    con=None
    cur=None
    def open_spider(self,spider):
        self.con = pymysql.connect(host='localhost', user='root', password='root', database='study', port=3306)
        self.cur = self.con.cursor()
    def process_item(self, item, spider):
        # values=(item["title_two"],item["scan_num"],item["title_two"])
        sql='update gcxy set title_two="%s",scan_num="%s" where title="%s"'%(item["title_two"],item["scan_num"],item["title_two"])
        try:
            self.cur.execute(sql)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        return item
    def close_spider(self,spider):
        self.cur.close()
        self.con.close()


