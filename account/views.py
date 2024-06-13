from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerialize


# Create your views here.


@api_view()
def list_account(request):
    accounts = Account.objects.all()
    serializer = AccountSerialize(accounts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def account_details(request, pk):
    account = Account.objects.get(pk=pk)
    serializer = AccountSerialize(account)
    return Response(serializer.data, status=status.HTTP_200_OK)
