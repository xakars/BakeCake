# Generated by Django 4.2.3 on 2023-07-30 10:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvetisementUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('link', models.CharField(max_length=20, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Рекламная ссылка',
                'verbose_name_plural': 'Рекламные ссылки',
            },
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_name', models.CharField(default='Кастомный торт', max_length=30, verbose_name='Название торта')),
                ('cake_text', models.CharField(blank=True, max_length=50)),
                ('image', models.CharField(blank=True, max_length=50, verbose_name='Путь к изображению торта')),
            ],
            options={
                'verbose_name': 'Торт',
                'verbose_name_plural': 'Торты',
            },
        ),
        migrations.CreateModel(
            name='CakeBerry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_berry', models.CharField(max_length=50, verbose_name='Ягоды')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Ягода',
                'verbose_name_plural': 'Ягоды',
            },
        ),
        migrations.CreateModel(
            name='CakeDecor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_decor', models.CharField(max_length=50, verbose_name='Декор')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Декор',
                'verbose_name_plural': 'Декор',
            },
        ),
        migrations.CreateModel(
            name='CakeLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Кол-во уровней')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Уровень торта',
                'verbose_name_plural': 'Уровни торта',
            },
        ),
        migrations.CreateModel(
            name='CakeShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.CharField(max_length=50, unique=True, verbose_name='Форма')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Форма торта',
                'verbose_name_plural': 'Формы тортов',
            },
        ),
        migrations.CreateModel(
            name='CakeTopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=50, unique=True, verbose_name='Топпинг')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Топпинг торта',
                'verbose_name_plural': 'Топпинги тортов',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=60, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('OPEN', 'Необработанный'), ('PROGRESSING', 'Готовится'), ('Transit', 'В пути'), ('CLOSED', 'Закрыт')], db_index=True, default='OPEN', max_length=20, verbose_name='Статус заказа')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('registrated_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата регистрации заказа')),
                ('delivery_address', models.CharField(blank=True, max_length=200, verbose_name='Адрес доставки')),
                ('delivery_date', models.DateField(blank=True, db_index=True, null=True, verbose_name='Дата доставки')),
                ('delivery_time', models.TimeField(blank=True, db_index=True, null=True, verbose_name='Время доставки')),
                ('delivery_comments', models.TextField(blank=True, verbose_name='Комментарий для курьера')),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='bakery.cake', verbose_name='Заказанный торт')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='bakery.user', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='cake',
            name='berry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='berries', to='bakery.cakeberry', verbose_name='Ягоды'),
        ),
        migrations.AddField(
            model_name='cake',
            name='decor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='decors', to='bakery.cakedecor', verbose_name='Декор'),
        ),
        migrations.AddField(
            model_name='cake',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='bakery.cakelevel', verbose_name='Кол-во уровней торта'),
        ),
        migrations.AddField(
            model_name='cake',
            name='shape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shapes', to='bakery.cakeshape', verbose_name='Форма торта'),
        ),
        migrations.AddField(
            model_name='cake',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='bakery.caketopping', verbose_name='Топпинг торта'),
        ),
        migrations.CreateModel(
            name='AdvetisementUrlCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('total_clicks', models.IntegerField(verbose_name='Количество')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='url', to='bakery.advetisementurl', verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Количество просмотров',
                'verbose_name_plural': 'Количество просмотров',
            },
        ),
    ]
