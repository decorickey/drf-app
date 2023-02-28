from rest_framework import serializers

from .models import FavoritePerformer, Performer, Program


class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = "__all__"


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class FavoritePerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePerformer
        exclude = ["user"]
