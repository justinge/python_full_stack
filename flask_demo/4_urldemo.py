from  flask import Flask,url_for,redirect

app=Flask(__name__)
@app.route("/index")
def index():
    return "hello flask"
@app.route("/post_only",methods=["GET","POST"])
def post_only():
    return "post page"
@app.route("/login")
def login():
    url=url_for("index")
    return  redirect(url)
@app.route("/h1")
@app.route("/h2")
def hi():
    return "hi page"
if __name__ == '__main__':
    #查看flask中的整个路由信息
    print(app.url_map)
    app.run()