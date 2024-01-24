from django.contrib import admin

from website.models import Site, DataSize


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'url']


@admin.register(DataSize)
class DataSizeAdmin(admin.ModelAdmin):
    list_display = ['website','sent_data_size', 'received_data_size']
