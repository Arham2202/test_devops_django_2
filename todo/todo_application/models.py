from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 99)
    description = models.TextField()
    created_on = models.CharField(max_length = 55)
    deadline = models.CharField(max_length = 55)
    completed = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title