from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255,null = True, blank = True) 

class Employee(models.Model):
    name = models.CharField(max_length=255)
    staffId = models.IntegerField()
    level = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    Projects = models.ManyToManyField(Project)

  