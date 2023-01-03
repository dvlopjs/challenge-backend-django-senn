from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=128)
    job_title = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=15, decimal_places=2)
