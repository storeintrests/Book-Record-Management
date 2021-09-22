from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Applier(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField(max_length=100)
    email = models.EmailField(max_length=100)
    intro = models.TextField(default='')
    position = models.TextField(default='')
    expect = models.IntegerField(max_length=100)
    passed = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.fname} {self.lname}(status: {self.passed})'


class BRMuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nickname
