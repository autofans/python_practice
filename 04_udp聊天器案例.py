import socket


def send_msg(udp_socket):
    """发送数据"""
    # 发送
    # 输入对方的ip/port
    des_ip = input("请输入对方的ip:")
    des_port = int(input("请输入对方的port:"))
    send_data = input("请输入要发送的内容：")
    udp_socket.sendto(send_data.encode("gbk"), (des_ip, des_port))


def rec_msg(udp_socket):
    """接收数据"""
    # 接收
    rec_data = udp_socket.recvfrom(1024)
    rec_m = rec_data[0]
    rec_a = rec_data[1]
    print("%s-->%s" % (rec_m.decode("gbk"), rec_a))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定ip/port
    udp_socket.bind(("", 6899))

    # 循环发送/接收数据
    while True:
        print("-----网络调试聊天器-----")
        print("1:发送数据")
        print("2:接收数据")
        print("0:退出系统")
        op = int(input("请输入要操作的功能："))

        if op == 1:
            # 发送数据
            send_msg(udp_socket)

        elif op == 2:
            # 接收数据
            rec_msg(udp_socket)

        elif op == 0:
            # 退出
            break

        else:
            print("输入有误，请重新输入！！！")

    udp_socket.close()


if __name__ == "__main__":
    main()