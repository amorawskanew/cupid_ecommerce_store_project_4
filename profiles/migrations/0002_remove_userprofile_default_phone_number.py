# Generated by Django 3.1.5 on 2021-01-29 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_phone_number',
        ),
    ]
