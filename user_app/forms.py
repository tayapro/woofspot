from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.utils.safestring import mark_safe
from django import forms

TEXT_STYLES = {
    'class': 'form-control',
    'style': 'min-width: 200px; width: 100%; font-weight: 300;',
}

class MySigninForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({**TEXT_STYLES})
    

class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({**TEXT_STYLES})

        self.fields['email'].required = True
        self.fields['email'].label = "Email:"


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your name",
        }),
        label="Name"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email",
        }),
        label="E-mail"
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4,
            "placeholder": "Enter your message",
        }),
        label="Comment"
    )
