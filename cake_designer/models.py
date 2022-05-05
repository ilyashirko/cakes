import uuid

from django.core.validators import (MaxValueValidator, MinLengthValidator,
                                    MinValueValidator)
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    uuid = models.CharField(
        "uuid",
        unique=True,
        default=uuid.uuid1,
        max_length=36,
        validators=[MinLengthValidator(36)],
        primary_key=True,
        editable=False
    )
    levels = models.SmallIntegerField(
        'Количество уровней',
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(3)
        ]
    )
    form = models.ForeignKey(
        'Form',
        on_delete=models.PROTECT,
        verbose_name="Форма коржей",
        related_name='orders'
    )
    topping = models.ForeignKey(
        'Topping',
        on_delete=models.PROTECT,
        verbose_name="Топпинг",
        related_name='orders'
    )
    berries = models.ForeignKey(
        'Berry',
        on_delete=models.PROTECT,
        verbose_name="Ягоды",
        related_name='orders',
        null=True,
        blank=True
    )
    decoration = models.ForeignKey(
        'Decoration',
        on_delete=models.PROTECT,
        verbose_name="Декор",
        related_name='orders',
        null=True,
        blank=True
    )
    signature = models.CharField(
        "Надпись на торте",
        max_length=50,
        blank=True
    )
    comment = models.TextField(
        "Комментарий",
        max_length=10000,
        blank=True
    )
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.PROTECT,
        verbose_name="Заказчик",
        related_name='orders'
    )
    delivery = models.ForeignKey(
        "Delivery",
        on_delete=models.SET_NULL,
        verbose_name="Параметры доставки",
        related_name='customer',
        null=True
    )
    utm = models.ForeignKey(
        "Utm",
        on_delete=models.PROTECT,
        verbose_name="UTM",
        related_name="orders",
        default=None,
        null=True
    )
    created_at = models.DateTimeField(
        "Заказ оформлен",
        auto_now_add=True,
        editable=False
    )

    def __str__(self):
        return (f'{self.created_at.date()}: {self.customer} - '
                f'{self.form} ({self.levels})')


class Form(models.Model):
    num = models.SmallIntegerField("Номер в админке", unique=True)
    title = models.CharField("Форма", max_length=30)
    cost = models.SmallIntegerField("Добавочная стоимость")

    def __str__(self):
        return self.title


class Topping(models.Model):
    num = models.SmallIntegerField("Номер в админке", unique=True)
    title = models.CharField("Топпинг", max_length=30)
    cost = models.SmallIntegerField("Добавочная стоимость")

    def __str__(self):
        return self.title


class Berry(models.Model):
    num = models.SmallIntegerField("Номер в админке", unique=True)
    title = models.CharField("Ягода", max_length=30)
    cost = models.SmallIntegerField("Добавочная стоимость")

    def __str__(self):
        return self.title


class Decoration(models.Model):
    num = models.SmallIntegerField("Номер в админке", unique=True)
    title = models.CharField("Украшение", max_length=30)
    cost = models.SmallIntegerField("Добавочная стоимость")

    def __str__(self):
        return self.title
        

class Customer(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    phonenumber = PhoneNumberField("Номер телефона", region="RU")
    mailbox = models.EmailField("E-mail")
    
    def __str__(self):
        return self.first_name


class Delivery(models.Model):
    address = models.CharField("Адрес доставки", max_length=100)
    datetime = models.DateTimeField("Дата и время доставки")
    comment = models.CharField("Комментарий для курьера", max_length=1000)

    def __str__(self):
        return f'{self.address}  |  {self.datetime}'


class Utm(models.Model):
    source = models.CharField("Which site sent the traffic", max_length=100)
    medium = models.CharField("Type of link", max_length=100)
    campaign = models.CharField("Аdvertising company", max_length=100)
    content = models.CharField(
        "Content",
        max_length=100,
        default=None,
        null=True
    )
    term = models.CharField(
        "Searching terms",
        max_length=100,
        default=None,
        null=True
    )

    def __str__(self):
        return f"{self.source} | {self.campaign}"