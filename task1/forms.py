from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EditForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]
