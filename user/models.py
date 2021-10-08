from django.db import models
from accounts.models import *
from django.core.validators import MinLengthValidator, MinValueValidator, EmailValidator
from django.core import validators


class Address(models.Model):
    STATUS_CHOICE = (
        ('Ernakulam', 'Ernakulam'),
        ('Kottayam', 'Kottayam'),
        ('Idukki', 'Idukki')
    )
    ADDRESS_CHOICE = (
        ('Home' , 'Home'),
        ('Office' , 'Office')
    )
    id = models.BigAutoField(
        primary_key=True
    )
    house_name = models.CharField(
        max_length=250,
        verbose_name='hose Name'
    )

    address_line_1 = models.CharField(
        max_length=250,
        verbose_name='Address Line 1'
    )

    address_line_2 = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Address Line 2',
        help_text='Optional'
    )

    pin = models.PositiveIntegerField(
        verbose_name='PIN CODE',
        validators=[
            validators.MaxValueValidator(999999)
        ]
    )

    phone_number = models.IntegerField(
        verbose_name='Mobile Number',
        validators=[
            validators.MaxValueValidator(9999999999)
        ]
    )
    district = models.CharField(
        max_length=25,
        choices=STATUS_CHOICE,
        verbose_name='Disctrict'
    )
    address_type = models.CharField(
        max_length=100,
        choices=ADDRESS_CHOICE
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )


class FeedBack(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=100,
        verbose_name='Name'
    )

    email = models.EmailField(
        max_length=100,
        verbose_name='Email'
    )

    subject = models.CharField(
        max_length=200,
        verbose_name='Subject'
    )

    message = models.TextField(
        verbose_name='Message'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )




class Book(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    address = models.ForeignKey(
        to=Address,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    has_completed = models.BooleanField(
        max_length=100,
        default=False
        
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )
