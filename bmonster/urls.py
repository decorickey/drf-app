from django.urls import include, path
from rest_framework import routers

from .views import PerformerViewSet, ProgramViewSet

app_name = "bmonster"

router = routers.DefaultRouter()
router.register("performers", PerformerViewSet, basename="performer")
router.register("programs", ProgramViewSet, basename="program")

urlpatterns = [
    path('', include(router.urls))
]
