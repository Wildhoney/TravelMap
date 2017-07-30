from django.db import models


class Pinned(models.Model):
    country = models.ForeignKey('api.Country', related_name='country', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    type = models.IntegerField()


class Country(models.Model):
    id = models.AutoField
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=128)
