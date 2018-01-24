from django.conf.urls import url

from .views import (
    IndexView,
    DetailView,
    RentalCreateView,
) 

app_name = 'rentals'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name="detail"),
    url(r'^create/$', RentalCreateView.as_view(), name="create"),
]
