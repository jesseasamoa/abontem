# Generated by Django 4.0.5 on 2022-06-21 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0017_weather'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='atmosphere',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='cloud',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='coo',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='temp',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='wind',
        ),
    ]
