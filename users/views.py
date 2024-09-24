from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
        'title': '52 - Авторизация'
    }

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': '52 - Регистрация'
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': '52 - Профиль'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    context = {
        'title': ''
    }

    return render(request, '', context)