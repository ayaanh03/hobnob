from django.urls import include, path

from UserProfile.views import *

urlpatterns = [
    path("profile/", get_profile, name="profile"),
    # path("interest/", InterestView.as_view(), name="interest"),
]
