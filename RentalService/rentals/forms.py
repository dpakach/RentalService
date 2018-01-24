from django import forms

from .models import Rental


class RentalCreateForm(forms.ModelForm):
    
    class Meta():
        model = Rental
        fields = ['title','description', 'rent', 'negotiable']
