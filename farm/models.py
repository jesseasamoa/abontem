from django.db import models
from django.urls import reverse

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



