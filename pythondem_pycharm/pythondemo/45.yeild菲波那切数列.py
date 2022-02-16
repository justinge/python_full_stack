def fib(n):
    current=0
    a,b=0,1
    while current<n:
        c=a
        a,b=b,a+b
        current+=1
        yield c
    return "ok"
ff=fib(5)
for f in ff:
    print(f)

#总结 yield关键字作用
   # 保存当前运行状态的断点的作用
   #yield表达式后面的值作为返回值返回 此时就是 return