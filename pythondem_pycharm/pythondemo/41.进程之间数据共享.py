import multiprocessing
'''
一个进程向queue中写入数据，另外一个进程从队列取数据
通过队列完成之后需要配合的进程数据共享

'''

def download_web(q):
    data=[1,2,3,4]
    #向队列写数据
    for temp in data:
        q.put(temp)
    print("下载到队列中了")
def dely_data(q):
    #数据处理
    waitting_data=list()
    #从队列中获取数据
    while True:
        data=q.get()
        waitting_data.append(data)
        if q.empty():
            break
    print(waitting_data)
def main():
    q=multiprocessing.Queue()
    #创建多个进程
    p1=multiprocessing.Process(target=download_web,args=(q,))
    p2=multiprocessing.Process(target=dely_data,args=(q,))
    p1.start()
    p2.start()
if __name__ == '__main__':
    main()