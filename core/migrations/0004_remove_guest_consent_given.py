# Generated by Django 3.2.4 on 2021-09-20 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210920_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='consent_given',
        ),
    ]
