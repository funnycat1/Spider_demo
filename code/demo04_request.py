"""
安装 requests: pip install requests
"""

import requests


""" # 搜狗所搜周杰伦
url = 'https://www.sogou.com/web?query=周杰伦'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
}

resp = requests.get(url, headers=headers)  # headers 模拟浏览器的请求头里的 User-Agent

print(resp)
print(resp.text)  # 拿到页面源代码
"""


""" # 翻译英文单词
url = 'https://fanyi.baidu.com/sug'

s = input('请输入你要翻译的英文单词：')

dat = {
    "kw": s
}

# 发送 post 请求, 发送的数据必须放在字典里，通过 data 参数进行传递
resp = requests.post(url, data=dat)
print(resp.json())  # 将服务器返回的内容直接处理成 json() => dict
"""


# 搜索豆瓣电影排行榜
url = 'https://movie.douban.com/j/chart/top_list'

# 封装参数
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49 "
}
# get 请求, 参数用字典格式传递给 params
resp = requests.get(url=url, params=param, headers=headers)

print(resp.json())
resp.close()  # 关掉resp
