from django.urls import include, path
from rest_framework import routers
from .views import ClientView, ValidtyView, ClientValidityView, PlaceView, PlaceCoachView,PlaceCategoryPlaceView,CoachView,CategoryPlaceView
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()

router.register(r'clients',ClientView,'clients')
router.register(r'validity',ValidtyView,'validity')
router.register(r'clientValidity',ClientValidityView,'clientValidity')
router.register(r'place',PlaceView,'place')
router.register(r'placeCoach',PlaceCoachView,'placeCoach')
router.register(r'placeCategoryPlace',PlaceCategoryPlaceView,'placeCategoryPlace')
router.register(r'coach',CoachView,'coach')
router.register(r'categoryPlace',CategoryPlaceView,'categoryPlace')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    
]
