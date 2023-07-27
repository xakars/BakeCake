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
        ('1', 'Круг'),
        ('2', 'Квадрат'),
        ('3', 'Прямоугольник'),
    ]
    TOPPING_CHOICES = [
        ('1', 'Без'),
        ('2', 'Белый соус'),
        ('3', 'Карамельный'),
        ('4', 'Кленовый'),
        ('5', 'Черничный'),
        ('6', 'Молочный шоколад'),
        ('7', 'Клубничный'),
    ]
    BERRY_CHOICES = [
        ('1', 'Ежевика'),
        ('2', 'Малина'),
        ('3', 'Голубика'),
        ('4', 'Клубника'),
    ]
    DECOR_CHOICES = [
        ('1', 'Фисташки'),
        ('2', 'Безе'),
        ('3', 'Фундук'),
        ('4', 'Пекан'),
        ('5', 'Маршмеллоу'),
        ('6', 'Марципан'),
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
