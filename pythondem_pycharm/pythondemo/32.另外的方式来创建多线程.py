#threading 我们可以定义一个新类继承threading.Thread模块重写run方法
import threading
import time
class My_thead(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print("我是%s-@-%d"%(self.name,i))
def main():
    for i in range(5):
        t=My_thead()
        t.start()
if __name__ == '__main__':
    main()