from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('login/' , user_Login , name='loginpage'),
    
    path('register/' , user_Register , name='registerpage'),

    path('logout' , user_logout , name='user_logout'),

    path('admin/add/staff/' , staff_user_register , name='create_staff'),

    path('admin/satff/list/' , staff_add , name='list_staff'),

    path('staff/remove/<id>/', remove_staff, name='remove_staff_user'),

    path('admin/home/' , admin_home , name='admin_home'),

    path('user/booking/view' , admin_user_booking_views , name='admin_list'),

    path('feedback/view/' , Feedback , name='admin_feedback_view'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="reset_password/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="reset_password/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="reset_password/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="reset_password/password_reset_done.html"), 
        name="password_reset_complete"),

]