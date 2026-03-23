from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Créez une API simple pour gérer une liste de livres en mémoire.

# Routes:
# - `GET /books` - Retourner tous les livres
# - `GET /books/<id>` - Retourner un livre par ID
# - `POST /books` - Ajouter un nouveau livre

books_db = {
    1: {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925
    },
    2: {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960
    },
    3: {
        "id": 3,
        "title": "Python pour les nuls",
        "author": "John Doe",
        "published_year": 2023
}   
}

next_book_id = 4


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({
        "success": True,
        "count": len(books_db),
        "data": list(books_db.values())
    }), 200

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    if id not in books_db:
        return jsonify({
            "success": False,
            "message": "Book not found"
        }), 404
    return jsonify({
        "success": True,
        "data": books_db[id]
    }), 200

@app.route('/books', methods=['POST'])
def add_book():
    global next_book_id
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data or 'published_year' not in data:
        return jsonify({
            "success": False,
            "message": "Missing required fields: title, author, published_year"
        }), 400
    
    new_book = {
        "id": next_book_id,
        "title": data['title'],
        "author": data['author'],
        "published_year": data['published_year']
    }
    books_db[next_book_id] = new_book
    next_book_id += 1
    
    return jsonify({
        "success": True,
        "data": new_book
    }), 201

if __name__ == '__main__':
    print("=" * 60)
    print("Flask Exercise: Simple Book API")
    print("=" * 60)
    app.run(debug=True, port=5000)
