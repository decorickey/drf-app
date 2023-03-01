from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

from .models import FavoritePerformer, Performer, Program


class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = "__all__"
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(queryset=model.objects.all(), message="registered"),
                    RegexValidator(regex=r"^[a-zA-Z.@]*$", message="invalid input"),
                ],
                "error_messages": {
                    "max_length": "too long",
                },
            },
        }


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=["performer", "vol"],
                message="registered",
            ),
        ]
        extra_kwargs = {
            "vol": {
                "validators": [
                    RegexValidator(regex=r"^[a-zA-Z0-9.-]*$", message="invalid input")
                ],
                "error_messages": {
                    "max_length": "too long",
                },
            },
            "old_vol": {
                "validators": [
                    RegexValidator(regex=r"^[a-zA-Z0-9.-]*$", message="invalid input")
                ],
                "error_messages": {
                    "max_length": "too long",
                },
            },
        }


class FavoritePerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePerformer
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=["user", "performer"],
                message="registered",
            ),
        ]

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
