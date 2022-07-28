"""
html简单语法：
<标签 属性=”值" 属性="值">被标记的内容</标签>

<br />
<img src="xxx.jpg" />
"""

"""
利用 bs4 找到 https://tieba.baidu.com/p/5472939573 里所有新垣结衣的图片
"""

import requests
from bs4 import BeautifulSoup
import time

url = "https://tieba.baidu.com/p/5472939573"
resp = requests.get(url)
resp.encoding = "utf-8"

# 图片都在 img 标签里，属性 class="BDE_Meme"，代码使用 class_ 是区别 python 里的关键字
main_page = BeautifulSoup(resp.text, "html.parser")
img_list = main_page.findAll("img", class_="BDE_Meme")
# print(pic_list)
# img_src_list = []
for img_src in img_list:
    # print(img_src.get("src"))
    # img_src_list.append(img_src.get("src"))
    src = img_src.get("src")

    # 下载图片
    img_resp = requests.get(src)
    img_resp.content  # 拿到的字节
    img_name = src.split("/")[-1]  # 图片的名字，url 中的最后一个 / 以后的内容
    img_path = "../img/"
    with open(img_path+img_name, mode="wb") as f:
        f.write(img_resp.content)

    print("over!", img_name)
    time.sleep(1)

print("all over!")
