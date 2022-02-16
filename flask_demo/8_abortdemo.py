from flask import Flask,request,abort,Response

app=Flask(__name__)
@app.route("/login",methods=["POST"])
def login():
    name=request.form.get("name")
    if name!="zs":
        #abort(404)
        resp=Response("login failed")
        abort(resp)
    return "login sucess"
#定义错误处理的方法
@app.errorhandler(404)
def handle_404_err(err):
    return "出现了404的错误错误信息是%s" %err
if __name__ == '__main__':
    app.run()