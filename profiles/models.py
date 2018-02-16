from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

# Create your models here.


class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    full_name       = models.CharField(max_length=128, blank=True, null=True)
    bio             = models.TextField(max_length=1024, blank=True, null=True) 
    birth_date      = models.DateField(null=True, blank=True)
    profession      = models.CharField(max_length=128, blank=True, null=True)
    pic             = models.FileField(upload_to='photos/user/', blank=True, null=True)
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Phone number must be in format +9999999999')
    phone_number    = models.CharField(validators=[phone_regex], max_length=17, blank=True)


    def __str__(self):
        return self.user.username

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
    instance.user_profile.save()
