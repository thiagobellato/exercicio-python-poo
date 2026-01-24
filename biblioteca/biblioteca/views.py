from django.shortcuts import render
from .models import Livro

def home(request):
    return render(request, 'biblioteca/home.html')

def listar_livros(request):
    query = request.GET.get('q')
    if query:
        livros = Livro.objects.filter(titulo__icontains=query)
    else:
        livros = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros})