from .views import ProfileDetailview, ProfileUpdateView

from django.conf.urls import url

app_name='profiles'

urlpatterns = [
    url(r'^update/$', ProfileUpdateView.as_view(), name='update'),
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailview.as_view(), name='detail'),
]
