# Generated by Django 4.2.1 on 2023-05-19 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_alter_projectmodels_authorized'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodels',
            name='authorized',
        ),
    ]