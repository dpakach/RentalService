from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse

# Create your models here.


class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    full_name   = models.CharField(max_length=128, blank=True)
    bio         = models.TextField(max_length=1024, blank=True) 
    birth_date  = models.DateField(null=True, blank=True)
    pic         = models.FileField(upload_to='photos/user/', blank=True, null=True)


    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        """
        returns absolute url for each rental object
        for eg /rentals/pk/
        where pk is primary key
        """
        return reverse('profiles:detail', kwargs={'username':self.user.username})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if-created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
