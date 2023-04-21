from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import CustomUser, Student, Teacher


@receiver(post_save, sender=CustomUser)
def create_student_or_teacher(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.is_student and not hasattr(instance, "student"):
        Student.objects.create(user=instance)
    if instance.is_teacher and not hasattr(instance, "teacher"):
        Teacher.objects.create(user=instance)
