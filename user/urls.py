from os import name
from django.urls import path
from .views import *
from .import apis as api





urlpatterns = [
    
    path('' , Home , name='homepage'),

    path('user/address/create/' , AddressCreateView.as_view() , name='address_create'),

    path( 'profile/', Profile , name='profile_edit'),

    path('profile/address/delete/<int:id>' , address_delete_view , name='address_delete'),

    path('profile/address/update/<int:id>/' , AddressUpdateView.as_view() , name='address_update'),

    path('api/get-address/<int:id>/', api.get_user_address, name='user_api_get_address'),

    path('contact/' , FeedBackCreateView.as_view() , name='feedback'),

    path('booking/history/' , user_booking_history , name='user_booking'),

    path('booking/section/', booking , name='bookig_section')


  
]