from django.shortcuts import render

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
    'eda': {
        'мука, кг': 1,
        'вода, л': 1,
    },
    # можете добавить свои рецепты ;)
}

MAX_SERVING = 6


def home_page(request):
    context = {
        'recipes': DATA.keys(),
        'range': [i + 1 for i in range(MAX_SERVING)]
    }
    return render(request, 'calculator/index.html', context)


def recipe_page(request, dish_name):
    if request.GET.get('servings'):
        number = int(request.GET.get('servings'))
    else:
        number = 1
    context = {
        'dish_name': dish_name,
        'servings': number,
        'ingredients': {ing: number * DATA[dish_name][ing] for ing in DATA[dish_name]}
    }
    return render(request, 'calculator/recipe.html', context)


