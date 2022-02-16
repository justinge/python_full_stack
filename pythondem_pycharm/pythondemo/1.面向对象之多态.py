#1.封装 将属性和方法封装到一个类中
#2.继承 实现了代码的重用相同的代码不需要重读的编写
#3.多态 不同的子类对象调用相同的父类方法产生不同的结果
#人和狗玩的案例  不具体的指定哪一种狗 不关心具体是什么狗

class Person(object):
    def __init__(self,name):
        self.name=name
    def game_with_dog(self,dog):
        print("%s和%s在快乐的玩耍"%(self.name,dog.name))
        dog.game()
class Dog(object):
    def __init__(self,name):
        self.name=name
    def game(self):
        print("%s在地上玩耍"%self.name)
class T_dog(Dog):
    def game(self):
        print("%s在平缓的地方玩耍"%self.name)
tdog=T_dog("泰迪")
person=Person("张三")
person.game_with_dog(tdog)

