#生成器是一种特殊的迭代器比迭代器简单
# L=(x*2 for x in  range(5))
# print(L)
# next(L)
# 自己创建一个生成器
#菲波那切数列   1 1 2 3 5
class Fibiter(object):
    def __init__(self,n):
        self.n=n
        #current用来保存当前数列的第几个数
        self.current=0
        #数列中第一个数0
        self.num1=0
        #用来保存前一个数初始值为数列中的第二个数
        self.num2=1

    def __next__(self):
        if self.current<self.n:
            num=self.num1
            self.num1,self.num2=self.num2,self.num1+self.num2
            self.current+=1
            return num
        else:
            raise StopIteration
    def __iter__(self):
        return self
fi=Fibiter(10)
for f in fi:
    print(f)