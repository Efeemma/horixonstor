# Generated by Django 4.2.2 on 2023-07-03 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0002_order_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cartitem',
        ),
    ]
