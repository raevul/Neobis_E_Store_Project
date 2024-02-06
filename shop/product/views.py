from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from djoser.permissions import CurrentUserOrAdminOrReadOnly
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from .permissions import IsOwnerOrReadOnly


class ProductsListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, CurrentUserOrAdminOrReadOnly]


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

