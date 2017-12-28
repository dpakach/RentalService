from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.


class Rental(models.Model):
    
    # Rental class  

    author = models.ForeignKey('User')
    title = models.CharField(max_length=128)
    discription = models.CharField(max_length=1024)
    created_date = models.DateTimeField(default=timezone.now())
    rent = models.BigIntegerField()
    negotiable = models.BooleanField()

    def __str__(self):
        return self.title



class Comment(models.Model):

    # Commnts for Rentals with star reviews

    rental = Post.ForeignKey('rental.Rental', related_name='comments')
    author = models.ForeignKey('User')
    text = models.CharField(max_length=256)
    stars = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.text
