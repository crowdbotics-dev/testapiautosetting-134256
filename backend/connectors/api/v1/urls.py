from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134256ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134256", Testconnectors134256ViewSet, basename="testconnectors134256"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
