from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate',
                                                       'placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')

    username = forms.CharField(max_length=15,
                               required=True,
                               help_text='Required. 15 char max.',
                               widget=forms.TextInput(attrs={'placeholder': '  Username'}))
    first_name = forms.CharField(max_length=30,
                                 required=True,
                                 help_text='Required',
                                 widget=forms.TextInput(attrs={'placeholder': '  First Name'}))
    email = forms.EmailField(max_length=100,
                             required=True,
                             help_text="Required. Provide a valid email address.",
                             widget=forms.TextInput(attrs={'placeholder': '  Email Address'}))
    password1 = forms.CharField(max_length=30,
                                required=True,
                                help_text="Password",
                                widget=forms.PasswordInput(attrs={'placeholder': '  Password'}))
    password2 = forms.CharField(max_length=30,
                                required=True,
                                help_text="Retype Password",
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': '  Confirm Password'}))
