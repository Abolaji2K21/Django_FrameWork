from rest_framework import serializers

from .models import Account, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'transaction_status', 'transaction_date', 'description']


class AccountSerialize(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)

    class Meta:
        model = Account
        fields = ['accountNumber', 'balance', 'account_type', 'transactions']


class AccountCreateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pin', 'account_type']
