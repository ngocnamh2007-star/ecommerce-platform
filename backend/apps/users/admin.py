"""
User admin
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """Custom user admin"""
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Thông tin bổ sung', {
            'fields': (
                'phone', 'avatar', 'gender', 'date_of_birth',
                'address', 'city', 'state', 'postal_code', 'country',
                'is_verified', 'is_seller'
            )
        }),
    )
    
    list_display = ['username', 'email', 'get_full_name', 'phone', 'is_seller', 'is_active', 'date_joined']
    list_filter = ['is_seller', 'is_verified', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone']
