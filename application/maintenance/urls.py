from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar'),
    path('updates/<int:event_id>/', views.maintenance_updates_view, name='maintenance_updates'),
]
