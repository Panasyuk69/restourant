from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('product/', views.product, name='product'),
    path('catalog/', views.catalog, name='catalog'),
]

