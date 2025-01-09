from django import forms
from .models import WoofspotEvent
from .models import Rating
from django.forms.widgets import ClearableFileInput

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
            'content', 
            'location',
            'event_date',
            'event_start_time',
            'event_end_time',
            'image',
        ]
        labels = {
            'title': 'Title',
            'content': 'Description',
            'location': 'Location',
            'event_date': 'Date',
            'event_start_time': 'From',
            'event_end_time': 'To',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                **TEXT_STYLES,  
                'placeholder': 'Enter event title',
            }),
            'content': forms.Textarea(attrs={
                **TEXT_STYLES, 
                'rows': 5,
                'placeholder': 'Enter description for your event',
            }),
            'location': forms.TextInput(attrs={
                **TEXT_STYLES,  
                'placeholder': 'Enter event location',
            }),
            'event_date': forms.DateInput(attrs={
                **DATE_TIME_STYLES,  
                'type': 'date',
            }),
            'event_start_time': forms.TimeInput(attrs={
                **DATE_TIME_STYLES,  
                'type': 'time',
            }),
            'event_end_time': forms.TimeInput(attrs={
                **DATE_TIME_STYLES,  
                'type': 'time',
            }),
            'image': CustomClearableFileInput(attrs={
                'class': 'form-control custom-clearable-file-input',
                'accept': 'image/*',
            }),
        }


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
        if not rating:
            raise ValidationError("Please select a rating.")

        return self.cleaned_data