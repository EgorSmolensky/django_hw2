from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def get_ingredients(request, dish):
    servings = int(request.GET.get('servings', 1))
    if dish in DATA:
        ingredients = {ingr: val * servings for ingr, val in DATA[dish].items()}
    else:
        ingredients = {}
    context = {
        'recipe': ingredients
                }
    return render(request, 'calculator/index.html', context)


def home_view(request):
    return HttpResponse("Укажите блюдо в адресной строке")
