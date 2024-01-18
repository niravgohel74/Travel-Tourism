from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = admin.site.site_title = "Travel Toruism"
admin.site.register(Master)