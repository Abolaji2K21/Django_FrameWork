from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Account
from user.models import User


@receiver(post_save, sender=User)
def create_account(instance, created, **kwargs):
    if created:
        Account.objects.create(
            user=instance,
            accountNumber=instance.phone[1:]
        )
