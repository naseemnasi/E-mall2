from django.core.validators import validate_comma_separated_integer_list
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description =  models.CharField(max_length=100)
    description1 = models.CharField(max_length=100,blank=True)
    img_url = models.CharField(max_length=2083)
    link = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class nearestloc(models.Model):
    location = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.location


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
#
# class Login(models.Model):
#     email = models.CharField(max_length=15, unique=True)
#     password = models.CharField(max_length=8)
#
#     def __str__(self):
#         return self.email

class payment(models.Model):
    nearestloc = models.ForeignKey(nearestloc, on_delete=models.CASCADE, )
    # qty = models.IntegerField()
    # deliveryMode = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class product(models.Model):
    c_name = models.ForeignKey(Category, on_delete=models.CASCADE, )
    pname = models.CharField(max_length=255)
    pimage = models.ImageField(null=True,blank=True)
    pdesc = models.CharField(max_length=2083)
    price = models.IntegerField()
    size = models.CharField(max_length=40,blank=True)
    stock = models.IntegerField()
