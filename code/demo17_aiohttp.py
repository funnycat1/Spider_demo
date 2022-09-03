# requests.get() 同步代码  -->  异步操作aiohttp

import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/mm/20211129/ilvxf1xtk3k.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211129/dgmjtw2rmxu.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211129/0popoomlcb1.jpg"
]


async def aiodownload(url):
    # s = aiohttp.ClientSession()   <==>   requests
    # s.get()  ==  requests.get()
    # s.post() == requests.post()
    # 发送请求
    # 得到图片内容
    # 保存到文件
    name = "../img/mm/" + url.rsplit("/", 1)[1]  # 从右边切一次，得到 [1] 位置内容
    async with aiohttp.ClientSession() as session:
        # with 将自动关闭 session
        async with session.get(url) as resp:
            # 读写文件也是 io，也可以异步，进一步学习 aiofiles 模块
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())  # 读取内容是异步的，需要 await 挂起

    print(name, "搞定")


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
