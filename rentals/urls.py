from django.conf.urls import url

from .views import (
    IndexView,
    DetailView,
    RentalCreateView,
    RentalUpdateView,
    CommentCreateView,
) 

app_name = 'rentals'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name="detail"),
    url(r'^create/$', RentalCreateView.as_view(), name="create"),
    url(r'^(?P<pk>[0-9]+)/update/$', RentalUpdateView.as_view(), name="update"),
    url(r'^(?P<pk>[0-9]+)/comment/$', CommentCreateView.as_view(), name="comment"),
]
