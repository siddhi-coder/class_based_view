from django.shortcuts import render
from .models import Student
from .forms import StudentForms
from django.views.generic.list import ListView

class StudentRetrieve(ListView):
    model = Student