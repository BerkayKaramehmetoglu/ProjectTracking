# Generated by Django 4.2.1 on 2023-05-17 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_projectmodels_add_projectmodels_dont_add_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodels',
            name='dont_add',
        ),
    ]
