class  Animal(object):
    @staticmethod
    def run():
        print("狗会跑%s")
#调用静态方法
Animal.run()   #调用静态方法通过类名.方法名