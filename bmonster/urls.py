from django.urls import include, path
from rest_framework import routers

from .views import FavoritePerformerViewSet, FavoriteProgramViewSet, PerformerViewSet, ProgramViewSet

app_name = "bmonster"

router = routers.DefaultRouter()
router.register("performers", PerformerViewSet, basename="performer")
router.register("programs", ProgramViewSet, basename="program")
router.register("favorite/performers", FavoritePerformerViewSet, basename="favorite_performer")
router.register("favorite/programs", FavoriteProgramViewSet, basename="favorite_program")

urlpatterns = [path("", include(router.urls))]
