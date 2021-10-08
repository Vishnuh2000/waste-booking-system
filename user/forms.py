from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *
from accounts.models import User


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['house_name', 'address_line_1', 'address_line_2',
                  'pin', 'phone_number', 'district', 'address_type']

        widgets = {
            'house_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'house name'
                }
            ),
            'address_line_1': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Address'
                }
            ),
            'address_line_2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Landmark'
                }
            ),
            'pin': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Pincode'
                }
            ),
            'phone_number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone Number'

                }
            ),
            'district': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'District'
                }
            ),
            'address_type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
