from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Status(models.Model):
    title = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Order status'
        verbose_name_plural = 'Order statuses'


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Order status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class ProductInOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')

    def __str__(self):
        return self.product

    class Meta:
        ordering = ('order', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
