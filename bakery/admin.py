from django.contrib import admin

from .models import Client, Cake


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'date')
    search_fields = ('name', 'email')


class CakeAdmin(admin.ModelAdmin):
    list_display = ('cake_name', 'client', 'cost')
    list_filter = ('layers', 'shape', 'topping')


admin.site.register(Client, ClientAdmin)
admin.site.register(Cake, CakeAdmin)
