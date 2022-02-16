from flask import Flask,current_app

#创建一个flask的应用对象
app=Flask(__name__)
#app.config.from_pyfile("config.cfg")

#使用对象来配置参数
class Config(object):
    PAOJIAO="spring"
app.config.from_object(Config)
#视图函数
@app.route("/")
def index():
    print(current_app.config.get("PAOJIAO"))
    #print(current_app.config.get("PAO"))
    return "hello  flask"

if __name__ == '__main__':
    app.run()