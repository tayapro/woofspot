from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from event_app.models import WoofspotEvent

# 1 to 5 stars
RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ratings')
    event = models.ForeignKey(WoofspotEvent, on_delete=models.CASCADE, related_name='event_ratings')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_average_rating(event):
        return event.event_ratings.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return f"{self.user} rated {self.event} - {self.rating} stars"

    class Meta:
        unique_together = ('user', 'event')  # Prevent duplicates
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['event']),
        ]
        verbose_name = "Rating"
