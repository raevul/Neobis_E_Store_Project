from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=800, blank=True, null=True)
    image = models.ImageField("Product image", upload_to="Product image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, verbose_name="category")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="author")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Review(models.Model):
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=40)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'These reviews for {self.product.title}'
