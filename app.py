"""
    API - É um lugar para disponibilizar recursos e/ou funcionalidades.
    1. Objetivo - Criar uma api que disponibiliza a consulta, criação e edição e exclusão de livros
    2. URL Base - localhost
    3. Endpoints(Rotas) - 
        -localhost/livros(GET)
        -localhost/livros/criar(POST)
        -localhost/livros/id(PUT)
        -localhost/livros/id(DELETE)
    4. Quais recursos - Livros
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'O Senhor dos Anéis - A Sociedade do Anel',
        'author': 'J.R.R Tokien',
    },
    {
        'id': 2,
        'title': 'O Senhor dos Anéis - As Duas Torres',
        'author': 'J.R.R Tokien',
    },
    {
        'id': 3,
        'title': 'O Senhor dos Anéis - O Retorno do Rei',
        'author': 'J.R.R Tokien',
    }
]

# Consultar(todos)


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Criar livro


@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book)


# Consultar(id)
@app.route('/books/<int:id>', methods=['GET'])
def get_books_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


# Editar
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    book_edited = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(book_edited)
            return jsonify(books[index])


# Excluir
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]

    return jsonify(books)


app.run(port=5000, host='localhost', debug=True)
