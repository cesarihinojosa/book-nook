from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import requests


add = Blueprint('add', __name__)

@add.route('/add', methods=['GET', 'POST'])
@login_required
def add_book():
    books = ''
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        books = search(query)
        assign_values(books)

    return render_template("add.html", books=books)

def search(query):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    response_data = response.json()
    return response_data["items"]

def assign_values(data):
    books = []
    for i in range(0, 10):
        book = []
        if "imageLinks" in data[i]["volumeInfo"]:
            print("image found")
        else:
            print("no image found")
            

