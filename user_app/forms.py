from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.utils.safestring import mark_safe

TEXT_STYLES = {
    'class': 'form-control',
    'style': 'min-width: 200px; width: 100%; font-weight: 300;',
}

class MySigninForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({**TEXT_STYLES})
    
    def get_errors_as_single_list(self):
        errors = []
        # Collect field errors
        for field, field_errors in self.errors.items():
            for error in field_errors:
                if field == "__all__":
                    errors.append(f"{error}")
                else:
                    errors.append(f"{field.capitalize()}: {error}")
        return errors


class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({**TEXT_STYLES})

        self.fields['email'].required = True
        self.fields['email'].label = "Email:"