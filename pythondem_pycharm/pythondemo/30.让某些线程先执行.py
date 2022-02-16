import threading
import time
#没有使用多任务的编程
def run():
    for i in  range(5):
        print("跑步")


def sing():
    for i in  range(5):
        print("唱歌")

def main():
    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=run)
    t1.start()
    time.sleep(1)
    print("11111")
    t2.start()
    time.sleep(1)
    print("2222")
if __name__ == '__main__':
    main()
