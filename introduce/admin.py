from django.contrib import admin

from introduce.models import AccessLog
from django.contrib import admin

# Register your models here.
@admin.register(AccessLog)
class AccessLog(admin.ModelAdmin):
    created_display = ('created_at')
    location_diplay = ('location')