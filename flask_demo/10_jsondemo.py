from flask import Flask,jsonify
import json

app=Flask(__name__)
@app.route("/index")
def index():
    # data={
    #     "name":"zs",
    #     "age":"27"
    # }
    # json_str=json.dumps(data)
    # return json_str,200,{"Content-Type":"application/json"}

    return jsonify(name="zs",age="34")

if __name__ == '__main__':
    app.run()