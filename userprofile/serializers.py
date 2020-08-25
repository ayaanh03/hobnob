from rest_framework import serializers
from .models import Profile,Interests

class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model=Profile
        fields='__all__'

class InterestsSerializer(serializers.ModelSerializer):
    class Meta():
        model=Interests
        fields='__all__'