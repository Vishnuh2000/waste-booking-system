# Generated by Django 3.2.4 on 2021-07-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_cart_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='pending...', max_length=20, verbose_name='status'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
