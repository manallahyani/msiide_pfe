from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Main(models.Model):
    name = models.CharField(max_length=40,default="-")
    about = models.TextField(default="-")
    fb = models.CharField(max_length=40,default="-")
    tw = models.CharField(max_length=40,default="-")
    yt = models.CharField(max_length=40,default="-")
    set_name = models.CharField(max_length=40,default="-")
    tel = models.CharField(max_length=40,default="-")
    link = models.CharField(max_length=40,default="-")
    picurl=models.TextField(default="-")
    picname=models.TextField(default="-")
    picurl2=models.TextField(default="-")
    picname2=models.TextField(default="-")
    
    def __str__(self):
        return self.set_name +' |'+str(self.pk)