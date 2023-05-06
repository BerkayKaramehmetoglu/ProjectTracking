from django.contrib import admin

from .models import ProjectModels


@admin.register(ProjectModels)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_technology', 'is_active')
# Register your models here.
