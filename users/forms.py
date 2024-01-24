from django import forms

from users.models import CustomUser

from django.contrib.auth.forms import UserCreationForm



class UserSignUpForm(UserCreationForm):
    """User registration form implementation"""

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2', ]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            'description'
        ]
        widgets = {'password': forms.PasswordInput(),
                   'description': forms.Textarea()}


class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email','description']
        widgets = {'password': forms.PasswordInput(),
                   'description' : forms.Textarea()}

