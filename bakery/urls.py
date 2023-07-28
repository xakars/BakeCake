from . import views
from django.urls import path

app_name = "bakery"

urlpatterns = [
    path('', views.view_index, name='main_page'),
    path('lk/', views.view_lk, name='lk_page'),
    path('order_cake/', views.order_cake, name='order_cake'),
    path('cakes/', views.view_cakes_from_catalogue, name='view_cakes_from_catalogue'),
    path('order_cake_from_catalogue/', views.order_cake_from_catalogue, name='order_cake_from_catalogue'),
]
