from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "form-control form-control-lg",
                'placeholder': "First Name",
            }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control form-control-lg",
                'placeholder': "Last Name",
            }),
        }
