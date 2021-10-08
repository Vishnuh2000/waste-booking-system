from GreenKerala.settings import EMAIL_HOST_USER
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from accounts.models import *
from accounts.forms import *
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from staff.models import *
from staff.forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string



def Home(request):
    return render(request, 'user/home.html')


class AddressCreateView(LoginRequiredMixin,CreateView):
    model = Address
    template_name = "address/create.html"
    form_class = AddressForm
    success_url = reverse_lazy('profile_edit')

    def form_valid(self, form):
        address = form.save(commit=False)
        address.user = self.request.user
        address.save()
        return HttpResponseRedirect(self.success_url)




class FeedBackCreateView(CreateView,LoginRequiredMixin):
    model = FeedBack
    form_class = FeedBackForm
    template_name = "user/contact.html"
    success_url = reverse_lazy('feedback')




def Profile(request):
    context={}
    context['address_list'] = Address.objects.filter(user=request.user)
    if request.method == 'GET':
        context['form'] = ProfileForm(instance=request.user)
        return render(request , 'user/profile.html' , context)

    elif request.method == 'POST':
        form = ProfileForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')

        else:
            context['form'] = form
            return render(request , 'user/profile.html' , context)
        




def address_delete_view(request,id):
    delete_list = get_object_or_404(Address,id=id)
    delete_list.delete()
    return redirect('profile_edit')



class AddressUpdateView(UpdateView):
    model = Address
    template_name = "address/create.html"
    form_class = AddressForm
    success_url = reverse_lazy('profile_edit')
    pk_url_kwarg = 'id'




@login_required
def booking(request):
    if request.method == 'GET':
        context={}
        context['address_list'] = Address.objects.filter(user=request.user)
        return render(request , 'Book/checkout.html' , context)

    elif request.method == 'POST':
        book = Book()
        address = Address.objects.filter(user=request.user , id=request.POST.get('address')).first()
        book.address = address
        book.user = request.user

        send_mail(

            subject='Green Kerala',
            message=f'{{request.user.first_name}}',
            html_message=render_to_string('Book/email_send.html',{'name':request.user.first_name}),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email],
            fail_silently=False
        )

        book.save()  
        return redirect('user_booking')




@login_required
def user_booking_history(request):
    context={}
    context['booking_list'] = Book.objects.filter(user=request.user)
    return render(request , 'Book/book_history.html' , context)