from django.core.management.base import BaseCommand
from sem_02.models import Product


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        product = Product(name='apple', price=10, description='fruit', quantity=1)
        product.save()
        self.stdout.write(f'{product}')
