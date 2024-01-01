from . import db
from flask_login import UserMixin

saved_books = db.Table('saved_books', 
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
                       )


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    subtitle = db.Column(db.String(150))
    author = db.Column(db.String(150))
    genre = db.Column(db.String(150))
    page_count = db.Column(db.Integer)
    cover = db.Column(db.String(500))
    isbn = db.Column(db.String, unique=True)
    date_published = db.Column(db.DateTime)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    read = db.relationship('Book', secondary=saved_books, backref='readers')

