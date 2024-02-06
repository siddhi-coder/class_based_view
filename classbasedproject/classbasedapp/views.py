from django.shortcuts import render
from .models import Student
from .forms import StudentForms
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView , UpdateView , DeleteView

class StudentRetrieve(ListView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    fields ="__all__"
    success_url = "/"

class StudentUpdate(UpdateView):
    model = Student
    template_name_suffix = "_edit_form"
    fields ="__all__"
    success_url = "/"

# class StudentDelete(DeleteView):
#     model = Student
#     fields ="__all__"
#     success_url = "/"