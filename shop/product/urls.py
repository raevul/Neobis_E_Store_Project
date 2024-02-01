from django.urls import path

from .views import ProductsListAPIView, ProductDetailAPIView

app_name = 'product'

urlpatterns = [
    path('products/', ProductsListAPIView.as_view(), name='products'),
    path('product_detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail')
]
