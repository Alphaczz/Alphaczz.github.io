from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feedemp(models.Model):

    fname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    date_time = models.DateTimeField()
    feed = models.TextField(max_length=200)

    def __str__(self):
        return self.fname + " - " + self.feed

class taskAlloc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    date = models.DateField()
    time = models.TimeField()
    priority = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    task = models.TextField(max_length=200)

    def __str__(self):
        return self.username