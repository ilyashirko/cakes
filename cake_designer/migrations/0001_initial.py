# Generated by Django 4.0.4 on 2022-05-04 12:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.SmallIntegerField(unique=True, verbose_name='Номер в админке')),
                ('title', models.CharField(max_length=30, verbose_name='Ягода')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid1, editable=False, max_length=36, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(36)], verbose_name='uuid')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', verbose_name='Номер телефона')),
                ('mailbox', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.SmallIntegerField(unique=True, verbose_name='Номер в админке')),
                ('title', models.CharField(max_length=30, verbose_name='Украшение')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес доставки')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время доставки')),
                ('comment', models.CharField(max_length=1000, verbose_name='Комментарий для курьера')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.SmallIntegerField(unique=True, verbose_name='Номер в админке')),
                ('title', models.CharField(max_length=30, verbose_name='Форма')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.SmallIntegerField(unique=True, verbose_name='Номер в админке')),
                ('title', models.CharField(max_length=30, verbose_name='Топпинг')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uuid', models.CharField(default=uuid.uuid1, editable=False, max_length=36, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(36)], verbose_name='uuid')),
                ('levels', models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='Количество уровней')),
                ('signature', models.CharField(blank=True, max_length=50, verbose_name='Надпись на торте')),
                ('comment', models.TextField(blank=True, max_length=10000, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Заказ оформлен')),
                ('berries', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='cake_designer.berry', verbose_name='Ягоды')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='cake_designer.customer', verbose_name='Заказчик')),
                ('decoration', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='cake_designer.decoration', verbose_name='Декор')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='cake_designer.form', verbose_name='Форма коржей')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='cake_designer.topping', verbose_name='Топпинг')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='delivery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='cake_designer.delivery', verbose_name='Параметры доставки'),
        ),
    ]
