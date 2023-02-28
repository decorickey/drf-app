from rest_framework.viewsets import ModelViewSet

from .models import Performer, Program
from .serializers import PerformerSerializer, ProgramSerializer


class PerformerViewSet(ModelViewSet):
    serializer_class = PerformerSerializer

    def get_queryset(self):
        return Performer.objects.all()


class ProgramViewSet(ModelViewSet):
    serializer_class = ProgramSerializer

    def get_queryset(self):
        return Program.objects.all()
