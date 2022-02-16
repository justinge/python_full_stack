from flask import Flask,redirect,url_for
from werkzeug.routing import BaseConverter

app=Flask(__name__)

#127.0.0.1/items/123
@app.route("/items/<int:goodsid>")
def goods_detail(goodsid):
    return "goods detail page %s" %goodsid
#127.0.0.1/phone/123
#定义一个自己的转换器
class MobileConverter(BaseConverter):
    def __init__(self,url_map):
        super(MobileConverter,self).__init__(url_map)
        self.regex=r'1[34578]\d{9}'
#将自己的转化器添加到flask的应用中
app.url_map.converters["mobile"]=MobileConverter

class RegexConverter(BaseConverter):
    def __init__(self,url_map,regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex=regex
    def to_python(self, value):
        print("to_python被调用了")  #value是进行正则表达式对路径进行提取时候的参数
        return value
    def to_url(self, value):
        print("to_url方法被调用")
        return value    #使用url_for

app.url_map.converters["re"]=RegexConverter

# @app.route("/send/<mobile:moblie_num>")
# def send_msg(moblie_num):
#     return "send msg %s" %moblie_num

@app.route("/send/<re(r'1[34578]\d{9}'):moblie_num>")
def send_msg(moblie_num):
    return "send msg %s" %moblie_num
@app.route("/index")
def index():
    url=url_for("send_msg",moblie_num="13911111111")
    return redirect(url)
if __name__ == '__main__':
    app.run()
