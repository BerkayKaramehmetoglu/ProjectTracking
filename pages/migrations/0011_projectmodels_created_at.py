# Generated by Django 4.2.1 on 2023-05-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_projectmodels_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodels',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
