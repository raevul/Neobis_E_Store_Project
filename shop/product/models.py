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
    description = models.TextField(max_length=800, blank=True, null=True)
    image = models.ImageField("Product image", upload_to="Product image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, verbose_name="category", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="author")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
