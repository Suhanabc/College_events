from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200)   # single definition
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')  # Prevent duplicate registrations

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"

