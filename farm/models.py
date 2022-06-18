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


class DashboardCrop(models.Model):
    name = models.CharField(max_length=20)
    cash = models.CharField(max_length=60)
    duration = models.IntegerField()
    price = models.IntegerField()
    soil = models.CharField(max_length=20, default='loam')
    humidity = models.IntegerField(default=0)
    temp = models.IntegerField(default=0)
    published = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard', kwargs={'pk': self.pk})


class DashboardLand(models.Model):
    region = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.region

    def get_absolute_url(self):
        return reverse('dashboard', kwargs={'pk': self.pk})


class Invest(models.Model):
    name = models.IntegerField(default=10)
    contact = models.IntegerField(default=10)
    email = models.IntegerField(default=10)
#     forest_no = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('invest', kwargs={'pk': self.pk})
