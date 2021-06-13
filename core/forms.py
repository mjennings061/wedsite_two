from django.forms import ModelForm
from core.models import Guest, Address


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['email', 'phone', 'RSVP', 'dietary']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['FirstLine', 'SecondLine', 'Town', 'County', 'PostCode', 'Country']
