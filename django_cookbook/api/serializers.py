"""Serializers."""

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

Serializer = serializers.ModelSerializer
if settings.DEBUG:
    Serializer = serializers.HyperlinkedModelSerializer  # type: ignore


class UserSerializer(Serializer):
    """User Serializer."""

    class Meta:
        model = get_user_model()
        fields = ['url', 'id', 'username', 'is_active', 'groups']


class GroupSerializer(Serializer):
    """Group Serializer."""

    class Meta:
        model = Group
        fields = ['url', 'id', 'name']
