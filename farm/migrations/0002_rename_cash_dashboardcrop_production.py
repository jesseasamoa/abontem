# Generated by Django 4.0.5 on 2022-07-22 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboardcrop',
            old_name='cash',
            new_name='production',
        ),
    ]
