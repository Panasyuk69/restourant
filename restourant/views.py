from django.shortcuts import render
from goods.models import Categories
# Create your views here.

def index(request):
    context = {
        'title': 'Ресторан 52',
        'content': 'Ресторан мировой кухни 52',
    }
    return render(request, 'main/index.html', context) 

def about(request):
    context = {
        'content': 'О нас',
        'text_page': 'бла-бла-бла',
    }
    return render(request, 'main/about.html', context)

