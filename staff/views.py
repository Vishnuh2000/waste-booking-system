from django.shortcuts import render,redirect
from accounts.models import *
from user.models import *
from .models import *
from .forms import *
from django.db.models import Q
from .filters import BookingFilter



def staff_home(request):
    return render(request , 'home/home.html')



def user_booking_staff_view(request):
         context = {}
         context['booking'] = Book.objects.filter(has_completed=0)
         context['search'] = BookingFilter(request.GET , queryset=context['booking'])
         context['booking']=context['search'].qs
         return render(request, 'details/req.html',context,)

   


def user_booking_admin_status(request,id):
    obj = Book.objects.get(pk=id)
    obj.has_completed = 1
    obj.save()
    return redirect('user_booking_staff_list') 





