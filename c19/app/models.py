from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    phone = models.IntegerField()
    doctor = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')

class Covid(models.Model):
    dry = models.IntegerField()
    fever = models.IntegerField()
    throat = models.IntegerField()
    difficulty = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='covid')