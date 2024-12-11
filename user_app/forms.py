from allauth.account.forms import LoginForm
from django import forms

class MySigninForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['login'].widget.attrs.update({'class': 'form-control text-body-secondary text-opacity-75'})
        # self.fields['password'].widget.attrs.update({'class': 'form-control text-body-secondary text-opacity-75'})
