#异常
#不能确定是否能正确执行代码
# try:
#     num=int(input("输入一个整数"))
# except:
#     print("请输入正确的数字")


#捕获错误类型
# try:
#     num=int(input("输入一个整数"))
#     result=8/num
#     print(result)
# except ZeroDivisionError:
#     print("不能除以0")
# except ValueError:
#     print("输入正确的数字")

#捕获未知的错误
# try:
#     num=int(input("输入一个整数"))
#     result=8/num
#     print(result)
# except ValueError:
#     print("输入正确的数字")
# except Exception as result:
#     print("未知错误%s"%result)