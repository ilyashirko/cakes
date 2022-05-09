# Generated by Django 4.0.4 on 2022-05-09 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake_designer', '0005_customer_user_alter_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='comment',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Комментарий для курьера'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='cake_designer.delivery', verbose_name='Параметры доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='utm',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='cake_designer.utm', verbose_name='UTM'),
        ),
    ]
