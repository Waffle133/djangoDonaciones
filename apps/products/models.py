from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

from apps.categories.models import Categories
from apps.products.validators import validate_sku


class Products(models.Model):
    name = models.CharField(
        max_length=150,
    )
    sku = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': "El producto con este SKU ya existe",
        },
        validators=[validate_sku]
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='products/pictures',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png'])
        ]
    )

    show = models.BooleanField(
        default=True,
    )

    category = models.ManyToManyField(Categories)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
