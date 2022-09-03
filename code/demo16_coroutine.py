# coroutine -- 协程
"""
input() 程序也是处于阻塞状态
requests.get(url) 在网络请求返回数据之前，程序也是处于阻塞状态
一般情况下，当程序处于 IO 操作的时候，线程都会处于阻塞状态

协程：当程序遇见了 IO 操作的时候，可以选择性的切换到其他任务上。
在微观上是一个任务一个任务的进行切换，切换条件一般就是 IO 操作
宏观上是我们能看到是多个任务一起在执行
多任务异步操作

上述都是单线程的条件下
"""


import time
import asyncio


def func():
    print("我爱黎明")
    time.sleep(3)  # 让当前线程处于阻塞状态，CPU是不为我工作的
    print("我真的爱黎明")


async def func1():
    print("你好啊，我叫赛利亚")


async def func2():
    print("你好啊，我叫赛利亚")
    # time.sleep(3)  # 当程序出现了同步操作时，异步就中断了，需要改成异步操作
    await asyncio.sleep(3)  # 异步操作，await 挂起操作放在协程对象前
    print("你叫什么")


async def func3():
    print("你好啊，我叫王小明")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("你想吃什么")


async def func4():
    print("你好啊，我叫洪小胖")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("你呢")


async def main():

    # 第一种写法（不推荐）
    # f2 = func2()
    # await f2  # await 挂起操作放在协程对象前

    # 第二种写法（推荐）
    f2 = func2()  # f2 一个协程对象
    f3 = func3()
    f4 = func4()
    tasks = [   # py3.8 不推荐，py3.11将抛弃
        f2, f3, f4
    ]
    # tasks = [   # 推荐自己将协程对象转换为 task，运行结果上同，当前py3.6不支持这个
    #     asyncio.create_task(f2),
    #     asyncio.create_task(f3),
    #     asyncio.create_task(f4),
    # ]
    await asyncio.wait(tasks)


if __name__ == "__main__":

    # func()

    # g = func1()  # 此时的函数是异步协程函数，此时函数的执行得到的是一个协程对象
    # asyncio.get_event_loop().run_until_complete(g)  # 协程程序运行需要 asyncio 模块支持
    # ## asyncio.run(g) 报错，是因为需要 python3.7，本代码环境是 python3.6.8

    # ##### 直接启动多个任务，协程
    # f2 = func2()
    # f3 = func3()
    # f4 = func4()
    # tasks = [
    #     f2, f3, f4
    # ]
    # t1 = time.time()
    # # 一次性启动多个任务（协程）
    # asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
    # t2 = time.time()
    # print(t2 - t1)

    # ##### 通过 main() 函数启动多个任务，协程
    t1 = time.time()
    asyncio.get_event_loop().run_until_complete(main())
    t2 = time.time()
    print(t2 - t1)


