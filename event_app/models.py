from django.db import models

# Create your models here.
class WoofspotEvent(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    location = models.CharField(max_length=200, unique=True)
    event_date = models.DateField()
    event_time = models.TimeField()
    duration = models.DurationField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Event: {self.title} at {self.location} on {self.event_date}"

    class Meta:
        ordering = ["-event_date", "event_time"]
        verbose_name = "Pet-Friendly Event"
