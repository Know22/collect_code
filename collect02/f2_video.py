import requests

def get_html(url, time=10):
    try:
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        "Referer":url}

        resp = requests.get(url, headers=head, timeout=time)  # 发送请求

        resp.encoding = resp.apparent_encoding  # 设置返回内容的字符集编码
        # resp.encoding="utf-8"

        resp.raise_for_status()  # 返回的状态码不等于200抛出异常

        return resp.json()  # 返回网页的文本内容

    except Exception as error:
        print(error)

# https://video.pearvideo.com/mp4/third/20220114/cont-1749961-11315812-084735-hd.mp4      真实
# https://video.pearvideo.com/mp4/third/20220114/1649558544111-11315812-084735-hd.mp4
def parser_save(html):
    dic=html
    srcurl=dic["videoInfo"]["videos"]["srcUrl"]
    systemtime=dic["systemTime"]
    srcurl=srcurl.replace(systemtime,f"cont-{contId}")

    resp2=requests.get(srcurl)
    with open("D:\Python\collect\爬的内容_pycharm\爬的视频\yuyin.mp4","wb") as f:
        f.write(resp2.content)

if __name__=='__main__':
    url = 'https://www.pearvideo.com/video_1749961'
    contId=url.split("_")[1]
    vid_url=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}"
    html=get_html(vid_url, time=10)

    parser_save(html)