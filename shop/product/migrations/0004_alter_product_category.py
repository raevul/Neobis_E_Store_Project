# Generated by Django 5.0.1 on 2024-02-02 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='product.category', verbose_name='category'),
        ),
    ]