"""
Forms for the `user_app`.

This module customizes forms provided by the `allauth` library 
for user authentication and registration.
It includes styling enhancements and additional 
configurations for form fields.
"""
from allauth.account.forms import LoginForm, SignupForm

# Common styles applied to all form fields
TEXT_STYLES = {
    'class': 'form-control',
    'style': 'min-width: 200px; width: 100%; font-weight: 300;',
}


class MySigninForm(LoginForm):
    """
    Custom Sign-in Form.

    Extends the default `allauth` LoginForm to apply consistent styling 
    to all form fields using the `TEXT_STYLES` dictionary.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply common styles to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({**TEXT_STYLES})


class MySignupForm(SignupForm):
    """
    Custom Sign-up Form.

    Extends the default `allauth` SignupForm to:
    - Apply consistent styling to all form fields using 
      the `TEXT_STYLES` dictionary.
    - Mark the email field as required and update its label.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply common styles to all form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({**TEXT_STYLES})

        # Enforce that the email field is required and update its label
        self.fields['email'].required = True
        self.fields['email'].label = "Email:"
