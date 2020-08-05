import threading
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
    # 创建两个线程，同时执行test1和test2函数
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
