
import re

url='''<div class="img" style="background-image: url('//img4.mukewang.com/6212fe63099c7a3305400304.png')"></div>'''

num='''< p class ="one" > 零基础 · 2229人报名 < / p >'''

obj_num=re.compile(r"\d+")
# obj_num=re.compile(r"零基础 · (?P<num>.*?)人报名")
row1=obj_num.finditer(num)
for n in row1:
    print(n.group())

obj_url=re.compile(r"('(?P<url>.*?)')")
row2=obj_url.finditer(url)
for i in row2:
    print(i.group("url"))
