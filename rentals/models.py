from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.


class Rental(models.Model):
    """
    Rental model
    contains author, title, discription, created_date, rent
    negotiable whis is a boolean value

    """

    # author = models.ForeignKey('User')
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    rent = models.BigIntegerField()
    negotiable = models.BooleanField()
    photo = models.FileField(upload_to='photos/', blank=True, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)


    def __str__(self):
        """
        str function for rental model 
        returns title of the rental
        """
        return self.title

    def get_absolute_url(self):
        """
        returns absolute url for each rental object
        for eg /rentals/pk/
        where pk is primary key
        """
        return reverse('rentals:detail', kwargs={'pk':self.pk})



class Comment(models.Model):
    """
    Comment model for the rentals 
    contains text, author,created_date and stars as in star review
    connected to a rental through a ForeignKey
    """


    rental = models.ForeignKey('Rental', related_name='comments')
    # author = models.ForeignKey('User')
    text = models.TextField(max_length=256)
    stars = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """
        str function for comment
        returns comment text
        """
        return self.text
