# Generated by Django 3.2.5 on 2021-08-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20210721_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
    ]
