import uuid

from django.db import models


class Performer(models.Model):
    class Meta:
        db_table = "performer"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, db_index=True, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    class Meta:
        db_table = "program"
        constraints = [
            models.UniqueConstraint(fields=["performer", "vol"], name='program_u_idx_1'),
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    vol = models.CharField(max_length=16)
    old_vol = models.CharField(null=True, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.performer}:{self.vol}"
