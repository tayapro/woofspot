from django import forms
from django.forms.widgets import ClearableFileInput
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, MinLengthValidator
from datetime import date, timedelta

from .models import WoofspotEvent, Rating

# Reusable styles for consistent form styling
TEXT_STYLES = {
    'class': 'form-control',
    'style': 'min-width: 200px; width: 100%;',
}

DATE_TIME_STYLES = {
    'class': 'form-control',
    'style': 'width: auto; max-width: 150px;',
}

class CustomClearableFileInput(ClearableFileInput):
    """
    Custom file input widget that uses a custom template for file uploads.
    """

    template_name = "event_app/custom_clearable_file_input.html"


class EventHostForm(forms.ModelForm):
    """
    A form for creating and editing events.

    This form maps to the WoofspotEvent model and includes custom widgets
    and validations. It allows users to input event details like title, 
    description, location, date, and time, with validations for fields 
    like title, description, and location.
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
        Specifies the associated model, fields, 
        labels, and widgets for the EventHostForm.
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
                'class': 'w-100 form-control custom-clearable-file-input',
                'accept': 'image/*',
            }),
        }


class ReviewForm(forms.ModelForm):
    """
    A form for submitting a review and rating for an event.

    Fields:
        - rating: A required field to select a rating from 1 to 5 stars.
        - review_text: An optional field for providing textual feedback about the event.
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
        Specifies the associated model, 
        fields, labels, and validation for the ReviewForm.
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
        ReviewForm requires an event to be passed when the form is initialized.
        """

        # Get 'event' from kwargs if provided.
        self.event = kwargs.pop('event', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        """
        Custom validation to ensure the rating is provided and review text 
        is processed.

        Raises:
            ValidationError if no rating is provided.
        """
        rating = self.cleaned_data.get('rating')

        # Ensure the rating is provided
        if not rating:
            raise ValidationError("Please select a rating.")

        review_text = self.cleaned_data.get('review_text')

        return self.cleaned_data


class ContactUsForm(forms.Form):
    """
    A form for submitting inquiries or feedback via the Contact Us page.

    Fields:
        - name: Required field for the user's name (min length: 2, max length: 100)
        - email: Required field for a valid email address.
        - comment: Required field for submitting a message (min length: 5).
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
