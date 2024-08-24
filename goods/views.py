from django.shortcuts import render

# Create your views here.

def product(request):
    
    return render(request, 'goods/product.html')

def catalog(request):
    context = {
        'name': 'name',
        'desription ': 'desription ',
        'price': 'price',
    }
    return render(request, 'goods/catalog.html', context)