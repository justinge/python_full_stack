from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/rexs",methods=["POST","GET"])
def rexs():
    text=""
    if request.method=="POST":
        text=request.form.get("text")
    return  render_template("rexs.html",text=text)

if __name__ == '__main__':
    app.run()