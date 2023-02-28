from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import FavoritePerformer, Performer, Program
from .serializers import FavoritePerformerSerializer, PerformerSerializer, ProgramSerializer


class PerformerViewSet(ModelViewSet):
    serializer_class = PerformerSerializer

    def get_queryset(self):
        return Performer.objects.all()


class ProgramViewSet(ModelViewSet):
    serializer_class = ProgramSerializer

    def get_queryset(self):
        return Program.objects.all()


class FavoritePerformerViewSet(ModelViewSet):
    serializer_class = FavoritePerformerSerializer

    def get_queryset(self):
        return FavoritePerformer.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["user"] = self.request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
