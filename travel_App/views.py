from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from django.db import IntegrityError

# Create your views here.

data = {}

index_page_link = "index.html"
login_page_link = "login_page.html"
register_page_link = "register_page.html"
profile_page_link = "profile_page.html"
forgot_page_link = "forgot_password.html"
otp_page_link = "otp_page.html"

## START: VIEW PAGES ##
def index(request):
    return render(request, index_page_link)

def login_page(request):
    return render(request, login_page_link)

def register_page(request):
    return render(request, register_page_link)

def forgot_password(request):
    return render(request, forgot_page_link)

def profile_page(request):
    return render(request, profile_page_link)

def otp_page(request):
    return render(request, otp_page_link)

## END: VIEW PAGES ##


## Email Function

def send_otp(request):
    otp = randint(000000, 999999)
    request.session['otp'] = otp

    send_to = [request.session['reg_data']['email']]
    send_from = settings.EMAIL_HOST_USER
    subject = 'One Time Password'
    message = f'Your One Time Password is: {otp}'
    
    send_mail(subject, message, send_from, send_to)

## Email Verification
def otp_verification(request):
    if int(request.POST['otp']) == request.session['otp']:
        master = Master.objects.create(Username=request.session['reg_data']['username'], Email=request.session['reg_data']['email'], Password=request.session['reg_data']['pwd'])
        print("Account Created Successfully.")
        return redirect(login_page)
    else:
        print("Invalid OTP!")

    return redirect(otp_page_link)


## START: PAGES FUNCTIONALITY ##

# REGISTER
def register_view(request):
    try:
        master = Master.objects.get(Email=request.POST['email'])
        print("Account Already Exist, Please Login.")
    except Master.DoesNotExist as err:
        print(err)
        print("Account Not Found")

        request.session['reg_data'] = {'username': request.POST['username'], 'email': request.POST['email'], 'pwd':request.POST['password']}
        send_otp(request)
        return redirect(otp_page)
    
    return redirect(login_page)

# LOGIN 
def login_view(request):
    try:
        master = Master.objects.get(Email=request.POST['email'])  
        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            return redirect(index)
        else:
            print("Invalid Password")
    except Master.DoesNotExist as err:
        print("Account Does Note Exist.")

    return redirect(login_page)

#LOGOUT
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(login_page)

## END: PAGES FUNCTIONALITY ##