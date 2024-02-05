from django.forms import fields
from .models import Student
from django import forms

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student 
        fields = "__all__"