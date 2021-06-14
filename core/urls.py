from django.urls import path, include
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('rsvp/', RsvpView.as_view(), name='rsvp'),
    path('rsvp_login/', RsvpLoginView.as_view(), name='rsvp_login'),
    path('rsvp_logout/', RsvpLogoutView.as_view(), name='rsvp_logout'),
    # summary of guests (admin view only)
    # wedding party
    # our story
    # itinerary/summary
    # gifts - paypal button - honeymoon plans
    # photo gallery
    # getting there
    # contact details
]
