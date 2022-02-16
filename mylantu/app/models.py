from flask import Flask,redirect,url_for,session,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField ,SubmitField
from wtforms.validators import DataRequired,EqualTo
from  flask_sqlalchemy import SQLAlchemy
from  app import db
#定义模型
class Author(db.Model):
    __tablename__="tb_authors"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32),unique=True)
    books=db.relationship("Book",backref="author")
class Book(db.Model):
    __tablename__ = "tb_books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    author_id=db.Column(db.Integer,db.ForeignKey("tb_authors.id"))