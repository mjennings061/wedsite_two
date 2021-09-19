from django.forms import ModelForm
from core.models import Guest, Address


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['email', 'phone', 'RSVP', 'dietary', 'song']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
