from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, UpdateView, TemplateView
from django.http import Http404

from .forms import ProfileForm
from .models import Profile
from rentals.models import Rental

User = get_user_model()

# Create your views here.


class ProfileDetailView(DetailView):
    template_name = "profiles/user.html"

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            username = self.request.user.username
        user = get_object_or_404(User, username__iexact=username, is_active=True)
        return user.user_profile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        user = self.get_object().user
        query = self.request.GET.get("uq")
        rentals_exists = Rental.objects.filter(author=user)
        qs = Rental.objects.filter(author=user)
        if query:
            qs = qs.search(query)
        if rentals_exists and qs.exists():
            context["rentals"] = qs
        if self.request.user.is_authenticated and self.request.user.intrested_rentals:
            qs = self.request.user.intrested_rentals.order_by("-rating")
            query = self.request.GET.get("int_uq")
            if query:
                qs = qs.search(query)
            context["intrested_rentals"] = qs
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = "profiles/update.html"

    def get_object(self):
        user = self.request.user
        return user.user_profile

    def get_queryset(self):
        """
        this method return the profile object to update in the UpdateView
        """
        user = self.request.user
        return user
