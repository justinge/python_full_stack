import socket
def main():
    #套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定一个端口号
    localaddr=("",7000)
    udp_socket.bind(localaddr)
    while True:
        #接收数据
        recv_data=udp_socket.recvfrom(1024)
        #接收的数据是元组类型的数据
        redv_msg=recv_data[0]#存储接收的数据
        send_addr=recv_data[1]#存储发送方的信息
        #打印接收到的数据
        print("%s:%s"%(str(send_addr),redv_msg.decode("gbk")))
    udp_socket.close()
if __name__ == '__main__':
    main()