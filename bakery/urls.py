from . import views
from django.urls import path


app_name = "bakery"


urlpatterns = [
    path('', views.view_index, name='main_page'),
    path('lk/', views.view_lk, name='lk_page'),
    path('order_cake/', views.order_cake, name='order_cake'),
]
