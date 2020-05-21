from django.db import models

# Create your models here.

class nearestloc(models.Model):
    location = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.location

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class payment(models.Model):
    nearestloc = models.ForeignKey(nearestloc,on_delete=models.CASCADE,)
    qty = models.IntegerField()
    deliveryMode = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    def __str__(self):
        return self.name
