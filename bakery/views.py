from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from bakery.models import User, Order, Cake, CakeLevel, CakeShape, CakeTopping, CakeBerry, CakeDecor


def order_cake(request):
    client_data = {
        'name': request.POST.get('NAME'),
        'phone_number': request.POST.get('PHONE'),
        'email': request.POST.get('EMAIL'),
    }

    try:
        client = User.objects.create(**client_data)
        client.full_clean()

    except ValidationError as e:
        return JsonResponse({'errors': str(e)}, status=400)

    try:
        level = CakeLevel.objects.get(level=int(request.POST.get('LEVELS')))
        shape = CakeShape.objects.get(id=int(request.POST.get('FORM')))
        topping = CakeTopping.objects.get(id=int(request.POST.get('TOPPING'))) if request.POST.get(
            'TOPPING') != '0' else None
        berry = CakeBerry.objects.get(id=int(request.POST.get('BERRIES'))) if request.POST.get('BERRIES') not in (
            '0', None) else None
        decor = CakeDecor.objects.get(id=int(request.POST.get('DECOR'))) if request.POST.get('DECOR') not in (
            '0', None) else None

    except (CakeLevel.DoesNotExist, CakeShape.DoesNotExist, CakeTopping.DoesNotExist, CakeBerry.DoesNotExist,
            CakeDecor.DoesNotExist):
        return JsonResponse({'errors': 'Missing one of the ingredients in db'}, status=400)

    cake_data = {
        'level': level,
        'shape': shape,
        'topping': topping,
        'berry': berry,
        'decor': decor,
        'cake_text': request.POST.get('WORDS'),
    }

    try:
        cake = Cake.objects.create(**cake_data)
        cake.full_clean()

    except ValidationError as e:
        return JsonResponse({'errors': str(e)}, status=400)

    order_data = {
        'status': 'OPEN',
        'customer': client,
        'cake': cake,
        'price': level.price + shape.price + (topping.price if topping else 0) + (berry.price if berry else 0) + (
            decor.price if decor else 0),
        'delivery_address': request.POST.get('ADDRESS'),
        'delivery_date': request.POST.get('DATE'),
        'delivery_time': request.POST.get('TIME'),
        'delivery_comments': request.POST.get('DELIVCOMMENTS'),
    }

    try:
        order = Order.objects.create(**order_data)
        order.full_clean()

    except ValidationError as e:
        return JsonResponse({'errors': str(e)}, status=400)

    return redirect('payment_page')


def view_index(request):
    return render(request, template_name='index.html', context={})


def view_lk(request):
    return render(request, template_name='lk.html', context={})
