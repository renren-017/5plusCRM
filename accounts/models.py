from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

from accounts.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email_address"), unique=True)
    full_name = models.CharField(_("full_name"), max_length=200, blank=True, null=True)
    phone_number = models.CharField(
        _("phone_number"), max_length=20, blank=True, null=True
    )

    date_joined = models.DateTimeField(default=timezone.now)
    verification_token = models.CharField(max_length=150, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def generate_verification_token(self):
        token = make_password(f"{self.email}-{self.date_joined}")
        self.verification_token = token
        self.save()

        return token


class Student(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.SET_NULL, related_name="student", null=True
    )


class Teacher(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.SET_NULL, related_name="teacher", null=True
    )
