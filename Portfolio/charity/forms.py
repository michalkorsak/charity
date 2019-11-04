from django.contrib.auth.forms import UserCreationForm, UsernameField
from registration.forms import User
from django import forms

"""
django default user
"""


class UserCreationFormExtended(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='username', widget=forms.TextInput(attrs={'placeholder': 'login'}))
    password = forms.CharField(max_length=50, label='hasło', widget=forms.PasswordInput(attrs={'placeholder': 'hasło'}))


