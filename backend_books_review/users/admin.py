from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    fields = (
        ("username", "email"),
        ("is_staff", "is_superuser"),
        "groups",
        "user_permissions",
        ("last_login", "date_joined"),
        "password",
    )
    readonly_fields = ("last_login", "date_joined", "password")


admin.site.register(User, UserAdmin)
