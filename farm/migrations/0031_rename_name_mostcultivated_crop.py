# Generated by Django 4.0.5 on 2022-07-06 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0030_alter_mostcultivated_hectares'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mostcultivated',
            old_name='name',
            new_name='crop',
        ),
    ]
