from rest_framework import serializers

from .models import Order, ProductInOrder


class ProductInOrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductInOrder
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    name = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = '__all__'
