# Generated by Django 3.0.3 on 2020-06-22 15:53

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('emallapp', '0011_addproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='size',
            field=models.CharField(blank=True, max_length=40, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
