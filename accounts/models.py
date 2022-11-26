import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_operator = models.BooleanField(
        default=False
    )
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
        db_table = "db_user"
