#list tuple str等类型数据 for in循环语法从其中依次拿到数据进行使用我们把这种
#过程称之为遍历也叫迭代
'''
如何判断一个对象是否可以迭代  isinstance(list,Iterable)

 可迭代对象的本质
 什么是迭代器
  我们在分析对象是否可以被迭代的过程中发现没迭代一次都会返回对象的下一条数据一直向后读取数据知道迭代了
  所有数据结束后有一个“人”在这个过程中记录每次访问了几条数据以便进行迭代时都可以返回下一条数据
  这个“人”我们称为迭代器 iterator
  可迭代对象通过__iter__方法提供了迭代器
    iter()  next()

    通过分析我们发现 next()函数其实是调用迭代器对象的__next__方法  python2中next()
    如果我们自己要构造一个迭代器我们就必须要实现__next__方法 __iter__

    实现了__next__ __iter__的方法的对象就是迭代器
'''
#自己实现一个可以迭代的对象
class My_iter(object):
    def __init__(self):
        self.names=list()
        self.current_num=0
    def add(self,name):
        self.names.append(name)
    def __iter__(self):
        return  self
    def __next__(self):
        if self.current_num<len(self.names):
            ret=self.names[self.current_num]
            self.current_num+=1
            return ret
        else:
            raise StopIteration
it=My_iter()
it.add("zs")
it.add("lisi")
it.add("www")
for name in it:
    print(name)


