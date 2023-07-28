from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from bakery.models import User, Cake


def view_index(request):
    return render(request, template_name='index.html', context={})


def view_lk(request):
    return render(request, template_name='lk.html', context={})
