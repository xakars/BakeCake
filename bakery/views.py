from django.db import transaction
from django.shortcuts import render, get_object_or_404

from bakery.models import Cake, CakeLevel, CakeShape, CakeTopping, CakeBerry, CakeDecor
from bakery.services import create_order


@transaction.atomic
def order_cake(request):
    cake_name = 'Кастомный торт'

    level_id = int(request.POST.get('LEVELS'))
    shape_id = int(request.POST.get('FORM'))
    topping_id = int(request.POST.get('TOPPING', 0))
    berry_id = int(request.POST.get('BERRIES', 0))
    decor_id = int(request.POST.get('DECOR', 0))

    level = get_object_or_404(CakeLevel, level=level_id)
    shape = get_object_or_404(CakeShape, id=shape_id)
    topping = get_object_or_404(CakeTopping, id=topping_id) if topping_id else None
    berry = get_object_or_404(CakeBerry, id=berry_id) if berry_id else None
    decor = get_object_or_404(CakeDecor, id=decor_id) if decor_id else None

    cake_data = {
        'level': level,
        'shape': shape,
        'topping': topping,
        'berry': berry,
        'decor': decor,
    }

    return create_order(request, cake_name, cake_data)


@transaction.atomic
def order_cake_from_catalogue(request):
    cake_name = request.POST.get('LEVELS')

    return create_order(request, cake_name)


def view_index(request):
    levels = CakeLevel.objects.all()
    shapes = CakeShape.objects.all()
    toppings = CakeTopping.objects.all()
    berries = CakeBerry.objects.all()
    decors = CakeDecor.objects.all()

    return render(request, template_name='index.html',
                  context={
                      'levels': levels,
                      'shapes': shapes,
                      'toppings': toppings,
                      'berries': berries,
                      'decors': decors
                  })


def view_lk(request):
    return render(request, template_name='lk.html', context={})


def view_cakes_from_catalogue(request):
    cakes = Cake.objects.exclude(cake_name='Кастомный торт')
    return render(request, template_name='cakes.html', context={'cakes': cakes})


def success(request):
    return render(request, template_name='success.html')


def cancel(request):
    return render(request, template_name='cancel.html')
