from rest_framework.generics import ListCreateAPIView
from djoser.permissions import CurrentUserOrAdminOrReadOnly

from .models import ProductInOrder, Order
from .serializers import ProductInOrderSerializer, OrderSerializer
from .permissions import IsOwnerPermissions


class ProductInOrderAPIView(ListCreateAPIView):
    queryset = ProductInOrder.objects.all()
    serializer_class = ProductInOrderSerializer
    permission_classes = [IsOwnerPermissions, CurrentUserOrAdminOrReadOnly]


class OrderAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerPermissions, CurrentUserOrAdminOrReadOnly]
