# Generated by Django 3.2.5 on 2021-08-19 13:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0019_delete_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Address',
        ),
    ]