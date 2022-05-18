# Generated by Django 4.0.4 on 2022-05-18 16:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake_designer', '0008_order_payment_id_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.SmallIntegerField(default=3000, null=True, validators=[django.core.validators.MinLengthValidator(0)], verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, editable=False, max_length=36, validators=[django.core.validators.MinLengthValidator(36)], verbose_name='Номер оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='promo',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='cake_designer.promo', verbose_name='Промокод'),
        ),
        migrations.AlterField(
            model_name='order',
            name='promo_cost',
            field=models.SmallIntegerField(default=3000, null=True, validators=[django.core.validators.MinLengthValidator(0)], verbose_name='С учетом скидки'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='number',
            field=models.SmallIntegerField(validators=[django.core.validators.MinLengthValidator(0)], verbose_name='Номинал'),
        ),
    ]
