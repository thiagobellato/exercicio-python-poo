from django.shortcuts import render
from .models import Livro

def home(request):
    return render(request, 'biblioteca/home.html')

def listar_livros(request):
    q = request.GET.get('q', '')
    livros = Livro.objects.filter(titulo__icontains=q)
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros})

def detalhes_livro(request, id):
    livro = Livro.objects.get(id=id)
    return render(request, 'biblioteca/detalhe_livro.html', {'livro': livro})