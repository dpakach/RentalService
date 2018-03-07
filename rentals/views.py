from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from .forms import CommentForm
from .forms import RentalCreateForm
from .models import Rental, Comment

# Create your views here.

class IndexView(generic.ListView):
    """
    indexView for showing the list of avilable rentals to the user
    """

    template_name = 'rentals/index.html'
    context_object_name = 'rentals_list'
    model = Rental
    paginate_by = 2

    def get_queryset(self):
        """
        ths method returns the context data of the rental objects for the index view
        """
        return Rental.objects.order_by('-rating')


    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        page = self.request.GET.get('page')
        qs = Rental.objects.order_by('-rating')
        if query:
            qs = qs.search(query)
            context['query'] = query
        paginator = Paginator(qs, 2)
        if page:
            qs = paginator.page(page)

        context['rentals_list'] = qs
        return context

    # def get_context_data(self, *args, **kwargs):
    #     context = super(IndexView, self).get_context_data(*args, **kwargs)
    #     query = self.request.GET.get('q')
    #     qs = Rental.objects.all().order_by('-rating')
    #     if query:
    #         qs = Rental.objects.search(query).order_by('-rating')
    #         context['query'] = query

    #     context['rentals_list'] = qs
    #     return context


class DetailView(generic.DetailView):

    """
    A single page detail view for displaying the details of a rental
    this view returns the info of a rental in detail along with the associated comments
    """

    model = Rental
    template_name = 'rentals/detail.html'

    def get_context_data(self, *args, **kwargs):
        """
        ths method returns the context data of the rental for the detail view
        """
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context['form'] = CommentForm
        return context


class RentalCreateView(LoginRequiredMixin, generic.CreateView):
    """
    CreateView to create new rentals
    This is a class based view for cereating new rental objects
    """

    form_class = RentalCreateForm 
    template_name = 'rentals/rental_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        #file_form.save()
        instance.author = self.request.user
        return super(RentalCreateView, self).form_valid(form)



class RentalUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    UpdateView to update rentals
    This is a class based view for updating rental objects
    """

    form_class = RentalCreateForm
    template_name = 'rentals/rental_form.html'

    def get_queryset(self):
        """
        this method return the rental object to update in the UpdateView
        """
        return Rental.objects.filter(pk = self.kwargs.get('pk', None))
    


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    """
    CreateView to create a new comment for a rental 
    this view gives a form to create new comment and rating for a rental
    """
    model = Comment
    form_class = CommentForm
    template_name = 'rentals/detail.html'

    def form_valid(self, form):
        """
        method to check if the form is valid 
        """

        obj = form.save(commit=False)
        obj.rental = Rental.objects.get(pk = self.kwargs.get('pk'))
        obj.rental.rating = (obj.rental.rating * obj.rental.comments.count() + obj.stars)/(obj.rental.comments.count() + 1)
        obj.rental.save()
        obj.author = self.request.user
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        """
        this method returns the url to renturn to if the form is submitted and valid
        """

        pk = self.kwargs['pk']
        return reverse('rentals:detail', kwargs={'pk':pk})


@login_required
def intrested_in_rental(request, pk=None):
    intrested_rental = get_object_or_404(Rental, pk__iexact=pk)
    if request.user.is_authenticated():
        is_intrested = Rental.objects.toggle_intrested(intrested_rental.pk, request.user)
    return redirect('rentals:detail', pk=intrested_rental.pk)


def search_api(request):
    # query = request.GET.get('query')
    # print('query')
    # data_list = []
    # if query:
    #     qs = []
    #     qs = Rental.objects.custom_search(query)
    data_list= []
    qs = Rental.objects.all()
    for obj in qs:
        data_list.append(obj.title)

    data = {
        'rentals': data_list[:5]
    }
    return JsonResponse(data)


def loc_api(request, pk):
    print(pk)
    rental = get_object_or_404(Rental, pk__iexact=pk)
    data = {
        'location': rental.location,
        'lat': rental.lat,
        'lng': rental.lng,
    }
    print(data);
    return JsonResponse(data)
