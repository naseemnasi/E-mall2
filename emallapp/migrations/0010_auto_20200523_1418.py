# Generated by Django 3.0.3 on 2020-05-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emallapp', '0009_category_description1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description1',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
