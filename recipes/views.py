from django.http import HttpResponse
from django.shortcuts import render


def home(request: object) -> HttpResponse:
    return render(request, 'recipes/pages/home.html')


def recipe(request: object, id: int) -> HttpResponse:
    return render(request, 'recipes/pages/recipe_view.html')
