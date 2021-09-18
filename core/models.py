from django.db import models
from django.contrib.auth.models import User


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
    phone = models.CharField(max_length=15, verbose_name="Mobile phone number")
    email = models.EmailField(blank=True, verbose_name="Email address")
    address = models.ForeignKey(
        'Address',
        verbose_name="Postal address",
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    RSVP = models.IntegerField(
        choices=CHOICES,
        verbose_name="Attendance selection",
        help_text="Please select your availability on the day of the wedding"
    )
    song = models.TextField(
        blank=True,
        verbose_name="Song recommendations",
        help_text="Suggest song(s) to be played at the evening party"
    )

    def __str__(self):
        return f'{self.user}'


class Address(models.Model):
    first_line = models.CharField(max_length=100, blank=True, verbose_name="First line")
    second_line = models.CharField(max_length=100, blank=True, verbose_name="Second line")
    town = models.CharField(max_length=100, blank=True, verbose_name="Town")
    county = models.CharField(max_length=50, blank=True, verbose_name="County")
    postcode = models.CharField(max_length=8, blank=True, verbose_name="Postcode", help_text="e.g. 'BT69 420'")
    country = models.CharField(max_length=100, blank=True, verbose_name="Country")

    # TODO: write an address_valid() method to check if all fields of address are correct

    def __str__(self):
        return f'{self.first_line}, {self.postcode}'
