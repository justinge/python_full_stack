#什么是协程 是python中另一种实现多任务的方式，只不过比线程更小的执行单元自带cpu上线文
#通俗的说在一个线程中的某个函数可以在任何地方保存当前函数的一些临时变量信息然后切换到另一个函数中执行
#是有函数做的 切换的次数和什么时候切换使我们程序员决定的

#线程切换比较消耗性能  而且 协程只是单纯的操作cpu上下文   所以一秒钟切换上百万次都能抗住
import time
def work1():
    while True:
        print("--work1--")
        yield
        time.sleep(0.5)
def work2():
    while True:
        print("--work2--")
        yield
        time.sleep(0.5)
def main():
    w1=work1()
    w2=work2()
    while True:
        next(w1)
        next(w2)
if __name__ == '__main__':
    main()