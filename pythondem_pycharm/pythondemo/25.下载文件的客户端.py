#客户端

import socket

def main():
    #创建tcp套接字
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #链接服务器
    server_ip=input("请输入要链接的服务器ip:")
    server_port=int(input("请输入服务器的port"))
    server_addr=(server_ip,server_port)
    tcp_socket.connect(server_addr)
    #获取下载文件的文件名
    download_file_name=input("输入下载的文件的名字:")
    #将文件名发送到服务器
    tcp_socket.send(download_file_name.encode("utf-8"))
    #接收文件中的数据
    recv_data=tcp_socket.recv(1024)
    if recv_data:
        #将接收到的数据保存到文件中
        with open("[新]"+download_file_name,"wb") as  f:
            f.write(recv_data)
    tcp_socket.close()
if __name__ == '__main__':
    main()