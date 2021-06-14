from django.urls.base import reverse_lazy
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .forms import GuestForm, AddressForm
from .models import Guest, Address
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponseForbidden


class IndexView(ListView):
    """Welcome page with Countdown?"""
    template_name = 'core/index.html'
    model = User
    # queryset = Guest.objects.order_by('user')[:5]


class RsvpLoginView(LoginView):
    """Log in using the Django LoginView class"""
    template_name = 'core/rsvp_login.html'


class RsvpLogoutView(LogoutView):
    """Log out the user"""
    pass


class RsvpView(LoginRequiredMixin, FormView):
    """Guest RSVP registration page using two ModelForms"""
    template_name = 'core/rsvp.html'
    form_class = GuestForm
    second_form_class = AddressForm
    login_url = reverse_lazy('core:rsvp_login')
    success_url = reverse_lazy('core:logout')

    def get_context_data(self, **kwargs):
        context = super(RsvpView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form_address'] = self.second_form_class()
        return context


class ItineraryView(View):
    pass


class AboutUsView(View):
    pass


class WeddingPartyView(View):
    pass


class GettingThereView(View):
    pass


class HoneymoonPlansView(View):
    pass


class GiftsInfoView(View):
    pass


class PhotosView(FormView):
    pass


class ContactDetailsView(View):
    pass


class GuestSummaryView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'core/guest_summary.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser
