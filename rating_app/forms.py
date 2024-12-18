from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
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

