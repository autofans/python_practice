import multiprocessing
import time


def task1():
    while True:
        print(".....1.....")
        time.sleep(1)


def task2():
    while True:
        print(".....2.....")
        time.sleep(1)


def main():
    # 创建两个进程，同时执行test1和test2函数
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()


