from django.db import models


# Create your models here.


class User(models.Model):
    """
    Поля модели «Клиент»:
    — имя клиента
    — электронная почта клиента
    — номер телефона клиента
    — адрес клиента
    — дата регистрации клиента
    """

    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    adress = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f'ID: {self.pk} Username: {self.name}, email: {self.email},  phone: {self.phone}, address: {self.adress}, '
            f'data_joined: {self.date_joined}')


class Product(models.Model):
    """
    Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Product name: {self.name}, price: {self.price},  description: {self.description}, '
                f'quantity: {self.quantity}')


class Order(models.Model):
    """
    Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа
"""

    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Customer: {self.customer.name}, products: {self.products},  date_ordered: {self.date_ordered}, '
                f'total_price: {self.total_price}')
