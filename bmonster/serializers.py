from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

from .models import FavoritePerformer, FavoriteProgram, Performer, Program


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
                "validators": [RegexValidator(regex=r"^[a-zA-Z0-9.-]*$", message="invalid input")],
                "error_messages": {
                    "max_length": "too long",
                },
            },
            "old_vol": {
                "validators": [RegexValidator(regex=r"^[a-zA-Z0-9.-]*$", message="invalid input")],
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
        extra_kwargs = {
            "star": {
                "validators": [
                    MaxValueValidator(5, message="value <= 5"),
                    MinValueValidator(1, message="1 <= value"),
                ],
            },
        }

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class FavoriteProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProgram
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=["user", "program"],
                message="registered",
            ),
        ]
        extra_kwargs = {
            "star": {
                "validators": [
                    MaxValueValidator(5, message="value <= 5"),
                    MinValueValidator(1, message="1 <= value"),
                ],
            },
        }

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
