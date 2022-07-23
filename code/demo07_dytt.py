"""
电影天堂：http://www.dytt89.com/
1. 定位到 2022必看热片
2. 从 2022必看热片 中提取到子页面的链接地址
3. 在请求页面的链接地址中，拿到下载地址
"""

import requests
import re
import json
import copy

domain = 'http://www.dytt89.com/'
resp = requests.get(domain)
resp.encoding = 'gb2312'
# print(resp.text)

# 找到 2022必看热片
obj1 = re.compile(r'2022必看热片.*?<ul>(?P<movie>.*?)</ul>', re.S)
movie_list = obj1.search(resp.text)  # search 匹配到第一个符合正则的字符串
movie_list_result = movie_list.group('movie')
# print(movie_list_result)


# 从 2022必看热片 中提取子页面的链接地址和电影名字
obj2 = re.compile(r"<li><a href='(?P<child_url>.*?)'.*?《(?P<movie_name>.*?)》", re.S)
# child_url_list = []
# movie_name_list = []
movie_dict_list = []
child_url_result = obj2.finditer(movie_list_result)
for cur in child_url_result:
    # # print(cur.group('child_url'))
    # child_url = domain + cur.group('child_url').strip('/')
    # # print(child_url)
    # child_url_list.append(child_url)
    #
    # # print(cur.group('movie_name'))
    # movie_name_list.append(cur.group('movie_name'))

    movie_dic = cur.groupdict()
    movie_dic['child_url'] = domain + cur.group('child_url').strip('/')
    # print(movie_dic)

    movie_dict_list.append(movie_dic)

# print(movie_dict_list)


# 在电影的子页面中，找到电影的下载链接
obj3 = re.compile(r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<movie_download_url>.*?)"', re.S)
movie_download_url_dict = dict()
movie_download_url_dict_list = []
for mdl in movie_dict_list:
    movie_name = mdl['movie_name']
    child_url = mdl['child_url']
    # print(child_url)

    child_url_resp = requests.get(child_url)
    child_url_resp.encoding = 'gb2312'
    mdu = obj3.findall(child_url_resp.text)
    # print(mdu)

    movie_download_url_dict['movie_name'] = movie_name
    movie_download_url_dict['download_url'] = mdu
    # print(movie_download_url_dict)
    movie_download_url_dict_list.append(copy.deepcopy(movie_download_url_dict))
    # break


# 将数据存入json文件中
data_dict = dict()
for i in range(len(movie_download_url_dict_list)):
    movie_i = 'movie{}'.format(i)
    data_dict[movie_i] = movie_download_url_dict_list[i]

# print(data_dict)

with open('dytt.json', mode='w', encoding='utf-8') as f:
    json.dump(data_dict, f)

print('over')

