from django.db import models
from django.contrib.auth.models import AbstractUser

from roles.models import Role


class User(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='users'
    )
