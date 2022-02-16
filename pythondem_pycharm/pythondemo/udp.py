import socket
def main():
    #创建一个socket套接字  Udp
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #使用套接字发送数据
    input_str="你好".encode("gbk")
    udp_socket.sendto(input_str,("192.168.0.101",6000))
    #关闭套接字
    udp_socket.close()
if __name__=="__main__":
    main()