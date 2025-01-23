from django import forms
from django.forms.widgets import ClearableFileInput
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, MinLengthValidator
from datetime import date, timedelta

from .models import WoofspotEvent, Rating

# Reusable styles
TEXT_STYLES = {
    'class': 'form-control',
    'style': 'min-width: 200px; width: 100%;',
}

DATE_TIME_STYLES = {
    'class': 'form-control',
    'style': 'width: auto; max-width: 150px;',
}


# Custom template
class CustomClearableFileInput(ClearableFileInput):
    template_name = "event_app/custom_clearable_file_input.html"


class EventHostForm(forms.ModelForm):
    """
    Form for creating and editing events.
    Maps to the WoofspotEvent model and includes custom widgets
    and validations.
    """

    # Title field with custom widget and validation
    title = forms.CharField(
        validators=[MinLengthValidator(5)],
        widget=forms.TextInput(attrs={
            **TEXT_STYLES,
            'placeholder': 'Enter event title',
        })
    )

    # Description field with custom widget and validation
    description = forms.CharField(
        validators=[MinLengthValidator(5)],
        widget=forms.Textarea(attrs={
            **TEXT_STYLES,
            'rows': 5,
            'placeholder': 'Enter description for your event',
        })
    )

    # Location field with custom widget and validation
    location = forms.CharField(
        validators=[MinLengthValidator(5)],
        widget=forms.TextInput(attrs={
            **TEXT_STYLES,
            'placeholder': 'Enter event location',
        })
    )

    class Meta:
        """
        Metadata for the EventHostForm.
        Specifies the associated model and its fields.
        """
        model = WoofspotEvent
        fields = [
            'title',
            'description',
            'location',
            'date',
            'start_time',
            'end_time',
            'image',
        ]
        labels = {
            # Labels for form fields
            'title': 'Title',
            'description': 'Description',
            'location': 'Location',
            'date': 'Date',
            'start_time': 'From',
            'end_time': 'To',
        }
        widgets = {
            # Custom widgets for consistent styling and enhanced usability
            'date': forms.DateInput(attrs={
                **DATE_TIME_STYLES,
                'type': 'date',
                # Restricts date selection to start from tomorrow
                'min': (date.today() + timedelta(days=1)).isoformat(),
            }),
            'start_time': forms.TimeInput(attrs={
                **DATE_TIME_STYLES,
                'type': 'time',
            }),
            'end_time': forms.TimeInput(attrs={
                **DATE_TIME_STYLES,
                'type': 'time',
            }),
            'image': CustomClearableFileInput(attrs={
                'class': 'form-control custom-clearable-file-input',
                'accept': 'image/*',
            }),
        }


class ReviewForm(forms.ModelForm):
    """
    Form for submitting a review and rating for an event.
    Fields:
        - rating: A required field to select a rating from 1 to 5 stars.
        - review_text: An optional field to add a textual review of the event.
    """

    review_text = forms.CharField(
        required=False,
        label="Add a review",
        widget=forms.Textarea(attrs={
            **TEXT_STYLES,
            'rows': 5,
            'placeholder': 'Write your review here...',
        })
    )

    class Meta:
        """
        Metadata for the ReviewForm.
        Specifies the associated model and its fields.
        """

        model = Rating
        fields = [
            'rating',
            'review_text'
        ]
        labels = {
            'rating': 'Overall rating',
        }
        error_messages = {
            # Message shown if no rating is provided.
            'rating': {
                'required': "Please select a rating.",
            },
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form, optionally associating it with a specific event.
        ReviewForm requires a specific event to be passed when the
        form is initialized.
        """

        # Get 'event' from kwargs if provided.
        self.event = kwargs.pop('event', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        """
        Custom validation for the form.
        Ensures that the rating is present and processes the review text
        if necessary.
        """
        rating = self.cleaned_data.get('rating')

        # Ensure the rating is provided
        if not rating:
            raise ValidationError("Please select a rating.")

        review_text = self.cleaned_data.get('review_text')

        return self.cleaned_data


class ContactUsForm(forms.Form):
    """
    Form for users to submit inquiries or feedback via the Contact Us page.
    Fields:
        - name: Required. The name of the user (min length: 2, max length: 100)
        - email: Required. A valid email address.
        - comment: Required. A message or feedback (min length: 5).
    """
    name = forms.CharField(
        required=True,
        max_length=100,
        validators=[MinLengthValidator(2)],
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your name",
        }),
        label="Name:"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email",
        }),
        label="E-mail:"
    )
    comment = forms.CharField(
        validators=[MinLengthValidator(5)],
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4,
            "placeholder": "Enter your message...",
        }),
        label="Comment:"
    )
