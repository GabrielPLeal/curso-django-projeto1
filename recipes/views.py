from django.http import HttpResponse
from django.shortcuts import render


def home(request: object) -> HttpResponse:
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Gabriel Leal',
    })
