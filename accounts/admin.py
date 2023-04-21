from django.contrib import admin

from accounts.models import Teacher, Student, CustomUser

admin.site.register(CustomUser)

admin.site.register(Student)

admin.site.register(Teacher)
