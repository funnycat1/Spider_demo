# 进程，线程
# 进程是资源单位，线程是执行单位，一个进程至少要有一个线程
# cpu运行时是找线程


# 启动每一个程序（进程）默认都会有一个主线程


# 多线程
from threading import Thread   # 线程类


# def func():
#     for i in range(1000):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     # 开辟一个新线程，target 告诉线程的任务
#     t = Thread(target=func)  # 创建子线程并给子线程安排任务
#     t.start()  # 开始执行该线程，实际是多线程状态为可以开始工作状态，具体的执行时间由CPU决定
#
#     for i in range(1000):
#         print("main", i)


class MyThread(Thread):
    def run(self):  # 固定的   ->  当线程被执行的时候，被执行的就是 run()
        for i in range(1000):
            print("子线程", i)


if __name__ == '__main__':

    t = MyThread()
    # t.run()  # 方法的调用，单线程
    t.start()  # 开启新线程，子线程

    for i in range(1000):
        print("主线程", i)
