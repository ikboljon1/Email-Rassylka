from django.db import models

# Create your models here.
from django.db import models 

class Subscriber(models.Model): 
 name = models.CharField(max_length=255)
 email = models.EmailField()
 birthdate = models.DateField() 

class Template(models.Model): 
 name = models.CharField(max_length=255) 
 html = models.TextField() 
 variables = models.CharField(max_length=255) 