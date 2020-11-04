from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome_start, name='welcome_start'),
]