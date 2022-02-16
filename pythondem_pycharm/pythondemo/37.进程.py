#一个进程是有多个线程组成的
#一个程序运行起来后代码加上用到的资源我们称之为进程他是操作系统分配资源的基本单元
#进程的状态
#新建-->就绪-->运行-->死亡
#       等待
#使用进程实现多任务
import  time
import multiprocessing

def tes1():
    while True:
        print("1111")
        time.sleep(1)
def tes2():
    while True:
        print("2222")
        time.sleep(1)
def main():
    p1=multiprocessing.Process(target=tes1)
    p2 = multiprocessing.Process(target=tes2)
    p1.start()
    p2.start()
if __name__ == '__main__':
    main()

#进程和线程的区别
'''
定义不同 进程是仙童进行资源分配和调度的独立单位
线程是进程的一个实体是cpu调度和分配的基本单位 比进程更小的独立运行的单位

区别 一个程序至少有一个进程一个进程至少有一个线程
线程的划分尺度小于进程多线程程序的并发性高
进程执行过程中拥有独立的内存单元 多个线程是共享内存的

'''