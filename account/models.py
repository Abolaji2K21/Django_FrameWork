from django.db import models

from account.utility import generate_account_number


# Create your models here.

class Account(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    pin = models.CharField(max_length=20)
    accountNumber = models.CharField(max_length=15, default=generate_account_number, unique=True, primary_key=True)
