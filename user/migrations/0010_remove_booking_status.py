# Generated by Django 3.2.4 on 2021-07-19 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
    ]