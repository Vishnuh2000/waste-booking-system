from django.urls import path
from .views import *




urlpatterns = [
    
    path('home/' , staff_home , name='staff_home'),

    path('user_booking/view/' , user_booking_staff_view , name='user_booking_staff_list'),

    path('admin/user_booking/collect/<id>' , user_booking_admin_status , name='collect'),
    
    #path('search/' , search , name='search')


]