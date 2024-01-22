from flask import Blueprint, render_template, request, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Book
from . import db
import requests
import json

add = Blueprint('add', __name__)
RESPONSE_DATA = []

@add.route('/add', methods=['GET', 'POST'])
@login_required
def search_add():
    return render_template("add.html")

@add.route('/add_book', methods=['POST'])
@login_required
def add_book():
    book_id = request.form.get('id')
    book = get_book_from_id(book_id)
    print(book_id)
    print(book)
    return render_template("add.html")

def get_book_from_id(id):
    for i in range(0, len(RESPONSE_DATA)):
        if id == RESPONSE_DATA['items'][i]['id']:
            return RESPONSE_DATA['items'][i]
    return []

@add.route('/handle_search', methods=['POST'])
@login_required
def handle_search():
    query = request.form.get('query')
    if query:
        global RESPONSE_DATA
        RESPONSE_DATA = search(query)
        filtered_data = filter_data(RESPONSE_DATA)
        return render_template("add.html", books=filtered_data)
    else:
        return render_template("add.html")
    
def filter_data(data):
    filtered_data = initialize_default_list(data)
    filtered_data = assign_values(data, filtered_data)
    return filtered_data

def initialize_default_list(data):
    filtered_data = []
    for i in range(0, len(data['items'])):
        filtered_data.append({
            "id": None,
            "thumbnail": url_for('static', filename='images/no-image.jpg')})
    return filtered_data

def assign_values(data, filtered_data):
    for i in range(0, len(filtered_data)):
        if 'id' in data['items'][i]:
            filtered_data[i]['id'] = data['items'][i]['id']
            if 'thumbnail' in data['items'][i]['volumeInfo']['imageLinks']:
                filtered_data[i]['thumbnail'] = data['items'][i]['volumeInfo']['imageLinks']['thumbnail'] + "&fife=w480-h690"
        else:
            del filtered_data[i]
    return filtered_data
    
@add.route('/handle_add', methods=['POST'])
@login_required
def handle_add():
    book = request.form.get('book')
    book = "'" + book + "'"
    book = json.loads(book)
    print(book)
    print("in handle add")
    return render_template("add.html")

def search(query):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    return response.json()

# def initialize_book_list(size):
#     books= []
#     for i in range(size):
#         books.append({"title": "title unavailable",
#                       "subtitle": None,
#                       "authors": "authors unavailable", 
#                       "category": "category unavailable", 
#                       "pageCount": 0, 
#                       "imageLinks": {
#                           "smallThumbnail": url_for('static', filename='images/no-image.jpg'), 
#                           "thumbnail": url_for('static', filename='images/no-image.jpg')
#                           }
#                     })
#     return books

# def assign_values_to_books(books, response_data):

#     for i in range(len(books)):
    
#         if "volumeInfo" in response_data["items"][i]:
#             books[i]["title"] = if_this_in_that("title", response_data["items"][i]["volumeInfo"], books[i]["title"])
#             books[i]["subtitle"] = if_this_in_that("subtitle", response_data["items"][i]["volumeInfo"], books[i]["subtitle"])
#             books[i]["authors"] = if_this_in_that("authors", response_data["items"][i]["volumeInfo"], books[i]["authors"])
#             books[i]["category"] = if_this_in_that("categories", response_data["items"][i]["volumeInfo"], books[i]["category"])
#             books[i]["pageCount"] = if_this_in_that("pageCount", response_data["items"][i]["volumeInfo"], books[i]["pageCount"])

#             if "imageLinks" in response_data["items"][i]["volumeInfo"]:
#                 books[i]["imageLinks"]["smallThumbnail"] = if_this_in_that("smallThumbnail", response_data["items"][i]["volumeInfo"]["imageLinks"], books[i]["imageLinks"]["smallThumbnail"])
#                 books[i]["imageLinks"]["thumbnail"] = if_this_in_that("thumbnail", response_data["items"][i]["volumeInfo"]["imageLinks"], books[i]["imageLinks"]["thumbnail"])
#                 books[i]["imageLinks"]["thumbnail"] += "&fife=w480-h690" #allows picture to be clear
#             else:
#                 pass
#         else:
#             pass

#     return books

# def if_this_in_that(this, that, default):
#     if this in that:
#         return that[this]
#     else:
#        return default
    
