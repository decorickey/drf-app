from rest_framework.viewsets import ModelViewSet

from .models import FavoritePerformer, Performer, Program
from .serializers import FavoritePerformerSerializer, PerformerSerializer, ProgramSerializer


class PerformerViewSet(ModelViewSet):
    serializer_class = PerformerSerializer

    def get_queryset(self):
        return Performer.objects.all().order_by("created_at")


class ProgramViewSet(ModelViewSet):
    serializer_class = ProgramSerializer

    def get_queryset(self):
        return Program.objects.all().order_by("created_at")


class FavoritePerformerViewSet(ModelViewSet):
    serializer_class = FavoritePerformerSerializer

    def get_queryset(self):
        return FavoritePerformer.objects.filter(user=self.request.user).order_by("created_at")
