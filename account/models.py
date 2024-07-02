from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from account.utility import generate_account_number
from account.validators import validate_pin


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    # firstName = models.CharField(max_length=255)
    # lastName = models.CharField(max_length=255)
    pin = models.CharField(max_length=4, validators=[validate_pin], default='0000')
    accountNumber = models.CharField(max_length=15,
                                     default=generate_account_number,
                                     unique=True,
                                     primary_key=True)
    balance = models.DecimalField(max_digits=10,
                                  decimal_places=2,
                                  default=0.00)
    ACCOUNT_TYPE = [
        ('S', 'SAVINGS'),
        ('C', 'CURRENT'),
        ('DOM', 'DOMICILIARY'),
    ]
    transactions = models.ManyToOneRel
    account_type = models.CharField(max_length=11,  # Updated max_length
                                    choices=ACCOUNT_TYPE,
                                    default='S')

    def __str__(self):
        return f'{self.account_type} {self.balance} {self.accountNumber}'


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('CRE', 'CREDIT'),
        ('TRA', 'DEBIT'),
        ('TRAN', 'TRANSFER'),
    ]
    TRANSACTION_STATUS = [
        ('S', 'SUCCESSFUL'),
        ('F', 'FAILED'),
        ('P', 'PENDING'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=7,
                                        choices=TRANSACTION_TYPE,
                                        default='CRE')

    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=15,
                                 decimal_places=2)
    description = models.TextField(blank=True)
    transaction_status = models.CharField(max_length=1,
                                          choices=TRANSACTION_STATUS,
                                          default='S')
