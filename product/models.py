import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from base.models import BaseModel
from product.utils import product_photo_directory_path

User = settings.AUTH_USER_MODEL


class Product(BaseModel):
    uid = models.CharField(
        max_length=40,
        default=uuid.uuid4,
        unique=True
    )
    posted_by = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='product_owner'
    )
    title = models.CharField(
        max_length=255
    )
    category = models.ForeignKey(
        'category.Category',
        models.RESTRICT,
        related_name='product_category'
    )
    price = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=0.00
    )
    discount_price = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=0.00
    )
    description = models.TextField()
    review = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    is_feature = models.BooleanField(
        default=False
    )
    status = models.CharField(
        max_length=12,
        choices=BaseModel.StatusChoices.choices,
        default=BaseModel.StatusChoices.PUBLISHED
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('status', '-created_at', 'title')
        verbose_name = "Product"
        verbose_name_plural = "Product"
        db_table = "db_product"


class ProductImage(models.Model):
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        related_name='product_image'
    )
    image = models.ImageField(
        upload_to=product_photo_directory_path
    )
