from django.db import models
from django.contrib.auth.models import AbstractUser


class Country(models.Model):
    id = models.AutoField
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ('code',)


class Pinned(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    type = models.IntegerField()


class User(AbstractUser):
    pins = models.ManyToManyField('Country', through='Pinned')
