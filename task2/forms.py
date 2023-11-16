from django import forms
from django.forms.widgets import FileInput

from .models import Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            "profile_img": FileInput(),
        }
