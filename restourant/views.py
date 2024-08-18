from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context: dict[str, str] = {
        'title': 'Ресторан 52',
        'content': 'Ресторан мировой кухни 52',
    }
    return render (request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'Ресторан 52 - О нас',
        'content': 'О нас',
        'text_page': 'потом',
    }
    return render (request, 'main/about.html', context)

def product(request):
    return render(request, 'main/product.html')

def catalog(request):
    return render(request, 'main/catalog.html')