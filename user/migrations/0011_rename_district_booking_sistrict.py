# Generated by Django 3.2.4 on 2021-07-19 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_booking_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='District',
            new_name='sistrict',
        ),
    ]
