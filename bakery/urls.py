from . import views
from django.urls import path
from .views import order_cake

app_name = "bakery"


urlpatterns = [
    path('', views.view_index, name='main_page'),
    path('lk/', views.view_lk, name='lk_page'),
    path('order_cake/', order_cake, name='order_cake'),
]
