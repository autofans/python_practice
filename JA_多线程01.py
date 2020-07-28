import threading
import time


def test1():
    while True:
        print("1.....")
        time.sleep(1)


def test2():
    while True:
        print("2.....")
        time.sleep(1)


def main():
    # 创建两个线程，同时执行test1和test2函数
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
