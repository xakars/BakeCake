from django.contrib import admin

from .models import Client, Cake
from .models import AdvetisementUrl, AdvetisementUrlCount


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'date')
    search_fields = ('name', 'email')


class CakeAdmin(admin.ModelAdmin):
    list_display = ('cake_name', 'client', 'cost')
    list_filter = ('layers', 'shape', 'topping')


admin.site.register(Client, ClientAdmin)
admin.site.register(Cake, CakeAdmin)


class AdvetisementUrlCountInline(admin.TabularInline):
    model = AdvetisementUrlCount
    extra = 0


@admin.register(AdvetisementUrl)
class AdvetisementUrlAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'link',
    ]
    inlines = [
        AdvetisementUrlCountInline,
    ]
