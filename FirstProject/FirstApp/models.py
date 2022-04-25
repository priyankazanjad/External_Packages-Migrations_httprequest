from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)
# Create your models here.
