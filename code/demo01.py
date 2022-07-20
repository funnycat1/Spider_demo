from urllib.request import urlopen


url = 'http://www.baidu.com'
resp = urlopen(url)

# print(resp.read().decode('utf-8'))
# encoding 参数解决写入中文乱码
with open('mybaidu.html', mode='w', encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))  # 读取到网页的页面源代码


print('over!')