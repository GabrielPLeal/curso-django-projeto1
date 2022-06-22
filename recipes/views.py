from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe


def home(request: object) -> HttpResponse:
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request: object, category_id: int) -> HttpResponse:
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request: object, id: int) -> HttpResponse:
    return render(request, 'recipes/pages/recipe_view.html', context={
        'recipe': Recipe.objects.filter(id=id).first(),
        'is_detail_page': True
    })
