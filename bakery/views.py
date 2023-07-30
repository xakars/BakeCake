from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from bakery.models import User, Order, Cake, CakeLevel, CakeShape, CakeTopping, CakeBerry, CakeDecor
import stripe


stripe.api_key=settings.STRIPE_SECRET_KEY
YOUR_DOMAIN="http://127.0.0.1:8000/"


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
        topping = CakeTopping.objects.get(id=int(request.POST.get('TOPPING'))) if request.POST.get('TOPPING') not in (
            '0', None) else None
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
        'price': level.price + shape.price + topping.price + (berry.price if berry else 0) + (
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


    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': order_data.get('price') * 100,
                        'product_data': {
                            'name': 'Торт', #TODO подтянуть имя торта??
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


def order_cake_from_catalogue(request):
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

    cake_name = request.POST.get('LEVELS')

    try:
        existing_cake = Cake.objects.get(cake_name=cake_name)

    except Cake.DoesNotExist:
        return JsonResponse({'errors': 'Missing this cake in db'}, status=400)

    order_data = {
        'status': 'OPEN',
        'customer': client,
        'cake': existing_cake,
        'price': existing_cake.level.price + existing_cake.shape.price + existing_cake.topping.price +
                 (existing_cake.berry.price if existing_cake.berry else 0) +
                 (existing_cake.decor.price if existing_cake.decor else 0),
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


    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': order_data.get('price') * 100,
                        'product_data': {
                            'name': cake_name
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


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
