# 多进程

from multiprocessing import Process


def func():
    for i in range(1000):
        print("子进程", i)


class MyProcess(Process):
    def run(self):
        for i in range(1000):
            print("子进程", i)


if __name__ == '__main__':

    # p = Process(target=func)
    # p.start()

    p = MyProcess()
    p.start()

    for i in range(1000):
        print("主进程", i)