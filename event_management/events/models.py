from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="events")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="events")
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_events")
    capacity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def is_upcoming(self):
        return self.date_time > timezone.now()

    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ['event', 'participant']
