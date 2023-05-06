from django.db import models


class ProjectModels(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_technology = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name
# Create your models here.
