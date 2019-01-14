from .views import ProfileDetailView, ProfileUpdateView

from django.conf.urls import url

app_name = "profiles"

urlpatterns = [
    url(r"^update/$", ProfileUpdateView.as_view(), name="update"),
    url(r"^$", ProfileDetailView.as_view(), name="user_detail"),
    url(r"^(?P<username>[\w-]+)/$", ProfileDetailView.as_view(), name="detail"),
]
