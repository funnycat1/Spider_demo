from lxml import etree

tree = etree.parse("xpath2.html")

# result = tree.xpath("/html")  # 返回: [<Element html at 0x1d06c290c88>]

# result = tree.xpath("/html/body/ul/li/a/text()")  # 返回: ['百度', '谷歌', '搜狗']

# result = tree.xpath("/html/body/ul/li[1]/a/text()")  # 返回: ['百度'], xpath 的索引从 1 开始

# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")  # 返回: ['大炮'], a[@href='dapao'] 属性筛选

# print(result)

ol_li_list = tree.xpath("/html/body/ol/li")

for li in ol_li_list:
    # print(li)
    # 从每一个 li 中提取到文字
    result = li.xpath("./a/text()")  # 从 li 中继续寻找, ./ 表示当前节点 li
    print(result)

    # 找到 a 标签的 href 属性值
    result2 = li.xpath("./a/@href")
    print(result2)

print(tree.xpath("/html/body/ul/li/a/@href"))  # ['http://www.baidu.com', 'http://www.google.com', 'http://www.sougou.com']

print(tree.xpath("/html/body/div[1]/text()"))  # ['小明']

print(tree.xpath("/html/body/ol/li/a/text()"))  # ['飞机', '大炮', '火车']
