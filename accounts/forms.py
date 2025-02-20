from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control w-100"}),
        label="Password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control w-100"}),
        label="Confirm Password",
    )

    class Meta:
        model = CustomUser
        fields = ["email", "fullname", "phone", "password1", "password2"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control w-100"}),
            "fullname": forms.TextInput(attrs={"class": "form-control w-100"}),
            "phone": forms.TextInput(attrs={"class": "form-control w-100"}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2


class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control w-100"}), label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control w-100"}),
        label="Password",
    )


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "fullname", "phone"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control w-100"}),
            "fullname": forms.TextInput(attrs={"class": "form-control w-100"}),
            "phone": forms.TextInput(attrs={"class": "form-control w-100"}),
        }



