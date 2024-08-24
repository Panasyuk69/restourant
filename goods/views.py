from django.shortcuts import render
from goods.models import Products
# Create your views here.

def product(request):
    
    return render(request, 'goods/product.html')

def catalog(request):

    goods = Products.objects.all()

    context = {
        'title': 'Меню',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)