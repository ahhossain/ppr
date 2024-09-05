import datetime 
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class entry(models.Model):
    index = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='index')
    Date = models.DateField()
    Address = models.TextField()
    County = models.TextField()
    Eircode = models.TextField()
    Price = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'regster'
