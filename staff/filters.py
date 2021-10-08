import django_filters
from user.models import *



class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        fields=['pin']