from django.urls import path

from .views import ProductInOrderAPIView, OrderAPIView

urlpatterns = [
    path('order/', OrderAPIView.as_view(), name='order'),
    path('product_order/', ProductInOrderAPIView.as_view(), name='product in order'),
]
