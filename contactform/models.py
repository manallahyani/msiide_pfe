from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=40,default="-")
    email = models.CharField(max_length=40,default="-")
    txt=models.TextField(default="-")
    date = models.CharField(max_length=12)
    time=models.CharField(max_length=12,default="00:00")
   
    
    
    def __str__(self):
        return self.name +' |'+str(self.pk)