from rest_framework.generics import ListAPIView
from djoser.permissions import CurrentUserOrAdmin

from .models import ProductInOrder, Order
from .serializers import ProductInOrderSerializer, OrderSerializer
from .permissions import IsOwnerPermissions


class ProductInOrderAPIView(ListAPIView):
    queryset = ProductInOrder.objects.all()
    serializer_class = ProductInOrderSerializer
    permission_classes = [IsOwnerPermissions, CurrentUserOrAdmin]


class OrderAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerPermissions, CurrentUserOrAdmin]
