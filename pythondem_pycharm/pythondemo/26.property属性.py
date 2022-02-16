#一种用起来像是使用的实例属性一样的特殊属性可以对应于某个方法
# class Goods:
#     @property
#     def size(self):
#         return 100
# obj=Goods()
# print(obj.size)
#分页
# class Pager:
#     def __init__(self,current_page):
#         self.current_page=current_page
#         #设置每页显示10
#         self.per_items=10
#     @property
#     def start(self):
#         val=(self.current_page-1)*self.per_items
#         return  val
#
#     @property
#     def end(self):
#         val = self.current_page* self.per_items
#         return val
# p=Pager(1)
# p.start
#p.end

# class Goods:
#     @property
#     def price(self):
#         print(" @property")
#     @price.setter
#     def price(self,value):
#         print("@price.setter")
#     @price.getter
#     def price(self):
#         print("@price.getter")
#
#     @price.deleter
#     def price(self):
#         print("@price.deleter")
# obj=Goods()
# obj.price
# obj.price=122
# del obj.price

# class Animal(object):
#     def __init__(self):
#         self.__name="zs"
#     def getAnimalname(self):
#         return self.__name
#     def setAnimalname(self,value):
#         if isinstance(value,str):
#             self.__name=value
#         else:
#             print("设置的数据的类型不对")
# ani=Animal()
# ani.setAnimalname("狗")
# print(ani.getAnimalname())

class Animal(object):
    def __init__(self):
        self.__name="zs"
    @property
    def animal(self):
        return self.__name
    @animal.getter
    def animal(self):
        return self.__name
    @animal.setter
    def animal(self,value):
        if isinstance(value,str):
            self.__name=value
        else:
            print("设置的数据的类型不对")
ani=Animal()
ani.animal="狗"
print(ani.animal)