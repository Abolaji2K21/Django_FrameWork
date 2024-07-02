from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from user.models import User
from user.serializer import UserSerializer


# Create your views here.


class UserRegistration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
