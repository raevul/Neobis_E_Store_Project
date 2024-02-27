from rest_framework import serializers

from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'username', 'text']


class ReviewSerializerHard(serializers.Serializer):
    username = serializers.CharField(max_length=40, required=True)
    text = serializers.CharField(max_length=500, required=True, min_length=1)


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'image', 'category', 'author', 'reviews']
