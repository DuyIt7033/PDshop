from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 
                       'password', 'password2', 'city', 'stage', 'address', 'phone','is_staff', 'is_activate')
        }),
    )



admin.site.register(CustomUser, CustomUserAdmin)
