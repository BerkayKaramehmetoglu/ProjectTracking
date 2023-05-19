from django.db import models


class ProjectModels(models.Model):
    project_owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    project_name = models.CharField(max_length=20)
    project_description = models.TextField(max_length=250)
    project_technology = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    add = models.BooleanField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.project_name
# Create your models here.
