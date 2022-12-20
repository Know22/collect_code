'''
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

def main(url):
    try:
        resp = requests.get(url)
        resp.encoding = resp.apparent_encoding
        resp.raise_for_status()
        html=resp.text
    except Exception as error:
        print(error)

    tree = etree.HTML(html)

    img_li = tree.xpath('//div[@class="list"]/ul//li')
    img_li.pop(2)
    img_li.pop(18)
    # print(len(img_li))
    for img in img_li:
        img_path = img.xpath("./a/img/@src")[0]

        img_name = img.xpath("./a/img/@alt")[0] + ".png"
        # print(img_name)
        img_resp = requests.get(img_path)
        img_resp_content = img_resp.content

        with open(f"D:\Python\collect\爬的内容_pycharm\爬的大图片\{img_name}", "wb") as f:
            f.write(img_resp_content)
            print(img_path,'提取完成!')

if __name__ == "__main__":

    with ThreadPoolExecutor(3) as t:
        for i in range(2,10):
            t.submit(main,f"http://www.netbian.com/meinv/index_{i}.htm")
    print("全部完成!")
'''