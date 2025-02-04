from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser 

class ReistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('email', 'phone_number', 'address', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser 
        fields = ('email', 'password')