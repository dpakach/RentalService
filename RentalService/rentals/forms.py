from django import forms

from .models import Rental, Comment


class RentalCreateForm(forms.ModelForm):
    
    class Meta():
        model = Rental
        fields = ['title','description', 'rent', 'negotiable']

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ['text', 'stars']
