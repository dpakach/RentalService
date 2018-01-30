from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from . import views as account_views

app_name = "accounts"

urlpatterns = [
    url(r'signup/$', views.signup, name='signup'),
    url(r'login/$', views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'logout/$', auth_views.logout, {'next_page': 'accounts/login'}, name='logout'),
    url(r'account_activation_sent/$', account_views.account_activation_sent, name='account_activation_sent'),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        account_views.activate, name='activate'),
]
