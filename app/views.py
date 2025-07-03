# Importa a função 'render' do Django para renderizar templates com contexto
from django.shortcuts import render

from typing import Any
from django.http import HttpRequest, Http404

# Importa a lista de posts do módulo 'data' dentro do app
from app.data import posts

# ------------------------------
# VIEW para a página inicial
# ------------------------------

def home_app(request):
    # Define o contexto que será passado para o template
    context = {
        'title': 'Site Teste',  # Título da página
        'posts': posts,         # Lista de posts (importada de data.py)
    }

    # Renderiza o template 'app/texto.html' com o contexto acima
    return render(request, 'app/texto.html', context)


# ------------------------------
# VIEW para uma página de post único
# ------------------------------

def post(request: HttpRequest, post_id: int):
    # Inicializa a variável que irá armazenar o post encontrado
    found_post: dict[str, Any] | None = None

    # Percorre todos os posts procurando o que tem o id igual ao passado na URL
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break  # Para o loop assim que encontrar o post

    if found_post is None:
        raise Http404('Post nao existe!')

    # Define o contexto com o post encontrado
    context = {
        'title': found_post['title'],
        'post': found_post,
    }

    # Renderiza o template 'partials/post.html' com o post específico
    return render(request, 'partials/post.html', context)
