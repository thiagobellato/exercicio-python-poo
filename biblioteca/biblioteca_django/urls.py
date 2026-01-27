from django.contrib import admin
from django.urls import path
from biblioteca.views import home, listar_livros, detalhes_livro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('livros/', listar_livros, name='listar_livros'),
    path('livro/<int:id>/', detalhes_livro, name='detalhes_livro'),  # NOVA
]