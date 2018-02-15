from django import forms
from django.core.exceptions import ValidationError
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
        fields = ['title','description', 'rent', 'negotiable','photo', 'location',]
        widgets={"photo":forms.FileInput(attrs={'id':'photo','required':True,'multiple':True})}



# class TagForm(forms.ModelForm):

#     class Meta:
#         model = Tag
#         fields = '__all__'

#     def clean_name(self):
#         n = self.cleaned_data['name']
#         if n.lower()=='tag' or n.lower()=='add' or n.lower()=='update':
#             raise ValidationError("Tag name cant be {}".format(n)) 
#         return n

class CommentForm(forms.ModelForm):
    """
    form to add new comment
    """

    class Meta():
        model = Comment
        fields = ['text', 'stars',]

# class FileForm(forms.ModelForm):
#     class Meta():
#         model = Upload
#         fields = '__all__'
#         widgets={"photos":forms.FileInput(attrs={'id':'pic','required':True,'multiple':True})}
