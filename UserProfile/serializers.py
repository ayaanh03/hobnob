from rest_framework import serializers

from UserProfile.models import *


class Profile2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile2
        fields = "__all__"

    def validate_phone(self, phone):
        phone_no = phone
        if len(str(phone_no)) != 10:
            raise serializers.ValidationError(
                "Hey! Please ensure phone number is 10 digits"
            )
        return phone


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"

    def validate_phone(self, phone):
        phone_no = phone
        if len(str(phone_no)) != 10:
            raise serializers.ValidationError(
                "Hey! Please ensure phone number is 10 digits"
            )
        return phone


class MomInfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomInfluencer
        fields = "__all__"

    def validate_phone(self, phone):
        phone_no = phone
        if len(str(phone_no)) != 10:
            raise serializers.ValidationError(
                "Hey! Please be ensure phone number must be 10 digit"
            )
        return phone


class CampusAmbassadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusAmbassador
        fields = "__all__"

    def validate_phone(self, phone):
        phone_no = phone
        if len(str(phone_no)) != 10:
            raise serializers.ValidationError(
                "Hey! Please be ensure phone number must be 10 digit"
            )
        return phone


class WorkingProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingProfessional
        fields = "__all__"

    def validate_phone(self, phone):
        phone_no = phone
        if len(str(phone_no)) != 10:
            raise serializers.ValidationError(
                "Hey! Please be ensure phone number must be 10 digit"
            )
        return phone


class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = "__all__"
