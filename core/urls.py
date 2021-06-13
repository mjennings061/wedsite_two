from django.urls import path, include
from core.views import IndexView, RsvpView, RsvpLoginView

app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('rsvp/', RsvpView.as_view(), name='rsvp'),
    path('rsvp_login/', RsvpLoginView.as_view(), name='rsvp_login'),
]
