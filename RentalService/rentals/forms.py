from django import forms

from .models import Rental


class RentalCreateForm(forms.ModelForm):
    """
    Form to create new Rental
    This form creates new rental
    """
    
    class Meta():
        model = Rental
        fields = ['title','description', 'rent', 'negotiable']
