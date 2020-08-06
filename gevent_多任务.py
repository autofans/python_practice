import gevent
import time
from gevent import monkey

monkey.patch_all()


def task1():
    while True:
        print(".....1.....")
        time.sleep(0.5)


def task2():
    while True:
        print(".....2.....")
        time.sleep(0.5)


def task3():
    while True:
        print(".....3.....")
        time.sleep(0.5)


def main():
    g1 = gevent.spawn(task1, 5)
    g2 = gevent.spawn(task2, 5)
    g3 = gevent.spawn(task3, 5)

    gevent.joinall([g1, g2, g3])


if __name__ == '__main__':
    main()
