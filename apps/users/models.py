from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    biography = models.TextField(
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': "Este número de celular ya está registrado.",
        },
    )

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    updated_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.user.username

    def getfullname(self):
        return self.user.first_name + ' ' + self.user.last_name
