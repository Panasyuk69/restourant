from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Главная страница - HOME',
    }
    return render (request, 'main/index.html', context)

def about(request):
    return render (request, 'main/about.html')