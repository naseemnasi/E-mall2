# Generated by Django 3.0.3 on 2020-05-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emallapp', '0006_auto_20200522_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
