from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Signup


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'
