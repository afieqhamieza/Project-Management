from django.db import models
from employee.models import Employee

# Create your models here.

# Create your models here.
class Staff(models.Model):
    name = models.TextField(null = True, blank = True)
    staff_id = models.IntegerField(null = True, blank=True, default='0')

class Engagement(models.Model):
    title = models.CharField(max_length=255,null = True, blank = True) 
    body = models.TextField(null = True, blank = True)
    # add on
    startDate = models.DateField(null = True, blank = True)
    endDate = models.DateField(null = True, blank = True)
    status = models.CharField(max_length=30, null = True, blank = True, default='just started')
    staff = models.ManyToManyField(Employee)
    progress = models.IntegerField(null = True, blank=True, default='0') 



    

