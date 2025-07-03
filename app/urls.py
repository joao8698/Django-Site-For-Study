# Importa a função path para definir as rotas da aplicação
from django.urls import path

# Importa as views do próprio app para associar às URLs
from . import views

# Define um namespace para o app, útil para usar em templates e URLs reversas
app_name = 'app'

# Lista de padrões de URLs da aplicação
urlpatterns = [
    # Rota para a página inicial do app, que chama a view 'home_app'
    # URL: /
    # Nome da URL: 'app:Home'
    path('', views.home_app, name='Home'),

    # Rota dinâmica para exibir um post individual com base no ID
    # URL: /posts/1/, /posts/2/, etc.
    # 'post_id' será passado como argumento para a view 'post'
    # Nome da URL: 'app:posts'
    path('posts/<int:post_id>/', views.post, name='posts'),
]