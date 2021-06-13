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
    phone = models.BigIntegerField(blank=True)
    email = models.EmailField(blank=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    RSVP = models.IntegerField(
        choices=CHOICES,
        help_text="Please select your availability on the day of the wedding"
    )

    def __str__(self):
        return f'{self.user}'


class Address(models.Model):
    FirstLine = models.CharField(max_length=100)
    SecondLine = models.CharField(blank=True, max_length=100)
    Town = models.CharField(max_length=100)
    County = models.CharField(max_length=50)
    PostCode = models.CharField(max_length=8)
    Country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.FirstLine}'
