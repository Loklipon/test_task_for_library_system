from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('email', 'last_name', 'first_name', 'phone_number', 'organization')
    search_fields = ('last_name', 'first_name', 'email', 'phone_number', 'organization__title')
    list_filter = ('organization__title',)
