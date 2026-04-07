from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from accounts.choices import RoleChoices
from accounts.manager import AccountUserManager
from WellnessNewProject.validators import MaxFileSizeValidator


# Create your models here.

class AccountUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = AccountUserManager()


class Profile(models.Model):

    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to="profile_pictures/",
        validators=[MaxFileSizeValidator(5 * 1024 * 1024)]
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )

    role = models.CharField(
        max_length=50,
        choices=RoleChoices.choices,
        default=RoleChoices.PARTICIPANT,
    )

    user = models.OneToOneField(
        AccountUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.first_name or self.last_name