#send唤醒可以向断点传入一个附件数据

def gen():
    i=0
    while i<5:
        temp=yield i
        print(temp)
        i+=1