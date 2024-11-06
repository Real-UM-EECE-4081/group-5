from django.contrib import admin
from maintenance.models import MaintenanceEvent, MaintenanceUpdate

# Register your models here.
admin.site.register(MaintenanceEvent)
admin.site.register(MaintenanceUpdate)

class MaintenanceEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time')

class MaintenanceUpdateAdmin(admin.ModelAdmin):
    list_display = ('event', 'timestamp', 'update_text')
