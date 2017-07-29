from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ('name',)