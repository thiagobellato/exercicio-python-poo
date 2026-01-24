from django.contrib import admin
from django.urls import path
from biblioteca.views import home, listar_livros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('livros/', listar_livros, name='listar_livros'),
]