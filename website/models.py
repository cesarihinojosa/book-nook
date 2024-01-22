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
    category = db.Column(db.String(15))
    page_count = db.Column(db.Integer)
    cover = db.Column(db.String(500))

    def __init__(self, title, subtitle, author, category, page_count, cover):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.category = category
        self.page_count = page_count
        self.cover = cover
        
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    read = db.relationship('Book', secondary=saved_books, backref='readers')

