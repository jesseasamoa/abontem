# Generated by Django 4.0.5 on 2022-06-16 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0004_rename_crop_name_crop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='published',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
