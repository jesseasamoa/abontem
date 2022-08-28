from django.db import models
from django.urls import reverse
import datetime
# from django_countries.fields import CountryField
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser

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
    production = models.CharField(max_length=60)
    duration = models.IntegerField()
    price = models.IntegerField()
    soil = models.CharField(max_length=20, default='loam')
    humidity = models.CharField(max_length=10)
    temp = models.CharField(max_length=10)
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
    whatsapp = models.CharField(max_length=10, default='0553612697')

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
    whatsapp = models.CharField(max_length=10, default='0553612697')

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
    whatsapp = models.CharField(max_length=10, default='0553612697')

    def __str__(self):
        return self.service

    def get_absolute_url(self):
        return reverse('finance', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Finance Page'


class ContactPage(models.Model):
    # country = CountryField(default='Kenya')
    country = models.CharField(max_length=50)
    phone = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__(self):
        return self.phone

    def get_absolute_url(self):
        return reverse('contact_us', kwargs={'pk', self.pk})

    class Meta:
        verbose_name_plural = 'Contact us'


class MostCultivated(models.Model):
    crop = models.CharField(max_length=20, unique=True)
    hectares = models.IntegerField()

    def __str__(self):
        return self.crop

    def get_absolute_url(self):
        return reverse('dashboard', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Most Cultivated'


class PaymentDetails(models.Model):
    channel = models.CharField(max_length=20)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('payments', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Payment Details'





