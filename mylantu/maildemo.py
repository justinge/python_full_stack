from  flask import Flask
from  flask_mail import Mail,Message

app=Flask(__name__)

#邮件的配置

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='916939772@qq.com', #发送方的邮箱地址
    MAIL_PASSWORD='dofxzdrnjsnfbbii',
)
mail=Mail(app)
@app.route("/")
def index():
    msg=Message("flask test",sender='916939772@qq.com',recipients=['zhang916939772@126.com'])
    msg.body="flask demo message"
    #发送邮件
    mail.send(msg)
    return "sent Succeed"
if __name__ == '__main__':
    app.run()