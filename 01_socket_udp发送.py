import socket


def main():
    # 创建一个UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # 从键盘获取数据
        send_data = input("输入要发送的数据：")
        # 如果输入的数据是exit，则退出程序
        if send_data == "exit":
            break

        # 使用套接字收发数据
        # udp_socket.sendto("要发送的字符串", （"对方的IP", port)）
        # udp_socket.sendto(b"hello", ("192.168.1.110", 8080))
        udp_socket.sendto(send_data.encode("gbk"), ("192.168.1.110", 8080))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
