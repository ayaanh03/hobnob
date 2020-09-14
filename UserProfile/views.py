from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from UserProfile.models import *
from UserProfile.serializers import *

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile2.objects.all()
    serializer_class  = Profile2Serializer

class InterestView(generics.ListCreateAPIView):
    queryset = Interests.objects.all()
    serializer_class  = InterestsSerializer