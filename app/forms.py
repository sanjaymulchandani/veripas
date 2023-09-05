from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserDetails

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control w-150', 'placeholder': 'Username'},
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control w-150', 'placeholder': 'Email'},
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control w-150', 'placeholder': 'Password'},
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control w-150', 'placeholder': 'Confirm Password'},
        )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control w-150', 'placeholder': 'Username'},
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control w-150', 'placeholder': 'Password'},
        )

    class Meta:
        model = User
        fields = ['username', 'password']

class UserDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control w-50', 'placeholder': 'Name'},
        )
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control w-50', 'placeholder': 'Username (optional)'},
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control w-50', 'placeholder': 'Password'},
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control w-50', 'placeholder': 'Email (optional)'},
        )
    class Meta:
        model = UserDetails
        fields = ['name','username', 'password', 'email']