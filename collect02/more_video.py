
import requests
'''
import re

from concurrent.futures import ThreadPoolExecutor

def main(url):
    try:
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"}
        resp = requests.get(url, headers=head)  # 发送请求
        resp.encoding = resp.apparent_encoding  # 设置返回内容的字符集编码
        resp.raise_for_status()  # 返回的状态码不等于200抛出异常
        html=resp.text  # 返回网页的文本内容
    except Exception as error:
        print(error)

    obj=re.compile(r"url: '(?P<srcurl>.*?)',")
    m3_url=obj.search(html).group("srcurl")

    resp2=requests.get(m3_url,headers=head)
    with open("D:\Python\collect\爬的内容_pycharm\爬的大视频\电影.m3u8","wb") as f:
        f.write(resp2.content)
    print("下载完成!")


if __name__=='__main__':

    with ThreadPoolExecutor(1) as t:#这个程序不需要这个操作
        t.submit(main,"https://www.91kanju2.com/vod-play/61534-1-1.html")
'''


# srcurl="https://m3api.awenhao.com/index.php?note=kkRq83chxtdnkwzjae9p6&raw=1&n.m3u8"
# url="https://www.91kanju2.com/vod-play/61534-1-1.html"
# video: {
# url: 'https://m3api.awenhao.com/index.php?note=kkRq83chxtdnkwzjae9p6&raw=1&n.m3u8',
'''
n=1
with open("D:\Python\collect\爬的内容_pycharm\爬的大视频\电影.m3u8",mode="r",encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if line.startswith("#"):
            continue
        resp3=requests.get(line)
        f=open(f"D:\Python\collect\爬的内容_pycharm\爬的大视频\{n}.ts",mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n+=1
        print("完成了1个!")
print("全部完成!")
'''

