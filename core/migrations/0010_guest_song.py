# Generated by Django 3.2.4 on 2021-09-18 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_guest_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='song',
            field=models.TextField(blank=True, help_text='Suggest a song to be played at the evening party'),
        ),
    ]