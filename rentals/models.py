from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


User = settings.AUTH_USER_MODEL


from taggit.managers import TaggableManager

# Create your models here.

class RentalQuerySet(models.query.QuerySet):
    """
    QuerySet class for Rental model
    this class is used for costom QuerySet while querying database
    """
    def search(self, query):
        """
        this function queries the database for search functionality in index view
        """
        return self.filter(
                Q(title__icontains=query)|
                Q(author__username__icontains=query)|
                Q(description__icontains=query)|
                Q(location__icontains=query)|
                Q(tags__name__icontains=query)
            ).distinct()


class RentalManager(models.Manager):
    """
    Rental Manager class
    this class makes querying the database easy
    """

    def get_queryset(self):
        """
        get queryset for the rental model
        """
        return RentalQuerySet(self.model, using=self._db)

    def search(self, query):
        """
        manage search functionality of the index view
        """
        return self.get_queryset().search(query)


class Rental(models.Model):
    """
    Rental model
    contains author, title, discription, created_date, rent
    negotiable whis is a boolean value

    """

    author          = models.ForeignKey(User)
    title           = models.CharField(max_length=128)
    description     = models.TextField(max_length=4096, blank=True, null=True)
    created_date    = models.DateTimeField(default=timezone.now)
    rent            = models.BigIntegerField(default=0)
    photo           = models.FileField(upload_to='photos/', blank=True, null=True)
    location        = models.CharField(max_length=256, blank=True, null=True)
    rating          = models.FloatField(default=0)

    tags = TaggableManager()

    objects = RentalManager()


    def __str__(self):
        """
        str function for rental model 
        returns title of the rental
        """
        if len(self.title) <= 25:
            return self.title[:25]

    def get_rating(self):
        pass;


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


    rental          = models.ForeignKey('Rental', related_name='comments')
    author          = models.ForeignKey(User)
    text            = models.TextField(max_length=1024)
    stars           = models.IntegerField(
                            default=1,
                            validators=[
                                MaxValueValidator(5),
                                MinValueValidator(1)
                            ]
                    )
    created_date    = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """
        str function for comment
        returns comment text
        """
        return self.text
