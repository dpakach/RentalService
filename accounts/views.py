from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode

from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.views import login as user_login
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from rentals.models import Rental

class Homeview(TemplateView):
    template_name='home.html'

    def get_context_data(self, *args, **kwargs):
        """
        ths method returns the context data of the rental for the detail view
        """
        context = super(Homeview, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            context['rentals_list'] = Rental.objects.filter(author=self.request.user).order_by('-rating')[:3]
            context['intrested_rentals_list'] = self.request.user.intrested_rentals.order_by('-rating')[:3]
        return context



def login(request, **kwargs):
    if request.user.is_authenticated():
        # return redirect(settings.LOGIN_REDIRECT_URL)
        return redirect('/accounts')
    else:
        return user_login(request, **kwargs)

def signup(request):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Rental Account'
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            user_login(request, user)
            return redirect('accounts:account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'accounts/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        user_login(request, user)
        return redirect('profiles:update')
    else:
        return render(request, 'accounts/account_activation_invalid.html')
