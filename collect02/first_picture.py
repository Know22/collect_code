import requests
from lxml import etree

def get_html(url):
    try:
        resp = requests.get(url)
        resp.encoding = resp.apparent_encoding
        resp.raise_for_status()
        return resp.text
    except exception as error:
        print(error)

def parser_and_save(html):
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

        with open("爬的图片/" + img_name, "wb") as f:
            f.write(img_resp_content)
            print('over!')


if __name__ == "__main__":
    url = "http://www.netbian.com/meinv/index_6.htm"
    html = get_html(url)

    parser_and_save(html)
