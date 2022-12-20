
# import requests
# import re
# import asyncio
# import aiohttp
# import aiofiles
#
# def get_html(url,head):  #1.拿到页面源代码
#     try:
#         resp = requests.get(url, headers=head)  # 发送请求
#         resp.encoding = resp.apparent_encoding  # 设置返回内容的字符集编码
#         resp.raise_for_status()  # 返回的状态码不等于200抛出异常
#         return resp.text  # 返回网页的文本内容
#     except Exception as error:
#         print(error)
# #https://m3api.awenhao.com/index.php?note=kkRzg5jmx8anb174pstqe&raw=1&n.m3u8
#
# def get_m3u8(html):  #2.从页面源代码中拿到m3u8文件的url
#
#     obj=re.compile(r"url: '(?P<srcurl>.*?)',")
#     m3_url=obj.search(html).group("srcurl")
#     return m3_url
#
# def download_m3u8(m3_url,head):  #3.下载m3u8文件
#
#     resp2=requests.get(m3_url,headers=head)
#     with open("D:\Python\collect\爬的内容_pycharm\协程\movie.txt", mode="wb") as f:
#         f.write(resp2.content)
#     print("m3u8文件下载完成!")
#
# async def download_ts(ts_url,name,session):   #4.下载视频
#     async with session.get(ts_url) as resp:
#         async with aiofiles.open(f"D:\Python\collect\爬的内容_pycharm\协程\{name}.ts",mode="wb") as f:
#             await f.write(await resp.content.read())
#     print(f"{name}下载完毕!")
#
# async def aio_download():   #5.读取m3u8文件，再下载视频
#     count=1
#     tasks=[]
#     async with aiohttp.ClientSession() as session:
#         async with aiofiles.open("D:\Python\collect\爬的内容_pycharm\协程\movie.txt", mode="r",encoding="utf-8") as f:
#             async for line in f:
#                 line = line.strip()
#                 if line.startswith("#"):
#                     continue
#                 task=asyncio.create_task(download_ts(line,count,session))
#                 tasks.append(task)
#                 count +=1
#             await asyncio.wait(tasks)
#
# def main():
#     head = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
#     }
#     url='https://www.91kanju2.com/vod-play/61534-1-2.html'
#     html=get_html(url,head)
#     m3_url=get_m3u8(html)
#     download_m3u8(m3_url, head)
#
# if __name__=="__main__":
#     main()
#     loop=asyncio.get_event_loop()
#     loop.run_until_complete(aio_download())
#     print("已成功下载全部视频!")




