# Generated by Django 4.0.4 on 2022-05-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake_designer', '0003_alter_order_levels'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.SmallIntegerField(default=None, null=True, verbose_name='Стоимость'),
        ),
    ]
