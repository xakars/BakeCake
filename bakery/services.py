import stripe

from datetime import datetime
from django.core.exceptions import ValidationError
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect

from bakery.models import User, Order, Cake

stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = "http://127.0.0.1:8000/"


def checkout(order, cake_name):
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'rub',
                    'unit_amount': int(order.total_order_price()) * 100,
                    'product_data': {
                        'name': cake_name
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success',
        cancel_url=YOUR_DOMAIN + '/cancel',
    )

    return checkout_session


def register_client(request):
    client_data = {
        'name': request.POST.get('NAME'),
        'phone_number': request.POST.get('PHONE'),
        'email': request.POST.get('EMAIL'),
    }

    client = User.objects.create(**client_data)

    return client


def register_order(request, client, cake, cake_text):
    order_data = {
        'status': 'OPEN',
        'customer': client,
        'cake': cake,
        'delivery_address': request.POST.get('ADDRESS'),
        'delivery_date': datetime.strptime(request.POST.get('DATE'), '%Y-%m-%d').date(),
        'delivery_time': request.POST.get('TIME'),
        'delivery_comments': request.POST.get('DELIVCOMMENTS'),
        'cake_text': cake_text
    }

    order = Order(**order_data)

    return order


def create_order(request, cake_name, cake_data=None):
    cake_text = request.POST.get('WORDS')
    try:
        client = register_client(request)
        client.full_clean()

        if cake_data:
            cake = Cake.objects.create(**cake_data)
            cake.full_clean()
        else:
            cake = Cake.objects.get(cake_name=cake_name)

        order = register_order(request, client, cake, cake_text)
        order.price = order.total_order_price()
        order.save()
        order.full_clean()

        checkout_session = checkout(order, cake_name)
        return redirect(checkout_session.url, code=303)

    except ValidationError as e:
        return JsonResponse({'errors': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'errors': str(e)}, status=400)
