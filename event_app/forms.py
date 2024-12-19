from django import forms
from .models import WoofspotEvent
from .models import Rating

# Reusable styles
COMMON_TEXT_STYLES = {
    'class': 'form-control',
    'style': 'min-width: 200px; width: 100%;',
}

DATE_TIME_STYLES = {
    'class': 'form-control',
    'style': 'width: auto; max-width: 200px;',
}

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
                **COMMON_TEXT_STYLES,  
                'placeholder': 'Enter event title',
            }),
            'content': forms.Textarea(attrs={
                **COMMON_TEXT_STYLES, 
                'rows': 5,
                'placeholder': 'Enter description for your event',
            }),
            'location': forms.TextInput(attrs={
                **COMMON_TEXT_STYLES,  
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
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

    def __init__(self, *args, **kwargs):
        # Pass event to the form
        self.event = kwargs.pop('event', None)  # Get the event from the kwargs
        super().__init__(*args, **kwargs)

    def save(self, user, commit=True):
        # Override the save method to include the user
        rating = super().save(commit=False)
        rating.user = user  # Set the user
        rating.event = self.event  # Set the event
        if commit:
            rating.save()
        return rating