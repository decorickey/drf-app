import uuid

from django.db import models
from django.contrib.auth import settings


class Performer(models.Model):
    class Meta:
        db_table = "performer"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    class Meta:
        db_table = "program"
        constraints = [
            models.UniqueConstraint(fields=["performer", "vol"], name="program_u_idx_1"),
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    vol = models.CharField(max_length=16)
    old_vol = models.CharField(blank=True, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.performer}:{self.vol}"


class FavoritePerformer(models.Model):
    class Meta:
        db_table = "favorite_performer"
        constraints = [
            models.UniqueConstraint(fields=["user", "performer"], name="favorite_performer_u_idx_1"),
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    comment = models.CharField(blank=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FavoriteProgram(models.Model):
    class Meta:
        db_table = "favorite_program"
        constraints = [
            models.UniqueConstraint(fields=["user", "program"], name="favorite_program_u_idx_1"),
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    comment = models.CharField(blank=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
