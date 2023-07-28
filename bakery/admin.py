from django.contrib import admin
from .models import User, Cake, CakeLevel, CakeShape, CakeTopping, CakeBerry, CakeDecor

from .models import AdvetisementUrl, AdvetisementUrlCount


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'date')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    search_fields = ('name', 'email')


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'topping', 'berry', 'decor', 'cake_text')


class AdvetisementUrlCountInline(admin.TabularInline):
    model = AdvetisementUrlCount
    extra = 0
    readonly_fields = [
        'date',
        'total_clicks',
    ]


@admin.register(AdvetisementUrl)
class AdvetisementUrlAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'link',
    ]
    inlines = [
        AdvetisementUrlCountInline,
    ]


@admin.register(CakeLevel, CakeShape,  CakeTopping, CakeBerry, CakeDecor)
class CakePartsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price')
    list_editable = ['price']
