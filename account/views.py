from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data

from .models import Account
from .serializers import AccountSerialize, AccountCreateSerialize


# Create your views here.


@api_view(['GET', 'POST'])
def list_account(request):
    if request.method == 'GET':
        try:
            accounts = Account.objects.all()
            serializer = AccountSerialize(accounts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response(data("Message Account does not exit"), status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = AccountCreateSerialize(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view()
def account_details(request, pk):
    account = get_object_or_404(Account, pk=pk)
    serializer = AccountSerialize(account)
    return Response(serializer.data, status=status.HTTP_200_OK)
