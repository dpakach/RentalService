from django import forms
from django.forms import Textarea

from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name", "bio", "birth_date", "phone_number", "profession", "pic"]
        widgets = {
            "birth_date": forms.DateInput(attrs={"class": "datepicker", "type": "date"})
        }
