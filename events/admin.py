from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ('title', 'get_organizations', 'image_thumbnail', 'date')
    search_fields = ('title', 'description', 'date', 'organizations__title')
    list_filter = ('title', 'date', 'organizations__title')

    def get_organizations(self, obj):
        return ', '.join([org.title for org in obj.organizations.all()])

    get_organizations.short_description = 'Organizations'
