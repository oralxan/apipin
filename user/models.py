from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    fullname = models.TextField(
        verbose_name='FullName',
        max_length=220,
        blank=True,
        null=True
    )
    profile_img = models.ImageField(
        verbose_name='Profile Image',
        upload_to='user_img/'
    )


    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'
