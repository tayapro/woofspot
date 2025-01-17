from allauth.account.forms import LoginForm, SignupForm


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