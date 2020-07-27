import socket


def main():
    # 创建TCP服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定IP/PORT
    tcp_server_socket.bind(("", 6899))

    # 把套接字设置为listen监听模式
    tcp_server_socket.listen(128)
    print("服务器正在监听.....")

    # 等待客户端的链接accept
    new_client_socket, client_add = tcp_server_socket.accept()
    print("服务器正在等待客户端的链接.....")
    print("%s客户端已链接进来了....." % str(client_add))

    # 接收客户端发来的数据
    rec_data = new_client_socket.recv(1024)
    print(rec_data.decode("gbk"))

    # 回送数据给客户端
    new_client_socket.send("你已经成功登录服务器.....".encode("gbk"))

    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
