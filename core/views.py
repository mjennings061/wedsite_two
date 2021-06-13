from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .forms import GuestForm, AddressForm
from .models import Guest, Address
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(ListView):
    """Welcome page with Countdown?"""
    template_name = 'core/index.html'
    context_object_name = 'guests'
    queryset = Guest.objects.order_by('user')[:5]


class RsvpLoginView(LoginView):
    template_name = 'core/rsvp_login.html'


class RsvpLogoutView(LogoutView):
    template_name = 'core/rsvp_login.html'


class RsvpView(LoginRequiredMixin, FormView):
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

# class RsvpPreviewView():
#     template_name =
#
#
# class IteneraryView(generic.ListView)
#     template_name =
#
#
# class AboutUsView(generic.ListView)
#     template_name =
#
#
# class WeddingPartyView(generic.ListView)
#     template_name =
#
#
# class TransportView(generic.ListView)
#     template_name =
#
#
# class HoneymoonPlansView(generic.ListView)
#     template_name =
#
#
# class GiftsInfoView(generic.ListView)
#     template_name =
#
#
# class PhotosView(FormView)
#     template_name =
#
#
# class ContactDetailsView(generic.ListView)
#     template_name =
