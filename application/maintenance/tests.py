from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import MaintenanceEvent, MaintenanceUpdate


class MaintenanceViewTests(TestCase):
    def setUp(self):

        self.admin_user = User.objects.create_user(username='TestAdmin', password='testpassword')

        self.active_event = MaintenanceEvent.objects.create(
            title="Server Maintenance",
            description="Description for currently active server Maintenance.",
            start_time=timezone.now() - timezone.timedelta(hours=1),
            end_time=timezone.now() + timezone.timedelta(hours=1),
        )

        self.upcoming_event = MaintenanceEvent.objects.create(
            title="Database Migration",
            description="Description for upcoming server Maintenance.",
            start_time=timezone.now() + timezone.timedelta(days=1),
            end_time=timezone.now() + timezone.timedelta(days=1, hours=1),
        )

        # Add updates to the events
        MaintenanceUpdate.objects.create(
            event=self.active_event,
            update_text="Active event update.",
            admin=self.admin_user
        )

    def test_calendar_view_status_code(self):

        response = self.client.get(reverse('calendar'))
        self.assertEqual(response.status_code, 200)

    def test_active_event_displayed_first(self):

        response = self.client.get(reverse('calendar'))
        self.assertContains(response, "Server Maintenance")
        self.assertContains(response, "Database Migration")

        active_index = response.content.decode().find("Server Maintenance")
        upcoming_index = response.content.decode().find("Database Migration")
        self.assertLess(active_index, upcoming_index, "Active events should appear before upcoming events")

    def test_latest_update_displayed_for_event(self):

        response = self.client.get(reverse('calendar'))

        self.assertContains(response, "Active event update.")

        self.assertContains(response, "No updates available")

    def test_upcoming_event_no_update(self):

        response = self.client.get(reverse('calendar'))
        self.assertContains(response, "No updates available")
