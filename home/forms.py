from django import forms
from .models import Student
from django.utils.translation import gettext_lazy as _

# class StudentForm(forms.Form):
#     name = forms.CharField()
#     roll = forms.IntegerField()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll',
        }
        help_texts = {
            "name": _("Some useful help text."),
        }
        error_messages = {
            "name": {
                "max_length": _("This writer's name is too long."),
            },
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
        }
