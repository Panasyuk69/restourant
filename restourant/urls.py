
from django.urls import path
from restourant import views

app_name = 'restourant'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('catalog/', views.catalog, name='catalog'),
]