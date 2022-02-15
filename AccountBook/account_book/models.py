from django.db import models
from django.utils import timezone


# Create your models here.
class AccountBook(models.Model):
    email = models.ForeignKey('user.User', on_delete=models.CASCADE)
    present_account = models.IntegerField()
