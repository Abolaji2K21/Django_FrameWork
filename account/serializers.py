from rest_framework import serializers

from .models import Account


class AccountSerialize(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['accountNumber', 'firstName', 'lastName', 'balance', 'account_type']


class AccountCreateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pin', 'firstName', 'lastName', 'account_type']