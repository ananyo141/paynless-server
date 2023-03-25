from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    BUSINESS = "business"


# Create your models here.
class User(AbstractUser):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=60)
    avatar = models.URLField(blank=True, null=True)
    role = models.CharField(
        max_length=50,
        choices=[(role.value, role.name) for role in Role],
        default=Role.USER.value,
    )
    username = models.CharField(max_length=100, unique=True)

    REQUIRED_FIELDS = ["id", "name"]

    def __str__(self):
        return f"{self.email}"
