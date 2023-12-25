from django.http import HttpResponse
from django.shortcuts import render
import copy

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

}
def omlet(request):
    servings = int(request.GET.get("servings", 1))
    context = {}
    context['omlet'] = copy.deepcopy(DATA['omlet'])
    for key in context['omlet']:
        context['omlet'][key] = context['omlet'][key] * servings
    print()
    return render(request, 'omlet.html', context)

def pasta(request):
    servings = int(request.GET.get("servings", 1))
    context = {}
    context['pasta'] = copy.deepcopy(DATA['pasta'])
    for key in context['pasta']:
        context['pasta'][key] = context['pasta'][key] * servings
    print()
    return render(request, 'pasta.html', context)

def buter(request):
    servings = int(request.GET.get("servings", 1))
    context = {}
    context['buter'] = copy.deepcopy(DATA['buter'])
    for key in context['buter']:
        context['buter'][key] = context['buter'][key] * servings
    print()
    return render(request, 'buter.html', context)