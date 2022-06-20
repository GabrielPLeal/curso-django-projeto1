from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request: object) -> HttpResponse:
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request: object, id: int) -> HttpResponse:
    return render(request, 'recipes/pages/recipe_view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })
