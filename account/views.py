from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView

from .models import Account, Transaction
from .serializers import AccountSerialize, AccountCreateSerialize


# Create your views here.


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerialize


# class ListAccount(ListCreateAPIView):
#
#     queryset = Account.objects.all()
#     serializer_class = AccountCreateSerialize

# def get_queryset(self):
#     return Account.objects.all()
#
# def get_serializer_class(self):
#     return AccountCreateSerialize

# def get(self, request):
#     accounts = Account.objects.all()
#     serializer = AccountCreateSerialize(accounts, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def post(self, request):
#     serializer = AccountCreateSerialize(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def list_account(request):
#     if request.method == 'GET':
#         try:
#             accounts = Account.objects.all()
#             serializer = AccountSerialize(accounts, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Account.DoesNotExist:
#             return Response(data("Message Account does not exit"), status=status.HTTP_404_NOT_FOUND)
#     elif request.method == 'POST':
#         serializer = AccountCreateSerialize(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class AccountDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountCreateSerialize

# def get_queryset(self):
#     return Account.objects.all()
#
# def get_serializer_class(self):
#     return AccountCreateSerialize

# def get(self, request, pk):
#     account = get_object_or_404(Account, pk=pk)
#     serializer = AccountSerialize(account)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def put(self, request, pk):
#     account = get_object_or_404(Account, pk=pk)
#     serializer = AccountCreateSerialize(account, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# def delete(self, request, pk):
#     account = get_object_or_404(Account, pk=pk)
#     account.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "PATCH", "PUT", "DELETE"])
# def account_details(request, pk):
#     account = get_object_or_404(Account, pk=pk)
#     if request.method == 'GET':
#         serializer = AccountSerialize(account)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AccountCreateSerialize(account, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     elif request.method == 'DELETE':
#         account.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["POST"])
# def deposit(request):
#     account_number = request.data['account_number']
#     amount = Decimal(request.data['amount'])
#     account = get_object_or_404(Account, pk=account_number)
#     account.balance += Decimal(amount)
#     account.save()
#     Transaction.objects.create(account=account,
#                                amount=amount
#                                )
#     return Response(data={"message : Transaction Successful"},
#                     status=status.HTTP_201_CREATED)

class Deposit(APIView):
    def post(self, request):
        account_number = request.data['account_number']
        amount = Decimal(request.data['amount'])
        account = get_object_or_404(Account, pk=account_number)
        account.balance += Decimal(amount)
        account.save()
        Transaction.objects.create(account=account,
                                   amount=amount
                                   )
        return Response(data={"message : Transaction Successful"},
                        status=status.HTTP_201_CREATED)


@api_view(["PATCH"])
def withdraw(request):
    account_number = request.data.get('account_number')
    amount = request.data.get('amount')
    pin = request.data.get('pin')
    transaction_type = request.data.get('transaction_type')

    if not all([account_number, amount, pin, transaction_type]):
        return Response(data={"message": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        amount = Decimal(amount)
    except ValueError:
        return Response(data={"message": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

    account = get_object_or_404(Account, pk=account_number)

    if account.pin != pin:
        return Response(data={"message": "Incorrect pin"}, status=status.HTTP_400_BAD_REQUEST)

    if account.balance < amount:
        return Response(data={"message": "Balance is lower than withdraw amount"}, status=status.HTTP_400_BAD_REQUEST)
    account.balance -= amount
    account.save()

    Transaction.objects.create(
        account=account,
        amount=amount,
        transaction_type=transaction_type
    )

    return Response(data={"message": "Withdrawal Successful"}, status=status.HTTP_200_OK)

#     class CreateAccount(CreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountCreateSerialize
