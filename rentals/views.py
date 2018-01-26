from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse

from .models import Rental, Comment
from .forms import RentalCreateForm
from .forms import CommentForm


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'rentals/index.html'
    context_object_name = 'new_rentals_list'

    def get_queryset(self):

        return Rental.objects.order_by('-created_date')[:10]


class DetailView(generic.DetailView):
    model = Rental
    template_name = 'rentals/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context['form'] = CommentForm
        return context


class RentalCreateView(generic.CreateView):
    form_class = RentalCreateForm
    template_name = 'rentals/rental_form.html'

class RentalUpdateView(generic.UpdateView):
    form_class = RentalCreateForm
    template_name = 'rentals/rental_form.html'

    def get_queryset(self):
        return Rental.objects.filter(pk = self.kwargs.get('pk', None))
    

class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.rental = Rental.objects.get(pk = self.kwargs.get('pk'))
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('rentals:detail', kwargs={'pk':pk})
