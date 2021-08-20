from django.shortcuts import render


def home(request):
    return render(request, 'twitter/newsfeed.html')


def register(request):
    return render(request, 'twitter/register.html')


def profile(request):

    return render(request, 'twitter/profile.html')


def editar(request):
    return render(request, 'twitter/editar.html')
