from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app=Flask(__name__)

class Config(object):
    #配置sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI="mysql://root:123@127.0.0.1:3306/flaskdmeo"
    #设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS=True

app.config.from_object(Config)

#创建工具对象
db=SQLAlchemy(app)

#创建模型类
class Role(db.Model):
    #给数据库表指定名字
    __tablename__="tbl_roles"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32),unique=True)
    users=db.relationship("User",backref="role")
    def __repr__(self):
        #让显示对象时候更加直观
        return "Role object:name=%s"%self.name
class User(db.Model):
    __tablename__="tbl_users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    phone=db.Column(db.String(64),unique=True)
    password=db.Column(db.String(128))
    role_id=db.Column(db.Integer,db.ForeignKey("tbl_roles.id"))
    def __repr__(self):
        #让显示对象时候更加直观
        return "User object:name=%s"%self.name

if __name__ == '__main__':
    #清空数据空中的所有数据
    db.drop_all()
    db.create_all()
    #创建对象
    role1=Role(name="admin")
    db.session.add(role1)
    db.session.commit()
    role2 = Role(name="test")
    db.session.add(role2)
    db.session.commit()
    us1=User(name="zs",phone="123555",password="dfdf",role_id=role1.id)
    us2 = User(name="lisi", phone="12444", password="qw", role_id=role2.id)
    us3 = User(name="chen", phone="12666", password="df", role_id=role1.id)
    us4 = User(name="wang", phone="12888", password="rt", role_id=role2.id)
    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()