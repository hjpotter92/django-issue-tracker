from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Project, CustomUser, Issue, Status,
    Priority, Comment, Membership)

from .forms.user import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'created')


for model, admin_model in (
        (Project, ProjectAdmin),
        (CustomUser, CustomUserAdmin),):
    admin.site.register(model, admin_model)

for model in (Issue, Status, Priority, Comment, Membership):
    admin.site.register(model)
