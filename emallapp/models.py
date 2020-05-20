from django.db import models

# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


