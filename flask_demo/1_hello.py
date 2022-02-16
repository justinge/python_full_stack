from flask import Flask

#创建一个flask的应用对象
app=Flask(__name__)

#视图函数
@app.route("/")
def index():
    return "hello  flask"

if __name__ == '__main__':
    app.run()