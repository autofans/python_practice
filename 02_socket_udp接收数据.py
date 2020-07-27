import socket


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地ip和port
    local_add = ("", 7890)
    udp_socket.bind(local_add)

    while True:
        # 接收数据
        rec_data = udp_socket.recvfrom(1024)
        # rec_data这个变量接收到的是一个元组(接收到的数据, (发送方的IP, port))
        rec_msg = rec_data[0]  # 接收到的数据
        rec_add = rec_data[1]  # 接收到的元组(ip, port)
        # 打印数据
        print("%s-->%s" % (rec_msg.decode("gbk"), str(rec_add)))
        continue

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
