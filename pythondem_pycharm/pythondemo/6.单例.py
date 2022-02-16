class Dog(object):
    #单例就是在内存中只有一个实例
    instance=None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:  #判断是否是空对象
            cls.instance=super().__new__(cls) #如果是空对象我们就为第一个对象分配内存空间
        return cls.instance
dog1=Dog()
dog2=Dog()
print(id(dog1))
print(id(dog2))



