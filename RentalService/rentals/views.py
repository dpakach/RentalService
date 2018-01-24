from django.shortcuts import render
from django.views import generic

from .models import Rental

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'rentals/index.html'
    context_object_name = 'new_rentals_list'

    def get_queryset(self):

        return Rental.objects.order_by('-created_date')[:10]


class DetailView(generic.DetailView):
    model = Rental
    template_name = 'rentals/detail.html'
