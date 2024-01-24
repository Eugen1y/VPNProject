from django.contrib import admin

from website.models import Site


@admin.register(Site)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'url']
