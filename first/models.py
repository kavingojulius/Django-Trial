from django.db import models
from django.forms import ModelForm

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    number = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Items'






