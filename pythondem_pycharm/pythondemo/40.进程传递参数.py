import multiprocessing
import os
import time
def game(a,b,c,*args,**kwargs):
    while True:
        print(a)
        print(b)
        print(c)
        print(args)
        print(kwargs)

def main():
    print("主进程pid=%d父进程pid=%d" % (os.getpid(), os.getppid()))
    p=multiprocessing.Process(target=game,args=(1,2,3,4,5,6,7),kwargs={"aa":11})
    p.start()
if __name__ == '__main__':
    main()