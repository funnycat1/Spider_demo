"""
web请求过程剖析：
1. 服务器渲染：
   在服务器那边直接把数据和html整合在一起，统一返回给浏览器
   在页面源代码中能看到数据
2. 客户端渲染：第一次请求只要一个html骨架，第二次请求拿到数据，进行数据展示
   在页面源代码中能看到数据
"""