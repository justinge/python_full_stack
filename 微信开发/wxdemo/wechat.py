# coding:utf-8
from flask import Flask,request,abort,render_template
import hashlib
import xmltodict
import time
from urllib.request import urlopen
import json
WX_APPID="wx4b9c93b3c71c5e38"
WX_TOKEN="paojiao"
WX_APPSECRET="e99d0a44d3f18236ae5e6f763eaac23a"

app=Flask(__name__)
@app.route("/wx",methods=["GET","POST"])
def wxchat():
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    if not all([signature,timestamp,nonce]):
        abort(400)
    #微信流程进行计算签名
    li=[WX_TOKEN,timestamp,nonce]
    #排序
    li.sort()
    #进行sha1加密
    tem_str="".join(li).encode("utf8")
    sign=hashlib.sha1(tem_str).hexdigest()
    if signature!=sign:
        #说明请求不是微信发的
        abort(403)
    else:
        #是微信发的
        if request.method=="GET":
            #第一次接入微信验证
            echostr=request.args.get("echostr")
            if not echostr:
                abort(400)
            return echostr
        elif request.method=="POST":
            #微信服务器发消息来了
            xml_data=request.data
            if not xml_data:
                abort(400)
            #对xml数据进行解析
            xml_dict=xmltodict.parse(xml_data)
            xml_dict=xml_dict.get("xml")
            #提取消息类型
            msg_type=xml_dict.get("MsgType")
            content=xml_dict.get("Content")
            if content=="hello":
                rest="python"

            if msg_type=="text":
                #发送的消息文本
                resp_dict={
                    "xml":{
                        "ToUserName":xml_dict.get("FromUserName"),
                        "FromUserName":xml_dict.get("ToUserName"),
                        "CreateTime":int(time.time()),
                        "MsgType":"text",
                        "Content":rest
                    }
                }
            elif msg_type=="image":
                resp_dict = {
                    "xml": {
                        "ToUserName": xml_dict.get("FromUserName"),
                        "FromUserName": xml_dict.get("ToUserName"),
                        "CreateTime": int(time.time()),
                        "MsgType": "image",
                         "Image":{
                             "MediaId":xml_dict.get("MediaId")
                          }

                    }
                }
            else:
                resp_dict = {
                    "xml": {
                        "ToUserName": xml_dict.get("FromUserName"),
                        "FromUserName": xml_dict.get("ToUserName"),
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content":"paojiao python"
                    }
                }
            #字段转换为xml
            resp_xml_str=xmltodict.unparse(resp_dict)
            return  resp_xml_str
@app.route("/acc")
def acc():
    url="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" %(WX_APPID,WX_APPSECRET)
    response=urlopen(url)
    json_str=response.read()
    print(json_str)
    return  json_str

@app.route("/wx/index")
def index():
    code=request.args.get("code")
    if not code:
        return "有code"
    url="https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code" %(WX_APPID,WX_APPSECRET,code)
    response=urlopen(url)
    json_str=response.read()
    resp_dict=json.loads(json_str)
    #提取access_token
    if "errcode" in resp_dict:
        return "获取access token失败"
    access_token=resp_dict.get("access_token")
    open_id=resp_dict.get("openid")
    urls=" https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN" %(access_token,open_id)
    response=urlopen(urls)
    user_json_str = response.read()
    user_resp_dict = json.loads(user_json_str)
    if "errcode" in user_resp_dict:
        return "获取用户信息失败"
    else:
        return render_template("index.html",user=user_resp_dict)
if __name__ == '__main__':
    app.run(port=8000,debug=True)
