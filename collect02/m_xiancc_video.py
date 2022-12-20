'''
import requests
from concurrent.futures import ThreadPoolExecutor

def download_ts(line,n):
    resp3 = requests.get(line)
    with open(f"D:/Python/collect/爬的内容_pycharm/线程池视频/{n}.ts", mode="wb") as f:
        f.write(resp3.content)
        resp3.close()


if __name__=="__main__":
    n = 1
    with open("D:/Python/collect/爬的内容_pycharm/电影.m3u8", mode="r", encoding="utf-8") as f:
        with ThreadPoolExecutor(10) as t:
            for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                t.submit(download_ts,line,n)
                n += 1
'''

# with ThreadPoolExecutor(3) as t:
#     for i in range(2, 10):
#         t.submit(main, f"http://www.netbian.com/meinv/index_{i}.htm")
# print("全部完成!")

