# Generated by Django 3.0.3 on 2020-05-22 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emallapp', '0005_payment_nearestloc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='deliveryMode',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='qty',
        ),
    ]
