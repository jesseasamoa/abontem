from django.db import models
from django.urls import reverse
import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django_countries.fields import CountryField

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

    class Meta:
        verbose_name_plural = 'Homepage Signup form'


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

    class Meta:
        verbose_name_plural = 'Investment Requests'


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Management(models.Model):
    service = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    email = models.EmailField(default='farm@abontem.com')
    whatsapp = models.CharField(max_length=10, default='0245003234')

    def __str__(self):
        return self.service

    def get_absolute_url(self):
        return reverse('farm_management', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Farm Management'


class Products(models.Model):
    service = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default='N/A')
    email = models.EmailField(default='farm@abontem.com')
    whatsapp = models.CharField(max_length=10, default='0245003234')

    def __str__(self):
        return self.service

    def get_absolute_url(self):
        return reverse('farm_products', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Farm Products'


class FinancePage(models.Model):
    service = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default='N/A')
    email = models.EmailField(default='farm@abontem.com')
    whatsapp = models.CharField(max_length=10, default='0245003234')

    def __str__(self):
        return self.service

    def get_absolute_url(self):
        return reverse('finance', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Finance Page'


class ContactPage(models.Model):
    country = CountryField(default='Ghana')
    phone = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=800)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact_us', kwargs={'pk', self.pk})

    class Meta:
        verbose_name_plural = 'Contact us'


class MostCultivated(models.Model):
    crop = models.CharField(max_length=20)
    hectares = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Most Cultivated'


