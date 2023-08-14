from django.urls import include, path
from rest_framework import routers
from .views import ClientView, ValidtyView


router = routers.DefaultRouter()

router.register(r'clients',ClientView,'clients')
router.register(r'validity',ValidtyView,'validity')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
