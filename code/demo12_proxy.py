# 原理：通过第三方的一个机器发送请求

import requests

# 101.200.127.149:3129
# 122.224.56.198:7302
# 218.60.8.83:3129
proxies = {
    # "https": "https://101.200.127.149:3129",
    "https": "https://218.60.8.83:3129"
}

resp = requests.get("https://www.baidu.com", proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
