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


def date_validation(value):
    """
    Ensure the event date is not set in the past.
    Raises:
        ValidationError: If the date is earlier than tomorrow.
    """

    if value <= date.today():
        raise ValidationError("Event date cannot be in the past.")


def file_validation(file):
    """
    Validate the uploaded image file.
    Ensures the file size and type meet specified requirements.
    Raises:
        ValidationError: If the file is invalid.
    """

    min_file_size = 20480  # Minimum file size: 20KB
    max_file_size = 1024 * 1024 * 2  # Maximum file size: 2MB
    allowed_types = ['image/png', 'image/jpg', 'image/jpeg']

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
    """
    Represents an event with details like title, location, and time.
    Allows for attendee and organizer tracking.
    """

    title = models.CharField(max_length=55, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=50)
    date = models.DateField(validators=[date_validation])
    start_time = models.TimeField()
    end_time = models.TimeField()
    attendees = models.ManyToManyField(User, related_name="events_attending",
                                       blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name="liked_events",
                                      blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="organized_events", default=1)
    image = CloudinaryField('image', folder=settings.CLOUDINARY_UPLOAD_FOLDER,
                            validators=[file_validation],
                            resource_type='auto', blank=True)

    def __str__(self):
        """
        Return a human-readable string representation of the event.
        """
        return f"Event: {self.title} at {self.location} on {self.date}"

    def clean(self):
        """
        Perform model-level validation for event timing.
        Ensures start and end times are valid and within
        specified constraints.
        """

        super().clean()

        if self.date < date.today() or (self.date == date.today() and
           self.start_time < datetime.now().time()):
            raise ValidationError("Event cannot be in the past")
        if self.end_time <= self.start_time:
            raise ValidationError("Event end time must be after " +
                                  "the start time")

        night_start = time(21, 0)
        night_end = time(9, 0)
        if self.start_time >= night_start or self.start_time < night_end:
            raise ValidationError("Event start time cannot be between " +
                                  "21:00 and 09:00")

        start_datetime = datetime.combine(datetime.now(), self.start_time)
        end_datetime = datetime.combine(datetime.now(), self.end_time)
        time_difference = end_datetime - start_datetime

        # 10800 is 3 hours
        if time_difference.total_seconds() > 10800:
            raise ValidationError("Please make sure the event is no longer " +
                                  "than three hours")

        if time_difference.total_seconds() < 3600:
            raise ValidationError("The minimum event duration is one hour")

    def save(self, *args, **kwargs):
        """
        Automatically generate a slug based on the title before saving.
        """

        if not self.slug:
            self.slug = slugify(self.title)
        self.full_clean()
        super().save(*args, **kwargs)

    def like_toggle(self, user):
        """
        Toggle like status for the given user.
        """

        if user in self.liked_by.all():
            self.liked_by.remove(user)
        else:
            self.liked_by.add(user)

    def like_count(self):
        """
        Return the total number of likes for the event.
        """

        return self.liked_by.count()

    def remove_image(self):
        """
        Remove the event image from Cloudinary and unset the image field.
        """

        public_id = self.image.public_id
        destroy(public_id, invalidate=True)
        self.image = None
        self.save(update_fields=['image'])

    class Meta:
        """
        Metadata for the WoofspotEvent model.

        - Default ordering by creation timestamp in descending order.
        - Name for the admin panel.
        """
        ordering = ["-date", "start_time"]
        verbose_name = "The Event"


# Define choices for a 1 to 5 star rating
RATING_CHOICES = [(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)]


class Rating(models.Model):
    """
    Represents a user's rating and optional review for an event.
    Includes metadata for creation and update timestamps.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_ratings')
    event = models.ForeignKey(WoofspotEvent, on_delete=models.CASCADE,
                              null=True, related_name='event_ratings')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review_text = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_average_rating(event):
        """
        Calculate the average rating for the specified event.
        Parameters:
            event: The event for which to calculate the average rating.
        Returns:
            float: The average rating for the event,
                   or None if no ratings exist.
        """

        return event.event_ratings.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        """
        Return a human-readable string representation of the rating.
        """

        return (f"Rating: {self.rating} stars by {self.user} for "
                f"{self.event.title}")

    class Meta:
        """
        Metadata for the Rating model.
        - Default ordering by creation timestamp in descending order.
        - Database indexes on user and event fields for optimized querying.
        - Name for the admin panel.
        """

        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['event']),
        ]
        verbose_name = "Rating"
