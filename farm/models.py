from django.db import models
from django.urls import reverse
import datetime

# Create your models here.


class FrontForm(models.Model):
    first_name = models.CharField(max_length=20)
    contact = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('dashbaord', kwargs={'pk': self.pk})


class Crop(models.Model):
    name = models.CharField(max_length=20)
    cash = models.IntegerField()
    duration = models.IntegerField()
    price = models.IntegerField()
    soil = models.CharField(max_length=10)
    temp = models.IntegerField()
    published = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard', kwargs={'pk': self.pk})


