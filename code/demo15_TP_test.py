# 用线程池爬取北京新发地
# 1. 如何爬取单个页面的数据
# 2. 上线程池，多个页面同时爬取


import requests
import csv
import time
from concurrent.futures import ThreadPoolExecutor


def download_one_page(url, header, dat):

    resp = requests.post(url, headers=header, data=dat)
    # print(resp.json()['list'][0]["prodName"])

    col_name = ["prodCat", "prodPcat", "prodName", "lowPrice", "avgPrice", "highPrice", "specInfo", "place", "unitInfo", "pubDate"]

    for i in range(dat['limit']):

        price_info = dict()

        for j in range(len(col_name)):
            price_info[col_name[j]] = resp.json()['list'][i][col_name[j]]

        with open('priceDetail.csv', mode='a', encoding='utf-8', newline='') as f:
            # mode='a'         追加写入csv文件
            # encoding='utf-8' 解决写入中文乱码的问题
            # newline=''       解决写入csv文件自动换行的问题
            csvwriter = csv.writer(f)
            csvwriter.writerow(price_info.values())

    print("第", dat["current"], "页数据已写入。")


if __name__ == "__main__":

    # 计时开始
    time_start = time.time()

    col_name = ["一级分类", "二级分类", "品名", "最低价", "平均价", "最高价", "规格", "产地", "单位", "发布日期"]
    with open('priceDetail.csv', mode='w', encoding='utf-8', newline='') as f:
        # mode='w'         写入csv文件
        # encoding='utf-8' 解决写入中文乱码的问题
        # newline=''       解决写入csv文件自动换行的问题
        csvwriter = csv.writer(f)
        csvwriter.writerow(col_name)

    url = "http://www.xinfadi.com.cn/getPriceData.html"

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
    }

    dat = {
        "limit": 20,
        "current": 1,
        "pubDateStartTime": "",
        "pubDateEndTime": "",
        "prodPcatid": "",
        "prodCatid": "",
        "prodName": ""
    }
    # download_one_page(url, header, dat)

    # # 单线程下载前100页的数据
    # for i in range(1, 101):
    #     dat["current"] = i
    #     download_one_page(url, header, dat)
    # time_end = time.time()  # 计时结束
    # time_sum = time_end - time_start
    # print("单线程同时写入前100页数据耗时：", time_sum)

    # 多线程下载，开辟一个包含50个线程的线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 101):  # 前100页的数据，每页20条，100*20=20000
            dat["current"] = i
            t.submit(download_one_page(url, header, dat))

    time_end = time.time()  # 计时结束
    time_sum = time_end - time_start
    print("50个线程同时写入前100页数据耗时：", time_sum)

    print("Well done")
