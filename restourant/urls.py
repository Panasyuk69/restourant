
from django.urls import path
from restourant import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]


app_name = 'restourant'