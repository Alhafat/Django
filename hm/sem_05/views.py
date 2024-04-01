from django.shortcuts import render
from .models import Customer, Product, Order


def customer_detail(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'customer_detail.html', {'customer': customer, 'orders': orders})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
