from  flask import Flask,Response,make_response
app=Flask(__name__)
@app.route("/index")
def index():
    #return "index page",200,[("pp","java"),("city","xian")]
    #return "index page", 200, {"name":"zs","age":22}
    resp=make_response("page index")
    resp.status="200"
    resp.headers["city"]="xian"
    return resp
if __name__ == '__main__':
    app.run()