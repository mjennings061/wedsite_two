from django.urls import path, include
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('rsvp/', RsvpView.as_view(), name='rsvp'),
    path('rsvp_login/', RsvpLoginView.as_view(), name='rsvp_login'),
    path('rsvp_logout/', RsvpLogoutView.as_view(), name='rsvp_logout'),
    # summary of guests (admin view only)
    path('guest_summary/', GuestSummaryView.as_view(), name='guest_summary'),
    # wedding party
    path('wedding_party/', WeddingPartyView.as_view(), name='wedding_party'),
    # our story
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    # itinerary/summary
    path('itinerary/', ItineraryView.as_view(), name='itinerary'),
    # gifts - paypal button - honeymoon plans
    path('gifts/', GiftsInfoView.as_view(), name='gifts'),
    # photo gallery
    path('photos/', PhotosView.as_view(), name='photos'),
    # getting there
    path('getting_there/', GettingThereView.as_view(), name='getting_there'),
    # contact details
    path('contact_details/', ContactDetailsView.as_view(), name='contact_details'),
    # honeymoon plans
    path('honeymoon/', HoneymoonPlansView.as_view(), name='honeymoon'),
]