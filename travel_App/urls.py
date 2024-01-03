from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("login_page/", login_page, name='login_page'),
    path("register_page/", register_page, name='register_page'),
    path("forgot_password/", forgot_password, name='forgot_password')

]