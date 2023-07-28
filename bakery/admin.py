from django.contrib import admin
from .models import User, Cake, CakeLevel, CakeShape, CakeTopping, CakeBerry, CakeDecor

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    search_fields = ('name', 'email')


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'topping', 'berry', 'decor', 'cake_text')


@admin.register(CakeLevel, CakeShape,  CakeTopping, CakeBerry, CakeDecor)
class CakePartsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price')
    list_editable = ['price']
