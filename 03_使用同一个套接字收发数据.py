import socket


def main():
    # 创建UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 输入对方的ip/port
    des_ip = input("请输入对方的ip：")
    des_port = int(input("请输入对方的port:"))

    # 从键盘输入数据
    send_data = input("请输入要发送的数据：")

    # 发送数据
    udp_socket.sendto(send_data.encode("gbk"), (des_ip, des_port))

    # 接收数据
    rec_data = udp_socket.recvfrom(1024)
    rec_msg = rec_data[0]
    rec_add = rec_data[1]
    print("%s-->%s" % (rec_msg.decode("gbk"), rec_add))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
