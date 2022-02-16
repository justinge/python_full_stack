from flask import Flask,redirect,url_for,session,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField ,SubmitField
from wtforms.validators import DataRequired,EqualTo
from  flask_sqlalchemy import SQLAlchemy
from  . import admin
from app import app,db
from app.admin.forms import AuthorBookForm
from app.models import Author,Book
@admin.route("/",methods=["GET","POST"])
def index():
    form=AuthorBookForm()
    if form.validate_on_submit():
        author_name=form.author_name.data
        book_name=form.book_name.data
        author=Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        book=Book(name=book_name,author_id=author.id)
        db.session.add(book)
        db.session.commit()
    author_li=Author.query.all()
    return render_template("bookstore.html",authors=author_li,form=form)
@admin.route("/delete_book")
def deletebook():
    bookid=request.args.get("bookid")

    book=Book.query.get(bookid)

    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))