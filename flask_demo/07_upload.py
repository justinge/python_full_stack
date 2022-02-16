from flask import Flask,request

app=Flask(__name__)

@app.route("/upload",methods=["POST"])
def upload():
    file_obj=request.files.get("pic")
    if file_obj is None:
        return "未上传文件"

    file_obj.save("./test.jpg")
    return "上传成功"

if __name__ == '__main__':
    app.run()