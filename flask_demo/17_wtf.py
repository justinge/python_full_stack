from flask import Flask,redirect,url_for,session,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField ,SubmitField
from wtforms.validators import DataRequired,EqualTo
app=Flask(__name__)

#定义一个表单的模型类
app.config["SECRET_KEY"]="fghthtjetrtrt"
class RegisterForm(FlaskForm):
    user_name=StringField(label=u"用户名",validators=[DataRequired(u"用户名不能为空")])
    password=PasswordField(label=u"密码",validators=[DataRequired(u"密码不能为空")])
    password2=PasswordField(label=u"密码",validators=[DataRequired(u"密码不能为空"),EqualTo("password",u"两次密码不一致的")])
    submit=SubmitField(label=u"提交")

@app.route("/regis",methods=["GET","POST"])
def register():
    form=RegisterForm()

    if form.validate_on_submit():
        name=form.user_name.data
        pwd=form.password.data
        pwd2=form.password.data
        print(name,pwd,pwd2)
        session["username"]=name
        return redirect(url_for("index"))
    return render_template("register.html",form=form)
@app.route("/index")
def index():
    u_name=session.get("username")
    return "hello %s"%u_name
if __name__ == '__main__':
    app.run()