from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(Enum):
    ADMIN = "admin"
    CLIENT = "client"
    SHOPKEEPER = "shopkeeper"


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=60)
    role = models.CharField(
        max_length=50,
        choices=[(role.value, role.name) for role in Role],
        default=Role.CLIENT.value,
    )

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["email", "name"]

    def __str__(self):
        return f"{self.email}"
