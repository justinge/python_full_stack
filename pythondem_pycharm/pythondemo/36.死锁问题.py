#现实社会中男女朋友 双方等着对方道歉 但是双方都不开口 凉凉
#线程间共享多个资源的时候如果两个线程分别占用一部分资源并且同时等待对方的资源就会死锁

import threading
import time

class My_thread(threading.Thread):
    def run(self):
        metexA.acquire()
        print(self.name+'do1 up')
        time.sleep(1)
        metexB.acquire()
        print(self.name+'do1 down')
        metexB.release()
        metexA.release()
class My_thread2(threading.Thread):
    def run(self):
        metexB.acquire()
        print(self.name+'do2 up')
        time.sleep(1)
        metexA.acquire()
        print(self.name+'do2 down')
        metexA.release()
        metexB.release()
metexA=threading.Lock()
metexB=threading.Lock()
if __name__ == '__main__':
    t1=My_thread()
    t2=My_thread2()
    t1.start()
    t2.start()