from django.contrib import admin

from .models import Order, ProductInOrder, Status


class ProductInOrderInLine(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInOrderInLine]


admin.site.register(Status)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder)
