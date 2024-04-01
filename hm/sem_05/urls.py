from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),  # добавляем пустой путь для перенаправления на список заказов
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('orders/', views.order_list, name='order_list'),
]