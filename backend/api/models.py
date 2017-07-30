from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.ManyToManyField('api.Country', through='api.Pinned')


class Pinned(models.Model):
    user = models.ForeignKey('api.User', related_name='auth_user', on_delete=models.CASCADE)
    country = models.ForeignKey('api.Country', related_name='api_country', on_delete=models.CASCADE)
    type = models.IntegerField()


class Country(models.Model):
    id = models.AutoField
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ('code',)
