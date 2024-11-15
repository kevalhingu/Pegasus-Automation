# myapp/admin.py
from django.contrib import admin
from .models import SupportRequest

admin.site.register(SupportRequest)
