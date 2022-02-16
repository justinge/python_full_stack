from  flask import Flask,render_template
from   flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:123@127.0.0.1:3306/flaskdmeo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SECRET_KEY"]="fghthtjetrtrt"
app.debug=True

db=SQLAlchemy(app)

#在db之后导入蓝图
from  app.admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint,url_prefix="/")


