from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    staffId = models.IntegerField()
    level = models.CharField(max_length=255)
    team = models.CharField(max_length=255)

# senior executive
# executive
# senior director
# director
# senior manager
# manager
# senior advisor
# advisor
# senior staffId
# intermediate staff
# associate staff