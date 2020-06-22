# Generated by Django 3.0.3 on 2020-06-22 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emallapp', '0016_auto_20200622_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=255)),
                ('pimage', models.ImageField(blank=True, null=True, upload_to='')),
                ('pdesc', models.CharField(max_length=2083)),
                ('price', models.IntegerField()),
                ('size', models.CharField(blank=True, max_length=40)),
                ('stock', models.IntegerField()),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emallapp.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='addproduct',
        ),
    ]