from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=99)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=99)