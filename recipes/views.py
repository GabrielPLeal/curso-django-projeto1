from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
# from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request: object) -> HttpResponse:
    recipes = Recipe.objects.filter(
        is_published=True
        ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request: object, category_id: int) -> HttpResponse:
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    title = f'{recipes[0].category.name} - Category | '
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': title
    })


def recipe(request: object, id: int) -> HttpResponse:
    recipe = get_object_or_404(
        Recipe,
        id=id,
        is_published=True
    )

    return render(request, 'recipes/pages/recipe_view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
