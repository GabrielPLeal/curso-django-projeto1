from django.http import HttpResponse
from django.shortcuts import render


def home(request: object) -> HttpResponse:
    return render(request, 'recipes/home.html', context={
        'name': 'Gabriel Leal',
    })


def sobre(request: object) -> HttpResponse:
    return HttpResponse('sobre')


def contato(request: object) -> HttpResponse:
    return render(request, 'temp.html')
