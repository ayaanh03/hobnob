from django.urls import path, include
from rest_framework import routers
from .views import InterestsClass,ProfileClass

router= routers.DefaultRouter()
router.register('profile',ProfileClass,'profile')
router.register('intrests',InterestsClass,'intrests')

urlpatterns=[
    path('api/',include(router.urls),name='api'),
]

