from django.contrib import admin

from courses.models import (
    Course,
    CourseEnroll,
    CourseMaterial,
    Answer,
    Question,
    CourseMaterialTest,
    Schedule,
    Attendance,
)


class ScheduleInline(admin.TabularInline):
    model = Schedule


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price", "teacher", "date_created")
    list_display_links = ("title",)
    inlines = [ScheduleInline]


@admin.register(CourseEnroll)
class CourseEnrollAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "student", "date_joined")
    list_display_links = ("id",)


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]


class CourseMaterialTestInline(admin.TabularInline):
    model = CourseMaterialTest
    extra = 1
    inlines = [QuestionInline]


@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "video_link", "date_created")
    list_display_links = ("title",)
    inlines = [CourseMaterialTestInline]


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "attended", "date")
    list_display_links = ("attended",)
