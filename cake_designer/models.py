from pickle import TRUE
import uuid

from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
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
    levels = models.ForeignKey(
        'Level',
        on_delete=models.PROTECT,
        verbose_name="Количество уровней",
        related_name='orders'
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
        related_name='orders',
        null=True
    )
    cost = models.SmallIntegerField("Стоимость", default=None, null=True)
    promo = models.ForeignKey(
        "Promo",
        on_delete=models.SET_NULL,
        default=None,
        verbose_name="Промокод",
        related_name='orders',
        null=True
    )
    promo_cost = models.SmallIntegerField("С учетом скидки", default=None, null=True)
    utm = models.ForeignKey(
        "Utm",
        on_delete=models.PROTECT,
        verbose_name="UTM",
        related_name="orders",
        default=None,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        "Заказ оформлен",
        auto_now_add=True,
        editable=False
    )

    def __str__(self):
        return (f'{self.created_at.date()}: {self.customer} - '
                f'{self.form} ({self.levels})')


class Level(models.Model):
    num = models.SmallIntegerField("Количество", unique=True)
    cost = models.SmallIntegerField("Добавочная стоимость")

    def __str__(self):
        return str(self.num)


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


class Promo(models.Model):
    title = models.CharField("Название", max_length=30)
    number = models.SmallIntegerField("Номинал")
    is_valid = models.BooleanField("Активен")


class Decoration(models.Model):
    num = models.SmallIntegerField("Номер в админке", unique=True)
    title = models.CharField("Украшение", max_length=30)
    cost = models.SmallIntegerField("Добавочная стоимость")

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField("Имя", max_length=50, null=True)
    phonenumber = PhoneNumberField("Номер телефона", region="RU", null=True)
    mailbox = models.EmailField("E-mail", null=True)

    def __str__(self):
        return f'{self.first_name} {self.phonenumber}'


class Delivery(models.Model):
    address = models.CharField("Адрес доставки", max_length=100)
    datetime = models.DateTimeField("Дата и время доставки")
    comment = models.CharField(
        "Комментарий для курьера",
        max_length=1000,
        blank=True
    )
    status = models.BooleanField(default=False)

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
