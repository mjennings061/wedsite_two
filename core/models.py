from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Guest(models.Model):
    CeremonyAndDinner = 0
    CeremonyOnly = 1
    CannotAttend = 2
    CHOICES = [
        (CeremonyAndDinner, 'I can attend the ceremony and the dinner'),
        (CeremonyOnly, 'I can attend only the ceremony'),
        (CannotAttend, 'I cannot attend'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)    # link to the user uploading the file
    dietary = models.TextField(
        blank=True,
        verbose_name="Dietary requirements",
        help_text="Please enter your dietary requirements or allergies",
    )
    phone = PhoneNumberField(
        verbose_name="Mobile phone number (*)",
        help_text="Phone number must be in international format e.g. +447889016685 if your number is 07889016685",
    )
    email = models.EmailField(blank=True, verbose_name="Email address")
    address = models.ForeignKey(
        'Address',
        verbose_name="Postal address",
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    RSVP = models.IntegerField(
        choices=CHOICES,
        verbose_name="Attendance selection (*)",
        help_text="Please select your availability on the day of the wedding. Mobile users: long press your selection"
    )
    song = models.TextField(
        blank=True,
        verbose_name="Song recommendations",
        help_text="Suggest song(s) to be played at the evening party"
    )

    def __str__(self):
        if self.user.first_name == '':
            return f'{self.user}'
        else:
            return f'{self.user.first_name} {self.user.last_name}'


class Address(models.Model):
    first_line = models.CharField(max_length=100, blank=True, verbose_name="First line")
    second_line = models.CharField(max_length=100, blank=True, verbose_name="Second line")
    town = models.CharField(max_length=100, blank=True, verbose_name="Town")
    county = models.CharField(max_length=50, blank=True, verbose_name="County")
    postcode = models.CharField(max_length=8, blank=True, verbose_name="Postcode", help_text="e.g. 'BT69 420'")
    country = models.CharField(max_length=100, blank=True, verbose_name="Country")

    def valid_address(self, address):
        pass

    def __str__(self):
        return f'{self.first_line}, {self.postcode}'
