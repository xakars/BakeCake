# Generated by Django 4.2.3 on 2023-07-26 12:17

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=30, region=None, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=60, verbose_name='Почта')),
                ('address', models.CharField(max_length=120, verbose_name='Адрес')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('courier_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий для курьера')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_name', models.CharField(default='Кастомный торт', max_length=30, verbose_name='Название торта')),
                ('layers', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], verbose_name='Количество уровней')),
                ('shape', models.CharField(choices=[('Round', 'Круг'), ('Square', 'Квадрат'), ('Rectangle', 'Прямоугольник')], max_length=30, verbose_name='Форма')),
                ('topping', models.CharField(choices=[('Nothing', 'Без'), ('White', 'Белый соус'), ('Caramel', 'Карамельный'), ('Maple', 'Кленовый'), ('Blueberry', 'Черничный'), ('Chocolate', 'Молочный шоколад'), ('Strawberry', 'Клубничный')], max_length=30, verbose_name='Топпинг')),
                ('berries', models.CharField(blank=True, choices=[('Blackberry', 'Ежевика'), ('Raspberry', 'Малина'), ('Blueberry', 'Голубика'), ('Strawberry', 'Клубника')], max_length=30, null=True, verbose_name='Ягоды')),
                ('decor', models.CharField(blank=True, choices=[('Pistachios', 'Фисташки'), ('Meringue', 'Безе'), ('Hazelnut', 'Фундук'), ('Pecan', 'Пекан'), ('Marshmallow', 'Маршмеллоу'), ('Marzipan', 'Марципан')], max_length=30, null=True, verbose_name='Декор')),
                ('lettering', models.CharField(blank=True, max_length=255, null=True, verbose_name='Надпись')),
                ('order_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='Стоимость торта')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Торт',
                'verbose_name_plural': 'Торты',
            },
        ),
    ]
