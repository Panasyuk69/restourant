from django.urls import path
from goods import views


urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='catalog'),
    path('<slug:category_slug>/<int:page>/', views.catalog, name='catalog'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]


app_name = 'goods'