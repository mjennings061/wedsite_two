from django.urls.base import reverse_lazy
from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .forms import GuestForm, AddressForm
from .models import Guest, Address
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


class IndexView(TemplateView):
    """Welcome page with Countdown?"""
    template_name = 'core/index.html'


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
        # TODO: Add toasts to denote success
        # TODO: Check if the user has already registered and update their details
        # save most of the guest form, minus the address and user
        guest = guest_form.save(commit=False)
        guest.user = self.request.user  # add the user to the model-to-be-saved
        # populate an empty GuestForm with the posted data
        address_form = self.second_form_class(self.request.POST)
        # check the address is valid
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
        return super().form_valid(guest_form)


class OnTheDayView(View):
    # TODO: Add timeline
    # TODO: Add venue details
    # TODO: Add menu
    pass


class AboutUsView(TemplateView):
    template_name = 'core/about_us.html'


class WeddingPartyView(View):
    # TODO: Add description of bridal party
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


class GuestSummaryView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'core/guest_summary.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        # Get a list of all users
        users = User.objects.all()
        # Filter users by their rsvp_choice in guest
        guests_going = self.names_from_queryset(users.filter(guest__RSVP=0))
        guests_ceremony = self.names_from_queryset(users.filter(guest__RSVP=1))
        guests_not_going = self.names_from_queryset(users.filter(guest__RSVP=2))
        # Get users with no guest profile attached
        guests_no_response = self.names_from_queryset(users.filter(guest=None))

        # TODO: get dietary requirements. Filter those that say None or blank

        # Return all four context lists
        context = {
            'going': guests_going,
            'ceremony': guests_ceremony,
            'not_going': guests_not_going,
            'no_response': guests_no_response,
        }
        return context

    def names_from_queryset(self, queryset):
        """Get a list of names from a queryset of Users"""
        names = []
        for user in queryset:
            if user.first_name is not '':
                names.append(f"{user.first_name} {user.last_name}")
            else:
                names.append(f"{user.username}")
        return names
