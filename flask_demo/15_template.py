from flask import Flask,render_template
app=Flask(__name__)

@app.route("/index")
def index():
    data={
        "name":"zs",
        "age":22,
         "my_list":[1,2,3,4,5],
        "my_dict":{"home":"xian"},
        "myint":1
    }
    return render_template("home.html",**data)
def list_2_ste(li):
    return li[::2]
app.add_template_filter(list_2_ste,"li2")
if __name__ == '__main__':
    app.run()