from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user
import requests

add = Blueprint('add', __name__)

@add.route('/add', methods=['GET', 'POST'])
@login_required
def search_books():
    books = ''
    if request.method == 'POST':
        query = request.form.get('query')
        response_data = search(query)
        books = initialize_book_list(10)
        books = assign_values_to_books(books, response_data)
    return render_template("add.html", books=books)

def search(query):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    return response.json()

def initialize_book_list(size):
    books= []
    for i in range(size):
        books.append({"title": "title unavailable", "authors": "authors unavailable", "description": "description unavailable", "pageCount": 0, "imageLinks": {"smallThumbnail": url_for('static', filename='images/no-image.jpg'), "thumbnail": url_for('static', filename='images/no-image.jpg')}})
    return books

def assign_values_to_books(books, response_data):

    for i in range(len(books)):
    
        if "volumeInfo" in response_data["items"][i]:
            books[i]["title"] = if_this_in_that("title", response_data["items"][i]["volumeInfo"], books[i]["title"])
            books[i]["authors"] = if_this_in_that("authors", response_data["items"][i]["volumeInfo"], books[i]["authors"])
            books[i]["description"] = if_this_in_that("description", response_data["items"][i]["volumeInfo"], books[i]["description"])
            books[i]["pageCount"] = if_this_in_that("pageCount", response_data["items"][i]["volumeInfo"], books[i]["pageCount"])

            if "imageLinks" in response_data["items"][i]["volumeInfo"]:
                books[i]["imageLinks"]["smallThumbnail"] = if_this_in_that("smallThumbnail", response_data["items"][i]["volumeInfo"]["imageLinks"], books[i]["imageLinks"]["smallThumbnail"])
                books[i]["imageLinks"]["thumbnail"] = if_this_in_that("thumbnail", response_data["items"][i]["volumeInfo"]["imageLinks"], books[i]["imageLinks"]["thumbnail"])
                books[i]["imageLinks"]["thumbnail"] += "&fife=w480-h690" #allows picture to be clear
            else:
                pass
        else:
            pass

    return books

def if_this_in_that(this, that, default):
    if this in that:
        return that[this]
    else:
        return default