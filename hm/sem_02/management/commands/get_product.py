from django.core.management.base import BaseCommand
from sem_02.models import Product


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('description', type=str, help='product description')

    def handle(self, *args, **kwargs):
        description = kwargs['description']
        product = Product.objects.get(description=description)
        self.stdout.write(f'{product}')
