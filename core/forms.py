from django.forms import ModelForm, BooleanField
from core.models import Guest, Address


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['RSVP', 'phone', 'email', 'dietary', 'song']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
