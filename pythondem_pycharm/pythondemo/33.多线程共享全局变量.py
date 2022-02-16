from threading import Thread
import time
g_num=100

def work1():
    global g_num
    for i in  range(3):
        g_num+=1
    print("work1,g_num is %d"%g_num)
def work2():
    global g_num
    print("work2,g_num is %d"%g_num)
print("没有线程之前 g_num is %d"%g_num)
t1=Thread(target=work1)
t1.start()

#延时保证t1线程先把事情做完

time.sleep(1)
t2=Thread(target=work2)
t2.start()
#总结在一个进程内共享线程的全局变量很方便
#缺点就是线程可以对全局变量进行修改导致全局变量混乱