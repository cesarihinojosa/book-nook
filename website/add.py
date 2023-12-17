from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import requests


add = Blueprint('add', __name__)

@add.route('/add', methods=['GET', 'POST'])
@login_required
def add_book():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        books = search(query)

    return render_template("add.html", books=books)

def search(query):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    response_data = response.json()
    print(response_data["items"][0]["volumeInfo"]["title"])
    return response_data["items"]