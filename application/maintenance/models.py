from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class MaintenanceEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

class MaintenanceUpdate(models.Model):
    event = models.ForeignKey(MaintenanceEvent, on_delete=models.CASCADE, related_name="updates")
    update_text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Update for {self.event.title} at {self.timestamp}"
