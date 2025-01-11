from django import forms
from .models import Student

# class StudentForm(forms.Form):
#     name = forms.CharField()
#     roll = forms.IntegerField()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        