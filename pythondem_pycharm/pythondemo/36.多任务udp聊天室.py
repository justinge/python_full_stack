#必须有发送数据和接收数据的功能
#命令窗口  1.发送消息 2.接收消息 0 退出系统
import socket
import threading
def send_msg(udp_socket):
    #对方ip
    dest_ip=input("输入对方的ip:")
    dest_port=int(input("输入对方端口号:"))
    send_data=input("输入要发送的信息")
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))
def recv_msg(udp_socket):
    recv_data=udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]),recv_data[0].decode("gbk")))

def main():
    #创建socket套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定信息
    udp_socket.bind(("",7000))

    while True:
        print("**欢迎来到聊天室**")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出系统")
        op=input("请输入功能")
        if op=="1":
            #发送
            send_msg(udp_socket)
        elif op=="2":
            t = threading.Thread(target=recv_msg, args=(udp_socket,))
            t.start()
            #recv_msg(udp_socket)
        elif op=="0":
            break
        else:
            print("输入有误")
if __name__ == '__main__':
    main()