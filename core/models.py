from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=226)
    email=models.CharField(max_length=100)
    content=models.TextField()
    subject=models.CharField(max_length=150)
    # timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
