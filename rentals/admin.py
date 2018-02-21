from django.contrib import admin

from .models import Rental, Comment

# Register your models here.

admin.site.register(Rental)
admin.site.register(Comment)
