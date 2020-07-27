import socket
import threading


def send_msg(udp_socket, des_ip, des_port):
    """发送数据"""
    while True:
        send_data = input("请输入要发送的内容：")
        udp_socket.sendto(send_data.encode("gbk"), (des_ip, des_port))


def rec_msg(udp_socket):
    """接收数据"""
    while True:
        rec_data = udp_socket.recvfrom(1024)
        rec_ss = rec_data[0]
        rec_add = rec_data[1]
        print("%s-->%s" % (rec_ss.decode("gbk"), str(rec_add)))


def main():
    # 创建UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地IP/PORT
    udp_socket.bind(("", 7890))

    # 获取对方的IP/PORT
    des_ip = input("请输入对方的IP:")
    des_port = int(input("请输入对方的PORT:"))

    # 创建2个线程分别执行发送和接收功能
    t_send = threading.Thread(target=send_msg, args=(udp_socket, des_ip, des_port))
    t_rec = threading.Thread(target=rec_msg, args=(udp_socket,))

    t_send.start()
    t_rec.start()


if __name__ == "__main__":
    main()
