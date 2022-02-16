#__new__创建对象的时候这个方法就会被调用
class Dog(object):
    def __new__(cls, *args, **kwargs):
        print("创建对象分配内存空间")
        #为对象分配内存空间
        instance=super().__new__()
        return instance
    def __init__(self):
        print("狗类被初始化")
dog=Dog()
print(dog)