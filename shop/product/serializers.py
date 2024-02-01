from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Product
        fields = '__all__'
