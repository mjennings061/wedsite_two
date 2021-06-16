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
    dietary = models.TextField(blank=True, help_text="Please enter your dietary requirements or allergies")
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True)
    RSVP = models.IntegerField(
        choices=CHOICES,
        help_text="Please select your availability on the day of the wedding"
    )

    def __str__(self):
        return f'{self.user}'


class Address(models.Model):
    FirstLine = models.CharField(max_length=100, blank=True)
    SecondLine = models.CharField(max_length=100, blank=True)
    Town = models.CharField(max_length=100, blank=True)
    County = models.CharField(max_length=50, blank=True)
    PostCode = models.CharField(max_length=9, blank=True)
    Country = models.CharField(max_length=100, blank=True)

    # TODO: write an address_valid() method to check if all fields of address are correct

    def __str__(self):
        return f'{self.FirstLine}'
