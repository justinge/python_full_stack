from flask import Flask,redirect,url_for,session,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField ,SubmitField
from wtforms.validators import DataRequired,EqualTo
from  flask_sqlalchemy import SQLAlchemy

class AuthorBookForm(FlaskForm):
    author_name=StringField(label=u"作者",validators=[DataRequired(u"作者必填")])
    book_name=StringField(label=u"书籍",validators=[DataRequired(u"书籍必填")])
    submit=SubmitField(label=u"保存")