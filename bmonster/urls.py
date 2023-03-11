from django.urls import include, path
from rest_framework import routers

from .views import FavoritePerformerViewSet, FavoriteProgramViewSet, PerformerViewSet, ProgramViewSet

app_name = "bmonster"

router = routers.DefaultRouter()
router.register("performers", PerformerViewSet, basename="Performer")
router.register("programs", ProgramViewSet, basename="Program")
router.register("favorite/performers", FavoritePerformerViewSet, basename="FavoritePerformer")
router.register("favorite/programs", FavoriteProgramViewSet, basename="FavoriteProgram")

urlpatterns = [path("", include(router.urls))]
