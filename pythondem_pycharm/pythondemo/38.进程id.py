import multiprocessing
import os
import time
def game():
    while True:
        print("子进程pid=%d父进程pid=%d"%(os.getpid(),os.getppid()))
        time.sleep(1)
def main():
    print("主进程pid=%d父进程pid=%d" % (os.getpid(), os.getppid()))
    p=multiprocessing.Process(target=game())
    p.start()
if __name__ == '__main__':
    main()