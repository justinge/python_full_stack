# def m1():
#     f=open("output.txt","w")
#     f.write("python啊啊啊啊")
#     f.close()
# m1()
#存在问题如果在调用write的过程中出现了异常那么后续的代码就无法执行资源就会一直被占用
# def m2():
#     f=open("output.txt","w")
#     try:
#         f.write("python啊啊啊啊")
#     except IOError:
#         print("io err")
#     finally:
#         f.close()
# m2()
#这种写法就是代码不够简洁

# def m3():
#     with open("output.txt","w") as f:
#         f.write("ssssssss")
# m3()     #系统自动关闭的

#什么是上线文
#app点击一个按钮跳转到新的界面也要保存那个屏幕过来的信息 防止你点击返回的时候能够正确的调回
#上线文管理器
#任何实现了__enter__() __exit__()的方法的对象都可以称之为上线文管理器 上线文管理器对象可以使用
#with关键字 file显然已经实现了

#实现上线文管理器的另外的方式
#python提供了contextmanger装饰器简化了上线文的实现方式 通过yeild将函数分割为两个部分  yeild之前的语句
#在__enter__ 之后的语句在 __exit__执行
from contextlib import contextmanager
@contextmanager
def my_test(path,mode):
    f=open(path,mode)
    yield f
    f.close()