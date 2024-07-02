from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Account
from user.models import User


@receiver(signal=post_save)
def create_account(self, instance, created, sender=User):
    if created:
        Account.objects.create(
            user=instance.user,
            accountNumber=instance.phone[1:]
        )
