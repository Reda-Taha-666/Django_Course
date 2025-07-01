from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="photo/%y/%m/%d/")
    active = models.BooleanField(default=True)
    date_time = models.DateTimeField(auto_now_add=True)