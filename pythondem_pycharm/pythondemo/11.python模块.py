#python导入模块
# import 测试模块1
# 测试模块1.say_hello()
# dog=测试模块1.Dog()
# print(dog)

#导入模块取别名

# import 测试模块1 as ce
# ce.say_hello()
# dog=ce.Dog()
# print(dog)

#第三种方式
# from  测试模块2 import Cat
# from  测试模块2 import  say_hello as say
#
# say()
# cat=Cat()
# print(cat)

#第四种方式
from 测试模块2 import *

say_hello()
cat=Cat()
print(cat)