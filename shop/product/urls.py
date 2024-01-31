from django.urls import path

from .views import ProductsListAPIView

app_name = 'product'

urlpatterns = [
    path('products/', ProductsListAPIView.as_view(), name='products'),
]
