from django import forms
from allauth.account.forms import ResetPasswordForm


class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control text-body-secondary text-opacity-75',
            'style': 'min-width: 300px; width: 100%;',
            'placeholder': 'Email address'
        })
