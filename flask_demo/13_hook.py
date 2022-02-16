from flask import Flask,request,url_for

app=Flask(__name__)

@app.route("/index")
def index():
    print("index被执行")
    a=1/0
    return "index page"
@app.route("/hi")
def hi():
    print("hi被执行")
    return "hi page"
#在第一次请求之前执行
@app.before_first_request
def before_first_request():
    print("before_first_request被执行")
@app.before_request  #每次请求之前都被执行
def before_request():
    print("before_request被执行")
@app.after_request          #在每次请求视图函数处理之后被执行前提是视图函数没有出现异常
def after_request(response):
    print("after_request被执行")
    return response
@app.teardown_request  #在每次请求视图函数处理之后被执行无论视图函数是否出现异常都会被执行工作在非调试模式
def teardown_request(response):
    path=request.path
    if path==url_for("index"):
        print("index视图")
    elif path==url_for("hi"):
        print("hi视图")
    print(" teardown_request被执行")
    return response
if __name__ == '__main__':
    app.run()

