from django import forms
from .models import WoofspotEvent

class EventOrganizerForm(forms.ModelForm):
    class Meta:
        model = WoofspotEvent
        fields = ['title', 
                  'content', 
                  'location',
                  'event_date',
                  'event_start_time',
                  'event_end_time'
                ]
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'event_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'event_end_time': forms.TimeInput(attrs={'type': 'time'}),
            }