# Generated by Django 3.2.5 on 2021-08-12 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
