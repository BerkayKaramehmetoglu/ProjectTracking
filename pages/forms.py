from django import forms
from django.forms import TextInput, Textarea

from pages.models import ProjectModels


# class MyProjectForm(forms.Form):
# project_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
# project_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
# project_technology = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class MyProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModels
        fields = ('project_name', 'project_description', 'project_technology', 'is_active')
        labels = {"project_name": "Project Name", "project_description": "Project Description",
                  "project_technology": "Project Technology"},
        widgets = {"project_name": TextInput(attrs={'class': 'form-control'}),
                   "project_description": Textarea(
                       attrs={'class': 'form-control',
                              'style': 'height: 220px; width: 100%; resize: none;'}),
                   "project_technology": TextInput(attrs={'class': 'form-control'}),
                   }


class MyProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = ProjectModels
        fields = ('project_name', 'project_description', 'project_technology', 'is_active')
        labels = {"project_name": "Project Name", "project_description": "Project Description",
                  "project_technology": "Project Technology"},
        widgets = {"project_name": TextInput(attrs={'class': 'form-control'}),
                   "project_description": Textarea(attrs={'class': 'form-control', 'rows': 8}),
                   "project_technology": TextInput(attrs={'class': 'form-control'}),
                   }
