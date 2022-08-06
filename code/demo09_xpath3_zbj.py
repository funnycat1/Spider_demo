"""
利用 xpath 解析豆瓣 Top250 的第一页：https://movie.douban.com/top250?start=0&filter=
"""
import requests
from lxml import etree

url = "https://movie.douban.com/top250?start=0&filter="

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
}

resp = requests.get(url, headers=header)
html = etree.HTML(resp.text)

# print(html.xpath("/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()"))  # ['肖申克的救赎']
film_list = html.xpath("/html/body/div[3]/div[1]/div/div[1]/ol/li")
for film in film_list:
    film_name = film.xpath("./div/div[2]/div[1]/a/span[1]/text()")      # 电影名字
    film_grade = film.xpath("./div/div[2]/div[2]/div/span[2]/text()")   # 电影评分
    film_people = film.xpath("./div/div[2]/div[2]/div/span[4]/text()")  # 电影评价人数
    print(film_name, film_grade, film_people)
