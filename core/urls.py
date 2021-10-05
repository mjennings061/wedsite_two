from django.urls import path, include
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('rsvp_form/', RsvpView.as_view(), name='rsvp'),
    path('rsvp/', RsvpLoginView.as_view(), name='rsvp_login'),
    path('rsvp_logout/', RsvpLogoutView.as_view(), name='rsvp_logout'),
    # summary of guests (admin view only)
    path('guest_summary/', GuestSummaryView.as_view(), name='guest_summary'),
    # wedding party
    path('wedding_party/', WeddingPartyView.as_view(), name='wedding_party'),
    # our story
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    # itinerary/getting there
    path('on_the_day/', OnTheDayView.as_view(), name='on_the_day'),
    # gifts - paypal button - honeymoon plans
    path('gifts/', GiftsInfoView.as_view(), name='gifts'),
    # photo gallery
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('privacy_policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('cookie_policy/', CookiePolicyView.as_view(), name='cookie_policy'),
]
