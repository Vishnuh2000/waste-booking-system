from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *




class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'First Name'
                }

            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Last Name'

                }

            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'type' :'email',
                    'placeholder' : 'Email-ID'

                }

            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'password'

                }
    

            ),
        }
