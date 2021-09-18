from django.forms import ModelForm
from core.models import Guest, Address


class GuestForm(ModelForm):
    # TODO: Change form line rendering to show "Email address" instead of "Email"
    class Meta:
        model = Guest
        fields = ['email', 'phone', 'RSVP', 'dietary', 'song']


class AddressForm(ModelForm):
    # TODO: Change form line rendering to show "First Line" instead of "FirstLine"
    class Meta:
        model = Address
        fields = ['FirstLine', 'SecondLine', 'Town', 'County', 'PostCode', 'Country']
