from django.shortcuts import render, redirect
from .models import *

# Create your views here.

data = {}

index_page_link = "index.html"
login_page_link = "login_page.html"
register_page_link = "register_page.html"
forgot_pwd_page_link = "forgot_password.html"

## START: VIEW PAGES ##
def index(request):
    return render(request, index_page_link)

def login_page(request):
    return render(request, login_page_link)

def register_page(request):
    return render(request, register_page_link)

def forgot_password(request):
    return render(request, forgot_pwd_page_link)

## END: VIEW PAGES ##   

## START: FUNCTIONALITY ##
## END: FUNCTIONALITY ##