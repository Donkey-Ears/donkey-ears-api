from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Fields",
            {
                "fields": ("gender", "age"),
            },
        ),
    )

    list_display = ("username", "gender", "age")

    list_filter = ("age", "gender")