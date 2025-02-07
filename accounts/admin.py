from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "fullname", "phone", "is_active"]
    ordering = ["email"]
    
    fieldsets = (
        (None, {"fields": ("email", "fullname", "phone", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "fullname", "phone", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )

    search_fields = ["email", "fullname", "phone"]
    ordering = ["email"]
    
    # ✅ Fix list_filter (Use a tuple instead of a list)
    list_filter = ("is_staff", "is_superuser", "is_active")

admin.site.register(CustomUser, CustomUserAdmin)
