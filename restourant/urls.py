
from django.urls import path
from restourant import views

app_name = 'restourant'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('goods/catalog.html', views.catalog, name='catalog'),
    path('goods/product.html', views.product, name='product'),
]