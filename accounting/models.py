from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import Student
from courses.models import Course


class PaymentRecord(models.Model):
    paid = models.FloatField(_("paid"))

    course = models.ForeignKey(
        _("course"), Course, on_delete=models.CASCADE, related_name="accounting_details"
    )
    student = models.ForeignKey(
        _("student"),
        Student,
        on_delete=models.CASCADE,
        related_name="accounting_details",
    )

    date_of_payment = models.DateField(_("date_of_payment"), auto_now_add=True)

    def __str__(self):
        return self.date_of_payment
