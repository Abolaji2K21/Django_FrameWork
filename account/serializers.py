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
        fields = ['user', 'accountNumber', 'pin', 'account_type']


class DepositWithdrawSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


class WithdrawSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    pin = serializers.CharField(max_length=10)
