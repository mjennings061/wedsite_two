from django.urls import path, include
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('rsvp_form/', RsvpView.as_view(), name='rsvp'),
    path('rsvp/', RsvpLoginView.as_view(), name='rsvp_login'),
    path('rsvp_logout/', RsvpLogoutView.as_view(), name='rsvp_logout'),
    path('guest_summary/', GuestSummaryView.as_view(), name='guest_summary'),
    path('privacy_policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('cookie_policy/', CookiePolicyView.as_view(), name='cookie_policy'),
    path('getting_there/', GettingThereView.as_view(), name='getting_there'),
]
