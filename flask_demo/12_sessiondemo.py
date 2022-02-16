from  flask import Flask,session,current_app

app=Flask(__name__)

#flask要使用session的时候我们需要用到秘钥字符串
app.config["SECRET_KEY"]="fdfsdghhtrttrtt"

@app.route("/login")
def login():
    session["name"]="zs"
    session["mobile"]="13999999999"
    return "login sucess"

@app.route("/index")
def index():
    name=session.get("name")
    return "hello %s" %name
if __name__ == '__main__':
    app.run()

