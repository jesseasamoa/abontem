# Generated by Django 4.0.5 on 2022-06-21 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0011_finance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Finance',
            new_name='Management',
        ),
        migrations.AlterModelOptions(
            name='management',
            options={'verbose_name_plural': 'Farm Management'},
        ),
        migrations.RenameField(
            model_name='management',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='management',
            old_name='title',
            new_name='service',
        ),
    ]
