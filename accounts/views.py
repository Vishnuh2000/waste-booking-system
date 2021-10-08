from django.shortcuts import render, redirect , HttpResponseRedirect , get_object_or_404
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from user.models import *
from user.models import *




def user_Login(request):
    if request.method == 'GET':
        context = {}
        context['form'] = AuthenticationForm()
        return render(request, 'accounts/login.html', context)

    elif request.method == 'POST':
        lf = AuthenticationForm(data=request.POST)
        if lf.is_valid():
            username = lf.cleaned_data.get('username')
            password = lf.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request,user)
            if user.is_superuser==True:
                return redirect('admin_home')

            elif user.is_staff==True:
                return redirect('staff_home')

            elif user:
                return redirect('homepage')
                
        else:
            messages.info(request,"Invalide Username Or Password")
            context = {}
            context['form'] = lf
            return render(request, 'accounts/login.html', context)



def user_Register(request):
    if request.method == 'GET':
        context = {}
        context['forms'] =RegisterForm()
        return render(request, 'accounts/register.html', context)

    elif request.method == 'POST':
        rf = RegisterForm(request.POST)
        if rf.is_valid():
            user=rf.save(commit=False)
            user.set_password(rf.cleaned_data.get('password'))
            user.save()
            return redirect('loginpage')
        else:
            print(rf.errors)
            context = {}
            context['forms'] = rf
            return render(request, 'accounts/register.html', context)



def user_logout(request):
    logout(request)
    return redirect('homepage')


def staff_user_register(request):
    if  request.method == 'GET':
        context = {}
        context['forms'] = RegisterForm()
        return render(request, 'accounts/register.html' , context)


    elif request.method == 'POST':
        sur = RegisterForm(request.POST)
        if sur.is_valid():
            user = sur.save(commit=False)
            user.is_customer = 0
            user.is_staff=1
            user.set_password(sur.cleaned_data.get('password'))
            user.save()
            return redirect('list_staff')


        else:
             print(sur.errors)
             context = {}
             context['forms'] = sur
             return render(request, 'accounts/register.html' , context)




@login_required(login_url='create_staff')
def staff_add(request):
    context = {}
    context['users'] = User.objects.filter(is_staff=1 , is_superuser=0)
    return render(request, 'owner/staff/staff_list.html' , context)




@login_required(login_url='create_staff')
def remove_staff(request, id):
    staff_user = get_object_or_404(User, pk=id)
    staff_user.delete()
    return redirect('list_staff')


@login_required
def admin_home(request):
    return render(request, 'owner/home/home.html')


@login_required
def admin_user_booking_views(request):
    context = {}
    context['booking_details'] = Book.objects.all()
    return render(request, 'owner/book_details/user_book.html' , context)


def Feedback(request):
    context = {}
    context['feedback'] = FeedBack.objects.all()
    return render(request, 'owner/home/feedback.html' , context)