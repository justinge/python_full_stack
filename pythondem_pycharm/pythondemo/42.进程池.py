#当创建的进程不多的时候我们可以使用multiprocessing 创建进程但是如果们进程比较多的时候任务比较大
#我们就需要使用进程池
from multiprocessing import  Pool

import os ,time,random

def worker(msg):
    t_start=time.time()
    print("%s开始执行，进程号为%d"%(msg,os.getpid()))
    #生成一个0-1的浮点数
    time.sleep(random.random()*2)
    t_stop=time.time()
    print(msg,"执行完毕耗时%0.2f"%(t_stop-t_start))
def main():
    po=Pool(3)
    for i in range(0,10):
        po.apply_async(worker,(i,))#每次循环将会用空闲的子进程去调用目标

    print("---start---")
    po.close()#进程池关闭
    po.join()#等待所有子进程执行完成  必须放在 close后面  主进程阻塞等待子进程退出
    print("end")

if __name__ == '__main__':
    main()
