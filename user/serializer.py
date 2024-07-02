from rest_framework import serializers

from user.models import User
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class UserSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'password']

