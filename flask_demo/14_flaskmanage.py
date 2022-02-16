from flask import Flask
from flask_script import Manager

app=Flask(__name__)

#创建一个manager对象
manager=Manager(app)
@app.route("/index")
def index():
    return "index page"

if __name__ == '__main__':
    manager.run()