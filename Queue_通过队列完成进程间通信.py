import multiprocessing


def down_data(q):
    """下载数据"""
    # 模拟从网上下载数据
    data = [11, 22, 33, 44]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)

    print("已下载完成，并已把数据存入到Queue队列中.....")


def an_data(q):
    """处理数据"""
    w_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        w_data.append(data)

        if q.empty():
            break

    print(w_data)


def main():
    # 创建一个队列Queue
    q = multiprocessing.Queue()

    # 创建多个进程，将队列的引用当作实参进行传递
    p1 = multiprocessing.Process(target=down_data, args=(q,))
    p2 = multiprocessing.Process(target=an_data, args=(q,))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
