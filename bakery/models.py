from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator


class User(models.Model):
    name = models.CharField(
        'Имя',
        max_length=30,
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        region='RU'
    )
    email = models.EmailField(
        'Почта',
        max_length=60,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


class CakeLevel(models.Model):
    level = models.PositiveSmallIntegerField(
        verbose_name='Кол-во уровней',
        unique=True,
        validators=[MinValueValidator(1)]
    )
    price = models.IntegerField(
        verbose_name='Стоимость'
    )

    class Meta:
        verbose_name = 'Уровень торта'
        verbose_name_plural = 'Уровни торта'

    def __str__(self):
        return str(self.level)


class CakeShape(models.Model):
    shape = models.CharField(
        max_length=50,
        verbose_name='Форма',
        unique=True
    )
    price = models.IntegerField(
        verbose_name='Стоимость'
    )

    class Meta:
        verbose_name = 'Форма торта'
        verbose_name_plural = 'Формы тортов'

    def __str__(self):
        return self.shape


class CakeTopping(models.Model):
    topping = models.CharField(
        max_length=50,
        verbose_name='Топпинг',
        unique=True
    )
    price = models.IntegerField(
        verbose_name='Стоимость'
    )

    class Meta:
        verbose_name = 'Топпинг торта'
        verbose_name_plural = 'Топпинги тортов'

    def __str__(self):
        return self.topping


class CakeBerry(models.Model):
    cake_berry = models.CharField(
        max_length=50,
        verbose_name='Ягоды',
    )
    price = models.IntegerField(
        verbose_name='Стоимость'
    )

    class Meta:
        verbose_name = 'Ягода'
        verbose_name_plural = 'Ягоды'

    def __str__(self):
        return self.cake_berry


class CakeDecor(models.Model):
    cake_decor = models.CharField(
        max_length=50,
        verbose_name='Декор'
    )
    price = models.IntegerField(
        verbose_name='Стоимость',
    )

    class Meta:
        verbose_name = 'Декор'
        verbose_name_plural = 'Декор'

    def __str__(self):
        return self.cake_decor


class Cake(models.Model):
    cake_name = models.CharField(
        'Название торта',
        max_length=30,
        default='Кастомный торт'
    )
    level = models.ForeignKey(
        CakeLevel,
        verbose_name='Кол-во уровней торта',
        on_delete=models.CASCADE,
        related_name='levels'
    )
    shape = models.ForeignKey(
        CakeShape,
        verbose_name='Форма торта',
        on_delete=models.CASCADE,
        related_name='shapes'
    )
    topping = models.ForeignKey(
        CakeTopping,
        verbose_name='Топпинг торта',
        on_delete=models.CASCADE,
        related_name='toppings',
    )
    berry = models.ForeignKey(
        CakeBerry,
        verbose_name='Ягоды',
        on_delete=models.CASCADE,
        related_name='berries',
        blank=True,
        null=True
    )
    decor = models.ForeignKey(
        CakeDecor,
        verbose_name='Декор',
        on_delete=models.CASCADE,
        related_name='decors',
        blank=True,
        null=True
    )
    cake_text = models.CharField(
        max_length=50,
        blank=True,
    )
    image = models.CharField(
        'Путь к изображению торта',
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'

    def __str__(self):
        return self.cake_name

    def total_price(self):
        total = self.level.price + self.shape.price + self.topping.price
        if self.berry:
            total += self.berry.price
        if self.decor:
            total += self.decor.price
        return total


class Order(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Необработанный'),
        ('PROGRESSING', 'Готовится'),
        ('Transit', 'В пути'),
        ('CLOSED', 'Закрыт')
    ]
    status = models.CharField(
        'Статус заказа',
        db_index=True,
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )
    customer = models.ForeignKey(
        User,
        verbose_name='Клиент',
        related_name='orders',
        on_delete=models.CASCADE
    )
    cake = models.ForeignKey(
        Cake,
        verbose_name='Заказанный торт',
        related_name='orders',
        on_delete=models.PROTECT,
    )
    price = models.IntegerField(
        verbose_name='Стоимость',
    )
    registrated_at = models.DateTimeField(
        verbose_name='Дата регистрации заказа',
        auto_now_add=True,
        db_index=True,
    )
    delivery_address = models.CharField(
        'Адрес доставки',
        max_length=200,
        blank=True,
    )
    delivery_date = models.DateField(
        'Дата доставки',
        blank=True,
        null=True,
        db_index=True
    )
    delivery_time = models.TimeField(
        'Время доставки',
        blank=True,
        null=True,
        db_index=True
    )
    delivery_comments = models.TextField(
        verbose_name='Комментарий для курьера',
        blank=True
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.cake} {self.customer.name}'
