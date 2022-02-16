#线程的概念     多个任务可以同时执行

#threading模块就是一个线程模块对线程进行了包装很方便我们使用
import threading
import time
#没有使用多任务的编程
def run():
    for i in  range(5):
        print("跑步")
        time.sleep(1)

def sing():
    for i in  range(5):
        print("唱歌")
        time.sleep(1)
def main():
    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=run)
    t1.start()
    t2.start()
    print(threading.enumerate())
if __name__ == '__main__':
    main()
