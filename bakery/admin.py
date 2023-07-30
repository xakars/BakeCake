from django.contrib import admin
from .models import User, Order, Cake, CakeLevel, CakeShape, CakeTopping, CakeBerry, CakeDecor


from .models import AdvetisementUrl, AdvetisementUrlCount


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'date')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    search_fields = ('name', 'email')


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('cake_name', 'topping', 'berry', 'decor', 'cake_text')



@admin.register(CakeLevel, CakeShape, CakeTopping, CakeBerry, CakeDecor)

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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
    'status', 'customer', 'cake', 'price', 'registrated_at', 'delivery_address', 'delivery_date', 'delivery_time')
    search_fields = ('status', 'customer__name', 'cake__cake_name')
    readonly_fields = ('cake_details',)

    def cake_details(self, obj):
        return f'Уровни: {obj.cake.level}, Форма: {obj.cake.shape}, Топпинг: {obj.cake.topping}, Ягоды: {obj.cake.berry}, Декор: {obj.cake.decor}, Надпись: {obj.cake.cake_text}'

    cake_details.short_description = 'Детали заказанного торта'
