def input_password():
    pwd=input("输入密码")
    #对密码进行判断
    if len(pwd)>=8:
        return pwd
    #小于8抛出异常
    ex=Exception("密码长度不够")
    #主动抛出异常
    raise  ex

#提示用户输入密码
try:
    print(input_password())
except Exception as  result:
    print(result)