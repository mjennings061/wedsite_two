from django.urls.base import reverse_lazy
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from .forms import GuestForm, AddressForm
from .models import Guest, Address
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):
    """Welcome page with Countdown?"""
    template_name = 'core/index.html'


class RsvpLoginView(SuccessMessageMixin, LoginView):
    """Log in using the Django LoginView class"""
    template_name = 'core/rsvp_login.html'
    success_message = "Logged in successfully"


class RsvpLogoutView(LogoutView):
    """Log out the user"""
    def dispatch(self, request, *args, **kwargs):
        # Append a message when logging out
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, "Successfully logged out")
        return response


class RsvpView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    """Guest RSVP registration page using two ModelForms"""
    template_name = 'core/rsvp.html'
    form_class = GuestForm
    second_form_class = AddressForm
    login_url = reverse_lazy('core:rsvp_login')
    success_url = reverse_lazy('core:rsvp_logout')
    success_message = "RSVP submitted successfully"

    def get_context_data(self, **kwargs):
        context = super(RsvpView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form_address'] = self.second_form_class()
        return context

    def form_invalid(self, form):
        """Show a warning message when the form is not valid"""
        messages.add_message(
            self.request,
            messages.WARNING,
            "Please check the form and resubmit - maybe check the phone number has '+44...'")
        return super().form_invalid(form)

    def form_valid(self, guest_form):
        # save most of the guest form, minus the address and user
        guest = guest_form.save(commit=False)
        # if the user has created a guest profile before, then block it
        if Guest.objects.filter(user=self.request.user):
            messages.add_message(
                self.request,
                messages.WARNING,
                "You have already submitted an RSVP, please contact us"
            )
            # break the form_valid method and return invalid
            return super().form_invalid(guest_form)
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


class OnTheDayView(TemplateView):
    # TODO: Add timeline
    # TODO: Add venue details
    # TODO: Add menu
    template_name = 'core/on_the_day.html'


class AboutUsView(TemplateView):
    template_name = 'core/about_us.html'


class WeddingPartyView(TemplateView):
    template_name = 'core/wedding_party.html'


class HoneymoonPlansView(TemplateView):
    # TODO: Add honeymoon plans with an image of where we are going
    # TODO: Add link to GiftsInfoView to donate
    template_name = 'core/honeymoon.html'


class GiftsInfoView(TemplateView):
    # TODO: Add a link to PayPal
    template_name = 'core/gifts.html'


class PhotosView(TemplateView):
    # TODO: Add hashtag viewer for instagram and twitter:
    # https://developers.facebook.com/docs/instagram-api/guides/hashtag-search
    template_name = 'core/photos.html'


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
        # Dietary requirements as [{username, dietary}]
        guests_dietary = self.get_dietary_requirements(users)
        # TODO: Add song recommendations by user


        # Return all four context lists
        context = {
            'going': guests_going,
            'ceremony': guests_ceremony,
            'not_going': guests_not_going,
            'no_response': guests_no_response,
            'dietary': guests_dietary
        }
        return context

    def names_from_queryset(self, queryset):
        """Get a list of names from a queryset of Users"""
        names = []
        for user in queryset:
            if user.first_name != '':
                names.append(f"{user.first_name} {user.last_name}")
            else:
                names.append(f"{user.username}")
        return names

    def get_dietary_requirements(self, users):
        """ Get a list of dicts with dietary requirements listed """
        # get a list of all guests with something in the dietary column other than None or blank
        guests = Guest.objects.exclude(dietary='').exclude(dietary='None').values('user_id', 'dietary')
        # put all responses in a list of dicts with [{name, dietary}]
        guests_dietary = []
        for guest in guests:
            # get the user object connected to the current guest
            user = users.get(id=guest['user_id'])
            # get the name of the user, or just get the username if its blank
            if user.first_name is not '':
                name = f'{user.first_name} {user.last_name}'
            else:
                name = user.username
            guests_dietary.append({
                'name': name,
                'dietary': guest['dietary'],
            })
        return guests_dietary
