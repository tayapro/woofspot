from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.
class WoofspotEvent(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    location = models.CharField(max_length=200)
    event_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    attendees = models.ManyToManyField(User, related_name="events_attending", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name="liked_events", blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_events", default=1)

    def __str__(self):
        return f"Event: {self.title} at {self.location} on {self.event_date}"

    def clean(self):
        # Validate that end time is after start time
        if self.event_end_time <= self.event_start_time:
            raise ValidationError("Event end time must be after the start time.")

        if self.event_date < date.today() or (self.event_date == date.today() and 
         self.event_start_time < datetime.now().time()):
            raise ValidationError("Event cannot be in the past.")

        super().clean()

    def save(self, *args, **kwargs):
        # Generate slug, perform validation and save the object
        if not self.slug:
            self.slug = slugify(self.title)
        self.full_clean()  
        super().save(*args, **kwargs)

    def toggle_like(self, user):
        # Toggle the like status of a user
        if user in self.liked_by.all():
            self.liked_by.remove(user)
        else:
            self.liked_by.add(user)

    def like_count(self):
        # Return the number of likes
        return self.liked_by.count()

    class Meta:
        ordering = ["-event_date", "event_start_time"]
        verbose_name = "Pet-Friendly Event"
