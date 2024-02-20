from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("index1/", index1, name="index1"),
    path("login_page/", login_page, name="login_page"),
    path("login_view/", login_view, name="login_view"),

    path("register_page/", register_page, name="register_page"),
    path("register_view/", register_view, name="register_view"),
    
    path("forgot_password/", forgot_password, name="forgot_password"),
    path("logout/", logout, name="logout"),

    path("otp_page/", otp_page, name="otp_page"),
    path("otp_verification/", otp_verification, name="otp_verification"),

    path("profile_page/", profile_page, name="profile_page"),
]