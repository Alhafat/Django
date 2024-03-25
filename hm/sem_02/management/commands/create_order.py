from django.core.management.base import  BaseCommand
from sem_02.models import User
from sem_02.models import Order
from sem_02.models import Product


class Command(BaseCommand):
    help = "Create order"

    def handle(self, *args, **kwargs):
        User_id = kwargs.get('id')
        Product_id: list = kwargs.get('id')

        user = User.objects.filter(pk=User_id).first()

        order = Order(customer=user)
        total_price = 0
        for i in range(0, len(Product_id)):
            product = Product.objects.filter(pk=Product_id[i]).first()
            total_price += float(product.price)
            order.total_price = total_price
            order.save()
            order.products.add(product)
