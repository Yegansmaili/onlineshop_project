from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # email = models.EmailField(unique=True, null=False, blank=False)
    age = models.PositiveIntegerField(blank=True, null=True)
