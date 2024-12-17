from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        'username',
        'email',
        'phone_number',
        'is_active',
        'is_staff'
    ]

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': (
                'avatar',
                'phone_number'
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': (
                'avatar',
                'phone_number'
            )
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)