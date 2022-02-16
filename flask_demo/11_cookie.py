from flask import Flask,make_response,request

app=Flask(__name__)
@app.route("/cookie")
def set_cookie():
    resp=make_response("success")
    #resp.set_cookie("paojiao","python")#浏览器一旦关闭cookie就没了
    #resp.set_cookie("paojiao","python",max_age=60)
    resp.headers["Set-Cookie"]="paojiao=java; Expires=Wed, 26-Jun-2019 15:04:56 GMT; Max-Age=360; Path=/"
    return resp

@app.route("/get_cookie")
def get_cookie():
    co=request.cookies.get("paojiao")
    return co

@app.route("/de_cookie")
def de_cookie():
    resp=make_response("del success")
    resp.delete_cookie("paojiao")
    return resp
if __name__ == '__main__':
    app.run()