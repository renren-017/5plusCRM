from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm


class CustomUserEditForm(UserEditForm):
    is_student = forms.BooleanField(required=False, label=_("Student"))
    is_teacher = forms.BooleanField(required=False, label=_("Teacher"))


class CustomUserCreationForm(UserCreationForm):
    is_student = forms.BooleanField(required=False, label=_("Student"))
    is_teacher = forms.BooleanField(required=False, label=_("Teacher"))
