from flask import Blueprint, render_template, request, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Book
import requests
import json

add = Blueprint('add', __name__)

@add.route('/add', methods=['GET', 'POST'])
@login_required
def search_books():
    books = ''
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            response_data = search(query)
            books = initialize_book_list(10)
            books = assign_values_to_books(books, response_data)
            return render_template("add.html", books=books)
        else:
            pass
    else:
        pass
    return render_template("add.html")

def search(query):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    return response.json()

def initialize_book_list(size):
    books= []
    for i in range(size):
        books.append({"title": "title unavailable", 
                      "subtitle": "subtitle unavailable" ,
                      "authors": "authors unavailable", 
                      "category": "category unavailable", 
                      "pageCount": 0, 
                      "imageLinks": {
                          "smallThumbnail": url_for('static', filename='images/no-image.jpg'), 
                          "thumbnail": url_for('static', filename='images/no-image.jpg')
                          }
                    })
    return books

def assign_values_to_books(books, response_data):

    for i in range(len(books)):
    
        if "volumeInfo" in response_data["items"][i]:
            books[i]["title"] = if_this_in_that("title", response_data["items"][i]["volumeInfo"], books[i]["title"])
            books[i]["subtitle"] = if_this_in_that("subtitle", response_data["items"][i]["volumeInfo"], books[i]["subtitle"])
            books[i]["authors"] = if_this_in_that("authors", response_data["items"][i]["volumeInfo"], books[i]["authors"])
            books[i]["category"] = if_this_in_that("categories", response_data["items"][i]["volumeInfo"], books[i]["category"])
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
    
@add.route('/add-book', methods=['POST'])
@login_required
def add_book():
    data = json.loads(request.data)
    print(data["book"]["authors"])
    #book = Book(data["book"]["title"], data["book"][""])
    return jsonify({})
    
