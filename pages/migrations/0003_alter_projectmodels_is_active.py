# Generated by Django 4.2.1 on 2023-05-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_projectmodels_is_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodels',
            name='is_active',
            field=models.BooleanField(default='Not Active'),
        ),
    ]
