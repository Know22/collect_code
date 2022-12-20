import requests
import pymysql
from lxml import etree

def get_html(url, time=10):
    try:
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}

        resp = requests.get(url, headers=head, timeout=time)  # 发送请求

        resp.encoding = resp.apparent_encoding  # 设置返回内容的字符集编码
        # resp.encoding="utf-8"

        resp.raise_for_status()  # 返回的状态码不等于200抛出异常

        return resp.text  # 返回网页的文本内容

    except Exception as error:
        print(error)

info = []

def parser(html):
    tree = etree.HTML(html)
    for row in tree.xpath("//*[@id='colR']/div[2]/dl/dd/ul/li"):
        cg_title = row.xpath("./a/text()")[0].strip()
        cg_time = row.xpath("./span/text()")[0].strip()
        info.append([cg_title, cg_time])

def save_mysql(sql,val,**dbinfo):  # 将爬取的内容存入mysql数据库
    try:
        con = pymysql.connect(**dbinfo)  # 连接mysql数据库
        cur = con.cursor()  # 创建游标对象
        cur.executemany(sql,val)
        con.commit()
    except Exception as e:  # 若报错，则获得错误类型
        con.rollback()
        print(e)
    finally:
        cur.close()  # 关闭游标
        con.close()  # 关闭链接

if __name__ == "__main__":

    for i in range(1,6):
        if i == 1:
            url = 'http://www.cqie.edu.cn/html/2/tzgg/'
        else:
            url = 'http://www.cqie.edu.cn/html/2/tzgg/List_{0}.shtml'.format(str(i))
        html = get_html(url, time=10)
        if html == None:
            print("已爬取全部数据!\n")
            break
        else:
            parser(html)
    parms={
        "host":"localhost",
        "user":"root",
        "password": "root",
        "database":"study",
        "port":3306
    }
    sql='insert into notice(news_title,news_time) values(%s,%s)'
    save_mysql(sql,info,**parms)
    print("已存储全部数据！")
