# Generated by Django 3.2.4 on 2021-12-06 20:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_guest_consent_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='dietary',
            field=models.TextField(blank=True, help_text='Please enter your dietary requirements or allergies', verbose_name='Dietary requirements'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number must be in international format e.g. +447889016685 if your number is 07889016685', max_length=128, region=None, verbose_name='Mobile phone number (*)'),
        ),
    ]