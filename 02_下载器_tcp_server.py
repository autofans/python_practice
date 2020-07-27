import socket


def send_file_2_client(new_client_socket):
    # 接收客户端发来的数据
    file_name = new_client_socket.recv(1024).decode("gbk")

    file_content = None
    # 打开这个文件读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有找到要下载的文件")

    # 回送数据给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定IP/PORT
    tcp_server_socket.bind(("", 7890))

    # 把套接字设为listen监听
    tcp_server_socket.listen(128)

    # 等待客户端链接accept
    new_client_socket, client_add = tcp_server_socket.accept()

    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()