from django.http import HttpResponse
from django.shortcuts import render
# from utils.recipes.factory import make_recipe
from .models import Recipe
from django.http import HttpResponseNotFound


def home(request: object) -> HttpResponse:
    recipes = Recipe.objects.filter(
        is_published=True
        ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request: object, category_id: int) -> HttpResponse:
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
        ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })


def recipe(request: object, id: int) -> HttpResponse:
    recipe = Recipe.objects.filter(
        id=id,
        is_published=True
        ).first()

    if recipe:
        return render(request, 'recipes/pages/recipe_view.html', context={
            'recipe': recipe,
            'is_detail_page': True
        })
    else:
        return HttpResponseNotFound()
