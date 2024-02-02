from django.contrib import admin

from .models import Order, ProductInOrder, Status

admin.site.register(Status)
admin.site.register(Order)
admin.site.register(ProductInOrder)
