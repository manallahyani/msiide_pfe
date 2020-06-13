from __future__ import unicode_literals
from django.db import models

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    txt_body = models.TextField()
    date = models.CharField(max_length=12)
    picname = models.TextField()
    picurl = models.TextField(default="-")
    writer = models.CharField(max_length=50)
    catname = models.CharField(max_length=50)
    catid = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.name