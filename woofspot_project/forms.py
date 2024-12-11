from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.utils.safestring import mark_safe


class MySigninForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control text-body-secondary text-opacity-75'})
            if field.label:
                field.label = mark_safe(f'<span class="form-label text-body-secondary text-opacity-75">{field.label}</span>')



class MySignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username'),
            Field('email'),
            Field('password1'),
            Field('password2'),
        )
        self.fields['username'].widget.attrs.update({'class': 'form-control text-body-secondary text-opacity-75'})
        self.fields['email'].widget.attrs.update({'class': 'form-control text-body-secondary text-opacity-75'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control text-body-secondary text-opacity-75'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control text-body-secondary text-opacity-75'})