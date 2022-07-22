# 豆瓣电影Top250页面源代码 requests
# re模块匹配到对应数据 re

import requests
import re
import csv


def get_doubanTop250(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
    }

    resp = requests.get(url, headers=headers)
    # print(resp.text)
    page_content = resp.text

    # 解析数据
    obj = re.compile(r'<li>.*?<span class="title">(?P<movie_name>.*?)</span>'
                     r'.*?<p class="">.*?(?P<movie_year>\d+)'
                     r'.*?<span class="rating_num" property="v:average">(?P<movie_score>.*?)</span>'
                     r'.*?<span>(?P<number_of_people>.*?)人评价</span>', re.S)

    result = obj.finditer(page_content)
    with open('doubanTop250.csv', mode='a', encoding='utf-8', newline='') as f:
        # mode='a'         追加写入csv文件
        # encoding='utf-8' 解决写入中文乱码的问题
        # newline=''       解决写入csv文件自动换行的问题
        csvwriter = csv.writer(f)
        for it in result:
            # print(it.group('movie_name'))
            # print(it.group('movie_year').strip())
            # print(it.group('movie_score'))
            # print(it.group('number_of_people'))
            dic = it.groupdict()
            dic['movie_year'] = dic['movie_year'].strip()
            csvwriter.writerow(dic.values())


if __name__ == '__main__':

    url = 'https://movie.douban.com/top250?start={}&filter='

    with open('doubanTop250.csv', mode='w', encoding='utf-8', newline='') as f:
        # mode='a'         追加写入csv文件
        # encoding='utf-8' 解决写入中文乱码的问题
        # newline=''       解决写入csv文件自动换行的问题
        csvwriter = csv.writer(f)
        csvwriter.writerow(['电影名称', '年份', '评分', '评价人数'])

    for i in range(0, 250, 25):
        url.format(i)  # i=1, url='https://movie.douban.com/top250?start=1&filter='
        get_doubanTop250(url)

    print('over')
