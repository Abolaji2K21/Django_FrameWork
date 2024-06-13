from django.db import models

from account.utility import generate_account_number


# Create your models here.

class Account(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    pin = models.CharField(max_length=20)
    accountNumber = models.CharField(max_length=15,
                                     default=generate_account_number,
                                     unique=True,
                                     primary_key=True)
    balance = models.DecimalField(max_digits=10,
                                  decimal_places=2,
                                  default=0.00)
    ACCOUNT_TYPE = [
        ('SAVINGS', 'S'),
        ('CURRENT', 'C'),
        ('DOMICILIARY', 'DOM'),

    ]
    account_type = models.CharField(max_length=1,
                                    choices=ACCOUNT_TYPE,
                                    default='SAVINGS')


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('CREDIT',   'CRE'),
        ('DEBIT',    'TRA'),
        ('TRANSFER', 'TRAN'),

    ]
    TRANSACTION_STATUS = [
        ('SUCCESSFUL', 'S'),
        ('FAILED',     'F'),
        ('PENDING',    'P')

    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=3,
                                        choices=TRANSACTION_TYPE,
                                        default='CRE')

    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10

                                 , decimal_places=2)
    description = models.TextField()
    transaction_status = models.CharField(max_length=1,
                                          choices=TRANSACTION_STATUS,
                                          default='SUCCESSFUL')
