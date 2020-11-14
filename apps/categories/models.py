from django.db import models
from django.utils import timezone

# from apps.products.models import Products


class Categories(models.Model):
    name = models.CharField(
        max_length=150
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    # products = models.ManyToManyField(Products)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    # events
    # nombre,fecha,dirección,owner
    # manyToMany Users

    # subcategorias
    # nombre,categoryId

