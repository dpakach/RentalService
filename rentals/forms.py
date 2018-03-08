from django import forms

from django.forms import Textarea

from .models import Rental, Comment


class RentalCreateForm(forms.ModelForm):
    """
    Form to create new Rental
    This form creates new rental
    """

    def __init__(self, *args, **kwargs):
        super(RentalCreateForm, self).__init__(*args, **kwargs)
    
    class Meta():
        model = Rental
        fields = ['title','description', 'rent', 'photo', 'location', 'tags']


class CommentForm(forms.ModelForm):
    """
    form to add new comment
    """

    class Meta():
        model = Comment
        fields = ['text', 'stars',]

        widgets = {
            'text': Textarea(attrs={'class': 'reviews__form__textarea', 'placeholder': 'Write a review'}),
            'stars': forms.NumberInput(
                attrs={'class': 'reviews__form__star' },
            )
        }

