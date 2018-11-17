from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    ordering = ['first_name']
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name')
        }), 
        ('Permissões', {
            'classes': ('wide'),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Dados complementares', {
            'classes': ('wide',),
            'fields': ('avatar', 'last_login',),
        }),
    )