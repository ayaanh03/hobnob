from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from UserProfile.models import *
from UserProfile.serializers import *


class ProfileView(APIView):
    def post(self, request):

        if request.data.get("your_role") is None:
            breakpoint()
            serializer = Profile2Serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response("Congratulation!!! your Profile data added")

        elif request.data.get("your_role") == "SOCIAL MEDIA STAR":

            serializer = SocialMediaSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    "Congratulation!!! your Profile data added for Social MEDIA Star Role"
                )

        elif request.data.get("your_role") == "MOM/DAD INFLUENCER":
            serializer = MomInfluencerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    "Congratulation!!! your Profile data added for Mom/Dad Influencer Role"
                )

        elif request.data.get("your_role") == "CAMPUS AMBASSADOR":
            serializer = CampusAmbassadorSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    "Congratulation!!! your Profile data added for Campus Ambassador Role"
                )

        else:
            serializer = WorkingProfessionalSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    "Congratulation!!! your Profile data added for working Professional Role"
                )


class InterestView(APIView):
    def post(self, request):
        serializer = InterestsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Congratulation!!! your field of Interests Added")
