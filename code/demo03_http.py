"""
http协议：Hyper Text Transfer Protocol 超文本传输协议
http协议将一条消息分为三大内容，无论是请求还是响应；


请求：
1. 请求行 -> 请求方式(get/post)，请求url地址，协议
2. 请求头 -> 放一些服务器要使用的附加信息
    请求头中常见的一些重要内容(爬虫需要)：
    2.1 User-Agent：请求载体的身份表示(用啥发送的请求)
    2.2 Referer：防盗链(这次请求是从哪个页面来的？反爬会用到)
    2.3 cookie：本地字符串数据信息(用户登录信息，反爬的token)
3. 请求体 -> 一般放一些请求参数


响应：
1. 状态行 -> 协议，状态码(200/404/500/302)
2. 响应头 -> 放一些客户端要使用的附加信息
    响应头中常见的一些重要内容：
    2.1 cookie：本地字符串数据信息(用户登录信息，反爬的token)
    2.2 各种神奇的莫名其妙的字符串(这个需要经验，一般都是token字样，防止各种攻击和反爬)
3. 响应体 -> 服务器返回的真正客户端要用的内容(HTML, json)等


请求方式：
    GET: 显示提交, 多用于查询
    POST: 隐式提交, 多用于修改
"""
