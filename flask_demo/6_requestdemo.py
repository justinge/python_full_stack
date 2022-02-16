from flask import Flask,request
app=Flask(__name__)

#127.0.0.1:5000/kw?python&city=xian
@app.route("/index",methods=["GET","POST"])
def index():
    kw=request.args.get("kw")  #url参数的提取
    city=request.args.get("city")
    #提取表单格式的数据
    name=request.form.get("name")
    age=request.form.get("age")
    name_li=request.form.getlist("name")
    print(name_li)
    #如果请求的数据不是表单格式的而是json的格式的
    print("json %s"% request.data)
    return  "hello kw=%s,city=%s,name=%s,age=%s"%(kw,city,name,age)
if __name__ == '__main__':
    app.run()

