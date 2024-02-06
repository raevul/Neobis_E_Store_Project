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
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
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
    quantity = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order by {self.user.username} on {self.product.title}'

    class Meta:
        ordering = ('order', )
        verbose_name = 'Product in order'
        verbose_name_plural = 'Products in order'
