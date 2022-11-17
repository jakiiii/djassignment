import uuid
from django.db import models

from base.models import BaseModel


class Category(models.Model):
    uid = models.CharField(
        max_length=40,
        default=uuid.uuid4,
        unique=True
    )
    name = models.CharField(
        max_length=100
    )
    status = models.CharField(
        max_length=12,
        choices=BaseModel.StatusChoices.choices,
        default=BaseModel.StatusChoices.PUBLISHED
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "db_category"
