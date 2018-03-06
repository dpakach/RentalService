from django.conf.urls import url

from .views import (
    IndexView,
    DetailView,
    RentalCreateView,
    RentalUpdateView,
    CommentCreateView,
    intrested_in_rental,
    search_api,
    loc_api,
) 

app_name = 'rentals'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name="detail"),
    url(r'^create/$', RentalCreateView.as_view(), name="create"),
    url(r'^(?P<pk>[0-9]+)/update/$', RentalUpdateView.as_view(), name="update"),
    url(r'^(?P<pk>[0-9]+)/comment/$', CommentCreateView.as_view(), name="comment"),
    url(r'^(?P<pk>[0-9]+)/intrested/$', intrested_in_rental, name="intrested"),
    url(r'^ajax/search/$', search_api, name="search"),
    url(r'^ajax/(?P<pk>[0-9]+)/loc/$', loc_api, name="loc"),
]
