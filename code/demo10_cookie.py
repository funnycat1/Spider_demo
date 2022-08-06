"""
cookie登录小说网站 https://passport.17k.com/ck/user/login

1. 登录, 得到 cookie
2. 带着 cookie 去请求得到 url
1 和 2 两个操作是连续的，使用 session 进行请求, session 是一连串的请求, 在这个过程中 cookie 不丢失
"""


import requests
"""
# 会话
session = requests.session()

# 1. 登录
url = "https://passport.17k.com/ck/user/login"

data = {
    "loginName": "13986424225",
    "password": "a741852"
}

resp = session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)  # kan cookie

# 2. 拿书架上的数据
# 使用 session 包含 cookie, 发送请求
resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(resp.json())
"""


# 不使用 session, 发送 requests.get 请求, 自带 cookie
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
header = {
    "Cookie": "GUID=5a7a8eab-ab7f-47a3-b79b-d330beca9ba4; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F78%252F61%252F97696178.jpg-88x88%253Fv%253D1659802857000%26id%3D97696178%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BRGU67rig0%26e%3D1675355091%26s%3Df35b1f5746736808; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2297696178%22%2C%22%24device_id%22%3A%2218273e12f8a59e-0a8d7f74d1753b-76492e2f-2073600-18273e12f8be9c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%225a7a8eab-ab7f-47a3-b79b-d330beca9ba4%22%7D"
}

resp = requests.get(url, headers=header)
print(resp.json())
