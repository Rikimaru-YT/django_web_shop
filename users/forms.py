from django import forms

from .models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control p-4',
        'placeholder': 'Username',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control p-4',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control p-4',
        'placeholder': 'Confirm Password',
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'avatar', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control p-4',
                'placeholder': 'Email',
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
            })
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control p-4',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control p-4',
        'placeholder': 'Password',
    }))
    class Meta:
        model = User
        fields = ['username', 'password']