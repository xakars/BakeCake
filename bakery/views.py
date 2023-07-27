from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect

from bakery.models import Client, Cake


def order_cake(request):
    client_data = {
        'name': request.POST.get('NAME'),
        'phone_number': request.POST.get('PHONE'),
        'email': request.POST.get('EMAIL'),
        'address': request.POST.get('ADDRESS'),
        'date': request.POST.get('DATE'),
        'time': request.POST.get('TIME'),
        'courier_comment': request.POST.get('DELIVCOMMENTS'),
    }

    try:
        client = Client.objects.create(**client_data)
        client.full_clean()
    except ValidationError as e:
        return JsonResponse({'errors': str(e)}, status=400)

    cake_data = {
        'layers': request.POST.get('LEVELS'),
        'shape': request.POST.get('FORM'),
        'topping': request.POST.get('TOPPING'),
        'berries': request.POST.get('BERRIES'),
        'decor': request.POST.get('DECOR'),
        'lettering': request.POST.get('WORDS'),
        'order_comment': request.POST.get('COMMENTS'),
        'client': client,
    }

    try:
        cake = Cake.objects.create(**cake_data)
        cake.full_clean()
    except ValidationError as e:
        return JsonResponse({'errors': str(e)}, status=400)

    return redirect('payment_page')  # TODO


def view_index(request):
    return render(request, template_name='index.html', context={})


def view_lk(request):
    return render(request, template_name='lk.html', context={})
