import socket


def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取服务器IP/PORT
    ser_ip = input("请输入服务器IP：")
    ser_port = int(input("请输入服务器的PORT："))

    # 链接服务器
    tcp_socket.connect((ser_ip, ser_port))

    # 获取要下载的文件名
    file_name = input("请输入要下载的文件名：")

    # 将文件名发送给服务器
    tcp_socket.send(file_name.encode("gbk"))

    # 接收服务器传输回来的数据
    rec_data = tcp_socket.recv(1024)

    # 保存传送回来的数据到文件中
    if rec_data:
        with open("[NEW]"+file_name, "wb") as f:
            f.write(rec_data)

    # 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()