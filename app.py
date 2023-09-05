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

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tokien',
    },
    {
        'id': 2,
        'titulo': 'O Senhor dos Anéis - As Duas Torres',
        'autor': 'J.R.R Tokien',
    },
    {
        'id': 3,
        'titulo': 'O Senhor dos Anéis - O Retorno do Rei',
        'autor': 'J.R.R Tokien',
    }
]
# Consultar(todos)


@app.route('/livros')
def obter_livros():
    return jsonify(livros)


# Consultar(id)
# Editar
# Excluir
app.run(port=5000, host='localhost', debug=True)
