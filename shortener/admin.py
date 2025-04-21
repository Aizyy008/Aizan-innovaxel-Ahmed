from django.contrib import admin
from .models import URL

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'short_code', 'created_at', 'updated_at', 'access_count')
    search_fields = ('url', 'short_code')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'short_code', 'access_count')
    ordering = ('-created_at',)
