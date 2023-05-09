from django.contrib.auth.models import User
from django.db import models

from django.conf import settings


def user_photos(instance, filename):
    return f'user_{instance.owner.id}/user_photos/{filename}'


class PersonalData(models.Model):
    class Meta:
        verbose_name = 'Personal data'

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='owner',
        on_delete=models.CASCADE,
        blank=False,
        related_name='personaldata'
    )

    information = models.TextField(
        blank=True
    )

    interests = models.TextField(
        blank=True
    )

    photo = models.ImageField(
        upload_to=user_photos,
        blank=True
    )

    birth_day = models.DateTimeField(
        blank=True,
        null=True
    )
