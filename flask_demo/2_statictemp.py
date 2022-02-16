from flask import Flask

#创建一个flask的应用对象
app=Flask(__name__,
          static_url_path="/pp",
          static_folder="static",
          template_folder="templates",)   #没有配置这个选项 那么前缀默认就是 static

#视图函数
@app.route("/")
def index():
    return "hello  flask"

if __name__ == '__main__':
    app.run()