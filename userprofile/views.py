from django.shortcuts import render
from rest_framework import viewsets,permissions
from .serializers import InterestsSerializer,ProfileSerializer
from .models import Profile,Interests

class ProfileClass(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class=ProfileSerializer

class InterestsClass(viewsets.ModelViewSet):
    queryset=Interests.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class=InterestsSerializer