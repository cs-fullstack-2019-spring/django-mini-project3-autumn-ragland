from django import forms
from .models import TeacherModel


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = ['name', 'school', 'subject', 'hours', 'workDate']
