# Generated by Django 4.2.1 on 2023-05-16 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0009_remove_projectmodels_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodels',
            name='project_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
