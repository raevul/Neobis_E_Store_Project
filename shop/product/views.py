from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializerHard
from .permissions import IsOwnerOrReadOnly


class ProductsListAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        try:
            products = Product.objects.all()
        except Exception as e:
            return Response({'data': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['product_id'])
        except Product.DoesNotExist:
            return Response({'data': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['product_id'])
        except Product.DoesNotExist:
            return Response({'data': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializerHard(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            text = serializer.data.get('text')
            Review.objects.create(username=username, text=text, product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['product_id'])
        except Product.DoesNotExist:
            return Response({'data': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"data": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['product_id'])
        except Product.DoesNotExist:
            return Response({'data': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'data': 'Successfully deleted'}, status=status.HTTP_200_OK)
