from django.urls import include, path

from UserProfile.views import *

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("interest/", InterestView.as_view(), name="interest"),
]
