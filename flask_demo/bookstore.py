from flask import Flask,redirect,url_for,session,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField ,SubmitField
from wtforms.validators import DataRequired,EqualTo
from  flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

#定义一个表单的模型类
app.config["SECRET_KEY"]="fghthtjetrtrt"
class Config(object):
    #配置sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI="mysql://root:123@127.0.0.1:3306/flaskdmeo"
    #设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS=True

app.config.from_object(Config)

db=SQLAlchemy(app)
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
class AuthorBookForm(FlaskForm):
    author_name=StringField(label=u"作者",validators=[DataRequired(u"作者必填")])
    book_name=StringField(label=u"书籍",validators=[DataRequired(u"书籍必填")])
    submit=SubmitField(label=u"保存")

@app.route("/",methods=["GET","POST"])
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
@app.route("/delete_book")
def deletebook():
    bookid=request.args.get("bookid")

    book=Book.query.get(bookid)

    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))
if __name__ == '__main__':
    app.run()
