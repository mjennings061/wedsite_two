from django.urls.base import reverse_lazy
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .forms import GuestForm, AddressForm
from .models import Guest, Address
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponseNotAllowed


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
    success_url = reverse_lazy('core:rsvp_logout')

    def get_context_data(self, **kwargs):
        context = super(RsvpView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form_address'] = self.second_form_class()
        return context

    def form_valid(self, guest_form):
        # TODO: check for a valid phone number before saving
        # save most of the guest form, minus the address and user
        guest = guest_form.save(commit=False)
        guest.user = self.request.user  # add the user to the model-to-be-saved
        # TODO: move the address checking code to models.Address. Return only the model object
        # populate an empty GuestForm with the posted data
        address_form = self.second_form_class(self.request.POST)
        if address_form.is_valid():
            # check if something has been entered in the address before saving it
            if len(address_form.cleaned_data['first_line']) > 1:
                # check there are no addresses matching that already
                if not Address.objects.filter(first_line=address_form.cleaned_data['first_line']).exists():
                    address = address_form.save()     # save to the database
                else:
                    # get the address from the database if it already exists
                    address = Address.objects.get(first_line=address_form.cleaned_data['first_line'])
                guest.address = address     # append to the model to be saved
        guest.save()
        # TODO: logout user after submitting the form
        return super().form_valid(guest_form)


class ItineraryView(View):
    pass


class AboutUsView(View):
    pass


class WeddingPartyView(View):
    # TODO: Add set-list
    # TODO:
    pass


class GettingThereView(View):
    # TODO: Add venue details
    pass


class HoneymoonPlansView(View):
    # TODO: Add honeymoon plans with an image of where we are going
    # TODO: Add link to GiftsInfoView to donate
    pass


class GiftsInfoView(View):
    # TODO: Add a link to PayPal
    pass


class PhotosView(FormView):
    # TODO: Add hashtag viewer for instagram and twitter:
    # https://developers.facebook.com/docs/instagram-api/guides/hashtag-search
    pass


class ContactDetailsView(View):
    pass


class GuestSummaryView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'core/guest_summary.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser
