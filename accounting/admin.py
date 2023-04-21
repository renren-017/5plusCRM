from django.contrib import admin

from accounting.models import PaymentRecord


@admin.register(PaymentRecord)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "paid", "date_of_payment")
    list_display_links = ("paid",)
