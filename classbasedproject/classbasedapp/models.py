from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField(primary_key = True)
    sname = models.CharField(max_length= 20)
    options = (('male', 'male'), ('female', 'female'))
    gender = models.CharField(max_length=50, choices=options)
    address = models.CharField(max_length = 50)
    percentage = models.FloatField()
    email = models.EmailField()
