from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    image = models.ImageField(upload_to='accounts/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'CustomUser'