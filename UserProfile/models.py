import datetime
from datetime import datetime

from django.db import models


# Create your models here.
class Profile2(models.Model):
    """
    Model for store user profile detail.
    """

    professional_picture = models.ImageField("/media", null=True)

    first_name = models.CharField(max_length=255, null=True)

    last_name = models.CharField(max_length=255, null=True)

    email = models.EmailField()

    phone = models.IntegerField()

    date_of_birth = models.DateField()

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=6, choices=gender_choice)

    country = models.CharField(max_length=255, null=True)

    state = models.CharField(max_length=255, null=True)

    district = models.CharField(max_length=255, null=True)

    role_choice = (
        ("SOCIAL MEDIA STAR", "SOCIAL MEDIA STAR"),
        ("MOM/DAD INFLUENCER", "MOM/DAD INFLUENCER"),
        ("CAMPUS AMBASSADOR", "CAMPUS AMBASSADOR"),
        ("WORKING PROFESSIONAL", "WORKING PROFESSIONAL"),
    )
    your_role = models.CharField(max_length=50, choices=role_choice, null=True)

    class Meta:
        db_table = "UserProfile"


class Profile(models.Model):
    """
    Model for store user profile detail.
    """

    class Meta:
        abstract = True
        db_table = "Profile"

    professional_picture = models.ImageField("/media", null=True)

    first_name = models.CharField(max_length=255, null=True)

    last_name = models.CharField(max_length=255, null=True)

    email = models.EmailField()

    phone = models.IntegerField()

    date_of_birth = models.DateField()

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=6, choices=gender_choice)

    country = models.CharField(max_length=255, null=True)

    state = models.CharField(max_length=255, null=True)

    district = models.CharField(max_length=255, null=True)

    role_choice = (
        ("SOCIAL MEDIA STAR", "SOCIAL MEDIA STAR"),
        ("MOM/DAD INFLUENCER", "MOM/DAD INFLUENCER"),
        ("CAMPUS AMBASSADOR", "CAMPUS AMBASSADOR"),
        ("WORKING PROFESSIONAL", "WORKING PROFESSIONAL"),
    )
    your_role = models.CharField(max_length=50, choices=role_choice, null=True)


class SocialMedia(Profile):

    agency_name = models.CharField(max_length=255, null=True)
    agent_name = models.CharField(max_length=255, null=True)
    agency_email = models.EmailField(null=True)
    agent_number = models.IntegerField(null=True)

    class Meta:
        db_table = "social_media"


class MomInfluencer(Profile):

    oldest_child = models.CharField(max_length=255, null=True)
    youngest_child = models.CharField(max_length=255, null=True)
    social_circle_choice = (
        ("YES", "YES"),
        ("NO", "NO"),
        ("SOMEWHAT", "SOMEWHAT"),
    )
    social_circle_friend = models.CharField(
        max_length=10, choices=social_circle_choice, null=True
    )

    class Meta:
        db_table = "mom_influencer"


class CampusAmbassador(Profile):

    college_name = models.CharField(max_length=255, null=True)
    branch = models.CharField(max_length=255, null=True)
    year_of_study = models.IntegerField(null=True)
    chartbox_experience = models.CharField(max_length=3, null=True)

    class Meta:
        db_table = "campus_ambassador"


class WorkingProfessional(Profile):

    company_name = models.CharField(max_length=255, null=True)
    designation = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "working_professional"


class Interests(models.Model):
    """
    Model for store user interests.
    """

    interests_choice = (
        ("Fashion", "Fashion"),
        ("Beauty & Makeup", "Beauty & Makeup"),
        ("Automobile", "Automobile"),
        ("Arts", "Arts"),
        ("Lifestyle", "Lifestyle"),
        ("Music & dance", "Music & dance"),
        ("Food & Beverages", "Food & Beverages"),
        ("Movies & TV", "Movies & TV"),
        ("Education & career", "Education & career"),
        ("Business & Startup", "Business & Startup"),
        ("Travel", "Travel"),
        ("Technology", "Technology"),
        ("Sports", "Sports"),
        ("Marketing & Social Media", "Marketing & Social Media"),
        ("Fitness & Health", "Fitness & Health"),
        ("Society & Politics", "Society & Politics"),
        ("Photography", "Photography"),
    )
    choose_interests_1 = models.CharField(
        max_length=255, choices=interests_choice, null=True
    )
    choose_interests_2 = models.CharField(
        max_length=255, choices=interests_choice, null=True
    )
    choose_interests_3 = models.CharField(
        max_length=255, choices=interests_choice, null=True
    )

    class Meta:
        db_table = "interests"
