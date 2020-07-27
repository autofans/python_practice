import socket


def main():
    # 创建TCP套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定IP/PORT
    tcp_server_socket.bind(("", 8876))

    # 把套接字设置为监听状态listen
    tcp_server_socket.listen(128)
    print("服务器正在监听.....")

    while True:  # 循环多次调用accept，为多个客户端服务
        # 等待客户端链接accept
        new_client_socket, client_add = tcp_server_socket.accept()
        print("%s客户端已经链接进来....." % str(client_add))

        while True:  # 为同一个客户端服务多次
            # 接收客户端发来的数据
            rec_data = new_client_socket.recv(1024)
            print(rec_data.decode("gbk"))

            if rec_data:
                # 回送数据给客户端
                new_client_socket.send("你已经成功登录服务器.....".encode("gbk"))
            else:
                break

        # 关闭套接字
        new_client_socket.close()
        continue

    tcp_server_socket.close()


if __name__ == "__main__":
    main()