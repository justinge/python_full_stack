from urllib.request import quote
res=quote("http://ppzxs.natapp1.cc/wx/index")
print(res)

#https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx4b9c93b3c71c5e38&redirect_uri=http%3A//ppzxs.natapp1.cc/wx/index&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect 若提示“该链接无法访问”，请检查参数是否填写错误，是否拥有scope参数对应的授权作用域权限。
