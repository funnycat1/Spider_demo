"""
正则表达式
元字符：具有固定含义的特殊符号
常用元字符，一个元字符一次匹配一个字符：
.   匹配除换行符以外的任意一个字符
\w  匹配一个字母或数字或下划线
\s  匹配任意一个空白符
\d  匹配一个数字
\n  匹配一个换行符
\t  匹配一个制表符

^   匹配字符串的开始
$   匹配字符串的结尾

\W  匹配一个非字母或数字或下划线
\S  匹配任意一个非空白符
\D  匹配一个非数字
a|b 匹配字符a或字符b
()  匹配括号内的表达式，也表示一个组
[...]  匹配字符组中的字符
[^...] 匹配除了字符组中的字符其他字符

量词：控制前面的元字符出现的次数
\d*      重复零次或更多次
\d+      重复一次或更多次
\d?      重复一次或一次
\d{n}    重复n次
\d{n,}   重复n次或更多次
\d{n, m} 重复n次到m次

.*   贪婪匹配--尽可能多的匹配字符
.*?  惰性匹配--尽可能少的匹配字符
"""


import re

# findall: 匹配字符串中所有符合正则的内容, 返回一个list
lst = re.findall(r"\d+", "我的电话是：10080，你的电话是：10010")
print(lst)

# finditer: 匹配字符串中所有符合正则的内容, 返回一个迭代器, 从迭代器中拿到内容需要.group()
it = re.finditer(r"\d+", "我的电话是：10080，你的电话是：10010")
for i in it:
    print(i.group())

# search: 匹配字符串中第一个符合正则的内容, 返回一个迭代器, 从迭代器中拿到内容需要.group()
s = re.search(r"\d+", "我的电话是：10080，你的电话是：10010")
print(s.group())

# match是从头开始匹配
s = re.match(r"\d+", "10080，你的电话是：10010")
print(s.group())


# 预加载正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话是：10080，你的电话是：10010")
for it in ret:
    print(it.group())


s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""
# (?P<分组名>正则) 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)  # re.S: 让.能匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group("name"))
    print(it.group("id"))
