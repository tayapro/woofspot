from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.core.files.uploadedfile import UploadedFile
from cloudinary.uploader import destroy
from datetime import datetime, date, time
from django.contrib.auth.models import User

def title_validation(value):
    if WoofspotEvent.objects.filter(title=value).exists():
        raise ValidationError("An event with this title already exists.")

# Validate that the event date is not in the past
def date_validation(value):
    if value < date.today():
        raise ValidationError("Event date cannot be in the past.")


# Validate event's image file
def file_validation(file):
    min_file_size = 20480 # 20kB
    max_file_size = 1024 * 1024 * 2 # 2mb file
    allowed_types = ['image/png', 'image/gif', 'image/jpg', 'image/jpeg']

    if not file:
        raise ValidationError("No file selected.")

    if isinstance(file, UploadedFile):
        if file.size < min_file_size:
            raise ValidationError("File should be larger than 20kB.")
        if file.size > max_file_size:
            raise ValidationError("File shouldn't be larger than 2MB.")

        if file.content_type not in allowed_types:
            raise ValidationError(f"Invalid image type.")


class WoofspotEvent(models.Model):
    title = models.CharField(max_length=200, unique=True, validators=[title_validation])
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    location = models.CharField(max_length=200)
    event_date = models.DateField(validators=[date_validation])
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    attendees = models.ManyToManyField(User, related_name="events_attending", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name="liked_events", blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_events", default=1)
    image = CloudinaryField('image', folder=settings.CLOUDINARY_UPLOAD_FOLDER, validators=[file_validation], resource_type='auto', blank=True)

    def __str__(self):
        return f"Event: {self.title} at {self.location} on {self.event_date}"

    def clean(self):
        super().clean()

        # Validate that end time is after start time
        if self.event_date < date.today() or (self.event_date == date.today() and 
          self.event_start_time < datetime.now().time()):
            raise ValidationError("Event cannot be in the past")
        if self.event_end_time <= self.event_start_time:
            raise ValidationError("Event end time must be after the start time")

        night_start = time(21, 0)
        night_end = time(9, 0)
        if self.event_start_time >= night_start or self.event_start_time < night_end:
            raise ValidationError("Event start time cannot be between 21:00 and 09:00")

        start_datetime = datetime.combine(datetime.now(), self.event_start_time)
        end_datetime = datetime.combine(datetime.now(), self.event_end_time)
        time_difference = end_datetime - start_datetime

        # 10800 is 3 hours
        if time_difference.total_seconds() > 10800:
            raise ValidationError("Please make sure the event is no longer than three hours")

        if time_difference.total_seconds() < 3600:
            raise ValidationError("The minimum event duration is one hour")

    def save(self, *args, **kwargs):
        # Generate slug, perform validation and save the object
        if not self.slug:
            self.slug = slugify(self.title)
        self.full_clean()  
        super().save(*args, **kwargs)

    def like_toggle(self, user):
        # Toggle the like status of a user
        if user in self.liked_by.all():
            self.liked_by.remove(user)
        else:
            self.liked_by.add(user)

    def like_count(self):
        # Return the number of likes
        return self.liked_by.count()

    def remove_image(self):
        public_id = self.image.public_id
        destroy(public_id, invalidate=True)
        self.image = None
        self.save(update_fields=['image'])

    class Meta:
        ordering = ["-event_date", "event_start_time"]
        verbose_name = "Pet-Friendly Event"


# 1 to 5 stars
RATING_CHOICES = [(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)]

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ratings')
    event = models.ForeignKey(WoofspotEvent, on_delete=models.CASCADE, null=True, related_name='event_ratings')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review_text = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_average_rating(event):
        return event.event_ratings.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return f"Rating: {self.rating} stars by {self.user} for {self.event.title}"

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['event']),
        ]
        verbose_name = "Rating"