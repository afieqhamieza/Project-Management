from django.db import models

# Create your models here.

class Engagement(models.Model):
    title = models.CharField(max_length=255,null = True, blank = True)
    body = models.TextField(null = True, blank = True)
    # add on
    startDate = models.DateField(null = True, blank = True)
    endDate = models.DateField(null = True, blank = True)
    status = models.CharField(max_length=30,null = True, blank = True)
    staffId = models.IntegerField(null = True, blank = True)
    progress = models.IntegerField(null = True, blank=True, default='0')

    

