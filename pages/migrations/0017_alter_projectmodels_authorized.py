# Generated by Django 4.2.1 on 2023-05-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_projectmodels_authorized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodels',
            name='authorized',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]