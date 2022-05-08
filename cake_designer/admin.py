from django.contrib import admin

from .models import (Berry, Customer, Decoration, Delivery, Form, Level, Order,
                     Topping, Utm)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'delivery',
        'customer',
        'utm',
    )


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cost',
    )


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cost',
    )


@admin.register(Berry)  
class BerryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cost',
    )


@admin.register(Decoration)
class DecorationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'cost',
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass


@admin.register(Utm)
class UtmAdmin(admin.ModelAdmin):
    pass


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'cost',
    )
