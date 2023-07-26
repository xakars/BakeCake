from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    name = models.CharField(
        'Имя',
        max_length=30,
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        max_length=30,
    )
    email = models.EmailField(
        'Почта',
        max_length=60,
    )
    address = models.CharField(
        'Адрес',
        max_length=120,
    )
    date = models.DateField(
        'Дата',
    )
    time = models.TimeField(
        'Время',
    )
    courier_comment = models.TextField(
        'Комментарий для курьера',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Cake(models.Model):
    LAYERS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]
    SHAPE_CHOICES = [
        ('Round', 'Круг'),
        ('Square', 'Квадрат'),
        ('Rectangle', 'Прямоугольник'),
    ]
    TOPPING_CHOICES = [
        ('Nothing', 'Без'),
        ('White', 'Белый соус'),
        ('Caramel', 'Карамельный'),
        ('Maple', 'Кленовый'),
        ('Blueberry', 'Черничный'),
        ('Chocolate', 'Молочный шоколад'),
        ('Strawberry', 'Клубничный'),
    ]
    BERRY_CHOICES = [
        ('Blackberry', 'Ежевика'),
        ('Raspberry', 'Малина'),
        ('Blueberry', 'Голубика'),
        ('Strawberry', 'Клубника'),
    ]
    DECOR_CHOICES = [
        ('Pistachios', 'Фисташки'),
        ('Meringue', 'Безе'),
        ('Hazelnut', 'Фундук'),
        ('Pecan', 'Пекан'),
        ('Marshmallow', 'Маршмеллоу'),
        ('Marzipan', 'Марципан'),
    ]

    cake_name = models.CharField(
        'Название торта',
        max_length=30,
        default='Кастомный торт'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Клиент',
    )
    layers = models.IntegerField(
        'Количество уровней',
        choices=LAYERS_CHOICES
    )
    shape = models.CharField(
        'Форма',
        max_length=30,
        choices=SHAPE_CHOICES
    )
    topping = models.CharField(
        'Топпинг',
        max_length=30,
        choices=TOPPING_CHOICES
    )
    berries = models.CharField(
        'Ягоды',
        max_length=30,
        choices=BERRY_CHOICES,
        blank=True,
        null=True
    )
    decor = models.CharField(
        'Декор',
        max_length=30,
        choices=DECOR_CHOICES,
        blank=True,
        null=True
    )
    lettering = models.CharField(
        'Надпись',
        max_length=255,
        blank=True,
        null=True
    )
    order_comment = models.TextField(
        'Комментарий к заказу',
        blank=True,
        null=True
    )
    cost = models.IntegerField(
        'Стоимость торта',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'
