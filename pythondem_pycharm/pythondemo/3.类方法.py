class Tool(object):
    count=0    #使用赋值语句定义类属性记录所有工具对象的数量
    #类方法
    @classmethod
    def show_toolcount(cls):
        print("工具对象总数%d"%cls.count)
    def __init__(self,name):
        self.name=name
        #类属性值加1
        Tool.count+=1
#创建对象
tool=Tool("钳子")
tool1=Tool("钳子1")
tool2=Tool("钳子2")
print(Tool.show_toolcount())
