from django.contrib import admin
from .models import *

"""
Tworzenie su: python manage.py createsuperuser
l: admin
h: Skradzione
"""

admin.site.register(File)
admin.site.register(Math)