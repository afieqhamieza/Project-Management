from django.db import models

# Create your models here.

class Engagement(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # startDate = models.DateField(input_formats=['%Y-%m-%d'])
    # endDate = models.DateField(input_formats=['%Y-%m-%d'])
    status = models.CharField(max_length=30)
    staffId = models.IntegerField()

