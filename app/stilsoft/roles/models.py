from django.db import models
from django.contrib.auth.models import Permission


class Role(models.Model):
    name = models.CharField(max_length=40, unique=True)

    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='role',
    )

    def __str__(self):
        return self.name
