from django import forms
from django.forms.widgets import ClearableFileInput
from cloudinary.forms import CloudinaryJsFileField
from datetime import date, timedelta
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, MinLengthValidator
from .models import WoofspotEvent
from .models import Rating

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


class EventOrganizerForm(forms.ModelForm):
    class Meta:
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
            'title': 'Title',
            'description': 'Description',
            'location': 'Location',
            'date': 'Date',
            'start_time': 'From',
            'end_time': 'To',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                **TEXT_STYLES,  
                'placeholder': 'Enter event title',
            }),
            'description': forms.Textarea(attrs={
                **TEXT_STYLES, 
                'rows': 5,
                'placeholder': 'Enter description for your event',
            }),
            'location': forms.TextInput(attrs={
                **TEXT_STYLES,  
                'placeholder': 'Enter event location',
            }),
            'date': forms.DateInput(attrs={
                **DATE_TIME_STYLES,  
                'type': 'date',
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
        image = CloudinaryJsFileField(
        attrs={'style': "margin-top: 30px"},
        options={
            'tags': "directly_uploaded",
            'crop': 'limit', 'width': 1000, 'height': 1000,
            'eager': [{'crop': 'fill', 'width': 150, 'height': 100}]
        })
        

class ReviewForm(forms.ModelForm):
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
        model = Rating
        fields = [
            'rating', 
            'review_text'
        ]
        labels = {
            'rating': 'Overall rating',
        }
        error_messages = {
            'rating': {
                'required': "Please select a rating.",
            },
        }
    
    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event', None)  
        super().__init__(*args, **kwargs)

    def clean(self):
        rating = self.cleaned_data.get('rating')
        review_text = self.cleaned_data.get('review_text')
        
        return self.cleaned_data


def validate_name(value):
    """Ensure name is not empty or only spaces."""

    if not value.strip():
        raise ValidationError("Name cannot be empty or spaces.")

def validate_comment(value):
    """Ensure comment is more than 2 characters and not just spaces."""
    
    if len(value.strip()) <= 2:
        raise ValidationError("Comment must be more than 2 characters and cannot be just spaces.")


class ContactUsForm(forms.Form):
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
