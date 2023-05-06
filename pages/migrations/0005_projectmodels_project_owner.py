# Generated by Django 4.2.1 on 2023-05-06 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0004_alter_projectmodels_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodels',
            name='project_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
