from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from courses.models import Course


class Social(models.Model):
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def clean(self):
        if Social.objects.exists() and self.id != Social.objects.first().id:
            raise ValidationError("Can only create one Social instance")

    def __str__(self):
        return "Company Socials"


class District(models.Model):
    title = models.CharField(_("title"), max_length=100)
    address = models.CharField(_("address"), max_length=200)
    phone_number = models.CharField(
        _("phone_number"), max_length=20, blank=True, null=True
    )

    courses = models.ManyToManyField(
        verbose_name=_("courses"), to=Course, related_name="districts"
    )
