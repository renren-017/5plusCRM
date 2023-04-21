from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from accounts.models import Teacher, Student

User = get_user_model()


class Course(models.Model):
    title = models.CharField(_("title"), max_length=200, unique=True)
    description = models.TextField(_("description"), blank=True, null=True)
    price = models.FloatField(_("price"))
    duration = models.PositiveIntegerField(
        _("duration"), help_text=_("Duration in months")
    )

    teacher = models.ForeignKey(
        verbose_name=_("teacher"),
        to=Teacher,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="courses",
    )

    date_created = models.DateField(_("date_created"), auto_now_add=True)

    def __str__(self):
        return self.title


class CourseEnroll(models.Model):
    course = models.ForeignKey(
        verbose_name=_("course"),
        to=Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="enrolls",
    )
    student = models.ForeignKey(
        verbose_name=_("student"),
        to=Student,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="enrolls",
    )

    date_joined = models.DateField(_("date_joined"), auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.email}-{self.course.title}"


class CourseMaterial(models.Model):
    title = models.CharField(_("title"), max_length=200)
    description = models.TextField(
        _("description"), max_length=20, blank=True, null=True
    )
    video_link = models.URLField(_("video_link"), max_length=20, blank=True, null=True)

    date_created = models.DateField(_("date_created"), auto_now_add=True)

    def __str__(self):
        return self.title


class CourseMaterialTest(models.Model):
    title = models.CharField(_("title"), max_length=200, default="Тест по материалу")

    course = models.ForeignKey(
        verbose_name=_("course"),
        to=CourseMaterial,
        on_delete=models.CASCADE,
        related_name="tests",
    )

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField(_("text"))

    test = models.ForeignKey(
        verbose_name=_("test"),
        to=CourseMaterialTest,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(_("text"), max_length=255)
    is_correct = models.BooleanField(_("is_correct"), default=False)

    question = models.ForeignKey(
        verbose_name=_("question"),
        to=Question,
        on_delete=models.CASCADE,
        related_name="answers",
    )

    def __str__(self):
        return self.text


class Schedule(models.Model):
    DAYS_OF_WEEK = (
        ("monday", _("Monday")),
        ("tuesday", _("Tuesday")),
        ("wednesday", _("Wednesday")),
        ("thursday", _("Thursday")),
        ("friday", _("Friday")),
        ("saturday", _("Saturday")),
        ("sunday", _("Sunday")),
    )

    day_of_week = models.CharField(
        _("day_of_the_week"), choices=DAYS_OF_WEEK, max_length=20
    )
    start_time = models.TimeField(_("start_time"))
    end_time = models.TimeField(_("end_time"), max_length=20, blank=True, null=True)

    course = models.ForeignKey(
        verbose_name=_("course"),
        to=Course,
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    def __str__(self):
        return (
            f"{self.course} - {self.day_of_week} ({self.start_time} - {self.end_time})"
        )


class Attendance(models.Model):
    date = models.DateField(_("date"))
    attended = models.BooleanField(_("attended"), default=False)

    course = models.ForeignKey(
        verbose_name=_("course"),
        to=Course,
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )
    student = models.ForeignKey(
        verbose_name=_("student"),
        to=Student,
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )

    def __str__(self):
        return f"{self.attended}"
